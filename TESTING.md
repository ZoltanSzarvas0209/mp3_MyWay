![Mockup](static/images/am_i_responsive.png)

# TABLE OF CONTENT

1. [ Manual Testing ](#manual)
2. [ Automated Testing ](#auto)
3. [ Bugs and Fixes ](#bugs)

# MANUAL TESTING <a name="manual"></a>

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

<details>

| **Feature** | **Test Method** | **Expectation** | **Outcome** |
|-------------|-----------------|-----------------|-------------|
| User Story 1 | visual checking | introduction section is available and clearly explains the purpose of the site. | PASS |
| User Story 2 | Upload a test image, edit said image and then delete it | all CRUD functionality working and easy to use | PASS |
| User Story 3 | visual inspection | image gallery available in a paginated format | PASS |
| User Story 4 | visual inspection for the communication board section and click images to test functionality | clciked images to appear on communication board | PASS |
| User Story 5 | click reset button to clear board. | communication board to reset to default placeholder images. | PASS |
| User Story 6 | Navigate to relevant pages, register a dummy account | able to register an account and login as | PASS |
| User Story 7 | visual inspection | contact page is available through navigation and is presenting a contact form | PASS |
| User Story 8 | fill in contact form with dummy information | feedback that message was sent to be presented to user | PASS |
| User Story 9 | Superuser feature, login to Djangos admin site | all message submitted available for review. | PASS |

- User story 6 , Criteria 3 is not fullfilled and is part of future improvement recommendations as it was out of the scope of this project.

</details>




# AUTOMATED TESTING <a name="auto"></a>

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

## PEP8 , python validation:

* Communication App:  No mayor errors, several whitespaces needed clearing, a few line of code were too long and some indentation needed adjusting.

-   <details> <summary> PASSED VALIDATION forms.py </summary>
    <img src="static/images/pep8validation/communication_forms.png">
    </details>

-   <details> <summary> PASSED VALIDATION models.py </summary>
    <img src="static/images/pep8validation/communication_model.png">
    </details>

-   <details> <summary> PASSED VALIDATION views.py </summary>
    <img src="static/images/pep8validation/communication_views.png">
    </details>

-   <details> <summary> PASSED VALIDATION test_forms.py </summary>
    <img src="static/images/pep8validation/communication_test.png">
    </details>

* Contact App: Cleared validation

-   <details> <summary> PASSED VALIDATION forms.py </summary>
    <img src="static/images/pep8validation/contact_form.png">
    </details>

-   <details> <summary> PASSED VALIDATION models.py </summary>
    <img src="static/images/pep8validation/contact_model.png">
    </details>

-   <details> <summary> PASSED VALIDATION views.py </summary>
    <img src="static/images/pep8validation/contact_views.png">
    </details>

-   <details> <summary> PASSED VALIDATION test_forms.py </summary>
    <img src="static/images/pep8validation/contact_test.png">
    </details>

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

## Django Automated Tests

- Django's Testing library was used to test Projects's forms. Corresponding PEP8 validation listed in PEP8 section above. Each form was tested with 3 tests.

-   <details> <summary> Communication App's form </summary>
    <img src="static/images/django_test1.png">
    </details>

-   <details> <summary> Communication App's form </summary>
    <img src="static/images/django_test2.png">
    </details>


# Bugs and Fixes <a name="bugs"></a>

Bugs found during development:

1. delete and edit functions direct back to the top of the page:

- solution: JavaScript added to implement required functionality.


2. edit function when triggered overwrites pagination and image gallery gets out of context.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_2.png">
    </details>

- solution: following code was addedmodified to rectify the issue. in communication/views.py 
if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)

        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully!")

            # Set session flag to scroll to image gallery
            request.session['scrollToImageGallery'] = True

            # Redirect to the gallery section with page number
            url = reverse('communication_home') + f'?page={page_number}#image-gallery'
            return redirect(url)
        else:
            messages.error(request, "Failed to update image. Please try again.")
    else:
        form = ImageForm(instance=image)

    paginator = Paginator(queryset, 4)
    page_obj = paginator.get_page(page_number)


3. add image section is not fitting in well with the design and pushes other elements out of place on laptop size(1024px).

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_3.png">
    </details>

4. main section pushed out of alignment.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_4.png">
    </details>

issue found: style.css , section styling's width settings coused the issue.

solution: removed styling to re-align elements.

5. Django messages out of alignment. : 

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelpment_issue_5.png">
    </details>

Solution: text-center class added to div with id="msg"

6. Add Image section squashed above 425px.

bootstrap classes initially applied were md-10 and md-2 respectively to section image gallery and add image.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_6.png">
    </details>

solution: classes modified to a md- 7 , md-5 ratio.


7. Register section: username, email and input fields should be in different rows under 425px.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_7.png">
    </details>

solution: css styling added to resolve issue
@media (max-width: 425px) {
    .signup p {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
}

8. Login section: username and password fields should be displayed in seperate rows under 425px.

-   <details> <summary> Image of issue </summary>
    <img src="static/images/bugs/duringdevelopment_issue_8.png">
    </details>

solution: css styling applied to login.html's form

    .login p {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

9. Register and Login pages cruashed after Deployment:

following error message was presented with DEBUG set to True in settings.py:

Exception Type:	DoesNotExist
Exception Value:	
Site matching query does not exist.
Exception Location:	/workspace/.pip-modules/lib/python3.12/site-packages/django/db/models/query.py, line 637, in get
Raised during:	allauth.account.views.LoginView
Python Executable:	/home/gitpod/.pyenv/versions/3.12.2/bin/python3

The error suggest there is no site object in the database that maches the domain.

Troubleshooting:
1. double checked all installed apps present as required in settings.py:
    'django.contrib.sites',
    'allauth',
    'allauth.account',

2. MAde sure SITE_ID is set to 1.

3. Used ChatGPT to guide me through checking for the site object using the Django shell:

- from django.contrib.sites.models import Site
    try:
    site = Site.objects.get(id=1)
    print(f"Site found: {site.domain}, {site.name}")
    except Site.DoesNotExist:
    print("No Site object with id=1 exists.")

No site object was found.

- from django.contrib.sites.models import Site
    Site.objects.create(
    id=1,
    domain='8000-zoltanszarvas0-mp3myway-n5zd8ad8dor.ws.codeinstitute-ide.net',
    name='MyWay'
    )
    print("Site object created.")

Created new Site object , Following this the issue was resolved in production enviroment.

- On re-check now the site object was found, so made migratitions to update database. Here I also run makemigrations as found that earlier changes in model.py was not migrated.(default cloudinary image).

