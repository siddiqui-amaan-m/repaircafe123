from django.shortcuts import render

def start_page(request):
    # Dummy data for classifieds
    classifieds = [
        {"title": "iPhone 14 for Sale", "description": "Barely used, excellent condition.", "price": "$799"},
        {"title": "2BHK Apartment", "description": "Spacious apartment in city center.", "price": "$1200/month"},
        {"title": "Gaming Laptop", "description": "RTX 4080, 32GB RAM.", "price": "$1500"},
    ]
    context = {'classifieds': classifieds}
    return render(request, 'classifieds/start_page.html', context)
