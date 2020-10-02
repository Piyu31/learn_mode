from flask import Flask,make_response,render_template,request,redirect,url_for,session,redirect,abort,flash


app=Flask(__name__)
app.config['SECRET_KEY']='thisissecret'


#setting the cookie 
@app.route('/setcookie')
def set():
	resp=make_response('Cookie is created')
	resp.set_cookie('framework','roch')
	return resp


#getting the cookie,read the cookie
@app.route('/getcookie')
def get():
	framework=request.cookies.get('framework')
	return 'The cookie is ' + framework
#creating session
@app.route('/setbackground/<mode>')
def set_bg(mode):
	session['mode']=mode
	return redirect(url_for('index'))


#dropping a session
@app.route('/dropsession')
def drop():
	session.pop('mode' , None)
	return redirect(url_for('index')

@app.route('/')
def index():
	return render_template('login.html')

#redirect
@app.route('/login',methods=['GET'])
def  hut():
	return redirect(url_for('index'))

#testing errors and abort
@app.route('/login', methods=['POST'])
def home():
	if request.method == 'POST':
		if request.form['user_name'] == 'Kent':
			return redirect(url_for('success'))
		else:
			abort(401)
	else:
		return redirect(url_for('index'))	

@app.route('/success')
def success():
	return 'logged in successfully'

@app.route('/flash')
def msg_flash():
	flash('This is a flashed message!')
	return redirect(url_for('flashup'))

@app.route('/flashing')
def flosh():
	return redirect(url_for('flashup.html'))

@app.route('/layout')
def layout():
	return redirect(url_for('layout.html'))




if __name__ == '__main__':
	app.run()