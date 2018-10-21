from flask import flask, sessions, jsonify, render_template, url_for
import random
import copy
import pickle
import time
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def initalize_game():
    game = requests.get()
 # on click start game

class rounds(ndbModel):
    entries = ndb.StructuredProperties(
        Entry, repeated = (true)
    )
class Entry(ndb.Model):
    player = ndb.UserProperty()
    picture = ndb.BlobProperty()
    location = ndb.StringProperty()
    votes = ndb.IntegerProperty()

class Upload(webapp2.RequestHandler):
    def post(self):
        rounds = rounds()
        rounds.player = self.request.get('player')
        rounds.picture = self.request.get('picture')
        rounds.location = self.request.get('location')
        rounds.votes = self.request.get('votes')
        rounds.put()
        self.redirect('/')

class MainPage(webapp2.RequestHandler):

    def get(self):
        round_number = self.request.get('round_number',
                                          DEFAULT_ROUND_NUMBER)
        # for round_number in range (0, NUMBER OF ENTRIES)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/new', Upload),
], debug=True)

''' sandy = Entry(
    player='sandy', picture=123, location='sandy@example.com', votes=123)
jake = Entry(
    player='jake', picture=123, location='sandy@example.com', votes=123)
mark = Entry(
    player='mark', picture=123, location='sandy@example.com', votes=123)
kathy = Entry(
    player='kathy', picture=123, location='sandy@example.com', votes=123)
'''
