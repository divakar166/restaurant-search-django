from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from django.http import JsonResponse
import json

def search_view(request):
    if request.method == 'GET':
        results = []
        query = request.GET.get('query', '')
        location = request.GET.get('location', '')
        cuisine = request.GET.get('cuisine', '')
        results = Restaurant.objects.all()
        if query:
            results = results.filter(items__icontains=query)
        if location:
            results = results.filter(location__icontains=location)
        if cuisine:
            results = results.filter(full_details__cuisines__icontains=cuisine)
        # results = [
        #     {'id': r.id, 'name': r.name, 'location': r.location, 'item': json.loads(r.items).get(query) }
        #     for r in results
        # ]

        results = [{'id': r.id, 'name': r.name, 'location': r.location, 'item': next((f"{name}: {price}" for name, price in json.loads(r.items).items() if query.lower() in name.lower()), 'Price not available')} for r in results]
        return JsonResponse({'results': results})

def index(request):
    return render(request, 'index.html')

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    lat, lng = restaurant.lat_long.split(',')
    items = json.loads(restaurant.items.replace("'", '"'))
    full_details = restaurant.full_details
    
    if isinstance(full_details, dict):
        full_details = json.dumps(full_details)
    full_details = json.loads(full_details)
    cuisines = full_details.get("cuisines", "")
    location = full_details.get("location", {})
    city = location.get("city", "")
    address = location.get("address", "")
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'lat': lat,
        'lng': lng,
        'items': items,
        'cuisines': cuisines,
        'city': city,
        'address': address,
    })