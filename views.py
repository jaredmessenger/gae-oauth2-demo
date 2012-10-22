import os
import urllib2
import cgi

import webapp2
import jinja2
import json

from oauth2client.appengine import OAuth2Decorator

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

decorator = OAuth2Decorator(client_id='968592128601.apps.googleusercontent.com',
                            client_secret='7ChU9MpHjd2MEU49qks0iPVU',
                            scope='https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email',
                            )

class LandingHandler(webapp2.RequestHandler):
    """
    If the user isn't logged in, will ask them to login
    else will redirect to their page
    """
    @decorator.oauth_aware
    def get(self):
        if not decorator.has_credentials():
            template_values = {
                'url': decorator.authorize_url(),
            }
            template = jinja_environment.get_template('templates/index.html')
            self.response.out.write(template.render(template_values))
        else :
            http = decorator.http()
            token = decorator.credentials.access_token
            data = json.load(urllib2.urlopen('https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s' %token))
            self.redirect('/%s' %data['id'])
            
class UserHandler(webapp2.RequestHandler):
    """
    Show the user's page
    """
    @decorator.oauth_required
    def get(self, userID):
        http = decorator.http()
        token = decorator.credentials.access_token
        data = json.load(urllib2.urlopen('https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s' %token))

        if userID == data['id'] :
            self.response.write('<img src="%s" /> Welcome %s id %s' %(data['picture'], data['name'], data['id'])) 
        else:
            self.error(401)
            self.response.out.write('access denied')