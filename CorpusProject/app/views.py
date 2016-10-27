# -*- coding: utf-8 -*-

from app import app
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for#, session

#from forms import SearchForm

from app import app

#from models import Entry

#from config import MAX_SEARCH_RESULTS



#from flask_wtf import Form
#from wtforms import TextField, SubmitField, SelectField



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
    
    #form = SearchForm()

    #alert = False
    #if form.validate_on_submit():
        #flash('Search query="%s", author=%s' %
        #      (form.query.data, str(form.author.data)))
        #return redirect('/index')
        #return redirect(url_for('search_results.html', author=request.form['author']))
    
    #return render_template('search.html', alert=request.args.get('alert'), title='Search', form = form)
    return render_template('search.html', title='Search')
    
   
    
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


'''
@app.route('/search_results', methods = ['GET', 'POST'])
def search_results():
    #author = request.form['author']
    #results = Entry.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    results = Entry.query.whoosh_search(author, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',author=author,
                           results=results)
'''
   
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
            #authorSaadi
            #authorHafiz = request.values.get('authorSaadi', None)
            print (authors)
            #if request.values.get('name', None) == 'asdf':
                #print('asdf')
                #render_template('search_results.html', msg=msg, author=author)
        #print('not asdf')
            return render_template('search_results.html', msg=msg, author=authors)
        else:
        #    alert = "empty"
        #    return redirect(url_for('search'), alert = alert)
            return redirect(url_for('search'))
    else:
        return redirect(url_for('search'))
		
		
#def searchCorpus(query, authors):
#    dirpath = 'static/corpus'
#    for root, dirs, filenames in os.walk(dirpath):
        
'''
    for root, dirs, filenames in os.walk(os.getcwd() + '/leo_tolstoy/xml_data/'):
            for fname in filenames:
                if doc.filename == fname:
                    new_path = os.path.join(root, fname)
                    my_doc, pages = parse_xml_doc(new_path, text_query)
                    if len(my_doc) > 0:
                        length = len(my_doc)
                        paragraph = my_doc[-1]
                        all_items += length
                        try:
                            cite = u'"'+doc.name + u'. "' + doc.source[:-1] + u', стр. ' + pages[-1]
                        except:
                            cite = u'"' + doc.name + u'. "' + doc.source[:-1]
                        results.append((doc.name, paragraph, doc.value, cite))
    return results, all_items
'''