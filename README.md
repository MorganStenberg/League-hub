# **League Hub**

League Hub is an user-friendly application where you can create your own league with friends and keep track of scores and standings. Wether it is in football, table-tennis or other games League hub is the place where you can finally solve that long standing issue of who is really the best? 

Create your own league, add matches to it, see all historically added matches for a specific league or in total. This is the place for friendly competition! 

The app is targeted at friends who want a help in keeping track of matches and points for a league, where the application does the counting for you!

Here is a link to the live site - [League Hub](https://league-hub-888548acadce.herokuapp.com/)


## Table of contents

- [League Hub](#league-hub)
- [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)
- [Agile Development](#agile-development)
- [Data Models and database](#data-models-and-database)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Testing](#testing)
- [Manual Testing](#manual-testing)
- [Validator Testing](#validator-testing)
- [Problems and Bugs](#problems-and-bugs)
- [Deployment](#deployment)
- [Technologies, Languages, Frameworks, Libraries, Servers, Programs and Sites used](#technologies-languages-frameworks-libraries-servers-programs-and-sites-used)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## **UX**

### Strategy
The strategy for League Hub app is about meeting the user need of providing an user-friendly way of organizing your own league. Where the focus is on making it easy for the user to create and be a part of a league. 

### **Target Audience**
This project is made for those that: 

- Want to have a place to organize a friendly and competetive league in the sport or game of their choosing.
- Want to keep track of score, matches and standings in a league with other users. 

### **User Stories**

The following User Stories were followed to develop the application.

#### - *Account registration*

As a Site User I can register an account so that I can set up my league and be a participant in other leagues

*Acceptance Criteria* 
- User can register an account with an email and a chosen username and password
- The user can log in with chosen username and password
- Visual confirmation is shown when successful registration of account

#### - *Create League*

As a Site user I can create a league so that I can keep track of scores and league standing with other users

*Acceptance Criteria*
- When logged in a user can create their own league
- When logged in a user can customize the league name
- When logged in, a user can select one or multiple users to add to their league


#### - *Search for other users while creating league*

As a site user I can search for other users while creating a league so that I don't have to scroll through a list of all users while creating league

*Acceptance Criteria*

- While logged in and creating a league a user can use a search bar, with autocomplete, to search for other users
- Being able to select users to add as league members from result of search
- Being able to select multiple users directly in the search bar


#### - *View all leagues*

As a Site user I can view a list of all leagues so that I can see my own leagues as well as what other leagues that have been created and choose any league to view in a detailed view

*Acceptance Criteria*

- A user can view a paginated list of all leagues with name and description of league visible
- A user can click on the league to enter a detailed view of the league


#### - *View my leagues*

As a Site user I can view all the leagues that I am a member of so that I can see what leagues I am a member of and choose what league to view in a detailed view

*Acceptance Criteria*

- When logged in a user can view a paginated list of all the leagues that they are a member of
- A user can click on the league to enter a detailed view of the league


#### - *Detailed view of league*

As a Site user I can choose a league to view so that I can see a detailed view of that league and what the score and standings are in that league

*Acceptance Criteria*

- A user can see the standings in the league, with points, games played, won, lost and draw matches visible.
- League members are displayed
- All matches connected to that league are displayed in a paginated list
- When logged in, a user that is a league creator or league member can add matches to the league
- When logged in, a user that is a league creator can edit or delete any match
- When logged in, a user that is a league member can edit or delete their own matches


#### - *View all my matches*

As a Site user I can view all my matches so that see all the matches that I am a part of and the league that they belong to

*Acceptance Criteria*

- When logged in, a user can view all their own matches that they have played and see what league they belong too
- When logged in, a user can view all their own matches and see what date they were added as well as what the score was


#### - *Add matches to league*

As a Site user I can add matches to a league so that the league standings can be updated

*Acceptance Criteria*

- When logged in, a user can add matches with other users to a league that they are a member of
- When logged in, and if the user is a league creator they can add matches for other users that are members of the league they have created


#### - *Modify or delete matches*

As a site user I can modify or delete matches that have been added to a league so that the league standings can be updated

*Acceptance Criteria*

- When logged in, a user can edit the results of already added matches that they a part of.
- When logged in, a user can delete already added matches that they a part of
- When logged in, a user that is a league creator can edit the results of matches for other users that are members of the league they have created
- When logged in, a user that is a league creator can delete matches for other user that are members of the league they have created


#### - *Admin login*

As a Site admin I can login and access the admin dashboard so that I can access the functionalities of a superuser

*Acceptance Criteria*

- Implement a secure login for superuser using Django authentication


#### - *Admin modify or delete leagues*

As a Site admin I can edit and delete created leagues so that I can manage the leagues created on the site

*Acceptance Criteria*

- As a site admin I can edit the description of a league
- As a site admin I can delete a league
- As a site admin I can add matches to a league
- As a site admin I can edit matches
- As a site admin I can delete matches


### **Design**

The site was designed with simplicity in mind, as to not clutter the view for the user and distract from the core functionality. With the use of a consistent color scheme throughout the site. 
The buttons and league standings are presented in a green color, as this is a color usually connected to sports league. The colors were also chosen with a good contrast ratio in mind, to make the site as accessible as possible. 
The font of 'Roboto' was also chosen for its clean and easy to read style. 

#### **Wireframes**

Basic wireframes was produced to have a basic guideline for the design of the site while building it. 

- ![Wireframe image landing page](documentation/wireframes/Wireframe_landing_page.PNG)
- ![Wireame image create league](documentation/wireframes/wireframe_create_league.PNG)
- ![Wireframe all leagues](documentation/wireframes/wireframe_all_leagues.PNG)
- ![Wireframe detaialed league](documentation/wireframes/wireframe_det_league.PNG)

## **Agile Development**

The application was built using an agile approach, using a Github Project Board and Issues. The Github project board can be found [here](https://github.com/users/MorganStenberg/projects/4). All user stories listed above were created with Github Issues. The user stories were used to keep track of progress throughout the project, via different columns specifying the status of the issue. With columns for 'Todo', 'In progress', 'Done' and 'DoD'. DoD, or Definition of Done was used for user stories that had been implemented and gone through testing. I also added a column for 'Backlog' for future features to be implemented, as a way to keep control of the scope of the project and be sure to deliver a MVP in time.  

## **Data models and database**

Below is and ERD for the custom models produced for the application. Which shows the structure of the PostgreSQL database used in this project. 

![An image of the ERD for the project](documentation/ERD.PNG)

Django AllAuth was used for the user model and user authentication system. 

The League model contains all the information on a league. Is connected to the user model both via the fields 'League Creator' and 'League Members'. For League Creator there is a many-to-one relationship to the user model, and for League Members there is a many-to-many relationship. 

The match model contains all the information on matches. The Match model is connected via ForeignKey to the League model, and via ForeignKey to the user model through the fields Home Team and Away Team.  

## **Features**

### **Existing features**

### **Future features**

## **Testing**

### **Manual testing**

### **Validator testing**

I have validated my HTML, CSS, Javascript and Python code with the websites listed below:

 - HTML: [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)
 - CSS: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
 - Javascript: [JShint](https://jshint.com/)
 - Python [CI Python Linter](https://pep8ci.herokuapp.com/)

JShint and W3C did not return any errors for the Javascript and CSS code.

- W3C image here
- Jshint image here

Python Linter did return errors regarding to long lines and trailing whitespaces, which were taken care of by formatting the code correctly and splitting up lines that
were too long. 
- python linter image here
- python linter another image here

The HTML validator had issues with the python code mixed in with the HTML, which caused warnings. But no warnings or errors were found other than 
those related to the Python code.
- insert image of wc3 html validation
- more images of html validation

### **Problems and bugs**

## **Deployment**

## **Technologies, Languages, Frameworks, Libraries, Servers, Programs and Sites used**

## **Credits**

## **Acknowledgements**