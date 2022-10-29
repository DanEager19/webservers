from flask import *
import db

app = Flask(__name__)
db = db.SqliteDB()

@app.route('/')
def index():
    rows = db.read_requests()
    return render_template('index.html', rows=rows)

@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        problem = request.form['problem']
        db.create_request(name, email, problem)
    return redirect(url_for('index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        db.update_request(id)
    return redirect(url_for('index'))

@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        db.delete_request(id)
    return redirect(url_for('index'))

if __name__ == 'main':
    app.run()