from math import sqrt
from functools import reduce

#(identificação, instante, ponto, num de vítimas)
def reg1(): return [('robo1', 1, (5, 8), 4), ('robo2', 2, (5, 4), 4), ('robo3', 3, (2, 2), 1), ('robo1', 4, (4, 9), 4), ('robo3', 5, (1, 3), 3), ('robo4', 6, (7, 5), 3), ('robo5', 7, (8, 6), 1), ('robo1', 8, (3, 2), 4), ('robo2', 9, (1, 8), 4)]

def robo(): return ('robo1', 1, (5, 8), 4)

# A - Calcular a distância percorrida por um determinado robô ao longo do processo de resgate das vítimas. Considere que a distância total percorrida deve ser calculada como a soma de todas as distâncias entre os pontos de passagem do robô

# Calcula a distancia entre dois pontos
def distancia(p1, p2):
    def dx(): return p1[0] - p2[0]
    def dy(): return p1[1] - p2[1]
    return sqrt(dx()**2 + dy()**2)

# Soma dois valores
def soma(x, y): return x+y

# Retorna uma lista com as coordenadas de um determinado robo saindo da origem 
def lista_coordenadas_robo(resgate, robo):
    return [(0, 0)] + [x[2] for x in resgate if x[0] == robo[0]]

# Retorna uma lista com as distancias entre os pontos do vetor passado como parametro 
def lista_distancias_robo(lista):
    return [distancia(lista[x],lista[x+1]) for x in range(0, len(lista) - 1)]

# Retorna a distancia total percorrida por um determinado robo 
def distancia_total_robo(resgate, robo):
    return reduce(soma, lista_distancias_robo(lista_coordenadas_robo(resgate, robo)))

# ========== TESTES ============
#print(lista_coordenadas_robo(reg1(), robo()))
#print(lista_distancias_robo(lista_coordenadas_robo(reg1(), robo())))
#print(distancia_total_robo(reg1(), robo()))

# B - Determine qual dos robôs apresenta o seu último ponto de passagem no terreno de busca que possui a maior distância em relação à origem. Exiba o caminho percorrido pelo robô e o tempo total do percurso;

# Retorna a maior distancia da origem percorrida do resgate 
def maior_distancia_da_origem(resgate):
    return max([distancia((0, 0), x[2]) for x in resgate])

# Retorna o robo que possui o ultimo ponto de passagem como sendo o mais distante da origem 
def robo_mais_distante(resgate):
    return [x for x in resgate if distancia((0, 0), x[2]) == maior_distancia_da_origem(resgate)] 

# Retorna o tempo total de instantes de um determinado robo 
def tempo_total(resgate, robo):
    # Lista os intantes de um determinado robo
    def lista_tempo(): return [x[1] for x in resgate if x[0] == robo[0]]
    # Soma os tempos da lista de instantes 
    return reduce(soma, lista_tempo())

# SERA QUE TEM COMO FAZER DE FORMA MAIS INTELIGENTE ?????????

# Retorna uma lista com as informações requeridas 
def lista_infoB(resgate):
    # AQUI SE TIVER DOIS ROBOS MAIS DISTANTES NAO IRÁ FUNCIONAR 
    return [robo_mais_distante(resgate)[0][0], lista_coordenadas_robo(resgate, robo_mais_distante(resgate)[0]), tempo_total(resgate, robo_mais_distante(resgate)[0])]

# ========== TESTES ============
#print(robo_mais_distante(reg1()))
#print(lista_infoB(reg1()))


# C - Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca, ordenados crescentemente pela distância total percorrida;

def caminhos_percorridos(resgate):
    return [(x[0], distancia_total_robo(resgate, x), lista_coordenadas_robo(resgate, x)) for x in resgate]

def ordena_distancia(lista):
    def aux(): return lista[0]
    for x in lista[1:]:
        return

print(caminhos_percorridos(reg1()))


# D - Forneça a identidade do(s) robô(s) que conseguiu(ram) informar o maior número de vítimas (considerando que não há duplicação de identificação de vítima por um mesmo robô).

# Calcula o total de vitimas atendidas por um determinado robo
def total_vitimas_robo(resgate, robo):
    def lista_numero_vitimas(): return [x[3] for x in resgate if x[0][0] == robo[0][0]]
    return reduce(soma, lista_numero_vitimas())

# SINTO QUE E TRABALHO REPETIDO 
# Lista a quantidade de vitimas atendidas por cada robo em um resgate 
def lista_total_vitimas_robo(resgate, robo):
    return [total_vitimas_robo(resgate, x) for x in resgate]

def robo_identifica_mais_vitimas(resgate):
    # NAO SEI SE O [0] ALI NO FINAL É GAMBIARRA PORQUE IMPRIME SEM AS ASPAS SIMPLES 
    return [x[0] for x in resgate if total_vitimas_robo(resgate, x) == max(lista_total_vitimas_robo(resgate, robo))][0]

# ========== TESTES ============
#print(robo_identifica_mais_vitimas(reg1()))