# Recipe website - Recipe World

In order to edit/delete recipes you must be the recipe creator. For the purpose of submitting this project and testing I have provided the username/password for the below recipes, although feel free to create your own user and add your own recipes to edit and delete.

- Username - test
- Password - test

- Recipes created with above user
    - Mango lassi
    - Champagne jelly
    - Chocolate pot with ginger


For this project I have developed a website using the Flask framework and MongoDB database. 
The purpose of this project was to create a website that users can store and easily access cooking recipes.

Website link below:

[Recipe World](https://recipe-milestone-project.herokuapp.com/)

## UX

The website was designed for users who simply want to view recipes as well as users who are interested in creating recipes to share.
To keep things clean any type of create, update and delete functionality is hidden behind a login feature.
Additionally there are filtering functions on the homepage which allows users to quickly find the recipe they are interested in.

### User stories

- A general users wants to try out some new recipes to advance their cooking abilities.
- A more advanced chef wants to share their recipes with the world to gain more popularity.
- A catering company are looking for new recipes to add to their portfolio.
- A user is throwing a dinner party and wants to know what the most popular dishes are currently.

## Wireframes


1. [Homepage - Desktop wireframe](https://ibb.co/ZXx7xyQ)

- The homepage remained similar to how I originally planned. As you can see I added the banner running across the top of the page which included the search function.

2. [Homepage - Mobile wireframe](https://ibb.co/v1BRWmC)

- Again the mobile view is very similar to the initial design with the variance being the search bar is now nested in the banner. Also the category images are seated with a better design.

3. [Recipe page - Desktop wireframe](https://ibb.co/NYGNXKv)

- The top banner and search bar also appear in the live site vs wireframes on this page. I also opted to hide the edit/delete button from users who did not create that specific recipe.

4. [Recipe page - Mobile wireframe](https://ibb.co/FbxHJhx)

- Same comments for mobile as desktop.

## Database

For the database I setup with the below collections.

1. Categories
    - This collection was created as users would be adding their own categories to the database if they did not already exist.
2. Cuisine
    - This collection was created as users would be adding their own categories to the database if they did not already exist.
3. Recipe
    - This collection was created to hold all key information about the recipe which is collected/edited by the users via the add/edit recipe functions.
4. Users
    - This collection was created to hold all user login details allowing for the login/register functions to protect users recipes from deletion.
5. Contact requests
    - This collection was created to capture users contact requests.

## Features

1. Base template (navbar & footer)
- Navbar
    - Site logo to navigate back to homepage.
    - Home button to navigate back to homepage.
    - Login button for existing users to log back in.
    - Register button for new users to register.
      Once the user has logged in.
    - Add recipe button to direct users to create new recipes.
    - Logout button to end their session.
- Footer
    - Contact us button linking to modal to capture users name, email and comment which sends information to database.
    - Social media buttons which currently link to nothing however would link to this websites social.

2. Most pages where relevant.
- Parallax container with food image and search function to navigate to recipes which match key word.
- Category filter buttons allowing users to navigate to recipes that match that criteria.

3. Index (homepage)
- Sort button which allows users to filter to either the latest recipes added or the most popular recipes by amount of views.
- Recipe cards which image, recipe name and views with on click scroll up that reveals crucial recipe information.
- View full recipe button to link to detailed recipe page.

4. Add recipe page.
- User input form allowing them to create new categories or cuisines as well as create new recipes and upload matching images.

5. Detailed recipe page.
- Detailed breakdown of recipes ingredients and method.
- (IF LOGGED IN AND CREATOR OF RECIPE) Edit and delete recipe buttons.

6. Login page.
- Checks users login details against DB and allows login.

7. Register page.
- Check users login details against DB, if do not already exist creates user a login.

### Features Left to Implement

In the future I would like to implement the below features.
- The ability for logged in users to leave comments on others recipes to either give tips or just discuss the recipes.
- Setup the contact form in the footer to direct comments to an email server rather than store in the database.
- As the site grows I would add some functionality to limit the number of recipes displayed at once.
- Create admin users who have the ability to edit/delete others recipes from the website in the case of 'fake' potentially dangerous recipes.
- Create the ability to screen recipes before they are added to the website to prevent the above.
- Reset password and forgotten username features to be added.
- Add a 'my recipe' link where users can see their own recipes separately from anyone else's.

## Technologies Used

- [materializecss](http://archives.materializecss.com/0.100.2/)
     - This was used for a basic HTML templates and styling.

- [Python 3](https://www.python.org/download/releases/3.0/)
    - The back end functionality of the application was written in python.

- [Flask](http://flask.pocoo.org/)
     - Flask was used to extend pythons functionality to the frond end.

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
     - A lot of the JavaScript was done by the frameworks used via jQuery however for items such as the datepicker JavaScript was required.


- [jQuery](https://jquery.com/)
     - This was used in conjunction with a number of Materializes functions such as the modals, collapsable navbar, datepicker etc.

- [Font Awesome](https://fontawesome.com/)
     - This was used for social icons in the footer.
  
- [Hover.css](https://ianlunn.github.io/Hover/)  
     - I used this to give the clickable links throughout the dashboard the Hover Grow effect to give the user confirmation the link is clickable.

## Testing

- I used [This HTML validator](https://validator.w3.org/) to ensure my code was legal.
- I used [This CSS validator](https://jigsaw.w3.org/css-validator/) to ensure my CSS was legal.
- I used [This Python validator](http://pep8online.com/) to ensure my Python was legal.

1. New user who has found himself with an excess of Chicken would line to find some Chicken related dishes:
    1. User lands on homepage and immediately sees the search bar.
    2. Searches 'Chicken' which redirects user to any recipe with the keyword Chicken included.
    3. Only 1 Chicken recipe available so user makes 50 'Chicken, pesto and rocket sandwiches'.

2. New user wants to create a recipe.
    1. User lands on homepage where the 'register' button is prominently displayed.
    2. User attempts to create a username however username is taken so is greeted with a message advising to choose a new username.
    3. User creates new username and is redirected to homepage with a message that displays "hello 'username'" confirming they are logged in.
    4. User now realises the buttons have changed to 'add recipe' and 'logout' where the previous 'register' and 'login' buttons had been.
    5. User tries to create recipe but realises their recipe doesn't fall within any of the existing cuisines.
    6. User adds their own cuisine.
    7. User attempts to submit recipe without crucial information and is prompted by validation to add requirement information.
    8. User submits completed recipe and is redirected to the homepage where their recipe is displayed.

3. Existing user wants to edit their recipe.
    1. User selects their own recipe from the homepage.
    2. User navigates to button off their recipe page where they are presented with an 'edit' and 'delete' button.
    3. User selects edit which redirects to an almost identical page as the 'add recipe' page but is already pre-populated with information.
    4. User amends required information and submits where they are redirected to the index page.

4. Existing user wants to delete their recipe.
    1. User follows above steps 1 and 2.
    2. User selects delete recipe button where they are prompted with a modal to confirm they want to delete this recipe.
    3. User confirms deletion and is redirected too homepage where their recipe is no longer.

5. Malicious user wants to delete others recipes.
    1. User selects recipe they intent to delete and selects the recipe ID from URL.
    2. User manually navigates to either /edit_recipe/(recipeID) or /delete_recipe(RecipeID).
    3. User is redirected to index page with no success due to if statements that check the users session ID vs the user who created the recipe.


## Viewport and responsive testing

1. Desktops & Laptops. 1024×768
    1. Initial issue i had was that all the recipes were different heights due to the length of names etc. This was resolved by using a truncate to cut off recipe names.
    2. Now displays as intended.

2. Tablet. 800 x 1280
    1. Displays as intended.

3. Mobile
    1. Galaxy S5 - 360 X 640, Pixel 2 - 411 x 731, Pixel 2 xl - 411 x 823, iPhone 5 - 320 x 568, iPhone 6,7,8 - 375 x 667, iPhone 6,7,8 Plus - 414 x 736, iPhone x - 375 x 812.

## Deployment

1. New Heroku Python App created.
2. Launched Heroku in the C9 environment.
3. Initiate new Git repository and run git remote add Heroku https://git.heroku.com/recipe-milestone-project.git to allow a push to the Heroku server.
4. To prevent a "push fail", the requirements.txt was updated using the following command sudo pip3 freeze --local >requirements.txt to keep track of dependancies.
5. A Procfile was created using the following code: echo web: python run.py > Procfile to inform Heroku which file to run for initiating the app.
6. To ensure that Web Processes are running the following command line was run in C9: Heroku ps:scale web=1.
7. Config Vars set as follows: IP=0.0.0.0 and PORT=5000.
8. Lastly, dynos were restarted in Heroku app.
9. Code added, committed and pushed to both GitHub and Heroku.
10. App launched successfully.
11. In addition, you can clone or download the code from this GitHub repository.


### Content
- The image URLs and recipe content were sourced from the [BBC site](https://www.bbcgoodfood.com/recipes).
- The main banners were sourced from [Pexels](https://www.pexels.com/) who advise all photos can be used for [free](https://www.pexels.com/photo-license/).
  
### Acknowledgements

- I received inspiration for this project from a combination of the mini projects leading up to this.
- The Slack community have been great on giving me feedback on my project (Shane Muirhead in particular has been very helpful).
- The tutors at code institute have also been helpful.
- My mentor Jim Richmond has supported with feedback on the project.