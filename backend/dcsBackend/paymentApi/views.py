from django.shortcuts import render
# payments/views.py

from django.http import HttpResponse

# Homepage for the payments system
def index(request):
    return HttpResponse("Welcome to the Payments page!")

# View to process a payment
def process_payment(request):
    return HttpResponse("Processing payment...")

# View to display payment history
def payment_history(request):
    return HttpResponse("Viewing payment history...")

# View for successful payment page
def payment_success(request):
    return HttpResponse("Payment was successful!")

# Create your views here.
