from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
from django.contrib import messages


# Get all images and template with introduction
def communication_view(request):
    """
    Render the main/home page with list of images and an upload form.

    **Context**

    - `images`: A queryset of all instances of the model `communication.Image`.
    - `form`: An instance of the `ImageForm` class used for uploading images.

    **Template:**

    template:`communication/index.html`
    """
    
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
        "form": form},  # Pass the queryset and the form to the template
    )


# view for deleting an image
def delete_image(request, image_id):
    """
    Delete an image specified by its ID.

    Parameters:
    - `image_id`: The primary key of the `Image` instance to be deleted.

    Behavior:
    Deletes the specified image from the database and redirects to the main/home page with a success message.

    Redirects To:
    - `communication_home`: The main/home page.
    """
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    messages.success(request, "Image deleted successfully!")
    return redirect('communication_home')

# view to edit an image
def edit_view(request, image_id):
    """
    Edit an image specified by its ID.

    Parameter:
    - `image_id`: The primary key of the `Image¬ instance to be edited.

    Behavior:
    Edits an existing Image from the database and then redirects to home page with success message.

    Redirects To:
    - `communication_home`: The main/home page.
    """
    image = get_object_or_404(Image, id=image_id)
    queryset = Image.objects.all()  # Fetch all Image objects

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image) # Bind form with POST data and the image instance
        
        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully!")
            return redirect('communication_home')
        else:
            messages.error(request, "Failed to update image. Please try again.")
    else:
        # Pre-populate the form with the existing image data
        form = ImageForm(instance=image)

    return render(
        request,
        "communication/index.html",
        {
            "form": form, 
            "image": image,  # Pass the specific image being edited
            "images": queryset,  # Pass the full list of images for the gallery
        },
    )