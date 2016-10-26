from app import app
from app import db

#import sys
#if sys.version_info >= (3, 0):
#    enable_search = False
#else:
#    enable_search = True
#    import flask.ext.whooshalchemy as whooshalchemy
enable_search = True
import flask.ext.whooshalchemy as whooshalchemy


class Entry(db.Model):
    __searchable__ = ['author','text']

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True, unique=False)
    text = db.Column(db.String(10000), index=True, unique=False)
    

    #def __repr__(self):
        #return '<%r>' % (self.text)
    def __init__(self, author, text):
        self.author = author
        self.text = text

if enable_search:
    whooshalchemy.whoosh_index(app, Entry)
    #print ('indexed')