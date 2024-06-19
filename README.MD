# ENSF 692 Spring 2024 - Assignment 5

## 📚 Learning Outcomes
* Create a simple Flask application with multiple routes
* Scrape and parse data from a single web page
* Store and manipulate data within a DataFrame
* Print a DataFrame object to a webpage

## 💻 Program Specifications
The demo program in Assignment 5 is a collaborative effort between Garth Johnson and Emily Marasco, and is used with permission.
Before submitting your files, you must complete the following tasks:
* Change "STUDENT NAME" to your own name in the code.
* Follow the "/hello/<name>" route by entering your own name. Take a screenshot of the display. 
* Modify the book table to display a new column with the sale price (reduced by 25%). Submit a screenshot of the modified table being displayed.
* Create a new route "/learn" that displays one thing that you learned in ENSF 692. Submit a screenshot of your answer being displayed.
* Your submitted code must match your provided screenshots.
* Your code will be run by the instructor/TAs as your end user.
* Please post all queries to the discussion board or email them to the instructor (Sarah Shah).
* The grading rubric will be posted to D2L.

To run your web application:
MAC/Linux
* Make sure you are working in the correct directory
* `export FLASK_ENV=development`
* `export FLASK_APP=web_data_app.py`
* `flask run`

Windows
* Make sure you are working in the correct directory
* `set FLASK_ENV=development`
* `set FLASK_APP=web_data_app.py`
* `flask run`

The FLASK_ENV variable might be deprecated in the latest version of Flask. If that's the case, you might have to use debug=True in app.run(). 

Once the application is running, browse the local system on port `5000` (typically http://localhost:5000/).  When you do, you should see the friendly message "Hello World!" in your browser and the following in the terminal where the application is running:
    ❯ flask run
    * Serving Flask app "web_data_app.py"
    * Debug mode: on
    * WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with watchdog (windowsapi)
    * Debugger is active!
    * Debugger PIN: 393-094-215
    127.0.0.1 - - [7/Jun/2023 23:07:39] "GET / HTTP/1.1" 200 -

Run the requirements file using `pip install -r requirements.txt` to ensure you have the correct versions necessary.
Make sure you are in your assignment working directory.

## 📝 Assignment Tasks
* Dowload relevant files to your local computer.
* Open VSCode and start a new terminal.
* `web_data_app.py` is provided as a starting point. Add your name to the header.
* Remember to test your program execution via the terminal: `run flask`
* Fulfill the tasks above and upload the successful execution screenshots to your assignment repository.
* Commit your screenshots and code.
* Push your local git history to github.
* Submit your repository HTTPS link to the Assignment 5 D2L dropbox.
* Tip: If you want to learn more about a specific aspect of Python or Flask, remember to take a look at the official documentation!

## 📚 Developer Comments
First off, much of this is inspired by https://realpython.com/flask-by-example-part-1-project-setup/ and various other sites, pages, and people encountered through the teaching and learning process.
This is a basic 'quick n simple' Python-Flask application tutorial written for general usage of Python/Flask. This will help a new (but probably not noob) Pythonista learn how to set up a basic web server application in Python with Flask running on a local server, and assumes that the the developer is using Visual Studio Code as their IDE of choice.
Flask is a Model-View-Controller (MVC) framework (see https://www.guru99.com/mvc-vs-mvvm.html for some insight to what MVC is and isn't, and also Real Python's https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/ page for more details.
If you'd like to try scraping more websites, take a look at http://toscrape.com/
If you'd like to expand on the book catalog example (without Flask), take a look at this link: https://towardsdatascience.com/a-really-gentle-introduction-to-web-scraping-in-python-83cb9e536db8
