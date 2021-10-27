from random import random
from random import choice

def obter_2ou4():

    #random() devolve um número escolhido aleatóriamente na game 0.0 a 1.0
    numero = random()
    if numero <= 0.9:
        return 2
    else:
        return 4

def obter_posicoes_vazias(g):

    #cada elemento é uma lista x, y em que x é o índice da linha e y o da coluna
    lista_posicoes_vazias = []

    for linha in [0, 1, 2, 3]:
        for coluna in [0, 1, 2, 3]:
            if g[linha][coluna] == 0:
                lista_posicoes_vazias.append([linha, coluna])
                
    return lista_posicoes_vazias
    
def inserir_2ou4(g):
    #1. Obter um 2 ou um 4 aleatoriamente com probabilidades 90% e 10% respetivamente.
    #2. Obter a lista de posições vazias
    #3. Obter uma posição vazia escolhida aleatoriamente
    #4. Colocar na posição vazia obtida em 3 o número obtido em 1

    dois_ou_quatro = obter_2ou4()
    posicoes_vazias = obter_posicoes_vazias(g)
    posicao_vazia = choice(posicoes_vazias)

    #índices de linha e coluna da posição vazia
    linha = posicao_vazia[0]
    coluna = posicao_vazia[1]

    g[linha][coluna] = dois_ou_quatro
    
def novo_jogo ():
    """A operação "novo jogo":
1. coloca todas as posições da "grelha" vazias;
2. coloca dois 2 ou 4, escolhidos aleatoriamente (2 com probabilidade 90%,
e 4 10%) em duas posições vazias, escolhidas aleatoriamente.
3. re-inicializa "fim" a False, "vitória" a False e "pontos" a 0;
""" 
    grelha = [[0 ,0 ,0 ,0],
             [0 ,0 ,0 ,0],
             [0 ,0 ,0 ,0],
             [0, 0, 0, 0]]
    fim     = False
    vitória = False
    pontos  = 0

    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
           
    return (grelha, fim, vitória, pontos)

def valor(jogo, linha, coluna):
    
    # jogo é o tuplo (grelha, fim, vitoria, pontos)

    grelha = jogo[0]

    return grelha[linha-1][coluna-1]


def mover_esquerda(uma_lista):

     resultado = []
     lenlista = len(uma_lista)
     
     for indice in range(lenlista):
         valor = uma_lista[indice]
         if valor != 0:
             resultado.append(valor)
             
     while len(resultado) < lenlista:
         resultado.append(0)  

     return resultado
    

def somar_esquerda(uma_lista):

    resultado = []
    lenlista  = len(uma_lista)    
    pontos    = 0
    indice    = 0
    
    while indice < lenlista - 1:
        valor = uma_lista[indice]
        if uma_lista[indice + 1] == valor:
            soma = valor + valor
            resultado.append(soma)
            pontos = pontos + soma
            indice = indice + 2
        else:
            resultado.append(valor)
            indice = indice + 1
            
    #tratar ultima posição       
    if indice == lenlista - 1:
        resultado.append(uma_lista[indice])

    while len(resultado) < lenlista:
         resultado.append(0)                  
    
    return (resultado, pontos)

def copiar_grelha(grelha):

    resultado = []
    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0]) #Assume-se que a grelha não é uma lista vazia

    for linha in range(numero_linhas):
        nova_linha = []
        
        for coluna in range(numero_colunas):
            nova_linha.append(grelha[linha][coluna])
            
        resultado.append(nova_linha)

    return resultado

def atualizar_grelha(grelha_inicial, grelha):

    diferentes = False

    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])

    for l in range(numero_linhas):
       for c in range(numero_colunas):
           if grelha_inicial[l][c] != grelha [l][c]:
               diferentes = True

    if diferentes == True:
       inserir_2ou4(grelha)

def get_vitoria(grelha):

    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])
    vitoria = False 

    for l in range(numero_linhas):
       for c in range(numero_colunas):
           if grelha[l][c] == 2048:
               vitoria = True
               
    return vitoria


def ha_iguais_adjacentes(grelha):

    ha = False    

    numero_linhas = len(grelha)
    numero_colunas = len(grelha[0])

     #testar por linhas
    for l in range(numero_linhas):
       for c in range(numero_colunas - 1):
           if grelha[l][c] == grelha [l][c + 1]:
               ha = True


     #testar por colunas
    for l in range(numero_linhas - 1):
       for c in range(numero_colunas):
           if grelha[l][c] == grelha [l + 1][c]:
               ha = True  

    return ha


def get_fim(grelha):

    fim = False
    ha_posicoes_vazias = True

    posicoes_vazias = obter_posicoes_vazias(grelha)
    if len(posicoes_vazias) == 0:
        ha_posicoes_vazias = False
    

    if not(ha_posicoes_vazias) and not(ha_iguais_adjacentes(grelha)):
        fim = True

    return fim
    
def reverte_linhas(grelha):
    grelha_nova = [[],[],[],[]]
    
    for l in range(len(grelha)):
            for c in reversed(grelha[l]):
                    grelha_nova[l].append(c)

    grelha = grelha_nova

    return(grelha)

def trocar_linhas_com_colunas(grelha):
    nova_lista=[]
    for l in range(len(grelha[0])):
        linha=[]
        for c in range(len(grelha)):
            linha.append(grelha[c][l])
        nova_lista.append(linha)

    return nova_lista 

def esquerda(jogo):
    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    #print ("operação \"esquerda\**")

    grelha  = jogo [0]
    fim     = jogo [1]
    vitoria = jogo [2]
    pontos  = jogo [3]

    grelha_inicial = copiar_grelha(grelha)
    

    for l in range(len(grelha)):
        linha = grelha[l]
        linha2 = mover_esquerda(linha)
        (linha3, pontos_a_somar) = somar_esquerda(linha2)
        grelha[l] = linha3
        pontos = pontos + pontos_a_somar

    atualizar_grelha(grelha_inicial, grelha)

    vitoria = get_vitoria(grelha)

    fim = get_fim(grelha)
    

    return (grelha, fim, vitoria, pontos)

    # jogo é o tuplo (grelha, fim, vitoria, pontos)

    
def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    
    grelha_revertida = reverte_linhas(grelha)    
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)    
    jogo_revertido_atualizado = esquerda(jogo_revertido)    
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    
    grelha_revertida = reverte_linhas(grelha)   
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    
    return jogo_atualizado


def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    
def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    
def terminou (jogo):
    #print ("operação \"terminou\**")
    return jogo[1]
    
    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    
def ganhou_ou_perdeu (jogo):
    #print ("operação \"ganhou_ou_perdeu\**")
    return jogo[2]

    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    
def pontuacao (jogo):
    #print ("operação \"pontuacao\**")
    return jogo[3]

    # jogo é o tuplo (grelha, fim, vitoria, pontos)
    

