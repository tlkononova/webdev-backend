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
    dirpath = root+'\\app\\static\\corpus\\'
    file='corpus.txt'
    f = open(dirpath+file, 'r')
    for line in f:       
        if query in line.decode('utf-8'):
            result.append(line)
            print result
    f.close()
    return result
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