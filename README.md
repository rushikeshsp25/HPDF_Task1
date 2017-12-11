# HPDF_Task1
This repository contains Hasura Product Developement Felloship Week 1 Task

The following tasks will have to be demonstrated:

A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own first name).

Add a route, for e.g. http://localhost:8080/authors, which:
fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
Respond with only a list of authors and the count of their posts (a newline for each author).

Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.

A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.
    
Please note that http://localhost:8080/ is just an example, you can run the flask, express web-servers at their default ports on your local machine. You will receive more instructions on deploying your app after the deadline.
