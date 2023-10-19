from flask import Flask, redirect,request,jsonify,json,session,render_template
from config.bd import app, db
from models.usuario import usuario, usuarioSchema


usuario_Schema = usuarioSchema()
usuarios_Schema = usuarioSchema(many=True)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def ingresar():
    email = request.form['email']
    clave = request.form['clave']
    usuario = db.session.query(usuario.id).filter(usuario.nombre == email, usuario.clave == clave).all()
    resultado = usuario_Schema.dump(usuario)

    if len(resultado) > 0:
        session['email'] = email
        return redirect('/Home')
    else:
        return redirect('/')

@app.route('/Home', methods=['GET'])
def home():
    if 'usuario' in session:
        return render_template('Home.html')
    else:
        return redirect('/')
        
if __name__ == "__main__":
    app.run(debug=True)