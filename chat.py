from flask import Flask, render_template, request, jsonify
from chat import consultar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/preguntar", methods=["POST"])
def preguntar():

    datos = request.json

    pregunta = datos["pregunta"]

    respuesta = consultar(pregunta)

    return jsonify({
        "respuesta": respuesta
    })


if __name__ == "__main__":
    app.run(debug=True)
