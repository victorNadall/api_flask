import mysql.connector
from flask import Flask, make_response, jsonify, request


mydb = mysql.connector.connect(
    host='localhost',
    user='MyUser',
    password='MainPassword',
    database='Pycodebr'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def get_carros():

    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM carros')
    meus_carros = cursor.fetchall()

    carros = list()
    for carro in meus_carros:
        carros.append(
            {
                'id': carro[0],
                'marca': carro[1],
                'modelo': carro[2],
                'ano': carro[3]
            }
        )

    return make_response(
        jsonify(
            mensagem='Lista de carros.',
            dados=carros
        )
    )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    cursor = mydb.cursor()
    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
    cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso.',
            carro=carro
        )
    )


app.run()
