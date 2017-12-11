# HPDF_Task1
This repository contains Hasura Product Developement Felloship Week 1 Task
This is implemented using Python based web framework -> Flask

To run this project on your local machine follow below given steps:

1] Clone this repo in your local machine

2] Install flask on your system (http://flask.pocoo.org/docs/0.12/installation/)

3] Open terminal and cd to HPDF_Task1

4] To run the application you can either use the flask command or python’s -m switch with Flask.

    
    Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable               
    $ export FLASK_APP=hello.py
    $ flask run
     * Running on http://127.0.0.1:5000/

    If you are on Windows you need to use set instead of export.
    Alternatively you can use python -m flask:

    $ export FLASK_APP=hello.py
    $ python -m flask run
     * Running on http://127.0.0.1:5000/
     
5]Open Your Favourite Browser 

-------------------------------------------------------------------------------------------------------------------------------

The following tasks are demonstrated:

1] http://localhost:5000/ that displays a simple string like "Hello World - Rushikesh"

2] Add a route, for e.g. http://localhost:5000/authors, which:
fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
Respond with only a list of authors and the count of their posts (a newline for each author).

3] Set a simple cookie (if it has not already been set) at http://localhost:5000/setcookie with the following values: 
name=rushikesh and age=21.

4] Fetch the set cookie with http://localhost:5000/getcookies and display the stored key-values in it.

5] Deny requests to your http://localhost:5000/robots.txt page. 

6] Render an HTML page at http://localhost:5000/html or an image at http://localhost:5000/image.

7] A text box at http://localhost:5000/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.
    
NOTE: Flask server runs at 127.0.0.1:5000
