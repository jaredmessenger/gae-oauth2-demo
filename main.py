import webapp2

import views
            
app = webapp2.WSGIApplication([('/', views.LandingHandler),
                               (r'/(\d+)$', views.UserHandler),
                               ],
                              debug=True)
