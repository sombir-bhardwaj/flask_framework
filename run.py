import flask as flask, render_templates, request, flash, redirect, session
from flask import render_template, request, redirect
from flask_sqlalchemy import sqlalchemy
from models.models import *

import pdb, time
import types

app = flask(__name__)
app.config.from_object('config')
db = sqlalchemy(app)

@app.route('/')
def cre():
    return "hello"

@app.route('/user',methods=['get','post'])
def index():
    user1_data = db.session.query(user),all()
    return render_template('index.html',user1_data=user1_data)

@app.route('/create',methods=['get','post'])
def create():
    if request.method =="post":
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        user_obj=user(name)
        user_obj.age=age
        user_obj.gender=gender
        db.session.add(user_obj)
        db.session.commit()
        db.session.close()


        if request.method =="get":
            user_data = types.simplenamespace()
            return render_template('create.html',user_data=user_data)

@app.route('/<int:user_id>/update',methods=['get','post'])
def update(user_id):
     if request.method == "Post":
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        user_update=db.session.query(user).filter(user.id==user_id).first()
        user_update.age=age
        user_update.name=name
        user_update.gender=gender
        db.session.commit()
        return redirect('/user')

     if request.method =="GET":
        user_data = user.query.filter_by(id = user_id).one()
        return render_template('create.html', user_data=user_data)



@app.route('/<int:user_id>/delete')
def delete(user_id):
    user_delete =db.session.query(user).filter_by(id=user_id).first()
    db.session.delete(user_delete)
    db.session.commit()
    return redirect('/user')

if __name__ =='__main__':
    app.run(debug=True)



