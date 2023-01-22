'''questão 8.
Crie um programa que seja uma API de um contador de números. Esta API irá
manter o número em sua memória, e esta irá iniciar com o valor 0 (zero).
Para o programa teremos as seguinte chamadas:
● POST /contador
{
"numero": <numero>
}
Irá definir um novo número para o nosso contador. O método irá retornar um
HTTP 201.
● GET /contador
Retorna o número que foi guardado na memória, em um JSON no formato:
{
"numero": <numero guardado>
}
E também um HTTP 200.
● PUT /contador/incrementa
Irá incrementar o valor do número em 1 e retornar um HTTP 202.
● DELETE /contador
Irá zerar o valor do contador. A API irá retornar um HTTP 202.
Seguem algumas chamadas que fizemos no terminal, para mostrar o
comportamento de nosso programa, considere que iniciamos o programa agora e
executamos os testes na ordem apresentada:
1) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 0}
2) curl -X POST 'http://localhost:5000/contador’ -d
'{"numero": 123}'
Retornou um HTTP 201.
3) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 123}
4) curl -X PUT 'http://localhost:5000/contador/incrementa’
Retornou um HTTP 202.
5) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 124}
6) curl -X DELETE 'http://localhost:5000/contador’
Retornou um HTTP 202.
7) curl -X GET 'http://localhost:5000/contador’
Retornou:
{ "numero": 0}
Dificuldade: Média. Tempo: 9-17 minutos. Tempo para pensar no número na
memória, e fazer cada método.'''

from flask import Flask, request, jsonify

app = Flask(__name__)

contador = 0

@app.route("/contador", methods=["POST"])
def set_contador():
    data = request.get_json()
    global contador
    contador = data.get("numero")
    return "", 201

#1
@app.route("/contador", methods=["GET"])
def get_contador():
    return jsonify({"numero": contador}), 200

#4
@app.route("/contador/incrementa", methods=["PUT"])
def incrementa_contador():
    global contador
    contador += 1
    return "", 202

@app.route("/contador", methods=["DELETE"])
def reset_contador():
    global contador
    contador = 0
    return "", 202

if __name__ == "__main__":
    app.run(debug=True)
