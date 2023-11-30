from flask import render_template

def get():
    return render_template('site/faq.html')
