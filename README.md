# Restaurant Search Application
Welcome to the Restaurant Search Application! This app allows users to search for restaurants based on a query term, location, and cuisine type. It also displays the first matching dish's name and price, with additional details about each restaurant.

## Features
 - Search for Restaurants: Search by dish name, location, and cuisine.
 - Display Search Results: Shows restaurant name, location, and the first matching dish's name and price.
 - Responsive Design: Works on both desktop and mobile devices.
 - Form Validation: Ensures that the search query is not empty and dynamically enables/disables location and cuisine fields.

## Technologies Used
 - Backend: Django with Django Rest Framework
 - Frontend: HTML, CSS, JavaScript (jQuery)
 - Database: SQLite (default), can be configured to use PostgreSQL, MySQL, etc.
 - Version Control: Git
 - Deployment: Can be deployed on any server or platform that supports Django applications

## Setup and Installation
### Prerequisites
Make sure you have the following installed:
 - Python 3.x
 - pip (Python package installer)

Clone the Repository
```
 git clone https://github.com/your-username/restaurant-search-app.git
 cd restaurant-search-app
```
Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
Install Dependencies
```
pip install -r requirements.txt
```
Apply Migrations
```
python manage.py migrate
```
Load data
```
python manage.py load_data
```
Run the Development Server
```
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/` in your browser to access the app.

## Usage
### Search for Restaurants
 1. Enter a Query: Type a dish name in the Search input field.
 2. Specify Location and Cuisine (optional): Enter a location and select a cuisine type.
 3. View Results: The results will be displayed below the search form. If the query field is empty, the location and cuisine fields will be disabled.

## Endpoints
### Search Endpoint
 - URL: /search/
 - Method: GET
 - Query Parameters:
   - query: Dish name to search for.
   - location: Optional. Location to filter restaurants.
   - cuisine: Optional. Cuisine type to filter restaurants.
  
### Example Request
```
GET /search/?query=Dosa&location=Bangalore&cuisine=South%20Indian
```
### Example Response
```
{
  "results": [
    {
      "id": 1,
      "name": "Restaurant A",
      "location": "Location A",
      "item": "Masala Dosa: 46.00 "
    },
    {
      "id": 2,
      "name": "Restaurant B",
      "location": "Location B",
      "item": "Cheese Dosa: 60.00 "
    }
  ]
}
```
## Contributing
I welcome contributions to improve the app. If you have suggestions, bug fixes, or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes.
4. Submit a pull request with a description of your changes.

