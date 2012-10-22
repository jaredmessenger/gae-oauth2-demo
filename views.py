import os
import urllib2
import cgi

import webapp2
import jinja2
import json
import httplib2

from oauth2client.appengine import OAuth2Decorator

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

decorator = OAuth2Decorator(client_id='968592128601.apps.googleusercontent.com',
                            client_secret='Uunj9V7owBRwdec-FFXuYE_J',
                            scope='https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email',
                            )


class LandingHandler(webapp2.RequestHandler):
    """
    Catches people that aren't logged and and forces them to User handler
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
            token = decorator.credentials.access_token
            data = json.load(urllib2.urlopen('https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s' %token))
            self.redirect('/%s' %data['id'])
            
class UserHandler(webapp2.RequestHandler):
    """
    Lists the projects the user can view
    """
    @decorator.oauth_required
    def get(self, userID):
        token = decorator.credentials.access_token
        http = decorator.http()
        try:
            data = json.load(urllib2.urlopen('https://www.googleapis.com/oauth2/v1/userinfo?access_token=%s' %token))
        except urllib2.HTTPError, e:
            self.response.out.write('access denied')
        else:
            if userID == data['id'] :
                self.response.write('<img src="%s" /> Welcome %s id %s' %(data['picture'], data['name'], data['id'])) 
            else:
                self.error(401)
                self.response.out.write('access denied')