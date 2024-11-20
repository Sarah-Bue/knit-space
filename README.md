# KnitSpace

![Mock Up Image]()

KnitSpace is a vibrant online community for knitters of all levels to come together to share, learn, and connect. Blog posts on a wide variety of knitting-related topics are available to browse without the need to log in. Users also have the option to create an account and save their favourite posts to their own dashboard and review them with ease. 

Visit the deployed application [here](https://knit-space-57239e7d6ce8.herokuapp.com/).

## Project Planning 

### Agile Methodology

Agile methodology played a crucial role in managing the development process. The project was divided into multiple, smaller sprints, with each sprint focusing on adding a specific feature or improving an existing function.
The first sprint focussed on setting up a basic blog application, which formed the foundation of the project. It allowed users to browse through post previews and open the full post by clicking on the preview. Users were not required to log in to the site to view posts. 
The next sprint focussed on implementing user authentication. Once implemented, it allowed users to create an account using their email address, and to log into and out of the account.
The next sprint focussed on setting up the dashboard and its functionality. The dashboard serves as a space for registered users to view their favourite posts. Posts can be saved to the dashboard as well as removed from the dashboard. 

GitHub Projects was an essential tool for tracking progress and managing tasks throughout the Agile development process. A Kanban style board was used to visually track the progress. Each issue was based on a user story, and was moved through the different phases of *To Do*, *In Progress*, and *Done*, in accordance with the corresponding sprints. 
Custom labels were created to visually distinguish the issues. Labels were used to assign a priority - *must-have*, *should-have*, *could-have* or *will-not-have*, based on the MOSCOW model of prioritisation -  as well as a functionality - *C*, *R*, *U*, or *D*, to reference their role within the *CRUD* functionality.


### Diagrams
### Design Choices
#### Color Palette

[Coolors](https://coolors.co/image-picker) was used to generate a color palette from the main background image. 

<details>
<summary> Color Pallette Image</summary>
<img src = "">
</details>

#### Typography

[Google Fonts](https://fonts.google.com) was used to pair and import fonts. 

<details>
<summary> Type Font Image</summary>
<img src = "">
</details>

#### Wireframes

[Balsamiq](https://balsamiq.com/) was used to create wireframes for each page to display their appearance on both mobile and larger devices.

Page | Desktop Version | Mobile Version
--- | --- | ---
Home | --- | ---
Dashboard | --- | ---
Blog Post | --- | ---

[Back to top ⇧](#knitspace)

## User Experience (UX)

### Project Goals

### User Stories

#### Blog Accessibility

- As a **guest user**, I can **view blog posts without the need to log in or register** so that **I can freely access content on the site**.
- As a **guest user**, I can **click on a post preview** so that **I can open the full post and read it in detail**.

#### Account Management

- As a **guest user**, I can **create an account** so that **I can have a personalized experience and access member-only features.**.
- As a **registered user**, I can **log in to my account** so that **I can access my dashboard and other member-only features**.
- As a **registered user**, I can **log out of my account** so that **I can ensure my account security and privacy**.

#### Dashboard Management

- As a **registered user**, I can **save posts to my dashboard** so that **I can easily access my favorite content**.
- As a **registered user**, I can **rearrange my saved posts** so that **arrange my content board according to my preferences**.
- As a **registered user**, I can **delete saved blog posts from my dashboard** so that **I can manage my content board**.
- As a **registered user**, I can **click on a saved post preview** so that **I can open the full post and read it in detail**.

#### 

- As a **registered user**, I can **access exclusive content** so that **I can engage with the community and share information**.

[Back to top ⇧](#knitspace)

## Features

### General

#### Header

The header is the same across pages to provide users with a familiar layout and allow them to focus on the content of each page. It contains the KnitSpace logo in the top left, which doubles as a link to the Home Page. It also contains links to all pages of the website in the top left, as well as the main background image. When a When a user is logged in, a link to their dashboard appears in the navigation bar.

<details>
<summary> Header Image Guest User</summary>
<img src = "">
</details>

<details>
<summary> Header Image Registered User</summary>
<img src = "">
</details>


#### Footer

The footer is the same across pages to provide users with a familiar layout and allow them to focus on the content of each page. It contains links to social media networks, which will open a new tab when clicked, as well as a copyright declaration.

<details>
<summary> Footer Image </summary>
<img src = "">
</details>

### Home Page

The home page contains a preview of all available blog posts, ordered from most to least recent. Each post is presented in a clickable which opens the full-page view when clicked. Arrows at the bottom of the page allow users to browse between multiple pages.

<details>
<summary> Home Page Image </summary>
<img src = "">
</details>

### Posts

When clicking on a blog post preview card, a full-page view is opened. It presents the user with the title of the post followed by the author and date, and the full text. A *Back* button above the post allows users to return to their previous place of browsing. Additionally, for logged in users, a *Save* button above the post allows users to save their favorite posts to their dashboard.

<details>
<summary> Post Preview Image</summary>
<img src = "">
</details>

<details>
<summary> Full Page Post Image </summary>
<img src = "">
</details>


### User Dashboard

The dashboard is where users can view all their saved posts in one continuous list. Each post is presented as a more condensed version of the post preview, and will open the full page post when clicked. Users can delete their saved posts from their dashboard at any time.

<details>
<summary> Dashboard Image </summary>
<img src = "">
</details>

### User Authentication

Users are able to create an account using their email address. Their username must be unique, and the password they chose must meet the standard safety criteria. No verification email is sent out by email.
Once the account has been created, users can use their credentials to log into the page and access exclusive content, such as their dashboards.

<details>
<summary> Sign Up Image </summary>
<img src = "">
</details>

<details>
<summary> Sign In Image </summary>
<img src = "">
</details>

### Future Features

### About Page
### Comments


[Back to top ⇧](#knitspace)

## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python ](https://en.wikipedia.org/wiki/Python_(programming_language))

### Tools

### Libraries, Frameworks & Packages

- [Django](https://www.djangoproject.com/) was used as web framework.

- [Django Template](https://jinja.palletsprojects.com) was used as a templating language for Django to display backend data to HTML.
   
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used to help with styling and responsiveness.

- [Google Fonts](https://fonts.google.com) was used to import the fonts into the html file, and were used on all parts of the site.

- [Font Awesome](https://fontawesome.com) was used throughout the website to add icons for aesthetic and UX purposes. 

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.
 
- [Gunicorn](https://gunicorn.org/) was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

- [Summernote](https://summernote.org/) was used as WYSIWYG editor.

- [Heroku Postgres](https://www.heroku.com/postgres) was used in production, as a service based on PostgreSQL provided by Heroku.

- [Cloudinary](https://cloudinary.com/) was used as an image storage solution.


### Tools and Programs

- [Git](https://git-scm.com) was used for version control. 

- [GitPod](https://gitpod.io/) was used for writing, committin, and ppushing code to GitHub.

- [GitHub](https://github.com) was used to store the code. 

- [Heroku](https://www.heroku.com) was used to host and deploy the website.

- [Am I Responsive](ami.responsivedesign.is) was used to preview the website across a variety of popular devices.

- [Coolors](https://coolors.co) was used to create a color pallette for the website.

- [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design phase of the project

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used during development process for code review and to test responsiveness.

- [W3C Markup Validator](https://validator.w3.org/) was used to validate the HTML code.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.

- [JSHint](https://jshint.com/) was used to validate the JavaScript code.

- [PEP8 Online Check](https://pep8ci.herokuapp.com) was used to validate the Python code.

- [Favicon.cc](https://www.favicon.cc/) was used to create the site favicon.

- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) was used to measure the quality of the page.

[Back to top ⇧](#knitspace)

## Testing

### Testing User Stories

#### Blog Accessibility
As a **guest user**, I can **view blog posts without the need to log in or register** so that **I can freely access content on the site**.
- Blog posts are available without users needing to create an account or log in.
- Previews of each post are available on the home page.
- Navigation on the bottom of the page allow users to browse previews across multiple pages.

As a **guest user**, I can **click on a post preview** so that **I can open the full post and read it in detail**.
- Previews of each post are available on the home page.
- Clicking on a preview opens a full-page view of the post.
- A *Back* button allows users to return to their previous spot after they finish viewing the full-page post.

#### Account Management
As a **guest user**, I can **create an account** so that **I can have a personalized experience and access member-only features.**.
- Users can create an account using their email address.
- Users are provided with feedback messages for invalid form inputs.

As a **registered user**, I can **log in to my account** so that **I can access my dashboard and other member-only features**.
- Users are able to log into their accounts using their username and password.
- Users are redirected to the home page after logging in.

As a **registered user**, I can **log out of my account** so that **I can ensure my account security and privacy**.
- Users are able to log out of their accounts.
- Users need to confirm that they want to log out before being logged out.
- Users are redirected to the home page after logging out.

#### Dashboard Management
As a **registered user**, I can **save posts to my dashboard** so that **I can easily access my favorite content**.
- For logged in users, a link to the dashboard is visible in the navigation bar.
- For logged in users, a button to save a blog post is visible on the full-page blog post.
- Once saved, the blog post appears on the users dashboard.
- A feedback message is provided to indicate a post has been saved successfully.

As a **registered user**, I can **rearrange my saved posts** so that **arrange my content board according to my preferences**.

As a **registered user**, I can **delete saved blog posts from my dashboard** so that **I can manage my content board**.
- A *Delete* button is displayed with each saved blog post preview.
- When clicked, the correspsonding blog post is removed from the dashboard.
- A feedback message is provided to indicate a post has been deleted successfully.

As a **registered user**, I can **click on a saved post preview** so that **I can open the full post and read it in detail**.
- Saved blogposts appear as previews on the dashboard.
- When the preview is clicked, the user is redirected to the full-page view of the post. 
- A *Back* button returns users to their dashboard from the full-page view.

As a **registered user**, I can **access exclusive content** so that **I can engage with the community and share information**.

### Code Validation

#### HTML

- [W3C Markup Validator](https://validator.w3.org/) was used to validate the HTML code of each templated page.

<details>
<summary> Home Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Dashboard Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Full Page Post Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Dashboard Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Sign In Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Sign Up Validation Image </summary>
<img src = "">
</details>

<details>
<summary> Sign Out Validation Image </summary>
<img src = "">
</details>

#### CSS

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the custom CSS code.

<details>
<summary> CSS Validation Image </summary>
<img src = "">
</details>

#### JavaScript

- [JSHint](https://jshint.com/) was used to validate the custom JavaScript code.

<details>
<summary> JavaScript Validation Image </summary>
<img src = "">
</details>

#### Python

- [PEP8 Online Check](https://pep8ci.herokuapp.com) was used to validate the Python code.

<details>
<summary> Python Validation Image </summary>
<img src = "">
</details>

### Manual Testing

#### Admin Features
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Create superuser | Yes | Successful |
|Create user | Yes | Successful |
|Delete user | Yes | Successful |
|Create post | Yes | Successful |
|Delete post | Yes | Successful |
|View all posts | Yes | Successful |
|Filter posts | Yes | Successful |

#### Account Management
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Create new account | Yes | Successful |
|Log in to account | Yes | Successful |
|Log out of account | Yes | Successful |

#### Home Page
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Browse paginated blog excerpts | Yes | Successful |
|Click on excerpt opens full-page blog entry | Yes | Successful |
|Click on back returns user to homepage | Yes | Successful |
|Save button on full-page entry is invisible for guest users | Yes | Successful |

#### Header
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Click on logo returns to homepage | Yes | Successful |
|Click on navigation bar links redirects to other internal pages  | Yes | Successful |
|Link to dashboard is invisible for guest users | Yes | Successful |

#### Footer
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Click on social media icon redirects to respective website | Yes | Successful |
|Social Media links open in new tab | Yes | Successful |

#### Dashboard
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Dashboard is only visible to logged in users | Yes | Successful |
|Saved blog posts appear on the dashboard | Yes | Successful |
|Saved blog posts can be deleted from the dashboard | Yes | Successful |

### Automated Testing

### Device and Browser Testing

#### Device Compatibility
Device | Outcome | Pass/Fail
--- | --- | ---
iPhone 13 Mini | No issues with appearance, responsiveness, or functionality. | ---
iPad 9th Generation | No issues with appearance, responsiveness, or functionality. | ---
MacBook Air 13” | No issues with appearance, responsiveness, or functionality. | ---
Acer Predator Helios 300 | No issues with appearance, responsiveness, or functionality. | ---
Black Shark PAR-HOA | No issues with appearance, responsiveness, or functionality. | ---
SAMSUNG Galaxy S23 | No issues with appearance, responsiveness, or functionality. | ---


#### Browser Compatibility
Browser | Outcome | Pass/Fail
--- | --- | ---
Safari | No issues with appearance, responsiveness, or functionality. | ---
Google Chrome | No issues with appearance, responsiveness, or functionality. | ---
Microsoft Edge | No issues with appearance, responsiveness, or functionality. | ---
Mozilla Firefox | No issues with appearance, responsiveness, or functionality. | ---
JoyUI Native Browsers | No issues with appearance, responsiveness, or functionality. | ---

Note: The hover effect for post previews does not appear in the deployed version. However, it works without issues on the local browser.


### Bugs
|Feature | Bug | Fix |
|---|---|---|
|Hover effect for preview cards | In the deployed version, the preview cards do not appear to lift when hovered over. However, the effect works as expected on the local server. | Not fixed |
|Random messages | Occasionally, feedback messages detailing the last step a user has taken are shown instead of just feedback for saving / deleting a post. | Not fixed |


### Accessibility

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) in [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to measure the quality of the page, focussing on performance, accessibility, best practices, and SEO scores.

<details>
<summary>Home Page Lighthouse Report</summary>
<img src = "">
</details>

<details>
<summary>Dashboard Lighthouse Report</summary>
<img src = "">
</details>

<details>
<summary>Full-Page Post Lighthouse Report</summary>
<img src = "">
</details>

<details>
<summary>Sign In Lighthouse Report</summary>
<img src = "">
</details>

<details>
<summary>Sign Up Lighthouse Report</summary>
<img src = "">
</details>

<details>
<summary>Sign Out Lighthouse Report</summary>
<img src = "">
</details>

[Back to top ⇧](#knitspace)

## Deployment

### GitHub

This website was developed using [GitPod](https://www.gitpod.io/), which was then committed and pushed to [GitHub](https://github.com/) using the GitPod terminal.

Here are the steps to deploy a website to GitHub Pages from its GitHub repository:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/).
2. At the top of the Repository, locate the Settings button on the menu.
3. Scroll down the Settings page until you locate the Pages section.
4. Under Source, click the dropdown called None and select Master Branch.
5. The page will refresh automatically and generate a link to your website.

### Heroku

Deployment to [Heroku](https://www.heroku.com) was completed using the following steps:

1. Prepare for deployment.
    - Create an env.py file in your main directory and add *DATABASE_URL*, *CLOUDINARY_URL*, and *SECRET_KEY* to it.
    - Import *DATABASE_URL* and *SECRET_KEY* into your *settings.py* file, and remove the default database confihuration.
    - Add your apps to the list of *Installed Apps* in *settings.py*.
    - Add Heroku to the *ALLOWED_HOSTS* list in *settings.py*.
    - Create a file named *Procfile* in your main directory, and add a command to execute your project.
    - Create a file named *python-version* in your main directory, and add the version of Python you are using.
    - Install *gunicorn* and *whitenoise* to virtual environment.
    - Update the *requirements.txt* file.
    - Change your *settings.py* file to read *DEBUG = FALE*.
2. Create a new App.
    - Log in to Heroku and from the Dashboard, click *Create New App*.
    - Enter a unique app name and choose your region.
    - Click *Create App*.
3. Update your *ConfigVars*.
    - Go to *Settings* > *Reveal ConfigVars* and update the following information:
        - SECRET_KEY
        - DATABASE_URL
4. Deploy the project.
    - Go to *Deploy* and specify deployment details.
    - Select *GitHub* as the *Deployment Method*.
        - When prompted to *Connect to GitHub*, find your repository and click *Connect*.
    - Select either *Automatic Deploys* or *Manual Deploys* and click *Deploy Branch*.
5. Once deployment has been completed, click *View* to view the deployed project. 

 
[Back to top ⇧](#knitspace)

## Credits

### Content

All conent was written by the developer.

### Media

- The image used for the Favicon is from [Pixabay](https://pixabay.com/), by Clker-Free-Vector-Images.
- All other images were generated by Alex Büttner using [Getimg.ai](https://getimg.ai/).
- The blogposts and user personas were generated with the help of [Gemini](https://gemini.google.com/). 

### Code

- The models for *BlogPost* and *BlogPostAdmin* were adapted from Code Institue’s “I think therefore I blog” walkthrough. 
- The navigation bar and footer were adapted from [Bootstrap's Clean Blog](https://startbootstrap.com/theme/clean-blog) template.
- Django Tutorials, especially [W3Schools](https://www.w3schools.com/django/), [Django documentation](https://docs.djangoproject.com/en/5.1/), and [Corey Shafer's YouTube Channel](https://www.youtube.com/@coreyms) were consulted regularly.

[Back to top ⇧](#knitspace)

## Acknowledgements


[Back to top ⇧](#knitspace)
