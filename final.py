from flask import Flask,make_response,render_template,request,abort
app=Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World - Rushikesh'
	

@app.route('/authors')
def authors():
	return 'Tried very hard but not able to complete this'
	
	
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
	return render_template('output.html',name='image')
	
	
@app.route('/input',methods = ['POST', 'GET'])
def input():
	if request.method == 'POST':
   		text = request.form['text']
   		return 'received :'+text
  		
   	return render_template('input_form.html')
	
if __name__=='__main__':
	app.run()
