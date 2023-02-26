import time

QUANTUM = 10

with open('processos.txt', encoding="utf8") as f:
    contents = f.read()


def atraso(tempo):
    time.sleep(tempo)


p1 = contents.split("\n")
matriz = []
lista_prioridades = [{}, {}, {}, {}, {}]


def qualPrioridade(lista):
    """
  Recebe a lista e percorre um for nela com o intuito de saber onde tem o processo de nivel mais alto
  return: int do valor da prioridade
  """
    prio_atual = 0
    for i in lista:
        if len(i) > 0:
            return prio_atual
        prio_atual += 1
    return - 1


# Os próximos dois "for" separa as informações do arquivo em uma lista com dicionários
# para ser trabalhada no código do escalonamento já ordenada com suas respectivas prioridades

for i in p1:
    matriz.append(i.split(";"))

for i in matriz:
    i[1] = int(i[1])
    i[2] = int(i[2])
    dic = {i[0]: i[1::]}
    lista_prioridades[dic[i[0]][1] - 1].update(dic)

lista_prioridades.reverse()

# Dicionário para armazenar os processos encerrados
processos_encerrados = {}

"""
Código utiliza a função qualPrioridade para trabalhar no indice correto da 'lista_prioridades' referente a prioridade
atual, com isso, foi feita a manipulação dentro de um while para ir decrementando os processos alternadamente
dentro de suas prioridades.
"""

# inteiro para saber a prioridade atual
p_atual = 0
while p_atual != -1:
    lista_removidos = []
    p_atual = qualPrioridade(lista_prioridades)
    for j in lista_prioridades[p_atual]:
        print("╭╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╮")
        print(f"            -Prioridade {lista_prioridades[p_atual][j][1]}-")
        print(f"Processo {j} executando. Tempo atual = {lista_prioridades[p_atual][j][0]}")
        atraso(1)
        if lista_prioridades[p_atual][j][0] > QUANTUM:
            lista_prioridades[p_atual][j][0] -= QUANTUM
            print(f"Quantum encerrado. Tempo restante = {lista_prioridades[p_atual][j][0]}")
        else:
            lista_prioridades[p_atual][j][0] = 0
            print(f"Processo {j} terminou")
            processos_encerrados.update({j: lista_prioridades[p_atual][j]})
            lista_removidos.append(j)
        print("╰╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╯")
        atraso(2)

    for i in lista_removidos:
        del lista_prioridades[p_atual][i]

print("\nTODOS OS PROCESSOS ENCERRADOS!")
print("━┅━┅━━┅━┅━━┅━┅━━┅━┅━━┅━┅━━┅━┅━─┒")
print("Lista em ordem de encerramento: ")
for i in processos_encerrados:
    print(f"{i} - {processos_encerrados[i][3]} - Prioridade {processos_encerrados[i][1]}")
print("━┅━┅━─━┅━┅━─━┅━┅━─━┅━┅━─━┅━┅━─┚")
