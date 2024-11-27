// this code was fixed with the use of chatGPT, functionality to handle images were implemented that way.

document.addEventListener('DOMContentLoaded', function () {
    // Get references to slots and the reset button
    const slots = document.querySelectorAll('.slot img');
    const resetButton = document.getElementById('reset-button');

    // Select all gallery images
    const galleryImages = document.querySelectorAll('.image-item img');

    // Function to handle image selection
    galleryImages.forEach((img) => {
        img.addEventListener('click', function () {
            const imageUrl = img.src; // Get the image URL
            const imageTitle = img.alt; // Get the image title or alt text

            // Find the first empty slot (a slot still showing the placeholder image)
            const emptySlot = Array.from(slots).find(slot =>
                slot.src.includes('placeholder.jpg')
            );

            if (emptySlot) {
                emptySlot.src = imageUrl; // Set the selected image in the slot
                emptySlot.alt = imageTitle; // Update alt text for accessibility
            } else {
                alert("All slots are full! Reset to add new images.");
            }
        });
    });

    // Reset button functionality
    resetButton.addEventListener('click', function () {
        slots.forEach(slot => {
            // Reset all slots to the placeholder image
            slot.src = '/static/images/placeholder.jpg';
            slot.alt = "Empty Slot"; 
        });
    });
});


// This section was added to resolve the issue of buttons making a jump to the top of the page. ChatGPT was used to create the below code.

// event listener for form submission (image add form)
document.addEventListener('DOMContentLoaded', function () {
    const addImageForm = document.getElementById('addimage');
    
    // Check if the page is redirected after editing or adding an image and scroll back to the gallery
    if (sessionStorage.getItem('scrollToImageGallery') === 'true') {
        const gallerySection = document.getElementById('image-gallery');
        if (gallerySection) {
            gallerySection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        sessionStorage.removeItem('scrollToImageGallery'); // Clear the flag
    }

    // Handle pagination links
    const paginationLinks = document.querySelectorAll('.pagination-controls a');
    paginationLinks.forEach(link => {
        link.addEventListener('click', function () {
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    });

    // Handle form submissions (e.g., delete image)
    const deleteForms = document.querySelectorAll('form[action*="delete_image"]');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function () {
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    });

    // Handle the 'Add Image' form submission
    if (addImageForm) {
        addImageForm.addEventListener('submit', function () {
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    }
});
