**Note: this readme is still under construction

Name:
ClimApp

Description:
An App for users to find climbing routes that match their experience level, equiptment needed, and by rating. 

First edition to include all the kernal elements required for the Greenfield/MVP project:

A brand-new codebase, never worked on before
A Flask Backend 
A Vue FrontEnd
With at LEAST 5 components
Parent components should pass Props to child components
A Postgres DB (We’ll start with SQLite3 and then migrate)
External API calls
Internal  API calls
A comprehensive README.md file

The Greenfield project MAY incorporate the following features:
Authentication
New technologies not yet discussed in this class-- eg:
Vuex (Store management)
Drag and Drop
D3.js (Charts and graphs)

Installation:

Clone the repo using git clone <https://github.com/Fiona-Gorrie/ClimbApp.git>

To get the server up and running, do the following from the project's root:
cd Server
pipenv install 
pipenv run python main.py

To get Vue running, do the following from the project's root in an additional terminal screen:
cd client
npm install
npm install vue-star-rating
npm run serve

Roadmap:
Future editions may include:

Seperate table containing climb grades

Weather information for the climbing area

Ability to search multiple types of route: Rock, Bouldering, Ice, Mixed. Each type having it's own dficulty rating system and required gear.

User Signup

State if you are open to contributions and what your requirements are for accepting them:

**
You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.
**

Authors and acknowledgment

Gratitude to the instructor, Phil Gonzalez, and TA's (Heath Naylor, Hamp Goodwin, Kyle Misencik, Chris Vincent) of Devetry's Code Forward Full Stack course for their time and support throughoutt the course and continued mentorship during our capstone projects and beyond into our hopeful employment as Jr dev's! 

**
License

For open source projects, say how it is licensed.
Project status

If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
**