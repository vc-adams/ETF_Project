from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# From the separate python file in this directory, we'll import the code that is used to scrape craigslist
import scrape_craigslist

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# identify the collection and drop any existing data for this demonstration
listings = mongo.db.listings
listings.drop()

# Render the index.html page with any craigslist listings in our database. 
# If there are no listings, the table will be empty.
@app.route("/")
def index():
    listing_results = listings.find()
    return render_template("index.html", listing_results=listing_results)

# This route will trigger the webscraping, but it will then send us back to the index route to render the results
@app.route("/scrape")
def scraper():

    # scrape_craigslist.scrape() is a custom function that we've defined in the scrape_craigslist.py file within this directory
    listings_data = scrape_craigslist.scrape(search_term="mountain bike")
    listings.insert_many(listings_data)
    
    # Use Flask's redirect function to send us to a different route once this task has completed.
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
