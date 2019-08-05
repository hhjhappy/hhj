from flask import Flask,url_for,request,render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/user/<username>')
def show_user(username):
    return 'User %s'% username

@app.route('/project/')
def pro():
    return 'The projrect page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/successful/')
def successful():
    return render_template('successful.html')

@app.route('/upload/',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/image/%s' % f.filename)
        #return redirect(url_for('successful'))
        return redirect(url_for('successful'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='220.243.129.4',port=80,debug=True)
