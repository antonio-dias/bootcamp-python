from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<string:name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    person = response.json()
    if name == "antonio":
        person = dict(name="antonio", gender="male", age="33")

    response_age = requests.get(f"https://api.agify.io?name={name}")
    age = response_age.json()['age']

    return render_template("guess.html", person=person, age=age)

@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/3a7586a2297d432db4ab")
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)

if  __name__ == "__main__":
    app.run(debug=True)