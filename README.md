# KnitSpace

![Mock Up Image]()

KnitSpace is a vibrant online community for knitters of all levels to come together to share, learn, and connect. Blog posts on a wide variety of knitting-related topics are available to browse without the need to log in. Users also have the option to create an account and save their favourite posts to their own dashboard and review them with ease. 

Visit the deployed application [here](https://knit-space-57239e7d6ce8.herokuapp.com/).

## Project Planning 

### Agile Methodology
### Diagrams
### Design Choices

#### Color Palette
#### Typography
#### Wireframes

[Back to top ⇧](#knit-space)

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
- As a **registered user**, I can **access exclusive content** so that **I can engage with the community and share information**.

[Back to top ⇧](#knit-space)

## Features

### General

#### Header
The header is the same across pages to provide users with a familiar layout and allow them to focus on the content of each page. It contains the KnitSpace logo in the top left, which doubles as a link to the Home Page. It also contains links to all pages of the website in the top left, as well as the main background image.

#### Footer
The footer is the same across pages to provide users with a familiar layout and allow them to focus on the content of each page. It contains links to social media networks, which will open a new tab when clicked, as well as a copyright declaration.

### Home Page
The home page contains a preview of all available blog posts, ordered from most to least recent. Each post is presented in a clickable which opens the full-page view when clicked. Arrows at the bottom of the page allow users to browse between multiple pages.

### Posts
When clicking on a blog post preview card, a full-page view is opened. It presents the user with the title of the post followed by the author and date, and the full text. A *Back* button above the post allows users to return to their previous place of browsing.


### User Dashboard
### User Authentication

### Future Features

### About Page
### Comments



[Back to top ⇧](#knit-space)

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

- [PEP8 Online Check](http://pep8online.com/) was used to validate the Python code

- [Favicon.cc](https://www.favicon.cc/) was used to create the site favicon.

- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) was used to measure the quality of the page.

[Back to top ⇧](#knit-space)

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
- Once saved, the blog post appears on the users dashboard

As a **registered user**, I can **rearrange my saved posts** so that **arrange my content board according to my preferences**.

As a **registered user**, I can **delete saved blog posts from my dashboard** so that **I can manage my content board**.

As a **registered user**, I can **click on a saved post preview** so that **I can open the full post and read it in detail**.

As a **registered user**, I can **access exclusive content** so that **I can engage with the community and share information**.

### Code Validation
### Manual Testing

#### Admin Features
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Create superuser | Yes | Successful |
|Create user | Yes | Successful |
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
|Click on excerpt opens full page blog entry | Yes | Successful |
|Click on back returns user to homepage | Yes | Successful |
|Save button on full-page entry is invisible for guest users | Yes | Successful |

#### Header
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Click on logo returns to homepage | Yes | Successful |
|Click on navigation bar links redirect to other internal pages  | Yes | Successful |
|Link to dashboard is invisible for guest users | Yes | Successful |

#### Footer
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Click on social media icon redirects to its website | Yes | Successful |
|Social Media links open in new tab | Yes | Successful |

#### Dashboard
| Feature | Tested? | User Feedback Provided |
|---|---|---|
|Dashboard is only visible to logged in users | Yes | Successful |
|Saved blog posts appear on the dashboard | Yes | Successful |

### Automated Testing

### Device and Browser Testing

#### Device Compatibility
Device | Outcome | Pass/Fail
--- | --- | ---

#### Browser Compatibility
Browser | Outcome | Pass/Fail
--- | --- | ---

### Bugs
|Feature | Bug | Fix |
|---|---|---|
|Hover effect for preview cards | In the deployed version, the preview cards do not appear to lift when hovered over. However, the effect works as expected on the local server. | Not fixed |


### Accessibility


[Back to top ⇧](#knit-space)

## Deployment

### GitHub
### Heroku

 
[Back to top ⇧](#knit-space)

## Credits

### Content
### Media
### Code


[Back to top ⇧](#knit-space)

## Acknowledgements


[Back to top ⇧](#knit-space)
