class FolhaPagamento():
    def __init__(self, mes, ano):
        self._mes = mes
        self._totalDesconto = 0.0
        self._totalProvento = 0.0
        self._totalSalario = 0.0
        self._ano = ano
        self.movimentos = []

    def inserirMovimentos(self, movimento):
        self.movimentos.append(movimento)

    def calcularFolha(self):
        cdAnterior = ''
        for x in self.movimentos: 
            cdAtual = x.getColaborador().getCodigo()
            if cdAtual != cdAnterior:
                self._totalSalario += x.getColaborador().getSalario()

            if x.getTipomovimento() == 'P':
                self._totalProvento += x.getValor()
            elif x.getTipomovimento() == 'D':
                self._totalDesconto += x.getValor()

            cdAnterior = x.getColaborador().getCodigo()
    
        return f'\nTotal de Salários:  {self.getTotalSalarios()}\
                 \nTotal de Proventos: {self.getTotalProventos()}\
                 \nTotal de Descontos: {self.getTotalDescontos()}\
                 \nTotal a Pagar:      {self.getTotalSalarios() + self.getTotalProventos() - self.getTotalDescontos()}\n'
    
    def getMes(self):
        return self._mes

    def getTotalDescontos(self):
        return self._totalDesconto

    def getTotalProventos(self):
        return self._totalProvento

    def getTotalSalarios(self):
        return self._totalSalario

