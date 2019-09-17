# 2019-mini-s47
BU Engineering EC463<br/>
Software Mini Project Group 47<br/>
Alex Fatyga + Yi Wei (Danny) Chen<br/>
<br/>
Website: https://ec463-group47.appspot.com/
<br/> Please make sure to use https so that the connection is considered secure by your browser and allows for location to be used
<br/>
<br/>
The web app uses Python (Flask) and HTML. Google Cloud has been used to allow for multiple users at the same time, a database was created on Cloud SQL (using Google Cloud) which is read in main.py and sent to the HTML mainpage. The sensor receives temperature data from the database but the values of humidity are randomized so that the sensor varies for each user. Upon log out, the location, map and user weather is still displayed because that is that uses the location permission and does not have to do with logging into Google.<br/>
APIs being used are Dark Sky for the user's weather and Google Maps for Javascript to show the map of the user's location.
<br/>
<br/>
## Schedule: <br/>
Set up front end and separate back end -> Danny <br/>
Cloud service provider -> Alex <br/>
--Put our started app on the cloud by Monday 9/9 <br/>
Google single sign on -> Alex <br/>
<br/>
Sprint 1 - 9/10 Tuesday to 9/11 Wednesday <br/>
Create a temperature and humidity graph-> Danny <br/>
Working Database that we can read from -> Alex <br/>
Sprint 2 - 9/12 Thursday to 9/15 Sunday<br/>
Receiving Location for the Weather API -> Danny <br/>
Weather API - user access to weather -> Danny<br/>
Have sensor data come from the database to then be put into the plot -> Alex<br/>
<br/>
## Meetings:<br/>
9/8 Sunday Night<br/>
9/10 Tuesday Night<br/>
9/12 Thursday Night<br/>
9/15 Sunday afternoon <br/>
<br/>
On 9/8, we decided we wanted a web app in Flask and started working<br/>
9/8 to 9/10 was spent setting up the cloud and the app itself<br/>
The meeting on 9/10 kicked off the 1st sprint and we set the goal to finish by our next meeting Thursday<br/>
The meeting on 9/12 tested sprint 1 and kicked off sprint 2 with the set goal to conclude on 9/15<br/>
The meeting on 9/15 concluded sprint 2 and began testing for sprint 2 and front end work <br/>
9/15 until the deadline will be spent on testing and improving the front end's appearance
<br/><br/>
## Tests:
Due to the way we have formatted our app, there is little user input meaning that all the user does is log in, allow their location to be used and log out. We have tested this by using a variety of emails, logging in and out multiple times, and checking if the map is correct. When a user log outs, the page no longer displays sensor data meaning this information is only displayed when the user is logged in. 
<br/><br/>
## How to use the web app:<br/>
-Go to the link listed above <br/>
-Click sign and sign into your google account <br/>
-allow your location to be used when the prompt pops up <br/>
-you will then see the plot of the data coming from the sensor and a map of your location with you current weather listed <br/>
<br/>
## Sources
https://cloud.google.com/python/getting-started/hello-world <br/>
https://cloud.google.com/sql/docs/mysql/connect-app-engine <br/>
https://cloud.google.com/sql/docs/mysql/connect-app-engine#configuring <br/>
https://developers.google.com/identity/sign-in/web/sign-in<br/>
https://medium.com/dailyjs/making-the-most-of-your-sphere-with-javascript-building-a-geolocation-based-weather-app-with-3df5ae1fcb27<br/>
https://developers.google.com/maps/documentation/javascript/examples/map-geolocation<br/>
https://www.w3schools.com/

