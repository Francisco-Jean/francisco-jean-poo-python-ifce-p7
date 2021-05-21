from colaborador import *
from movimentoFolha import *
from folhaPagamento import *

class main():
    FP = FolhaPagamento(9, 2019)

    CL01 = Colaborador('100', 'Manoel Claudino', 'Av 13 de Maio 2081', '88671020',
    'Benfica', '60020-060' , '124543556-89', 4500.00)
    
    CL02 = Colaborador('200', 'Carmelina da Silva', 'Avenida dos Expedicionários 1200', '3035-1280',
    'Aeroporto', '60530-020' , '301789435-54',2500.00)
    
    CL03 = Colaborador('300', 'Gurmelina Castro Saraiva', 'Av João Pessoa 1020','3235-1089',
    'Damas', '60330-090', '350245632-76', 3000.00)


    MF01 = MovimentoFolha(CL01, 'Gratificacao', 4500.00, 'P')

    MF02 = MovimentoFolha(CL01,'Plano Saúde',1000.00,'P')

    MF03 = MovimentoFolha(CL01,'Pensão', 600.00,'D')

    MF04 = MovimentoFolha(CL02, 'Gratificacao', 2500.00, 'P')

    MF05 = MovimentoFolha(CL02, 'Plano Saúde', 1000.00, 'P')

    MF06 = MovimentoFolha(CL02, 'Faltas', 600.00, 'D')

    MF07 = MovimentoFolha(CL03, 'Gratificacao', 4500.00, 'P')

    MF08 = MovimentoFolha(CL03, 'Plano Saúde', 1000.00, 'P')

    MF09 = MovimentoFolha(CL03, 'Pensão', 600.00, 'D')

    FP.inserirMovimentos(MF01)
    FP.inserirMovimentos(MF02)
    FP.inserirMovimentos(MF03)
    FP.inserirMovimentos(MF04)
    FP.inserirMovimentos(MF05)
    FP.inserirMovimentos(MF06)
    FP.inserirMovimentos(MF07)
    FP.inserirMovimentos(MF08)
    FP.inserirMovimentos(MF09)

    CL01.inserirMovimentos(MF01)
    CL01.inserirMovimentos(MF02)
    CL01.inserirMovimentos(MF03)

    CL02.inserirMovimentos(MF04)
    CL02.inserirMovimentos(MF05)
    CL02.inserirMovimentos(MF06)

    CL03.inserirMovimentos(MF07)
    CL03.inserirMovimentos(MF08)
    CL03.inserirMovimentos(MF09)

    print(FP.calcularFolha())

    print(CL02.calcularSalario())

if __name__ == '__main__':
    main()