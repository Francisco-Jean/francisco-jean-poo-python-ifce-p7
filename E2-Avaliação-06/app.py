from flask import Flask, Response, request
import json
from models import Cliente, Produto, ItemNotaFiscal, NotaFiscal


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

listadeclientes = [
    Cliente(1, 'Nathalia', 1000, '4002892200', 'P. Física'),
    Cliente(2, 'Robert', 2000, '3334442220', 'P. Jurídica'),
    Cliente(3, 'Ricardo', 3000, '0119574231', 'P.Física')
]

listadeprodutos = [
    Produto(1, 10, 'Blusas', 15.50),
    Produto(2, 20, 'Caixa de som', 100.00),
    Produto(3, 30, 'Moletom', 250.00),
    Produto(4, 40, 'Camisa', 200.00)
]

listadeitens = [
    ItemNotaFiscal(1, 1, 5, listadeprodutos[0].to_json()),
    ItemNotaFiscal(2, 2, 5, listadeprodutos[1].to_json()),
    ItemNotaFiscal(3, 3, 10, listadeprodutos[2].to_json())
]

listadenotas = [
    NotaFiscal(1, 1, listadeclientes[0].to_json()),
    NotaFiscal(2, 2, listadeclientes[1].to_json())
]

listadenotas[0].adicionar_item(listadeitens[0].to_json())
listadenotas[0].adicionar_item(listadeitens[1].to_json())
listadenotas[0].calcular_total_nota()
listadenotas[1].adicionar_item(listadeitens[2].to_json())
listadenotas[1].calcular_total_nota()


@app.route("/clientes", methods=["GET"])
def seleciona_clientes():
    clientes_json = []
    for cliente in listadeclientes:
        clientes_json.append(cliente.to_json())

    return gera_response(200, "clientes", clientes_json)

@app.route("/cliente/<id>", methods=["GET"])
def seleciona_cliente(id):
    for cliente in listadeclientes:
        if str(cliente.id) == str(id):
            cliente_objeto = cliente
            cliente_json = cliente_objeto.to_json()

            return gera_response(200, "cliente", cliente_json)


@app.route("/cliente", methods=["POST"])
def cria_cliente():
    body = request.get_json()

    try:
        cliente = Cliente(id=body["id"], nome=body["nome"],
                          codigo=body["codigo"], cnpjcpf=body["cnpjcpf"],
                          tipo=body["tipo"])
        listadeclientes.append(cliente)
        return gera_response(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao cadastrar")


@app.route("/cliente/<id>", methods=["PUT"])
def atualiza_cliente(id):
    cliente_objeto = None
    for cliente in listadeclientes:
        if str(id) == str(cliente.id):
            cliente_objeto = cliente
    body = request.get_json()

    try:
        if 'id' in body:
            cliente_objeto.id = body['id']
        if 'nome' in body:
            cliente_objeto.nome = body['nome']
        if 'codigo' in body:
            cliente_objeto.codigo = body['codigo']
        if 'cnpjcpf' in body:
            cliente_objeto.cnpjcpf = body['cnpjcpf']
        if 'tipo' in body:
            cliente_objeto.tipo = body['tipo']

        listadeclientes.append(cliente_objeto)
        return gera_response(200, "cliente", cliente_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao atualizar")


@app.route("/cliente/<id>", methods=["DELETE"])
def deleta_cliente(id):
    try:
        cliente_objeto = None
        for cliente in listadeclientes:
            if str(id) == str(cliente.id):
                cliente_objeto = cliente

        for posicao_cliente in range(0, len(listadeclientes)):
            if listadeclientes[posicao_cliente] == cliente_objeto:
                del(listadeclientes[posicao_cliente])

        return gera_response(200, "cliente", cliente_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao deletar")


@app.route("/produtos", methods=["GET"])
def seleciona_produtos():
    produtos_json = []
    for produtos in listadeprodutos:
        produtos_json.append(produtos.to_json())

    return gera_response(200, "produtos", produtos_json)


@app.route("/produto/<id>", methods=["GET"])
def seleciona_produto(id):
    produto_objeto = None
    for produto in listadeprodutos:
        if str(id) == str(produto.id):
            produto_objeto = produto
    produto_json = produto_objeto.to_json()

    return gera_response(200, "produto", produto_json)

@app.route("/produto", methods=["POST"])
def cria_produto():
    body = request.get_json()

    try:
        produto = Produto(id=body["id"],
                          codigo=body["codigo"],
                          descricao=body["descricao"],
                          valorUnitario=body["valorUnitario"])
        listadeprodutos.append(produto)
        return gera_response(201, "produto", produto.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao cadastrar")


@app.route("/produto/<id>", methods=["PUT"])
def atualiza_produto(id):
    produto_objeto = None
    for produto in listadeprodutos:
        if str(id) == str(produto.id):
            produto_objeto = produto
    body = request.get_json()

    try:
        if 'id' in body:
            produto_objeto.id = body['id']
        if 'codigo' in body:
            produto_objeto.codigo = body['codigo']
        if 'descricao' in body:
            produto_objeto.descricao = body['descricao']
        if 'valorUnitario' in body:
            produto_objeto.valorUnitario = body['valorUnitario']

        listadeprodutos.append(produto_objeto)
        return gera_response(200, "produto", produto_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao atualizar")


@app.route("/produto/<id>", methods=["DELETE"])
def deleta_produto(id):
    try:
        produto_objeto = None
        for produto in listadeprodutos:
            if str(id) == str(produto.id):
                produto_objeto = produto

        for posicao_produto in range(0, len(listadeprodutos)):
            if listadeprodutos[posicao_produto] == produto_objeto:
                del(listadeprodutos[posicao_produto])

        return gera_response(200, "produto", produto_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao deletar")


@app.route("/itens", methods=["GET"])
def seleciona_itens():
    itens_json = []
    for item in listadeitens:
        itens_json.append(item.to_json())


    return gera_response(200, "itens", itens_json)

@app.route("/item/<id>", methods=["GET"])
def seleciona_item(id):
    item_objeto = None
    for item in listadeitens:
        if str(id) == str(item.id):
            item_objeto = item
    item_json = item_objeto.to_json()

    return gera_response(200, "item", item_json)



@app.route("/item", methods=["POST"])
def cria_item():
    body = request.get_json()

    try:
        item = ItemNotaFiscal(id=body["id"],
                              sequencial=body["sequencial"],
                              quantidade=body["quantidade"],
                              produto=body["produto"])
        listadeitens.append(item)
        return gera_response(201, "item", item.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao cadastrar")

@app.route("/item/<id>", methods=["PUT"])
def atualiza_item(id):
    item_objeto = None
    for item in listadeitens:
        if str(id) == str(item.id):
            item_objeto = item
    body = request.get_json()

    try:
        if 'id' in body:
            item_objeto.id = body['id']
        if 'sequencial' in body:
            item_objeto.sequencial = body['sequencial']
        if 'quantidade' in body:
            item_objeto.quantidade = body['quantidade']
        if 'produto' in body:
            item_objeto.produto = body['produto']

        listadeitens.append(item_objeto)
        return gera_response(200, "item", item_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao atualizar")


@app.route("/item/<id>", methods=["DELETE"])
def deleta_item(id):
    try:
        item_objeto = None
        for item in listadeitens:
            if str(id) == str(item.id):
                item_objeto = item

        for posicao_item in range(0, len(listadeitens)):
            if listadeitens[posicao_item] == item_objeto:
                del(listadeitens[posicao_item])

        return gera_response(200, "item", item_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao deletar")



@app.route("/notas", methods=["GET"])
def seleciona_notas():
    notas_json = []
    for notas in listadenotas:
        notas_json.append(notas.to_json())

    return gera_response(200, "notas", notas_json)



@app.route("/nota/<id>", methods=["GET"])
def seleciona_nota(id):
    nota_objeto = None
    for nota in listadenotas:
        if str(id) == str(nota.id):
            nota_objeto = nota
    nota_json = nota_objeto.to_json()

    return gera_response(200, "nota", nota_json)


@app.route("/nota", methods=["POST"])
def cria_nota():
    body = request.get_json()

    try:
        nota = NotaFiscal(id=body["id"],
                          codigo=body["codigo"],
                          cliente=body["cliente"],
                          lista_itens=body['itens'])

        listadenotas.append(nota)

        return gera_response(201, "nota", nota.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao cadastrar")


@app.route("/nota/<id>", methods=["PUT"])
def atualiza_nota(id):
    nota_objeto = None
    for nota in listadenotas:
        if str(id) == str(nota.id):
            nota_objeto = nota
    body = request.get_json()

    try:
        if 'id' in body:
            nota_objeto.id = body['id']
        if 'codigo' in body:
            nota_objeto.codigo = body['codigo']
        if 'cliente' in body:
            nota_objeto.cliente = body['cliente']
        if 'itens' in body:
            nota_objeto.lista_itens = body['itens']

        listadenotas.append(nota_objeto)
        return gera_response(200, "nota", nota_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao atualizar")

@app.route("/nota/<id>", methods=["DELETE"])
def deleta_nota(id):
    try:
        nota_objeto = None
        for nota in listadenotas:
            if str(id) == str(nota.id):
                nota_objeto = nota

        for posicao_nota in range(0, len(listadenotas)):
            if listadenotas[posicao_nota] == nota_objeto:
                del(listadenotas[posicao_nota])

        return gera_response(200, "nota", nota_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao deletar")

@app.route("/calculanf/<id>", methods=["GET"])
def calcula_nota(id):
    try:
        nota_objeto = None
        for nota in listadenotas:
            if str(id) == str(nota.id):
                nota_objeto = nota

        total_nota = nota_objeto.calcular_total_nota(True)

        return gera_response(200, "calculanf", f'Total: {total_nota} R$', "Calculado com sucesso!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "calculanf", {}, "Erro ao calcular!")

@app.route("/imprimenf/<id>", methods=["GET"])
def imprime_nota(id):
    try:

        nota_objeto = None
        for nota in listadenotas:
            if str(id) == str(nota.id):
                nota_objeto = nota
        nota_objeto.calcular_total_nota()
        nota_impressa = nota_objeto.imprimir_nota_fiscal()

        return gera_response(200, "imprimenf", nota_impressa, "Impressa com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "imprimenf", {}, "Erro ao imprimir")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run(debug=True)
