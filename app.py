from flask import Flask, render_template, request, redirect

from database import engine, session
from models import Base, User

app = Flask(__name__)


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    users = session.query(User).all()
    return render_template('home.html', users=users)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        age = request.form['age']
        user = User(username=username,
                    phone=phone,
                    email=email,
                    age=age)
        session.add(user)
        session.commit()
        return redirect('/')
    return render_template('add-user.html')


@app.route('/edit-user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = session.query(User).filter(User.id==id).first()
    if request.method == 'POST':
        user.username = request.form['username']
        user.phone = request.form['phone']
        user.email = request.form['email']
        user.age = request.form['age']
        session.commit()
        return redirect('/')
    return render_template('edit-user.html',user=user)



@app.route('/delete-user/<int:id>', methods=['GET','POST'])
def delete(id):
    user = session.query(User).filter(User.id==id).first()
    session.delete(user)
    session.commit()
    return redirect('/')


# new_user = User(username='john', email='john@example.com')
# session.add(new_user)
# session.commit()


if __name__ == '__main__':
    app.run()
