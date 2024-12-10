from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
from django.contrib import messages
from django.core.paginator import Paginator, Page
from django.urls import reverse
from django.http import QueryDict


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
    # Fetch all Image objects
    queryset = Image.objects.all()
    # Paginate the queryset with 4 images per page
    paginator = Paginator(queryset, 4)
    # Get the current page number from the request
    page_number = request.GET.get('page')
    # Get the page object
    page_obj = paginator.get_page(page_number)
    form = ImageForm()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully!")
            return redirect('communication_home')
        else:
            messages.error(request, "Failed to upload image.Please try again.")

    return render(
        request,
        "communication/index.html",
        # Pass the paginated images instead of the full queryset
        # and pass the form to the template.
        {"images": page_obj,
         "form": form, }
    )


# view for deleting an image
def delete_image(request, image_id):
    """
    Delete an image specified by its ID.

    Parameters:
    - `image_id`: The primary key of the `Image` instance to be deleted.

    Behavior:
    Deletes the specified image from the database and
    redirects to the main/home page with a success message.

    Redirects To:
    - `communication_home`: The main/home page.
    """
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    messages.success(request, "Image deleted successfully!")

    url = reverse('communication_home') + '#image-gallery'
    return redirect(url)


# view to edit an image
def edit_view(request, image_id):
    """
    Edit an image specified by its ID.

    Parameters:
    - `image_id`: The primary key of the `Image` instance to be edited.

    Behavior:
    Allows the user to update the details of an existing image,
    including its title and file.
    If the form is valid, the changes are saved,
    a success message is displayed,
    and the user is redirected to the main/home page with
    the updated gallery section visible.

    Redirects To:
    - `communication_home`: The main/home page with a `#image-gallery`
    fragment and the correct page number.
    """
    image = get_object_or_404(Image, id=image_id)
    queryset = Image.objects.all()
    page_number = request.GET.get('page', 1)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)

        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully!")

            # Set session flag to scroll to image gallery
            request.session['scrollToImageGallery'] = True

            # Redirect to the gallery section with page number
            url = reverse('communication_home') \
                + f'?page={page_number}#image-gallery'
            return redirect(url)
        else:
            messages.error(request, "Failed to update image.Please try again.")
    else:
        form = ImageForm(instance=image)

    paginator = Paginator(queryset, 4)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "communication/index.html",
        {
            "form": form,
            "image": image,
            "images": page_obj,
        },
    )
