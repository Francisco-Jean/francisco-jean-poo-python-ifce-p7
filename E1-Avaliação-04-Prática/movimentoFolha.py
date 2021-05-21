class MovimentoFolha():

    #  Tipos de Movimento:          Exemplo:
    #  'D' = Desconto               Plano de saúde: Provento (P)
    #  'P' = Provento               Faltas: Desconto (D)

    def __init__(self, colaborador, descricao, valor, tipomovimento):
        self._colaborador = colaborador
        self._descricao = descricao
        self._valor = valor
        self._tipomovimento = tipomovimento
        
    def getColaborador(self):
        return self._colaborador

    def getDescricao(self):
        return self._descricao

    def getValor(self):
        return self._valor

    def getTipomovimento(self):
        return self._tipomovimento

    def setColaborador(self, newcolaborador):
        self._colaborador = newcolaborador

    def setDescricao(self, newdesc):
        self._descricao = newdesc

    def setValor(self, newvalor):
        self._valor = newvalor

    def setTipoMovimento(self, newtipo):
        self._tipomovimento = newtipo