from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
from django.contrib import messages


# Get all images and template with introduction
def communication_view(request):

    queryset = Image.objects.all()  # Fetch all Image objects
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully!")
            return redirect('communication_home')
        else:
            messages.error(request, "Failed to upload image. Please try again.")


    return render(
        request,
        "communication/index.html", 
        {"images": queryset,
        "form": form},  # Pass the queryset to the template
    )

# view for deleting an image
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    messages.success(request, "Image deleted successfully!")
    return redirect('communication_home')