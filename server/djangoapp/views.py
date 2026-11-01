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
    return HttpResponse(f"Dealer Details #{dealer_id}")

def get_dealer_reviews(request, dealer_id):
    return JsonResponse({"status": 200, "reviews": [
        {"id": 1, "review": "Fantastic services", "sentiment": "positive", "dealership": dealer_id}
    ]})

def add_review(request, dealer_id=1):
    html = f"""
    <html>
    <head>
        <title>Post Review</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 p-3 rounded">
            <a class="navbar-brand text-white" href="#">Dealership Application</a>
            <div class="ms-auto text-white">
                <span class="me-3">Welcome, <strong>hraddha</strong></span>
            </div>
        </nav>
        <h1>Add a Review for Classic Cars Chicago</h1>
        <p class="text-muted">Current URL: <code>http://localhost:8000/djangoapp/dealer/{dealer_id}/review</code></p>
        
        <form>
            <div class="mb-3">
                <label for="content" class="form-label"><strong>Enter the review content:</strong></label>
                <textarea class="form-control" id="content" rows="4">Fantastic services and great buying experience!</textarea>
            </div>
            <div class="mb-3">
                <label for="purchased" class="form-label"><strong>Select Car (Purchased):</strong></label>
                <select class="form-select" id="purchased">
                    <option selected>Pathfinder - SUV (2023)</option>
                    <option>Rogue - SUV (2022)</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="purchase_date" class="form-label"><strong>Purchase Date:</strong></label>
                <input type="date" class="form-control" id="purchase_date" value="2026-10-15">
            </div>
            <button type="submit" class="btn btn-primary">Submit Review</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)
