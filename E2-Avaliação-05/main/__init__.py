from flask import Flask, request, url_for, redirect, render_template, flash
from main.models.tables import Cliente


app = Flask(__name__)


idGeralCliente = 8
codigoGeralCliente = 136


def refresh1(cliente):
    global idGeralCliente
    global codigoGeralCliente
    idGeralCliente += 1
    codigoGeralCliente += 17
    clientes.append(cliente)


def deletar(cliente):
    clientes.remove(cliente)



clientes = [Cliente(1, 'Jean', 17, '111.222.333-44', 'P.Física'),
            Cliente(2, 'Jonas', 34, '200.100.345-35', 'P.Física'),
            Cliente(3, 'Rei pele', 51, '200.100.345-37', 'P.Jurídica'),
            Cliente(4, 'Joao prdero', 68, '200.100.345-38', 'P.Física'),
            Cliente(5, 'Luis', 85, '200.100.345-39', 'P.Jurídica'),
            Cliente(6, 'Lazaro', 102, '200.100.345-40', 'P.Física'),
            Cliente(7, 'Zé', 119, '200.100.345-41', 'P.Jurídica')]


@app.route("/PaginaInicial")
@app.route("/home")
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if request.form['fisijurid'] == '1':
            cliente = Cliente(idGeralCliente, request.form['nome'], codigoGeralCliente, request.form['cpfcnpj'], 'P. Física')
            refresh1(cliente)
            flash('Adicionado!')
            return redirect(url_for('read'))
        elif request.form['fisijurid'] == '2':
            cliente = Cliente(idGeralCliente, request.form['nome'], codigoGeralCliente, request.form['cpfcnpj'], 'P. Jurídica')
            refresh1(cliente)
            flash('Adicionado!')
            return redirect(url_for('read'))
        else:
            flash('Escolha direito!')
            return redirect(url_for('create'))
    return render_template('create.html')


@app.route("/read")
def read():
    return [clientes[0].get_nomeUsuario(), clientes[0].get_cnpfcpfUsuario, clientes[0].get_tipoUsuario]


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        ClienteId = int(request.form['id'])
        cliente = [c for c in clientes if ClienteId == c.get_usuarioID()][0]
        cliente.set_nomeUsuario(request.form['nome'])
        cliente.set_cnpjcpfUsuario(request.form['cpfcnpj'])
        flash('Atualizado com sucesso!')
        return redirect(url_for('read'))
    return render_template('atualizar.html')


@app.route("/delete", methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        ClienteId = int(request.form['id'])
        cliente = [c for c in clientes if ClienteId == c.get_usuarioID()][0]
        deletar(cliente)
        flash('Removido com sucesso')
        return redirect(url_for('read'))
    else:
        return render_template('remover.html')
