from flask import Flask, render_template, jsonify
import pandas as pd
import logging
import os
from bs4 import BeautifulSoup
import requests

# Explicitly specify the templates folder
app = Flask(__name__, template_folder=r'C:\ENSF 692\Assignments\A5\ENSF692-Assignment5\templates')
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_there(name):
    from datetime import datetime
    import re

    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! Welcome to Assignment 5. It's " + formatted_now
    return content

@app.route("/data")
def book_data():
    try:
        logging.debug("Starting book data route")
        logging.debug(f"Current working directory: {os.getcwd()}")
        template_path = os.path.join(app.template_folder, 'template.html')
        logging.debug(f"Template path: {template_path}")
        logging.debug(f"Template exists: {os.path.exists(template_path)}")
        
        source = requests.get("http://books.toscrape.com/")
        logging.debug("Fetched source data")
        
        soup = BeautifulSoup(source.content, 'html.parser')
        logging.debug("Parsed HTML content with BeautifulSoup")
        
        book_results = soup.find_all(attrs={'class': 'product_pod'})
        logging.debug("Found all book results")

        titles = []
        prices = []

        for book in book_results:
            titles.append(book.h3.a.get('title'))
            prices.append(float(book.find('p', class_="price_color").text[1:]))

        logging.debug(f"Extracted titles: {titles}")
        logging.debug(f"Extracted prices: {prices}")

        book_data = pd.DataFrame(list(zip(titles, prices)), columns=['Titles', 'Prices'])
        book_data['Sale Prices'] = book_data['Prices'] * 0.75  # Reduced by 25%

        logging.debug("Created DataFrame successfully")
        logging.debug(book_data)

        return render_template('template.html', tables=[book_data.to_html(classes='data')], titles=book_data.columns.values)
    
    except Exception as e:
        logging.error("Error occurred in /data route", exc_info=True)
        return jsonify(error=str(e)), 500

@app.route("/learn")
def learn():
    return "I learned how to build a web application using Flask."

if __name__ == '__main__':
    app.run(debug=True)
