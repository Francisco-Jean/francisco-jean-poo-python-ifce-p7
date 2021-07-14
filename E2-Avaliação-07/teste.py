from logging import debug
from flask import Flask, url_for
from markupsafe import escape
from sql_configd import *
import json

app = Flask(__name__)
app.config()

clientes = {'1':'Jean', '2':'Camila', '3':'Francisco'}

@app.route('/api/clientes')
def clientes():
    return '<p>Bom dia</p>'.format(str(clientes))

app.run()