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


// This section was added to resolve the issue of buttons making a jump to the top of the page. ChatGPT was used to help create initial code 
//and then reorganised and modified to suit project needs.

// event listener for form submission (image add form)
document.addEventListener('DOMContentLoaded', function () {
    const addImageForm = document.getElementById('addimage');
    const crudButtons = document.querySelectorAll('.image-item a.crudbtn'); // Select all crud buttons

    // Handle pagination links
    const paginationLinks = document.querySelectorAll('.pagination-controls a');
    paginationLinks.forEach(link => {
        link.addEventListener('click', function () {
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    });

     // Add click event listeners to all crud buttons
    crudButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Save a session storage flag to scroll back to the image gallery
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    });

    // Handle the 'Add Image' form submission
    if (addImageForm) {
        addImageForm.addEventListener('submit', function () {
            sessionStorage.setItem('scrollToImageGallery', 'true');
        });
    }

    // Check if the page is redirected after an edit operation
    if (sessionStorage.getItem('scrollToImageGallery') === 'true') {
        const gallerySection = document.getElementById('image-gallery');
        if (gallerySection) {
        // Scroll back to the image gallery section smoothly
            gallerySection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
            sessionStorage.removeItem('scrollToImageGallery'); // Clear the flag
    }
});

// Pop-up window section
document.addEventListener('DOMContentLoaded', function () {
    // Get references to the pop-up image and the confirm button
    const popUpImage = document.getElementById('pop-up-image'); // Pop-up image placeholder
    const confirmButton = document.getElementById('confirm-button'); // Confirm button
    // Select all gallery images
    const galleryImages = document.querySelectorAll('.image-item img');

    // Add click event listener to each gallery image
    galleryImages.forEach((img) => {
        img.addEventListener('click', function () {
            const imageUrl = img.src; // Get the image URL
            const imageTitle = img.alt; // Get the image title or alt text
            const popUpWindow = document.getElementById('pop-up'); // get pop up window 

            popUpWindow.style.display = 'block'; // Make the pop-up window visible

            if (popUpImage) {
                popUpImage.src = imageUrl; // Set the selected image in the pop-up
                popUpImage.alt = imageTitle; // Update alt text for accessibility
            } else {
                alert("Pop-up image placeholder not found!");
            }
        });
    });

    // Add click event listener to the confirm button
    confirmButton.addEventListener('click', function () {
        const popUpWindow = document.getElementById('pop-up'); // get pop up window 
        popUpWindow.style.display = 'none'; // Hide pop-up window
        if (popUpImage) {
            popUpImage.src = ""; // Clear the pop-up image
            popUpImage.alt = ""; // Clear the alt text
        }
    });
});
