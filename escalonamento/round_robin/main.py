import time

QUANTUM = 5

with open('processos.txt', encoding="utf8") as f:
    contents = f.read()


def atraso(tempo):
    time.sleep(tempo)


p1 = contents.split("\n")
matriz = []
dic_processos = {}

# Os próximo "for" separa as informações do arquivo em um dicionário
# para ser trabalhada no código do escalonamento Round-Robin

for i in p1:
    atual = i.split(";")
    atual[1] = int(atual[1])
    atual[2] = int(atual[2])
    dic = {atual[0]: atual[1::]}
    dic_processos.update(dic)

# Dicionário para armazenar os processos encerrados
processos_encerrados = {}

while len(dic_processos) > 0:
    lista_removidos = []
    for i in dic_processos:
        print("╭╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╮")
        print(f"Processo {i} executando. Tempo atual = {dic_processos[i][0]}")
        atraso(0.5)
        if dic_processos[i][0] > QUANTUM:
            dic_processos[i][0] -= QUANTUM
            print(f"Quantum encerrado. Tempo restante = {dic_processos[i][0]}")
        else:
            dic_processos[i][0] = 0
            print(f"Processo {i} terminou")
            processos_encerrados.update({i: dic_processos[i]})
            lista_removidos.append(i)
        print("╰╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╯")
        atraso(0.5)

    for i in lista_removidos:
        del dic_processos[i]

print("\nTODOS OS PROCESSOS ENCERRADOS!")
print("━┅━┅━━┅━┅━━┅━┅━━┅━┅━━┅━┅━━┅━┅━─┒")
print("Lista em ordem de encerramento: ")
for i in processos_encerrados:
    print(f"{i} - {processos_encerrados[i][3]} - Prioridade {processos_encerrados[i][1]}")
print("━┅━┅━─━┅━┅━─━┅━┅━─━┅━┅━─━┅━┅━─┚")
