import os
import re
import codecs
import hashlib
import hmac
import random
import string
import webapp2
import jinja2

from users import *

from google.appengine.ext import ndb


def blog_key(name='default'):
    """Return Key for Blog"""
    return ndb.Key('blogs', name)


class BlogPost(ndb.Model):
    """Blog Info"""
    subject = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    author = ndb.StructuredProperty(User)
    likes = ndb.IntegerProperty(default=0)


class Comment(ndb.Model):
    """Comment Info"""
    post_id = ndb.IntegerProperty(required=True)
    author = ndb.StructuredProperty(User)
    content = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)


class Like(ndb.Model):
    """Like Info"""
    post_id = ndb.IntegerProperty(required=True)
author = ndb.StructuredProperty(User)