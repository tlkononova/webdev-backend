# -*- coding: utf-8 -*-

from app import app
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for, session

from forms import SearchForm

from app import app, db

from models import Entry

from config import MAX_SEARCH_RESULTS



#from flask_wtf import Form
#from wtforms import TextField, SubmitField, SelectField



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods = ['GET', 'POST'])
def search():
    #user = {'nickname': 'Miguel'}  # fake user
    '''posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ] '''  

    form = SearchForm()
    
    if form.validate_on_submit():
        #flash('Search query="%s", author=%s' %
        #      (form.query.data, str(form.author.data)))
        #return redirect('/index')
        return redirect(url_for('search_results.html', author=request.form['author']))
    
    return render_template('search.html', title='Search', form = form)
    #return redirect(url_for('search_results', query=g.search_form.search.data))
   
    
'''
@app.route('/searching', methods=['POST'])
def searching():
    #if not g.search_form.validate_on_submit():
    #    return redirect(url_for('index'))
    author = request.form['author']
    #author = Entry(request.form['author'])#, request.form['text'])
    #return redirect(url_for('search_results.html', query=form.query.data))
    return redirect(url_for('search_results.html', author=author))
'''



@app.route('/search_results', methods = ['GET', 'POST'])
def search_results():
    #author = request.form['author']
    #results = Entry.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    results = Entry.query.whoosh_search(author, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',author=author,
                           results=results)