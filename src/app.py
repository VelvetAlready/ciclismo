from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask import Flask, render_template, session, request, redirect, json,jsonify, redirect
from config.db import app, db
from models.Clientes import Clientes, ClienteSchema


clienteschema = ClienteSchema()
clienteschemas = ClienteSchema(many=True) 

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    cliente = db.session.query(Clientes.nombre).filter(Clientes.nombre == usuario, Clientes.contraseña == contraseña).all()

    if len(cliente) > 0:
        session['usuario'] = usuario
        return render_template('Home.html')
    else:
        return redirect('/')
