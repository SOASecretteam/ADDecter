from flask import Flask,render_template,session, redirect, url_for
from flask_script import Manager
#bootstrap
from flask_bootstrap import Bootstrap
#Flask form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#data base
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class PictureURL(db.Model):
    __tablename__ = 'website'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64), unique=True)
    WebEntity = db.relationship('WebEntity', backref='pictureURL') #relationship between PictureURL|WebEntity

    def __repr__(self):
        return '<PictureURL %r>' % self.url


class WebEntity(db.Model):
    __tablename__ = 'Entity'
    id = db.Column(db.Integer, primary_key=True)
    Entity = db.Column(db.String(64), unique=True, index=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id')) #relationship between PictureURL|WebEntity

    def __repr__(self):
        return '<WebEntity %r>' % self.Entity

class UrlForm(FlaskForm):
    url = StringField('Please Enter the picture url', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    if form.validate_on_submit():
        session['url'] = form.url.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, url=session.get('url'))


if __name__ == '__main__':
    manager.run()

test_url=PictureURL(url='https://www.youtube.com/watch?v=zRwy8gtgJ1A')
test_url2=PictureURL(url='https://github.com/bradtraversy/myflaskapp')
test_url3=PictureURL(url='https://www.bootstrapcdn.com/bootswatch/')
web=WebEntity(Entity='sky',website_id='test_url')
web2=WebEntity(Entity='building',website_id='test_url2')
web3=WebEntity(Entity='lake',website_id='test_url3')

db.session.add(test_url)
db.session.add(test_url2)
db.session.add(test_url3)
db.session.add(web)
db.session.add(web2)
db.session.add(web3)
db.session.commit()
print(test_url.id)