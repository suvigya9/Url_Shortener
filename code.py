
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db' 
# database path:  os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(3))

    def __init__(self, long, short):
        self.long = long
        self.short = short

@app.before_first_request
def create_tables():
    db.create_all()


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

def shorten_url():
	return "abc"

@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == "POST":
         url_received = request.form["nm"]
         #return url_received
         found_url = Urls.query.filter_by(long=url_received).first()

         if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
    #else:    
     #    return render_template("home.html")
    else:
    	short_url = shorten_url()
        print(short_url)
        new_url = Urls(url_received, short_url)
        db.session.add(new_url)
        db.session.commit()
        return short_url

else:
        return render_template('url_page.html')

if __name__ == '__main__':
   app.run(port=5000, debug=False)