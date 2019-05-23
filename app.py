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

@app.route('/recipes/<item_id>')
def recipes(item_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(item_id)})
    return render_template('recipes.html', recipes = the_recipe)
    

@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    recipe_detail = mongo.db.recipes.find()
    return render_template('editrecipe.html', recipes=the_recipe, detail=recipe_detail, recipes1=mongo.db.recipes.find(), categories=mongo.db.categories.find(), cuisine=mongo.db.cuisine.find(), serving_size=mongo.db.serving_size.find(), difficulty=mongo.db.difficulty.find()  )


@app.route('/update_recipe/<recipes_id>', methods=['POST'])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipes_id)},
    {
        'recipe_name':request.form['recipe_name'],
        'image':request.form['image'],
        'description':request.form['description'],
        'category_name': request.form['category_name'],
        'cuisine_type': request.form['cuisine_type'],
        'prep_time':request.form['prep_time'],
        'cook_time':request.form['cook_time'],
        'serving_size':request.form['serving_size'],
        'difficulty':request.form['difficulty'],
        'date_added':request.form['date_added'],
        'author_name':request.form['author_name'],
        'ingredients_1':request.form['ingredients_1'],
        'ingredients_2':request.form['ingredients_2'],
        'ingredients_3':request.form['ingredients_3'],
        'ingredients_4':request.form['ingredients_4'],
        'ingredients_5':request.form['ingredients_5'],
        'ingredients_6':request.form['ingredients_6'],
        'ingredients_7':request.form['ingredients_7'],
        'ingredients_8':request.form['ingredients_8'],
        'ingredients_9':request.form['ingredients_9'],
        'ingredients_10':request.form['ingredients_10'],
        'method_1':request.form['method_1'],
        'method_2':request.form['method_2'],
        'method_3':request.form['method_3'],
        'method_4':request.form['method_4'],
        'method_5':request.form['method_5'],
        'method_6':request.form['method_6'],
        'method_7':request.form['method_7'],
        'method_8':request.form['method_8'],
        'method_9':request.form['method_9'],
        'method_10':request.form['method_10']
        
    })
    return redirect(url_for('index'))

@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('index'))
    
    # url for delete recipe
# {{ url_for('delete_recipe', recipes_id=recipes._id) }}

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            