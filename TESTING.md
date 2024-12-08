![Mockup](static/images/am_i_responsive.png)


# MANUAL TESTING

### Testing Responsiveness

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Header Responsivness | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout | PASS |
| Footer Responsiveness | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Introduction Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Image Gallery Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Communication Board Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Contact Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Register Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS |
| Login Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 
| Logout Section | Developer Tools: 320px/375px/425px/768px/1024px/1440px | Fully Responsive Layout| PASS | 

</details>

### Testing Functionality of Buttons/Links

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Navigation Links | Click each link | Route to relevent page | PASS |
| Image Gallery - delete | click button | remove selected image | PASS |
| Image Gallery - edit | clcik button | fill "Add Image" section with details from selected image| PASS |
| Image Gallery - pagination controls | click all pagination buttons | next/previous/last/first buttons navigate to correvt page | PASS |
| Image Gallery - Add image | clcik add image button after with upload image section filled.| Image uploaded is added to Gallery| PASS |
| Image Gallery - Image/Schoose file | click on choose image | file browser pop up to select desired image | PASS |
| Image Gallery - image selection | clcik desired images in Gallery | image clicked is loaded in Communication board section| PASS |
| Communication Board - reset | click reset button | Images revert back to place holders in Communication Board Section | PASS | 
| Footer - Social links | click each social link | links should direct user to relevent page | PASS | 

</details>

### Testing Layout/Structure

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Layout header | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout footer | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Introduction Section | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Communication Board | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Image Gallery | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Image Gallery - Add Image | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Contact Us | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Register | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Login | visual inspection | page/feature to appear as expected/designed | PASS |
| Layout Logout | visual inspection | page/feature to appear as expected/designed | PASS |

</details>

### Form Validation testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Contact Form | Enter invalid input: No Title | No submission allowed - "Please fill in this field response" | PASS |
| Contact Form | Enter invalid input: No Content | No submission allowed - "Please fill in this field response" | PASS |
| Contact Form | Enter valid input | Submission allowed - "confirmation feedback" | PASS |
| AddImage Form | Enter invalid input: No Title | No submission allowed - "Please fill in this field response" | PASS |
| AddImage Form | Enter invalid input: No file | No submission allowed - "Please select a file" | PASS |
| AddImage Form | Enter invalid input: No Content | No submission allowed - "Please fill in this field response" | FAIL |
| AddImage Form(2) | Enter invalid input: No Content | No submission allowed - "Please fill in this field response" | PASS |
| AddImage Form | Enter valid input | Submission allowed - "confirmation feedback message" | PASS |


- One test failed: AddImage with no content was successfully submitted:
    - Solution: description = models.TextField(blank=True, null=True) 
    The above line in the Image model allowes the filled to be left empty. This was removed and re-test had passed.

</details>

### Browser Testing

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| Google Chrome | non scripted test of features on desktop | full functionality and compatibility with browser | PASS |
| Google Chrome | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |
| Microsoft Edge | non scripted test of features on desktop | full functionality and compatibility with browser | PASS |
| Microsoft Edge | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |
| Samsung Internet | non scripted test of features on mobile | full functionality and compatibility with browser | PASS |

</details>

### TESTING USER STORIES




# AUTOMATED TESTING

### HTML,CSS and JS validation

* HTML VALIDATION:    

W3C validators used for HTML and CSS and JsHint is used to validate JAvaScript.
    
-   <details> <summary> Initial validation </summary>
    <img src="static/images/html_validation/html_validation_initial.png">
    </details>

-   <details> <summary> PASSED VALIDATION </summary>
    <img src="static/images/html_validation/html_validation_passed.png">
    </details>

    1. trailing / from meta element removed.
    2. Alt atribute added to logo image.
    3. h1 element removed from article and added before it as section header.
    4. article element replaced with div element.

* CSS VALIDATION: 
    
-   <details> <summary> PASSED VALIDATION </summary>
    <img src="static/images/css_validation/css_validation.png">
    </details>

    1. validation passed on first attempt.

* JavaScript VALIDATION: 
    
-   <details> <summary> PASSED VALIDATION </summary>
    <img src="static/images/jshint_validation.png">
    </details>

    1. validation passed on first attempt.

## Lighthouse 

-   <details> <summary> INITIAL LIGHTHOUSE RESULTS </summary>
    <img src="static/images/initial_lighthouse_results.png">
    </details>

-   <details> <summary> IMPROVED LIGHTHOUSE RESULTS </summary>
    <img src="static/images/improved_lighthouse_results.png">
    </details>

-   <details> <summary> FINAL LIGHTHOUSE TESTS </summary>
    <img src="static/images/lighthouse_bestpractises.png">
    </details>

    1. refactored complete style.css file with the use of ChatGPT to completly eliminate unused and duplicate code.
    2. used https://coolors.co/contrast-checker/305b5f-ffffff to find more suitable color for navigation links to improve contrast.
    3. Best PRactises results came in low due to Cloudinary cookies and http , unsecure requests being used.
        - Following code was used in settings.py to force cloudinary to use https:
        import cloudinary
        cloudinary.config(secure=True)
