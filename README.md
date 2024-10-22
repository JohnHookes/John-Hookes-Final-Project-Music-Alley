 MUSIC-ALLEY ---------------------

Music-Alley is a site for musicians and music fans so that they can share their music and fans can find new artist and old favourites. Musicians will be able to share, not only their music but also any recent events, updates, daily musings and any gigs coming up helping them grow their fan base.  Fans will be able to not just enjoy their music but connect with artists and find out what gigs are coming up.

-----------------------------------

WEBSITE

https://music-alley-cdf33fde4248.herokuapp.com/


The site was deployed to Heroku  pages. At this address
•	https://dashboard.heroku.com/apps/music-alley/deploy/github

GITHUB REPOSITORY

https://github.com/JohnHookes/John-Hookes-Final-Project-Music-Alley

PROJECT
Username: ProjectTester
Password: MusicAlley

Link to github Repository Music-Alley	https://github.com/users/JohnHookes/projects/5/views/1

-------------------------------
PROJECT DEPLOYMENT

-Procfile
In the project root directory, there is a file named Procfile. This file tells Heroku how to run your application

in the Procfile is the code
      web: gunicorn music_alley.wsgi
--gunicorn is a WSGI HTTP server for Python used in production with the project name being music_alley

-install gunicorn  ( I have used version gunicorn==20.1.0)

-Add gunicorn to your requirements.txt file

-Update ALLOWED_HOSTS in settings.py 

    ALLOWED_HOSTS = ['.herokuapp.com', '8000-johnhookes-johnhookesfi-4s5ooq8cdxl.ws.codeinstitute-ide.net', '8000-johnhookes-johnhookesfi-st5czepzlm7.ws.codeinstitute-ide.net']

    with '8000-johnhookes-johnhookesfi-4s5ooq8cdxl.ws.codeinstitute-ide.net', '8000-johnhookes-johnhookesfi-st5czepzlm7.ws.codeinstitute-ide.net' being local hosts

Add DATABASE_URL and Cloudinary
- Heroku provides a database URL 

    Log in to Heroku

    Select Your App
      -Once logged in, navigate to the Dashboard and select the app you want to add a database to.

    Go to the "Resources" Tab
      -In your app’s dashboard, click on the Resources tab at the top of the page.

    Add a Heroku Postgres Add-on
      -In the "Add-ons" section of the Resources page, search for "Heroku Postgres" in the search box that says "Add-ons".
      -Select Heroku Postgres from the results.
      -Choose the free plan (hobby-dev) or any other suitable plan based on your needs.
      -Click Provision.

    Retrieve the DATABASE_URL
      -After provisioning the database, go to the Settings tab of your app.
      -Scroll down to the Config Vars section and click Reveal Config Vars.
      -Here, you should see the DATABASE_URL listed as one of the environment variables.

    The DATABASE_URL will automatically be created when the Postgres add-on is provisioned, and you can now use this URL in your app for database connections.

Update your settings.py to handle the DATABASE_URL environment variable using dj_database_url:
  - pip install dj-database-url and  psycopg2 ( I have used version dj-database-url==0.5.0 and 
  psycopg==3.2.1)

In settings.py
-  import dj_database_url
   import os

-DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

SECRET_KEY = os.environ.get('SECRET_KEY')

Static Files Handling
Django needs to know how to handle static files in production. Install whitenoise to simplify serving static files.
    -pip install whitenoise

Update MIDDLEWARE in settings.py:
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

Configure static files:
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [os.path.join(BASE_DIR/ 'static'), ]
  STATIC_ROOT = os.path.join(BASE_DIR/ 'staticfiles')

Create a file in the root directory env.py and add to .gitignore

os.environ.setdefault(
    "DATABASE_URL", "postgres://u3gotcqundo:*************")
os.environ.setdefault("SECRET_KEY", "<Your_secret_key >")
    os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://<your_api_key>:<your_api_secret>@dv185mjri")

these will be set in reveal configvars in your project settings at heroku.com.

Run Migrations
  -heroku run python manage.py migrate

Collect Static Files
  -python manage.py collectstatic

Before Adding commiting and push changes to website make sure to set DEBUG=False
in setting.py

From inside your project at heroku.com go to the deploy tab scroll down and click Deploy Branch

----------------------------------------

Music-Alley
Music-Alley is a site for musicians and music fans so that they can share their music and fans can find new artist and old favourites. Musicians will be able to share, not only their music but also any recent events, updates, daily musings and any gigs coming up helping them grow their fan base.  Fans will be able to not just enjoy their music but connect with artists and find out what gigs are coming up.

----------------------------------------

PROJECT PREPARATION

----------------------------------------


User Stories

--Admin/Superuser--

As admin you I can create new admin users so they can admin the site if there are any undesired or inappropriate posts

- create new users inculding passwords

- view user details

- edit user details

- delete old or banned users, including any posts they may have created

- create new post

- read posts

- update posts if there are errors

- delete posts if neccesary

- update their password


--BANDS/ARTIST(User)--
	-Signup as an Artist and set password so that they have secure access and can let the world know what is new in their musical world

-User MUST be able to Create, Read, Update and Delete their profile requiring a password for login.

- Profile SHOULD include Name of Band or Artist, Genre of Music, Picture/Artwork, about section, Discography and link to where the music can be listened to or purchased, Social Media, contact info. 

-User COULD be able to post upcoming gigs Inc city, venue, date, time, cost and where to buy tickets with some artist imagery and link to where info about venue accessibility can be found. 

-They COULD be able to add photos from the gig and a few lines about how the gig went

-


--FANS(CASUAL USERS)--
-Fans MUST be able to browse Artist posts and 

-Fans SHOULD be able Sign up as a Fan and set a password 

-Fans COULD be able to create, Read, Update and delete their profile requiring a password for login.

-Fans Could be able to search for bands/artist by Genre, Artist Name, Song title, Album title

-Fans should be able to leave comments below artists posts

-Fans should be able to search for gigs by city, venue, genre and date

-Fans WON'T be able to edit artists Posts


Models/Databases

User_Type:
		-admin
		-Artist
		-Fan

	
	Admin:
		ID-------------------- Integer
		Username--------- String
		Password---------- String

	Artist:
		ID ------------------- Integer
		Username--------- String/Charfield
Password---------- String/Charfield
		Artist Name------- String/Charfield primary
		Genre -------------- String/Charfield
		About--------------- String/TextField
Profile pic---------- Imagefile/summertime
Artwork------------- Image file/summertime
Albums------------- String/ForeignKey
Songs--------------- String/foreignKey
Social media/Contact Info - Links
Gigs------------------Foreign Key



	Fans:
		ID--------------------- Integer
		Username---------- String/Charfield
		Password----------- String/Charfield
		Favourite Genres—
		
		

Album:
		ID--------------------- Integer
		Name---------------- String/Charfield
		Artist----------------- String/Charfield/Foreign Key
		Songs----------------- string/charfield/ Foreign Key
		Date------------------ ?????? 
		Link to listen-------
		Link to Buy --------

	Song:	
		ID-------------------- Integer
		Name--------------- String/Charfield
		Album-------------- String/Charfield/ForeignKey
		Artist---------------- String/Charfield/ForeignKey
		Link to listen------
		Link to Buy

	Gigs: 
		ID---------------------Integer
		Artist----------------String/Charfield/ForeignKey
		City------------------ String/Charfield
Venue-------------- String/Charfield
Date time---------- ??????????
Price---------------- float 2 decimal places
Link to purchase tickets -
Venue Web site – Link ---



Must Have
User login
Artist posting including CRUd


Should Have
comments including crud


Could Have
Songs posting page
gigs posting page

Wont have
ticket purchase




Wireframes

LANDING PAGE BEFORE LOGIN - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/7c33bc65-5c71-4eeb-b2e3-b55273c7fccb)


LANDING PAGE BEFORE LOGIN - PHONE

![image](https://github.com/user-attachments/assets/b5697e4e-dafb-4b0e-9c8e-9e3c744f6e0b)


LANDING PAGE AFTER LOGIN - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/d809e592-2585-47d3-bf0e-fba979443c5d)

LANDING PAGE AFTER LOGIN - PHONE

![image](https://github.com/user-attachments/assets/51502a01-a2a3-4f74-b33f-32859cdb7cde)

INDIVIDUAL ARTIST POST PAGE - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/86871449-d39d-4d05-a159-c125ff7f975e)

INDIVIDUAL ARTIST POST PAGE - PHONE   ------------ NEED

SIGN IN PAGE - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/bd29fff5-844a-46a3-91b3-3c15631a6187)

SIGN IN PAGE - PHONE ---------- NEED

REGISTER PAGE - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/91854faa-ef6d-4eaa-9062-0117836777c3)

REGISTER PAGE - PHONE   -------- NEED

ABOUT PAGE - BROWSER WINDOW

![image](https://github.com/user-attachments/assets/9142027d-4587-4d50-8c85-bf90c97dad43)

ABOUT PAGE - PHONE -------- NEED


Features
•	Navigation Bar
o	Featured on all five pages, the full responsive navigation bar includes links to the Logo, Home page, Songs, gigs and Sign Up page(if not registered) login page(if not logged in) and logout page( if logged in) and is identical in each page to allow for easy navigation. These fold into a burger on smaller screens
o	 
o	 ![image](https://github.com/user-attachments/assets/e230968a-9ede-4ad2-9e31-84636ab4807b)

o	
o	This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button.
o	You also have next and previous buttons to view more artists
•	Main
o	Artist Post snippet will be displayed on larger screens 3 x 2 total 6
o	Artist Post snippet will be displayed on smaller screens 1 x 6 total 6
o	There is a form at the bottom If you would like to make a New artist Posting
•	Footer
o	This will include links to my social media so people can contact me if necessary
•	Links
o	Clicking on the title of a post will take you through to a more details page

 

•	
•	
•	 
•	Landing Page
o	Header Image displaying different Musical artists instantly helping you know this site is about a variety of music.
 
![image](https://github.com/user-attachments/assets/95d2ded7-c179-4868-b0c8-fd72f6c79b21)


o	Background Image is of magical colourful sheet music
•	
o	Immediately serves up a selection of  6 Artists for you to browse with Next and previous buttons
 
•	New artist Posting section
	 
 ![image](https://github.com/user-attachments/assets/08a5ba58-e136-4964-9826-8a4d812f62e7)



•	Artist Posting Details Section
o	Clinking on the title of the posting will take you through to the Artist Posting details page
o	This section shows you the full rundown of the posting allowing fans to find out more about whats going on in the artists life at the moment
o	User should be able to edit and delete postings if they where the user who created it. Needs fixing
o	 
•	Users can Also leave a comment that needs to be approved by the User that posted
•	Users can see other comments that have been approved
•	User that leaves a comment has the ability to edit and delete it
 ![image](https://github.com/user-attachments/assets/bf259ceb-95c9-4bfa-a135-1f26a876ccf3)


•	About Section
o	This section Allows Me To Let people Know about Me as a Coder and as a musician. The can also contact me if they want to Collaborate for either.

 
•	The Sign Up Page
o	This page will allow the user to get signed up to Music-Alley so they can leave Post listings or leave comments
o	![image](https://github.com/user-attachments/assets/dd2dbb75-f417-4fbe-8f0a-c013f1304f07)

o	 .
o	Some CSS Styling is necessary
•	 
•	Shows that you are logged In and changes the nav bar
•	 

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:
Features Left to Implement
•	Individual songs Page
•	Gigs page
Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.
Validator Testing
•	HTML
o	Some errors were returned when passing through the official W3C validator
•	 ![image](https://github.com/user-attachments/assets/b8606d09-ccdc-4acb-8241-66f5f04928d8)

Solved

•	CSS
o	No errors were found when passing through the official (Jigsaw) validator
Unfixed Bugs


Sign up Page
	Some CSS styling is necessary to make the words clearer
Error when deleting or editing post
	
 
There is an error with collecting the right url extension. Problem getting the right slug?

Resizing Issue
 

Some adjustments need to be made to the CSS to ensure the picture and text fit nicely in there boxes
You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.
Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub)
•	The site was deployed to Heroku  pages. At this address
•	https://dashboard.heroku.com/apps/music-alley/deploy/github



•	 The steps to deploy are as follows:
Make sure Debug = False in Setting.py
deploy from this page in Heroku
https://dashboard.heroku.com/apps/music-alley/deploy/github
scroll down and click on deploy

GitHub Repository

https://github.com/JohnHookes/John-Hookes-Final-Project-Music-Alley


•
In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism
You can break the credits section up into Content and Media, depending on what you have included in your project.
Content
•	A lot of code was taken From previous Projects at codeInstitute Tutor Support
•       Chatgpt helped with a lot of debugging issues


•	The icons in the footer were taken from Font Awesome
Media
•	The images of the cartoon musicians where taken from shutterstock background music notes from getty Images The photos used on the home and sign up page are from This Open Source site
•	The images used for the gallery page were taken from this other open source site



Congratulations on completing your Readme, you have made another big 
Other General Project Advice
Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work!
•	One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through this article by Chris Beams on How to Write a Git Commit Message
o	Make sure to keep the messages in the imperative mood
•	When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
o	For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept.
•	Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
o	Writing Your Best Code
o	HTML & CSS Coding Best Practices
o	Google HTML/CSS Style Guide
Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process!





![image](https://github.com/user-attachments/assets/5df13787-9fa9-4899-bf05-87887259b680)


Welcome John Hooks,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**



## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
