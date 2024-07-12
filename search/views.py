from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant

def search_view(request):
    query = request.GET.get('query', '')
    if query:
        results = Restaurant.objects.filter(items__icontains=query)
        results = [{'name': r.name, 'location': r.location} for r in results]
        return JsonResponse({'results': results})
    return render(request, 'index.html')
