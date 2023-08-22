from lib.extension import db
from lib.model import Data
from flask import request, redirect, url_for, flash, render_template


def insert():

    if request.method == 'POST':

        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Add Successfuly")

        return redirect(url_for('Data.Index'))

def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.phone = request.form['phone']
        my_data.email = request.form['email']

        db.session.commit()
        flash("Updated Successfully")

        return redirect(url_for('Data.Index'))
    
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Successfully")

    return redirect(url_for('Data.Index'))
