# Introduction


## Live site link here


## Repository link here


## Table of contents

 1. [ UX ](#ux)
 2. [ Technologies and Tools ](#technologies)    
 3. [ Research ](#research) 
 4. [ Target Audience ](#audience)  
 5. [ User Stories ](#user)
 6. [ Planning, Structure and Design ](#design)
     - [ Iterations ](#iterations)
     - [ Layout ](#layout)
     - [ Features ](#features)
     - [ Design Choices ](#designchoice)
     - [ Wireframes ](#wireframes)
     - [ Database ](#database)
        - [ Entity Relationship Diagram ](#erd) 
 7. [ Deployment ](#deployment)
 8. [ Testing/Bugs/Fixes ](#testing)
     - [ HTML,CSS and JS Validation](#htmlandcss)
     - [ Manual Testing ](#alltesting)
          - [ Pre-deployment ](#predeployment)
          - [ post-deployment ](#postdeployment)
     - [ User Testing ](#usertest)
     - [ Accessibility ](#access)
 9. [ Media ](#media)
 10. [ Credits ](#credit)  

## UX <a name="ux"></a>


### Technologies and Tools Used <a name="technologies"></a>

<details><summary> Technologies </summary>

* Languages

    * HTML
    * CSS
    * JavaScript
    * Python
    * DTL - Django Template Language

* Version Control

    * Git
    * Github
    * Gitpod
    * Heroku

* Frameworks

    * Django
    * Bootstrap

* Database

    * PostgreSQL


* Additional resources

    * Coolors: https://coolors.co/ 
    * FontAwesome: https://fontawesome.com/search?o=r&m=free&s=solid
    * Perplexity: perplexity.ai
    * ChatGPT: https://chat.openai.com/
    * Google Fonts: https://fonts.google.com/
    * W3School: https://www.w3schools.com/

* Testing

    * Google Lighthouse
    * JSHint: https://jshint.com/
    * JSLint: https://www.jslint.com/
    * W3C HTML Validator: https://validator.w3.org/
    * W3C CSS Validator: https://jigsaw.w3.org/css-validator/

</details>

### Research <a name="research"></a>

### Target Audience <a name="audience"></a>

* This app is made for children who cannot speak, including those with autism, speech delays, or other challenges. It helps them express their needs, feelings,
 and thoughts using simple communication or picture cards. The app also supports parents, caregivers, and teachers by making it easier to communicate and connect with these children.

### User Stories <a name="user"></a>

<details><summary> USER STORIES </summary>

* User story 1:

    - As a user, I want to view an introduction section explaining the purpose of the app:

    1. Acceptance criteria : when the site is loaded, the user is presented with an introduction explaining the purpose of the site.

* User story 2:

    - As a user, I want to upload, edit, and delete images in the gallery so that I can manage my content:
    
    1. Acceptance criteria : I can upload a new image to the gallery.
    2. Acceptance criteria : An unwanted image can be removed/deleted from the gallery.
    3. Acceptance criteria : I can edit/replace the image and or it's title.

* User story 3:

    - As a user, I want to view the image gallery in a paginated format to navigate easily.
    
    1. Acceptance criteria : when the site is loaded, an image gallery is available with communication cards.
    2. Acceptance criteria : the images are displayed in a paginated format.

* User story 4:

    - As a user, I want to select up to 3 images from the gallery to showcase in a special section.
    
    1. Acceptance criteria : A section is available with empty image slots for communication.
    2. Acceptance criteria : When the slots are clicked the images tore is available to choose desired image from. 

* User story 5: 

    - As a user, I want to remove images from the showcase section so that I can update it as needed.
    
    1. Acceptance criteria : When all slots are filled the image can be removed/replaced. 

* User story 6:

    - As a user, I want authentication features so that I can log in, sign up, and manage content securely.
    
    1. Acceptance criteria : When visiting the site, a login link is available to submit my details
    2. Acceptance criteria : A register link is available to sign up as a new user.
    3. Acceptance criteria : When a user logs in, previously selected images are available in the Display section. 

* User story 7:

    - As a user, I want to view a contact page header with an image and description.
    
    1. Acceptance criteria : when visiting the site, a contact link is available in navigation bar and is presenting a contact form for the user. 

* User story 8:

    - As a user, I want to fill out a contact form with my name, email, and message
    
    1. Acceptance criteria : visiting the contact page should present a form that is sent for admin review.

* User story 9:

    - As an admin, I want to view submitted contact form entries in the admin panel.
    
    1. Acceptance criteria : AS an admin I should be seeing submitted contact requests.

</details>

## Planning, Structure and Design <a name="design"></a>


### Iterations <a name="iterations"></a>

#### MoSCoW Prioritization

<details>

| **User Story** | **Story Points** | **Priority** | **Notes** |
|-------------|-----------------|-----------------|-------------|
| 1. Introduction Section | 2 | Must Have | Static content- introduction |
| 2. Gallery Managemennt | 8 | Must Have | Full CRUD Functionality for managing images |
| 3. View Image Gallery | 5 | Must Have | Paginated image display |
| 4. Display Section | 8 | Must Have | Communication board to showcase selected images |
| 5. Update Display | 3 | Must Have | Remove and Add images in Display section |
| 6. Authentication | 5 | Should Have | Should have authentication using Django's AllAuth |
| 7. Contact Page | 3 | Could Have | Static contact for contact information |
| 8. Contact Form | 5 | Could Have | Saves form entries to database |
| 9. Contact Page Admin | 3 | Could Have | Admin view for enquiries |


</details>

#### Iterations Summary

<details>

| **Iteration** | **Features** | **Story Points** | **MoSCoW Focus** |
|-------------|-----------------|-----------------|-------------|
| Iteration 1 | Introduction, Gallery Managment and Image Gallery | 15 | Must Have |
| Iteration 2 | Display Section,Update Display and Authentication | 16 | Must Have and Should Have |
| Iteration 3 | Contact Page , Form and Admin | 11 | Could Have |

</details>

### Layout: <a name="layout"></a>

### Design Choices: <a name="designchoice"></a>

* Colors: Coolors (https://coolors.co/) palette generator was used on the logo designed to pick the below colors for the project. 

-  #C7DA31  - PEAR
-  #B1C2C3  - ASH GREY
-  #689CA0  - MOONSTONE
-  #FFFFFF  - WHITE
-  #D7E46D  - MINDARO



* Font family: 

- I picked the "Parkinsans" font family with san-serif as a fall back.


### Features: <a name="features"></a>

### Wireframes: <a name="wireframes"></a>

### Database: <a name="database"></a>

#### Entity Relationship Diagram: <a name="erd"></a>


## Deployment <a name="deployment"></a>


## Testing/Bugs/Fixes <a name="testing"></a>

Notes for testing:

Bugs found during development:
1. delete and edit functions direct back to the top of the page:

2. edit function when triggered overwrites pagination and image gallery gets out of context.

3. add image section is not fitting in well with the design and pushes other elements out of place.

4. Main functionality is not reasonable/inconvinient to use --- will address this if times allow it ,however I think the app is not designed for mobile size


### HTML,CSS and JS validation: <a name="htmlandcss"></a>

### Manual Testing <a name="alltesting"></a>

### Initial testing items below arose during development and most were dealt with at the time.  <a name="predeployment"></a>

### Form Validation testing

### User Testing <a name="usertest"></a>


## Accesibility <a name="access"></a>


## Media <a name="media"></a>


## Credits <a name="credit"></a>


## Acknowledgement
            
