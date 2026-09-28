from flask import Flask, request, url_for, session, redirect, render_template, flash
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "saflñdsfldkiijukiekswdx sfdafsafgrerjtretrt68545375473fefe432tewyp0o7ik7564utr4utj2jhg4"

@app.route("/")
def inicio():
    usuarios = Usuario.get_all()

    return render_template("index.html", usuarios=usuarios)

@app.route("/usuario_nuevo")
def form_usuario():
    return render_template("registro.html")

@app.route("/Crear", methods=['POST'])
def Crear_usuario():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email') 

    try:
        user_id = Usuario.save({
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
        })

        if not user_id:
            flash("No se pudo crear la cuenta.", "error")
            return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect("/")

    return redirect("/"), flash("Cuenta creada correctamente", "success")

@app.route("/usuario")
def usuario_html():
    render_template("usuario.html")

@app.route("/usuario/<int:user_id>")
def usuario(user_id):

    datos = {
        "id": user_id
    }

    usuario = Usuario.get_by_id(datos)

    return render_template("usuario.html", usuario=usuario)

@app.route("/editar/<int:user_id>")
def editar_html(user_id):
    datos = {
        'id': user_id
    }
    usuario = Usuario.get_by_id(datos)
    return render_template("edicion.html", usuario = usuario)

@app.route("/Editar/<int:user_id>", methods=['POST'])
def editar(user_id):
    data = {
        "id": user_id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.actualizar(data)
    return redirect(f"/usuario/{user_id}")

@app.route("/borrar/<int:user_id>")
def borrar(user_id):
    datos = {
        "id": user_id
    }
    Usuario.borrar(datos)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)