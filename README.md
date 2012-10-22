gae-oauth2-demo
===============

Using Google's AppEngine, webapp2, Oauth2 and Python 2.7 to verify users

To view example visit https://gae-oauth2.appspot.com/

Setting up on localhost
----
1.  Setup a project in the api console so we have a client_id and client_secret https://code.google.com/apis/console
*  Create Project
*  Click API Access
*  Click Create an OAuth 2.0 client ID...
*  Enter in a product Name and Product logo (optional) > click next
*  Choose Web application, Choose http:// (not secure https://),  enter localhost, click Create client ID
*  Copy the client_id and paste it in the views.py where decorator = (client_id = 'past client_id here')
*  Copy the client_secret and also past it in the views.py decorator.


Creating app on appspot.com
----
1. Create a new app https://appengine.google.com/
*  Choose a Application Identifier that no one has used yet (this is often the most difficult part)
*  **Authentication Options** (Advanced) CHECK (Experimental) Open to all users with an OpenID Provider
*  Click Create Application
*  On the dashboard, left navigation bar, under Adminstration, click Application Settings
*  **Set Authentication Options** to Google Accounts API
*  Save Settings


Updating oauth2 to point to appspot instead of localhost
----
1.  In API Access, Click edit settings on the right side of the Client ID (originally created for localhost)
*   Remove "localhost"
*   Add http://<_your_application_id_>.appspot.com/oauth2callback to the redirect uri
*   Also add https://<_your_application_id_>.appspot.com/oauth2callback to the redirect uri
*   Change the javasript Origins to http://<_your_application_id_>.appspot.com

