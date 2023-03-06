import time

QUANTUM = 5

with open('processos.txt', encoding="utf8") as f:
    contents = f.read()


def atraso(tempo):
    time.sleep(tempo)


def primeiro_da_ordem(dici):
    """
    Recebe o dicionário referente aos processos e retorna uma string referente ao processo atual
    que ira rodar
    """
    if len(dici) > 0:
        for processo in dici:
            return processo
    return ""


p1 = contents.split("\n")
matriz = []
dic_processos = {}

# Os próximo "for" separa as informações do arquivo em um dicionário
# para ser trabalhada no código do escalonamento FIFO

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
    p_atual = primeiro_da_ordem(dic_processos)
    print("╭╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╮")
    print(f"Processo {p_atual} executando. Tempo atual = {dic_processos[p_atual][0]}")
    atraso(0.5)
    if dic_processos[p_atual][0] > QUANTUM:
        dic_processos[p_atual][0] -= QUANTUM
        print(f"Quantum encerrado. Tempo restante = {dic_processos[p_atual][0]}")
    else:
        dic_processos[p_atual][0] = 0
        print(f"Processo {p_atual} terminou")
        processos_encerrados.update({p_atual: dic_processos[p_atual]})
        lista_removidos.append(p_atual)
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
