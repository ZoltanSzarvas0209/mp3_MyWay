from django.shortcuts import render
from .models import Image


# Get all images and template with introduction
def communication_view(request):

    queryset = Image.objects.all()  # Fetch all Image objects


    return render(
        request,
        "communication/index.html", 
        {"images": queryset},  # Pass the queryset to the template
    )
