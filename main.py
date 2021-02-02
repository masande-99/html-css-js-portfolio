from flask import Flask
from flask import render_template
import smtplib


app = Flask(__name__)


@app.route('/index.html/')
@app.route('/index.html/<name>')
def index_html(name=None):
    return render_template('index.html',name=name)


@app.route('/about.html/')
@app.route('/about.html/<name>')
def about_html(name=None):
    return render_template('about.html',name=name)


@app.route('/projects.html/')
@app.route('/projects.html/<name>')
def projects_html(name=None):
    return render_template('projects.html',name=name)


@app.route('/ratings.html/')
@app.route('/ratings.html/<name>')
def rating_html(name=None):
    return render_template('ratings.html',name=name)

@app.route('/contact-us.html/')
@app.route('/contact-us.html/<name>')
def contact_us_html(name=None):
    return render_template('contact-us.html',name=name)

s = smtplib.SMTP('smtp.gmail.com',587)
sender_email_id = 'Masandelifechoices@gmail.com'
receiver_email_id = 'gontyelenimasande@gmail.com'
password = input('enter sender email password')

s.starttls()

s.login(sender_email_id,password)

message ="this is a tests "

s.send_message(sender_email_id,receiver_email_id,message)

s.quit()











