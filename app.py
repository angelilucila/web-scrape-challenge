from flask import Flask, render_template, redirect
import scrape_mars

app = Flask(__name__)

@app.route("/")
def scrape():
    return render_template("index.html", title= mars.news_title, news_p = mars.news_p ,jpl_url = mars.featured_image_url, hem_img = mars.image_url, description=description, image_title = mars.image_title, table = mars.html_table)

