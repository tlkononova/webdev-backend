# -*- coding: utf-8 -*-

from app import app
from flask import render_template, request, flash, redirect, url_for
from app import app



@app.route('/')
@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search', methods = ['GET', 'POST'])
def search():
    #return render_template('search.html', alert=request.args.get('alert'), title='Search', form = form)
    return render_template('search.html', title='Search')
    

   
@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    msg = ''
    subcorpus = False
    authors = []
    if request.method == 'POST':
        if request.values.get('name', None):
            msg = request.values.get('name', None)
            if request.values.get('authorSaadi', None) == 'on':
                authors.append('Saadi')
                subcorpus = True
            if request.values.get('authorHafiz', None) == 'on':
                authors.append('Hafiz')
                subcorpus = True
            
            #print (authors)
            
            result=searchCorpus(msg)
            return render_template('search_results.html', msg=msg, author=authors, result=result)
        else:
        #    alert = "empty"
        #    return redirect(url_for('search'), alert = alert)
            return redirect(url_for('search'))
    else:
        return redirect(url_for('search'))

import os

def searchCorpus(query):
    result = []
    root=os.getcwd()
    print root
    dirpath = root+r'/app/static/corpus/'
    file='corpus.txt'
    f = open(dirpath+file, 'r')
    for line in f:       
        if query in line.decode('utf-8'):
            result.append(line)
            #print result
    f.close()
    return result
