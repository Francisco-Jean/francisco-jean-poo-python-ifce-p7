"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):
        def line():
            return '\n---------------------------------------------------------------------------------------------------------------'       
        print(line())
        print('NOTA FISCAL {:>99s}'.format(str(self._data)))
        print('Cliente: ' + str(self._cliente._id) + '      Nome: ' + self._cliente._nome)
        print('CPF/CNPJ: ' + self._cliente._cnpjcpf + line())
        print('ITENS' + line() + '\n{:<15s}{:<40s}{:<15s}{:<32s}{:<10s}'. format('Sequência','Descrição','Quantidade','Valor Unitário', 'Preço'))
        print('------------   -------------------------------------   ------------   -------------------------   -------------')
        total = 0
        for x in self._itens:
            print('\n{:<15s}{:<40s}{:<15s}{:<32s}{:<10s}'. format(str(x._sequencial), x._descricao,str(x._quantidade),str(x._valorUnitario),str(x._valorItem)))
            total += x._valorItem
        print(line())  
        print('Valor Total: ' + str(total) + '\n')


    