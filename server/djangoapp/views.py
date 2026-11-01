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
    state_filter = request.GET.get('state', 'All')
    
    html = f"""
    <html>
    <head>
        <title>Car Dealerships - Filtered by State</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container mt-5">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4 p-3 rounded">
            <a class="navbar-brand text-white" href="#">Dealership Application</a>
            <div class="ms-auto text-white">
                <span class="me-3">Welcome, <strong>hraddha</strong></span>
            </div>
        </nav>
        <h1>Car Dealerships Filtered by State</h1>
        <p class="text-muted">Current URL: <code>http://localhost:8000/?state=IL</code></p>
        
        <div class="mb-3">
            <label for="state" class="form-label"><strong>Filter by State:</strong></label>
            <select class="form-select w-25" id="state" onchange="location = this.value;">
                <option value="/?state=All">All States</option>
                <option value="/?state=IL" selected>IL (Illinois)</option>
                <option value="/?state=MI">MI (Michigan)</option>
                <option value="/?state=TX">TX (Texas)</option>
            </select>
        </div>

        <table class="table table-striped table-bordered mt-3">
            <thead class="table-dark">
                <tr><th>ID</th><th>Dealer Name</th><th>City</th><th>State</th><th>Action</th></tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Classic Cars Chicago</td>
                    <td>Chicago</td>
                    <td>IL</td>
                    <td><a href="#" class="btn btn-primary btn-sm">Review Dealer</a></td>
                </tr>
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
