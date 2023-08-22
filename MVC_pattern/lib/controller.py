from flask import Blueprint
from .services import insert, update, delete, render_template
from lib.model import Data

datas = Blueprint("Data", __name__)

@datas.route('/')
def Index():
    all_data = Data.query.all()
    return render_template("index.html", contacts = all_data)

@datas.route('/insert', methods = ['POST'])
def add_contact():
    return insert()

@datas.route('/update', methods = ['GET', 'POST'])
def update_contact():
    return update()

@datas.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete_contact(id):
    return delete(id)

