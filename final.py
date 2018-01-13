from flask import Flask,make_response,render_template,request,abort,jsonify
import json
import urllib
import sys
app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World - Rushikesh'

auth_dict={}
post_dict={}

def make_req():
    auth_dict.clear()
    post_dict.clear()
    authors=urllib.urlopen('https://jsonplaceholder.typicode.com/users').read().decode()
    auths=json.loads(authors)
    for i in auths:
        auth_dict[i['id']]=i['name']
    posts=urllib.urlopen('https://jsonplaceholder.typicode.com/posts').read().decode()
    post=json.loads(posts)
    for i in post:
        try:
            post_dict[i['userId']]+=1
        except:
            post_dict[i['userId']]=1
    return

def join():
    make_req()
    str1=""
    for i in auth_dict.keys():
        try:
            str1+="Author : "+str(auth_dict[i]+ "<br/>" + "Number of posts : "+str(post_dict[i])+"<br/>")
        except:
            pass
    return str1

@app.route('/authors')
def parse():
    temp = join()
    return temp	
	
@app.route('/setcookie')
def setcookie():
	resp = make_response(render_template('cookie.html'))
    	resp.set_cookie('name', 'Rushikesh')
    	resp.set_cookie('age', '20')
	return resp
	

@app.route('/getcookies')
def getcookies():
	name = request.cookies.get('name')
	age=request.cookies.get('age')
	return '<h3>name ->'+' '+name+'<br>age ->'+' '+age+'</h3>'
	

@app.route('/robots.txt')
def deny_request():
	abort(401)
	return 'deny request->This will never executes'
	

@app.route('/html')
def html():
	return render_template('output.html',name='html') 
	
	
@app.route('/image')
def image():
	return send_file('hasura1.jpeg',mimetype='image/gif')
	
	
@app.route('/input',methods = ['POST', 'GET'])
def input():
	if request.method == 'POST':
   		text = request.form['text']
   		return 'received :'+text
  		
   	return render_template('input_form.html')
	
if __name__=='__main__':
	app.run()
