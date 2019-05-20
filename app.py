import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipe_site'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", recipes=mongo.db.recipes.find())
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find(), cuisine=mongo.db.cuisine.find(), serving_size=mongo.db.serving_size.find(), difficulty=mongo.db.difficulty.find() )

@app.route('/add_new_category', methods=['POST'])
def add_new_category():
    category_name = mongo.db.categories
    category_name.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))
    
@app.route('/add_new_cuisine', methods=['POST'])
def add_new_cuisine():
    cuisine_type = mongo.db.cuisine
    cuisine_type.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            