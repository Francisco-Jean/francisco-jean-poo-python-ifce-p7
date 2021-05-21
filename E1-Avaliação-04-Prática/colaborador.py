class Colaborador():
    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioAtual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salarioAtual = salarioAtual
        self.movimentos = []
        self._totalProventos = 0.0
        self._totalDescontos = 0.0

    def inserirMovimentos(self, movimento):
        self.movimentos.append(movimento)

    def calcularSalario(self):
        valorLiquido = 0.0
        for x in self.movimentos:
            if x.getTipomovimento() == 'P':
                self._totalProventos += x.getValor()
                valorLiquido += x.getValor()
            elif x.getTipomovimento() == 'D':
                self._totalDescontos += x.getValor()
                valorLiquido -= x.getValor()
            else:
                print(f'WARNING: ALGUM MOVIMENTO CRIADO TEM UM TIPO INVÁLIDO')

        return f'\nCódigo: {self.getCodigo()} Nome: {self.getNome()}\
                 \nSalário: {self.getSalario()} Total de Proventos: {self.getProventos()} Total de Descontos: {self.getDescontos()}\
                 \nValor Líquido: {valorLiquido + self.getSalario()}\n'

    def getProventos(self):
        return self._totalProventos

    def getDescontos(self):
        return self._totalDescontos
    
    def getCodigo(self):
        return self._codigo

    def getNome(self):
        return self._nome

    def getEndereco(self):
        return self._endereco

    def getTelefone(self):
        return self._telefone

    def getBairro(self):
        return self._bairro

    def getCep(self):
        return self._cep

    def getCpf(self):
        return self._cpf

    def getSalario(self):
        return self._salarioAtual

    def setCodigo(self, cod):
        self._codigo = cod

    def setNome(self, name):
        self._nome = name

    def setEndereco(self, newendereco):
        self._endereco = newendereco

    def setTelefone(self, tel):
        self._telefone = tel

    def setBairro(self, newbairro):
        self._bairro = newbairro

    def setCep(self, newcep):
        self._cep = newcep

    def setCpf(self, newcpf):
        self._cpf = newcpf

    def setSalario(self, newsalario):
        self._salarioAtual = newsalario