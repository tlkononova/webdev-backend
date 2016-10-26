# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField

#from flask_wtf import Form


from wtforms.validators import Required

class SearchForm(Form):
    #openid = TextField('openid', validators = [Required()])
    #remember_me = BooleanField('remember_me', default = False)
 
    query = StringField("search", validators = [Required()])
    author = SelectField('Author', choices = [('saadi', 'Saadi'), ('hafiz', 'Hafiz')])
    #submit = SubmitField("Search")
