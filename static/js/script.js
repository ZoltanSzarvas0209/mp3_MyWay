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