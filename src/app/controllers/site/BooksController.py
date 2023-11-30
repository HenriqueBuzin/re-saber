from flask import render_template

def get():
   return render_template('site/books.html')
