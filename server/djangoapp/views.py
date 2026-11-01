from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)

def get_cars(request):
    car_makes = [
        {"id": 1, "name": "Pathfinder", "type": "SUV", "year": 2023, "dealer_id": 1},
        {"id": 2, "name": "Rogue", "type": "SUV", "year": 2022, "dealer_id": 2},
        {"id": 3, "name": "Altima", "type": "Sedan", "year": 2023, "dealer_id": 3},
        {"id": 4, "name": "Leaf", "type": "EV", "year": 2024, "dealer_id": 4},
        {"id": 5, "name": "Titan", "type": "Truck", "year": 2023, "dealer_id": 5}
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
        <p class="text-muted">Welcome to our dealership portal. Browse dealers below:</p>
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

def get_dealer_reviews(request, dealer_id):
    return JsonResponse({"status": 200, "reviews": []})

def get_dealer_details(request, dealer_id):
    return JsonResponse({"status": 200, "dealer": {"id": dealer_id, "full_name": "Sample Dealer"}})

def add_review(request):
    return JsonResponse({"status": 200})
