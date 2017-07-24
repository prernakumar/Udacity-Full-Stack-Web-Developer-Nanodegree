import os
import re
import codecs
import hashlib
import hmac
import random
import string
import webapp2
import jinja2

from google.appengine.ext import ndb

secret = 'blog'

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PWD_RE = re.compile(r"^.{3,20}$")


def valid_username(username):
    """Validate Username"""
    return USER_RE.match(username)


def valid_password(password):
    """Validate Password"""
    return PWD_RE.match(password)


def hash_str(s):
    """Encrypt Password with HMAC"""
    return hmac.new(secret, s).hexdigest()


def make_secure_val(s):
    """Make secure value"""
    return "%s|%s" % (s, hash_str(s))


def check_secure_val(h):
    """Validate secure value"""
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val


def make_salt():
    """Generate salt for hashing"""
    return ''.join(random.choice(string.letters) for x in xrange(5))


def make_pw_hash(name, pw, salt=None):
    """Encrypt password with HASH"""
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)


def valid_pw(name, pw, h):
    """Decrypt Password"""
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)


def users_key(group='default'):
    """Return User Key"""
    return ndb.Key('users', group)


class User(ndb.Model):
    """User Info"""
    username = ndb.StringProperty(required=True)
pwd_hash = ndb.StringProperty(required=True)
