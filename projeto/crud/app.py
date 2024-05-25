from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://developer:1234567@localhost/crud-python'


db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'customer'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    cpf = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def __init__(self, name, phone, cpf, email):
        self.name = name
        self.phone = phone
        self.cpf = cpf
        self.email = email


with app.app_context():
    db.create_all()


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        cpf = request.form['cpf']
        email = request.form['email']
        if name and phone and cpf and email:
            person: Person = Person(name, phone, cpf, email)
            db.session.add(person)
            db.session.commit()
    return redirect(url_for('index'))


@app.route('/list')
def list_persons():
    persons = Person.query.all()
    return render_template('list.html', persons=persons)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    person = Person.query.filter_by(_id=id).first()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        if person.name and person.phone and person.email:
            person.name = name
            person.phone = phone
            person.email = email

            db.session.commit()
            return redirect(url_for('list_persons'))

    return render_template('update.html', person=person)

@app.route('/delete/<int:id>')
def delete(id):
    person = Person.query.filter_by(_id=id).first()
    db.session.delete(person)
    db.session.commit()

    persons = Person.query.all()
    return render_template('list.html', persons=persons)


if __name__ == '__main__':
    app.run(debug=True)
