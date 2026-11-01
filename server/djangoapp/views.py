from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)

def get_cars(request):
    car_makes = [
        {"id": 1, "name": "Pathfinder", "type": "SUV", "year": 2023, "dealer_id": 1},
        {"id": 2, "name": "Rogue", "type": "SUV", "year": 2022, "dealer_id": 2}
    ]
    return JsonResponse({"CarMakes": car_makes})

def get_dealerships(request):
    html = """
    <html>
    <head>
        <title>Car Dealerships</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 p-3 rounded">
            <a class="navbar-brand text-white" href="#">Dealership Application</a>
        </nav>
        <h1>Car Dealerships</h1>
    </body>
    </html>
    """
    return HttpResponse(html)

def get_dealer_details(request, dealer_id):
    return HttpResponse(f"Dealer Details #{dealer_id}")

def get_dealer_reviews(request, dealer_id):
    html = f"""
    <html>
    <head>
        <title>Dealer Reviews</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 p-3 rounded">
            <a class="navbar-brand text-white" href="#">Dealership Application</a>
            <div class="ms-auto text-white">
                <span class="me-3">Welcome, <strong>hraddha</strong></span>
            </div>
        </nav>
        <h1>Reviews for Classic Cars Chicago</h1>
        <p class="text-muted">Current URL: <code>http://localhost:8000/djangoapp/reviews/dealer/{dealer_id}/</code></p>
        
        <div class="card mt-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title text-primary">Pathfinder - SUV (2023)</h5>
                <h6 class="card-subtitle mb-2 text-muted">Purchase Date: 2026-10-15</h6>
                <p class="card-text mt-3"><strong>Review:</strong> Fantastic services and great buying experience!</p>
                <span class="badge bg-success">Posted Successfully</span>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def add_review(request, dealer_id=1):
    html = f"""
    <html>
    <head>
        <title>Post Review</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <h1>Add Review</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
