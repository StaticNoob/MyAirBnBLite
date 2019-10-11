from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, NewPropertyForm
from pymongo import MongoClient

app = Flask(__name__)

# Keep this secret! Securely signs session cookie 
app.config['SECRET_KEY'] = 'de88ba613c5b497dbe8d9ae73b070d78'
#   ^^^^ Dictionary called config 

# default host and port
client = MongoClient('localhost', 27017)

db = client.testdatabase

# temp database
postings = [

    {
        "renter": "Ryan",
        "house_type": "Apartment",
        "city": "Seattle",
        "cost_daily": "60",
        "post_date": "9/3/19"
    }, 
    {
        "renter": "Colin",
        "house_type": "House",
        "city": "Putney",
        "cost_daily": "45",
        "post_date": "7/23/19"

    }  

]


# HOME PAGE
# Both routes handled by home() function
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=postings)
    # posts=postings gives template access to variables(in postings)



@app.route("/about")
def about():
    return render_template("about.html", title="About")
    # return "<h1>About Page</h1>"

# Route for /register.   /register accepts GET and POST requests
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # 'flash' method sends a one time message, 'success' is a bootstrap class
        flash(f"Account created for {form.username.data}!", 'success')
            # ^^ This is an 'f' string, allows embedding 
            # of python code inside a strig literal using '{ }'
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)
    # form=form gives template access to the form made in register()

@app.route("/login", methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ryanyap@bu.edu' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Check username and password.", 'danger')
    return render_template('login.html', title='Login', form=form)
    # form=form gives template access to the form made in register()

@app.route("/postNewProperty", methods=['GET', 'POST'])
def postNewProperty(): 
    form = NewPropertyForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            flash("Post Successfully Submitted!", 'success')

            post = {
                "postTitle": request.form['post_title'],
                "houseType": request.form['house_type'],
                "city": request.form['city'],
                "dailyPrice": request.form['daily_price'],
                "description": request.form["description"]
            }

            # New collection in Mongo database called 'posts'
            posts = db.properties
            # Insert 'post' into collection posts
            posts.insert_one(post)

            return redirect(url_for("home"))
        else:
            flash("Post Unsuccessful", 'danger')

    

    return render_template('postNewProperty.html', title='New Property', form=form)

   


# If running this method directly from app.py(this module)
# then run app on localhost with debug mode(no need
# to rerun to show changes)
if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
                                