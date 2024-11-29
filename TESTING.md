# KnitSpace Testing

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
    1. [Blog Accessibility](#blog-accessibility)
    2. [Account Management](#account-management)
    3. [Dashboard Management](#dashboard-management)
    4. [Content Management](#content-management)
    5. [Engagement and Information](#engagement-and-information)
2. [Code Validation](#code-validation)
    1. [HTML](#html)
    2. [CSS](#css)
    3. [JavaScript](#javascript)
    4. [Python](#python)
3. [Manual Testing](#manual-testing)
    1. [General](#general)
    2. [Admin Features](#admin-features)
    3. [Account Management](#account-management)
    4. [Pages](#pages)
4. [Device and Browser Testing](#device-and-browser-testing)
    1. [Device Compatibility](#device-compatibility)
    2. [Browser Compatibility](#browser-compatibility)
5. [Bugs](#bugs)
6. [Accessibility](#accessibility)

## Testing User Stories

### Blog Accessibility
As a **guest user**, I can **view blog posts without the need to log in or register** so that **I can freely access content on the site**.
- Blog posts are available without users needing to create an account or log in.
- Previews of each post are available on the home page.
- Navigation on the bottom of the page allows users to browse previews across multiple pages.

As a **guest user**, I can **click on a post preview** so that **I can open the full post and read it in detail**.
- Previews of each post are available on the home page.
- Clicking on a preview opens a full-page view of the post.
- A *Back* button allows users to return to their previous spot after viewing the full-page post.

As a **registered user**, I can **access exclusive content** so that **I can engage with the community and share information**.
- Only registered and logged-in users can access and update their Dashboard.
- Only registered and logged-in users can create, edit, or delete posts.

**Note**: Due to time constraints, the ability for logged-in users to create and edit comments and / or participate in forum discussions, which was part of this User Story, has not been implemented.

### Account Management

As a **guest user**, I can **create an account** so that **I can have a personalized experience and access member-only features.**.
- Users can create an account using their email address.
- Users are provided with feedback messages for invalid form inputs.
- Users do not receive a confirmation email after successful registration.

As a **registered user**, I can **log in to my account** so that **I can access my Dashboard and other member-only features**.
- Users can log into their accounts using their username and password.
- Users are redirected to the home page after logging in.
- Logged-in users can access more sites and features than guest users, such as their Dashboard and the ability to create, edit, and delete posts.

As a **registered user**, I can **log out of my account** so that **I can ensure my account security and privacy**.
- Users can log out of their accounts.
- Users need to confirm that they want to log out before being logged out.
- Users are redirected to the home page after logging out.

### Dashboard Management

As a **registered user**, I can **save posts to my Dashboard** so that **I can easily access my favorite content**.
- A link to the Dashboard is visible in the navigation bar for logged-in users.
- A button to save a blog post is visible for logged-in users on the full-page blog post.
- The blog post will appear on the user's Dashboard once saved.
- A feedback message indicates a post has been saved successfully.

As a **registered user**, I can **rearrange my saved posts** so that **arrange my content board according to my preferences**.
- Saved posts are presented as a list.
- Using AJAX drag and drop, users can move their saved posts to a different position.
- Drag-and-drop functionality is implemented on desktop and mobile devices.

**Note**: When reloading a page after rearranging the order of saved posts, the new order does not remain.

As a **registered user**, I can **delete saved blog posts from my Dashboard** so that **I can manage my content board**.
- Each saved blog post preview displays a *Delete* button.
- When clicked, the corresponding blog post is removed from the Dashboard.
- A feedback message indicates a post has been deleted successfully.

As a **registered user**, I can **click on a saved post preview** so that **I can open the full post and read it in detail**.
- Saved blog posts appear as previews on the Dashboard.
- When clicking on the preview, the user is redirected to the full-page view of the post. 
- A *Back* button returns users to their Dashboard from the full-page view.

### Content Management

As a **registered user**, I can **create a new blog post** so that **I can share my knitting experiences and tips with the community**.
- A form to create a new blog post is available for logged-in users.
- A WYSIWYG editor is provided to improve the users' experience.
- Users can upload an optional image to their post. A placeholder image is provided where users choose not to upload a custom image.
- Users are redirected to the full-page view of their newly created post after successful submission.

As a **registered user**, I can **update my existing blog posts** so that **I can correct or update the content I have shared with the community**.
- Logged-in users see an *Edit* button on posts that they authored.
- A WYSIWYG editor is provided to improve the users' experience.
- After submission, a user feedback message informs users that their post has been updated successfully.
- After submission, users are redirected to the full-page view of their updated post.

As a **registered user**, I can **delete my blog posts** so that **I can remove content that I no longer want to share with the community**.
- Logged-in users see a *Delete* button on posts that they authored.
- After submission, a user feedback message informs users that their post has been deleted successfully.
- After submission, users are redirected to the home page.

As a **registered user**, I can **access and manage all my authored posts from a central page** so that **I can efficiently maintain and update my content**.
- Users can access a list of all their authored posts from their account drop-down menu. 
- Users can open, update, or delete each post straight from their post list. 
- Users can easily switch between views of their authored and saved posts. 

### Engagement and Information

As a **guest user**, I can **submit a contact form** so that **I can communicate with the support team for inquiries or feedback**.
- The Contact Us form is available to guest users.
- Users can submit a request by entering their name, email address, and message.
- Incoming contacts can be handled in the */admin* section of the project.

As a **guest user**, I can **learn about Frau Wolle's knitting journey and experiences** so that **I feel connected to the community and inspired to engage with the content**.
- The *About* page is available to view without needing to create an account or log in.
- Users can learn more about Frau Wolle and her knitting journey by reading her short biography and viewing an image of her.

[Back to top ⇧](#knitspace-testing)

## Code Validation

### HTML

[W3C Markup Validator](https://validator.w3.org/) was used to validate the HTML code of each templated page. HTML validation was performed via source code text input.

| Tested | Result | View Result | Pass |
--- | --- | --- | ---
|Home | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|About | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Contact Us | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Dashboard | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|My Posts | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Full Page Post View | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Create Post | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Edit Post | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Sign In | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Sign Up | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|Sign Out | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |
|404 | No errors or warnings to show. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/no-errors-html-validation.png)</details>| Pass |


### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the custom CSS code.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|style.css | No Error Found. | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/css-validation.png)</details>| Pass |


### JavaScript

[JSHint](https://jshint.com/) was used to validate the custom JavaScript code.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|script.js | No errors | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/js-validation.png)</details>| Pass |


### Python

[PEP8 Online Check](https://pep8ci.herokuapp.com) was used to validate the custom Python code.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|about/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-admin-validation.png)</details> | Pass |
|about/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-models-validation.png)</details> | Pass |
|about/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-urls-validation.png)</details>| Pass |
|about/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/about-views-validation.png)</details>| Pass |
|blog/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/blog-admin-validation.png)</details>| Pass |
|blog/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/blog-forms-validation.png)</details>| Pass |
|blog/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/blog-models-validation.png)</details>| Pass |
|blog/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/blog-urls-validation.png)</details>| Pass |
|blog/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/blog-views-validation.png)</details>| Pass |
|contact/admin.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-admin-validation.png)</details> | Pass |
|contact/forms.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-forms-validation.png)</details> | Pass |
|contact/models.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-models-validation.png)</details> | Pass |
|contact/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-urls-validation.png)</details> | Pass |
|contact/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/contact-views-validation.png)</details> | Pass |
|dashboard/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/dashboard-urls-validation.png)</details>| Pass |
|dashboard/views.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/dashboard-views-validation.png)</details>| Pass |
|knitspace/settings.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/knitspace-settings-validation.png)</details>| Pass |
|knitspace/urls.py | All clear, no errors found | <details><summary>Validation Image</summary>![Result](assets/readme-files/code-validations/knitspace-urls-validation.png)</details>| Pass |

[Back to top ⇧](#knitspace-testing)

## Manual Testing

### General

#### Header

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Logo | Click on logo redirects user to homepage | Pass | |
| Navigation Bar | Click on page name redirects user to corresponding page | Pass | |
| Navigation Bar | Available links depend on user status | Pass | *Dashboard* link is only visible to logged-in users | 
| Navigation Bar | Active page links change color | Pass | | 
| Admin Dropdown | Display of dropdown depends on user status | Pass | Logged-in users see a peronalized greeting|
| Admin Dropdown | Available links depend on user status | Pass | Logged-in users see links to *My Posts*, *Dashboard*, and *Create New Post* |
| Admin Dropdown | Logging menu depend on user status | Pass | Logged-in users see *Sign Out* rather than *Sign In* and *Sign Up* |
| Hero Image | Greeting on the image is only visible on homepage | Pass | |

#### Footer

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Social Media links | Click on icon redirects user to corresponding page | Pass | |
| Social Media links | Social Media pages open in new tab | Pass | For the purposes of this project, the login pages of each Social Media site have been provided |

### Admin Features

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Create Superuser | A Superuser is created | Pass | |
| Manage users | New users can be created, updated, and deleted | Pass | |
| Manage posts | New posts can be created, updated, and deleted | Pass | |
| Manage contacts | Incoming contacts can be viewed and edited | Pass | |
| Manage *About* content | The Superuser can edit the contents of the *About* page | Pass | |

### Account Management

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| *Sign Up* page | Users can create a new account using their email address | Pass | Confirmation emails are not provided at the moment |
| *Sign In* page | Users can sign in using their username and password | Pass | |
| *Sign Out* page | Users can sign out of their account | Pass | |

### Pages

#### *Home* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Post Previews | Posts are shown as preview cards, displaying the image, title, author, date, and excerpt | Pass |  |
| Default Image | Posts displayed with a default image if no custom image has been provided | Pass |  |
| Clickable Cards | Clicking on a preview card will open the full-page post view | Pass |  |
| Pagination | Users can browse posts across multiple pages | Pass |  |

#### *About* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| *Return* Button | Users will be returned to their previous place of browsing | Pass |  |
| Availability | Users can access the *About* page without needing to log in | Pass |  |
| Backend Management | The contents of the *About* page can be managed in the */admin* panel |  |

#### *Contact Us* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Form | An empty form is loaded for users to fill out | Pass |  |
| Form Validation | Valid information has to be provided in all fields before successful submission | Pass |  |
| *Confirmation* Message | A feedback message is displayed to the user after successul form submission | Pass |  |
| *Take Me Home* Button | Users are redirected to the homepage | Pass |  |

#### *Full-Page Post Views* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Full-Page View | Blog posts are displayed on a full page, showing the title, author, date, and content | Pass |  |
| Image Display | Only custom images are displayed | Pass |  |
| *Save to Dashboard* Button | Blog posts are saved to the Dashboard | Pass | This button is only available after successful login |
| *Confirmation* Message | A feedback message is displayed after saving a post to the Dashboard | Pass |  |
| *Return* Button | Users are redirected to the homepage | Pass | After a feedback message is displayed, users have to doubleclick this button to return to the homepage |
| *Action* Dropdown - Edit Post | Users get redirected to the *Edit Your Post* page | Pass | The dropdown is only visible to the author of a post |
| *Action* Dropdown - Delete Post | A *Confirmation* modal pops up asking users to confirm post deletion | The dropdown is only visible to the author of a post |

#### *Create a New Post* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Form | An empty form is loaded | Pass |  |
| Text Editor | Users can apply stylings to the content of their posts using the editor | Pass |  |
| *Back* button | Users can discard their changes | Pass |  |
| Title | Users need to choose a unique title for their post | Pass | An error message will appear if the title is not unique |
| Optional excerpt | Posts can be created without an excerpt | Pass |  |
| Optional image | Posts can be created without an image | Pass |  |
| *Account* Dropdown | Users can access this page from the account dropdown | Pass | The link only appears to logged-in users|
| *Confirmation* Message | A confirmation message displays after successfully creating a post | Pass |  |
| Full-Page Post Redirection | Users get redirected to the full-page post view after successfully creating a post | Pass |  |

#### *Edit Your Post* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| Form | The form is prepopulated with the existing information | Pass |  |
| Text Editor | Users can apply stylings to the content of their posts using the editor | Pass |  |
| *Back* button | Users can discard their changes | Pass |  |
| Title | Users need to choose a unique title for their post | Pass | An error message will appear if the title is not unique |
| Optional excerpt | Posts can be created without an excerpt | Pass |  |
| Optional image | Posts can be created without an image | Pass |  |
| *Action* Dropdown | Users can access this page from the action dropdown appearing on posts | Pass | The dropdown only appears to the author of a post on the full-page view or the *My Post* list |

#### *My Posts* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| List View | Users can view all their authored posts in one place | Pass |  |
| List View | Newly authored posts automatically appear here | Pass |  |
| Preview Cards | Authored posts appear as preview cards showing the titlle and creation date of each post | Pass |  |
| *Action* Dropdown | Users can choose to view, edit, and delete each post | Pass |  |
| *Confirmation* Modal | Before deleting a post, users will be asked to confirm in a modal | Pass | Clicking outside of the modal will close the modal |
| *Switch to Dashboard* Button | Users will be redirected to the *Dashboard* page | Pass |  |
| *Create a New Post* Button | Users will be redirected to the *Create a New Post* page | Pass |  |
| *Confirmation* Modal | Before deleting a post, users will be asked to confirm in a modal | Pass | Clicking outside of the modal will close the modal |

#### *Dashboard* 

| Element | Expected Outcome | Pass/Fail | Notes |
|---|---|---|---|
| List View | Users can view all their saved posts in one place | Pass |  |
| List View | Saved posts automatically appear on the Dashboard | Pass |  |
| Preview Cards | Saved posts appear as preview cards showing the titlle, author, and creation date of each post | Pass |  |
| *Delete* Button | Posts will be removed from the Dashboard | Pass |  |
| *Switch to My Posts* Button | Users will be redirected to the *My Posts* page | Pass |  |
| Navigation Bar Link | The link is only visible after successful login | Pass |  |
| Drag and Drop | Users are able to rearrange their saved posts using drag and drop functionality | Pass |  |
| Drag and Drop | The updated oder remains between visits | Fail |  The updated order reverts back after refreshing the page |

[Back to top ⇧](#knitspace-testing)

## Device and Browser Testing

### Device Compatibility

Device | Outcome | Pass/Fail
| --- | --- | --- |
| iPhone 13 Mini | No issues with appearance, responsiveness, or functionality. | Pass |
| iPad 9th Generation | No issues with appearance, responsiveness, or functionality. | Pass |
| iPad Pro (9.7-inch) | No issues with appearance, responsiveness, or functionality. | Pass |
| MacBook Air 13" | No appearance, responsiveness, or functionality issues. | Pass |
| Asus Vivobook Pro 15 | No appearance, responsiveness, or functionality issues. | Pass |
| Black Shark PAR-HOA | No issues with appearance, responsiveness, or functionality. | Pass |
| Samsung Galaxy S23 | No issues with appearance, responsiveness, or functionality. | Pass |

**Note**: When viewing *My POsts* on mobile and tablet devices, the dropdown button overlaps the post title for longer titles. However, this has no impact on the functionality.

### Browser Compatibility

Browser | Outcome | Pass/Fail
| --- | --- | --- |
| Safari | No appearance, responsiveness, or functionality issues. | Pass |
| Google Chrome | No appearance, responsiveness, or functionality issues. | Pass |
| Microsoft Edge | No appearance, responsiveness, or functionality issues. | Pass |
| Mozilla Firefox | No appearance, responsiveness, or functionality issues. | Pass |
| JoyUI Native Browsers | No appearance, responsiveness, or functionality issues. | Pass |

[Back to top ⇧](#knitspace-testing)

## Bugs

| Feature | Bug | Fix |
|---|---|---|
|Hover effect for preview cards | In the deployed version, the preview cards do not appear to lift when hovered over. However, the effect works as expected on the local server. | Fixed |
|Random messages | Feedback messages detailing the last steps a user has taken are shown ahead of the feedback message for saving/deleting a post. | Fixed |
|Saving updated post order | The updated order of a user's saved posts on their Dashboard does not remain after reloading the page| Not fixed |
|404 page after post deletion | If a user double clicks on a post's *Delete* button (saved or authored), they get redirected to a 404 page. The post is still deleted.| Not fixed |
|Return to the previous page | Where the *Return* button takes users back to their previous location rather than a specific page, they have to click twice if a feedback message has been displayed. | Not fixed |

[Back to top ⇧](#knitspace-testing)

## Accessibility

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) in [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to measure the page's quality, focusing on performance, accessibility, best practices, and SEO scores.
<br>
The scores are ordered as *Performance* - *Accessibility* - *Best Practices* - *SEO*.

| Tested | Result | View Result | Pass/Fail |
--- | --- | --- | ---
|Home | 79 - 93 - 74 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/home-lighthouse.png)</details>| Pass |
|About | 80 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/about-lighthouse.png)</details>| Pass |
|Contact Us |  | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/contact-lighthouse.png)</details>| Pass |
|My Posts | 86 - 86 - 100 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/my-posts-lighthouse.png)</details>| Pass |
|Dashboard | 84 - 93 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/dashboard-lighthouse.png)</details>| Pass |
|Full Page Post View | 85 - 95 - 78 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/view-post-lighthouse.png)</details>| Pass |
|Create Post | 87 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/create-post-lighthouse.png)</details>| Pass |
|Edit Post | 87 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/edit-post-lighthouse.png)</details>| Pass |
|Sign In | 87 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-in-lighthouse.png)</details>| Pass |
|Sign Up | 88 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-up-lighthouse.png)</details>| Pass |
|Sign Out | 86 - 95 - 96 - 100 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/sign-out-lighthouse.png)</details>| Pass |
|404 | 89 - 100 - 96 - 90 | <details><summary>Lighthouse Image</summary>![Result](assets/readme-files/lighthouse-reports/404-lighthouse.png)</details>| Pass |

[Back to top ⇧](#knitspace-testing)
<br>
<br>
[Return to Main Readme](README.md)