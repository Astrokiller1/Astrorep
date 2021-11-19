import os
import random
import statistics

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
NUM_ALUNOS = 10
NOTAS = []


def start_program():
    opçoes = [
        ' Menu',
        '****************************************************',
        ' [1] - Inserção de notas a partir de um ficheiro csv',
        ' [2] - Inserção de notas a partir do teclado',
        ' [3] - Listar notas',
        ' [4] - Apresentação do gráfico e histogramas',
        ' [5] - Apresentação de medidas de tendência central',
        ' [6] - Apresentação de medidas de dispersão',
        ' [7] - Apagar notas',
        ' [8] - Sair do programa',
        '****************************************************',
        'qPor favor escolhe uma das opções [entre 1 e 8]: '
    ]

    for i in opçoes:
        if i[0] == 'q':
            q = input(' ' + i[1:])
            return q
        else:
            print(i)
    return None


def error_program():
    cannot_compute = [
        '--> Não compreendi o pedido.',
        'A gerar novo menu...',
        ' '
    ]
    for yolo in cannot_compute:
        print(yolo)
    return None


def continua_exec():
    input("Prima uma tecla para continuar...")
    return None


def exit_program():
    print("Programa terminado...!")
    return None


def content_program(sel, continua=True):
    if sel == '1':
        # inserir do csv
        if len(NOTAS) != 0:
            print("Já há notas presentes na nossa lista.")
            res = input("Esta ação irá apagar as notas na lista existente e importar o ficheiro novamente? i/N: ")
            if res.lower() == 's':
                NOTAS.clear()
                importa_ficheiro()
            elif res.lower() == 'n':
                print("A lista de notas manter-se-á igual.")
        else:
            importa_ficheiro()
        continua_exec()

    elif sel == '2':
        # inserir notas do teclado
        q2 = True
        while q2:
            if len(NOTAS) != 0:
                print("Já há notas presentes na nossa lista.")
                res = input("Esta ação irá apagar as notas na lista existente e adicionar as notas manualmente. i/N: ")
                if res.lower() == 's':
                    NOTAS.clear()
                    # inserir notas manualmente aqui
                    inserir_notas(NOTAS)
                else:
                    print("A lista de notas manter-se-á igual.")
            else:
                # inserir notas manualmente aqui
                inserir_notas(NOTAS)
            q2 = False
        continua_exec()

    elif sel == '3':
        # listar notas
        if len(NOTAS) > 0:
            print("A listar notas.")
            for nota in range(len(NOTAS)):
                print("Nota #{}: {}".format(nota + 1, NOTAS[nota]))
        else:
            print("Não há notas inseridas para apresentar.")
        continua_exec()

    elif sel == '4':
        # histograma
        plot_me(titulo='Histograma Freq Absoluta', label='Notas', x_label='Notas dos alunos', y_label='Frequência')
        continua_exec()

    elif sel == '5':
        # tendência central
        tend = tendencias()
        for k, v in tend.items():
            print("{}: {}".format(k, v))
        continua_exec()

    elif sel == '6':
        # dispersão
        disp = dispersao()
        for k, v in disp.items():
            print("{}: {}".format(k, v))
        continua_exec()

    elif sel == '7':
        # apagar notas
        NOTAS.clear()
        print("Notas apagadas.")
        continua_exec()

    elif sel == '8':
        # exit
        continua = False

    else:
        error_program()

    return sel, continua


def gera_ficheiro(nome_ficheiro='notas.txt', num_notas=NUM_ALUNOS):
    with open(os.path.join(CURR_DIR, nome_ficheiro), 'w') as fp:
        # generate nota:
        rand_notas = []
        for nota in range(num_notas):
            random_nota = round(random.uniform(0.0, 20.0), 2)
            rand_notas.append(str(random_nota))

        fp.write(','.join(rand_notas))
    print("Ficheiro {} foi criado com notas aleatórias.".format(nome_ficheiro))


def inserir_notas(dados=NOTAS, num_notas=NUM_ALUNOS):
    print("Por favor insira as notas para a turma composta por {} alunos.".format(num_notas))
    # o nº de notas está definido pela variável NUM_ALUNOS.
    # alterar se necessário.
    try:
        i = 0
        while i < num_notas:
            q = float(input("Insira a nota {}: ".format(i + 1)))
            if 0 < q <= 20:
                dados.append(float(q))
                i += 1
            else:
                print("Nota terá que ser entre 0 e 20.")
        print("Notas adicionadas.")
    except Exception as e:
        NOTAS.clear()
        print(e)
    finally:
        return


def importa_ficheiro(dados=NOTAS, nome_ficheiro='notas.txt'):
    try:
        with open(os.path.join(CURR_DIR, nome_ficheiro), 'r') as fp:
            notas = fp.readlines()[0].strip().split(',')
            for nota in notas:
                dados.append(float(nota))
            print("Ficheiro {} importando com sucesso.".format(nome_ficheiro))
    except Exception as e:
        print(e)
    finally:
        return


def plot_me(dados=NOTAS, titulo='', label='', x_label='', y_label=''):
    copy = np.array(dados)
    plt.hist(copy, bins='auto', label=label)
    plt.title(titulo)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()


def tendencias(dados=NOTAS):
    np_arr = np.array(dados)
    med_arit = np_arr.mean()
    med_harm = statistics.harmonic_mean(np_arr)
    med_geo = statistics.geometric_mean(np_arr)
    mediana = statistics.median_low(np_arr)
    moda1 = statistics.multimode(np_arr)
    moda2 = statistics.mode(np_arr)

    if len(moda1) >= 2:
        moda = moda2
    else:
        moda = moda1

    result = {
        'Média Aritmética': (med_arit),
        'Média Harmónica': (med_harm),
        'Média Geométrica': (med_geo),
        'Mediana': (mediana),
        'Moda': moda
    }

    return result


def dispersao(dados=NOTAS):
    np_arr = np.array(dados)
    var1 = sum((item - np_arr.mean()) ** 2 for item in np_arr) / (len(np_arr) - 1)
    var2 = statistics.variance(np_arr)
    dev1 = var1 ** 0.5
    dev2 = statistics.stdev(np_arr)
    skew1 = (sum((item - np_arr.mean()) ** 3 for item in np_arr) * len(np_arr) / (
                (len(np_arr) - 1) * (len(np_arr) - 2) * dev1 ** 3))
    skew2 = scipy.stats.skew(np_arr, bias=False, nan_policy='omit')
    percentil = statistics.quantiles(np_arr, n=2)
    quartis = statistics.quantiles(np_arr, n=4, method='inclusive')
    maximo = np_arr.max()
    minimo = np_arr.min()
    gama = maximo - minimo

    result = {
        'Variância 1': (var1),
        'Variância 2': (var2),
        'Desvio Padrão 1': (dev1),
        'Desvio Padrão 2': (dev2),
        'Skewness 1': (skew1),
        'Skewness 2': (skew2),
        'Percentil': (percentil),
        'Quartis': "{}".format(quartis),
        'Máximo': (maximo),
        'Mínimo': (minimo),
        'Gama': (gama)
    }

    return result


# cria o ficheiro csv e importa as notas aleatórias por predefinição
gera_ficheiro()
importa_ficheiro(NOTAS)

CONTINUE = True

while CONTINUE:
    # inicia prompt
    q = start_program()

    # conteúdo e retorna a seleção e se é para continuar numa tuple
    sel, CONTINUE = content_program(q, CONTINUE)

exit_program()
