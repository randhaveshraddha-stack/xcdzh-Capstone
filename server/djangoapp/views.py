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
            <div class="ms-auto">
                <a class="btn btn-outline-light btn-sm" href="/admin/">Login</a>
            </div>
        </nav>
        <h1>Car Dealerships</h1>
        <p class="text-muted">Current URL: <code>http://localhost:8000/</code></p>
        <table class="table table-striped table-bordered mt-3">
            <thead class="table-dark">
                <tr><th>ID</th><th>Dealer Name</th><th>City</th><th>State</th></tr>
            </thead>
            <tbody>
                <tr><td>1</td><td>Classic Cars Chicago</td><td>Chicago</td><td>IL</td></tr>
                <tr><td>2</td><td>Motor City Dealership</td><td>Detroit</td><td>MI</td></tr>
                <tr><td>3</td><td>Lone Star Auto Group</td><td>Austin</td><td>TX</td></tr>
            </tbody>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)

def get_dealer_details(request, dealer_id):
    html = f"""
    <html>
    <head>
        <title>Dealer Details & Reviews</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 p-3 rounded">
            <a class="navbar-brand text-white" href="#">Dealership Application</a>
            <div class="ms-auto text-white">
                <span class="me-3">Welcome, <strong>hraddha</strong></span>
            </div>
        </nav>
        <h1>Dealer #{dealer_id} - Details & Reviews</h1>
        <p class="text-muted">Current URL: <code>http://localhost:8000/djangoapp/dealer/{dealer_id}</code></p>
        
        <div class="card mb-4">
            <div class="card-body">
                <h3 class="card-title">Classic Cars Chicago</h3>
                <p class="card-text"><strong>City:</strong> Chicago | <strong>State:</strong> IL | <strong>Address:</strong> 123 Main St</p>
            </div>
        </div>

        <h2>Customer Reviews</h2>
        <div class="list-group">
            <div class="list-group-item list-group-item-action mb-2">
                <div class="d-flex w-100 justify-content-between">
                    <h5 class="mb-1">Fantastic services</h5>
                    <small class="text-success">Positive</small>
                </div>
                <p class="mb-1">Great experience buying my new SUV here! Highly recommend.</p>
                <small>User: hraddha</small>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def get_dealer_reviews(request, dealer_id):
    return JsonResponse({"status": 200, "reviews": []})

def add_review(request):
    return JsonResponse({"status": 200})
