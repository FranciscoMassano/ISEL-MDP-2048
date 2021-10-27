import pygame, os
from pygame.locals import*

from j2048_motor_40708 import novo_jogo
from j2048_motor_40708 import valor
from j2048_motor_40708 import terminou
from j2048_motor_40708 import esquerda
from j2048_motor_40708 import pontuacao
from j2048_motor_40708 import direita
from j2048_motor_40708 import acima
from j2048_motor_40708 import abaixo
from j2048_motor_40708 import ganhou_ou_perdeu

from j2048_gestor_40708 import inicializa_semente
from j2048_gestor_40708 import le_identificacao
from j2048_gestor_40708 import regista_grelha_inicial
from j2048_gestor_40708 import regista_jogada
from j2048_gestor_40708 import regista_pontos
from j2048_gestor_40708 import escreve_registo

#vai iniciar o modulo pygame
pygame.init()

#largura e altura da janela
janela_w = 400
janela_h = 400

#display do jogo
janela = pygame.display.set_mode((janela_w,janela_h))
jogo = novo_jogo()

#relogio para ter frames por segundo
clock = pygame.time.Clock()

#dizemos que os fps sao iguais a 5, ou seja, os 5 frames per second
fps = 5

#tem de estar na mesma pasta (diretoria) que o ficheiro
background = pygame.image.load("isel.png")

#define as cores usadas nos tiles, definidas em rbg
Branco    = (255,255,255)
Cinzento7 = (224,224,224)
Cinzento6 = (192,192,192)
Cinzento5 = (160,160,160)
Cinzento4 = (128,128,128)
Cinzento3 = (96,96,96)
Cinzento2 = (64,64,64)
Cinzento1 = (32,32,32)
Preto     = (0,0,0)

#conjunto das cores dos "tiles", variam consante o numero que estiver na grelha, na respectiva posição
cores_tiles= {0:Branco,2:Branco,4:Branco,8:Branco,16:Cinzento7,32:Cinzento6,64:Cinzento5,128:Cinzento4,
        256:Cinzento3,512:Cinzento2,1024:Cinzento1,2048:Preto} 

#conjunto das cores dos numeros, variam consoante o numero que estiver na grelha, na respectiva posição
cores_numeros={0:Preto,2:Preto,4:Preto,8:Preto,16:Preto,32:Preto,64:Preto,128:Preto,
               256:Preto,512:Cinzento6,1024:Cinzento7,2048:Branco}

#funcao que desenha a grelha do jogo, recorrendo a funcao rect, cada tile é um valor da grelha 
def grelha():
    
    #argumentos da funcao draw.rect
    #(posicao x, posicao y, largura, altura)
    #desenha o "tile", com o valor da grelha do motor, na respectiva posição
    #com a função draw.rect, escolhe a cor do conjunto "cores_tiles" consoante o valor
    #que está actualmente nessa posição            
    tile1 = pygame.draw.rect(janela, cores_tiles[valor(jogo,1,1)], (70,120, 60, 60))
    preencher(valor(jogo,1,1),tile1)
    tile2 = pygame.draw.rect(janela, cores_tiles[valor(jogo,2,1)], (70,190, 60, 60))
    preencher(valor(jogo,2,1),tile2)
    tile3 = pygame.draw.rect(janela, cores_tiles[valor(jogo,3,1)], (70,260, 60, 60))
    preencher(valor(jogo,3,1),tile3)
    tile4 = pygame.draw.rect(janela, cores_tiles[valor(jogo,4,1)], (70,330, 60, 60))
    preencher(valor(jogo,4,1),tile4)
    tile5 = pygame.draw.rect(janela, cores_tiles[valor(jogo,1,2)], (140,120, 60, 60))
    preencher(valor(jogo,1,2),tile5)
    tile6 = pygame.draw.rect(janela, cores_tiles[valor(jogo,2,2)], (140,190, 60, 60))
    preencher(valor(jogo,2,2),tile6)
    tile7 = pygame.draw.rect(janela, cores_tiles[valor(jogo,3,2)], (140,260, 60, 60))
    preencher(valor(jogo,3,2),tile7)
    tile8 = pygame.draw.rect(janela, cores_tiles[valor(jogo,4,2)], (140,330, 60, 60))
    preencher(valor(jogo,4,2),tile8)
    tile9 = pygame.draw.rect(janela, cores_tiles[valor(jogo,1,3)], (210,120, 60, 60))
    preencher(valor(jogo,1,3),tile9)
    tile10 = pygame.draw.rect(janela,cores_tiles[valor(jogo,2,3)], (210,190, 60, 60))
    preencher(valor(jogo,2,3),tile10)
    tile11 = pygame.draw.rect(janela,cores_tiles[valor(jogo,3,3)], (210,260, 60, 60))
    preencher(valor(jogo,3,3),tile11)
    tile12 = pygame.draw.rect(janela,cores_tiles[valor(jogo,4,3)], (210,330, 60, 60))
    preencher(valor(jogo,4,3),tile12)
    tile13 = pygame.draw.rect(janela,cores_tiles[valor(jogo,1,4)], (280,120, 60, 60))
    preencher(valor(jogo,1,4),tile13)
    tile14 = pygame.draw.rect(janela,cores_tiles[valor(jogo,2,4)], (280,190, 60, 60))
    preencher(valor(jogo,2,4),tile14)
    tile15 = pygame.draw.rect(janela,cores_tiles[valor(jogo,3,4)], (280,260, 60, 60))
    preencher(valor(jogo,3,4),tile15)
    tile16 = pygame.draw.rect(janela,cores_tiles[valor(jogo,4,4)], (280,330, 60, 60))
    preencher(valor(jogo,4,4),tile16)

#função que atribui os parametros do rectagulo(valor e dimensoes)
def preencher(valor,rect):
    font = pygame.font.Font(None,40)
    if valor==0:
        #preenche a grelha criada em pygame, com os valores da grelha gerada no motor
        texto=font.render('',1,Branco)
        janela.blit(texto,rect)
    else:
        texto=font.render(str(valor),1,cores_numeros[valor])
        janela.blit(texto,rect)

#funcao principal do jogo
def main():
    janela.blit(background,(0,0))#define o background
    le_identificacao() 
    inicializa_semente(None) 
    novo_jogo()
    grelha()
    regista_grelha_inicial(valor(jogo,1,1), valor(jogo,1,2), valor(jogo,1,3), valor(jogo,1,4),
                           valor(jogo,2,1), valor(jogo,2,2), valor(jogo,2,3), valor(jogo,2,4),
                           valor(jogo,3,1), valor(jogo,3,2), valor(jogo,3,3), valor(jogo,3,4),
                           valor(jogo,4,1), valor(jogo,4,2), valor(jogo,4,3), valor(jogo,4,4))
    

 
main()

#loop principal do jogo
jogar = True
while jogar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogar = False
            pygame.quit()
            sys.exit()
        elif not terminou(jogo):
            #funcoes acima, baixo, esquerda, direita, que estao no como estao no motor
            if event.type == KEYDOWN and event.key == K_w:
                jogo = acima(jogo)
                grelha()
                regista_jogada('w')
            elif event.type == KEYDOWN and event.key == K_s:
                jogo = abaixo(jogo)
                regista_jogada('s')
                grelha()
            elif event.type == KEYDOWN and event.key == K_a:
                jogo = esquerda(jogo)
                grelha()
                regista_jogada('a')
            elif event.type == KEYDOWN and event.key == K_d:
                jogo = direita(jogo)
                grelha()
                regista_jogada('d')

            #funcao para novo jogo(n)    
            elif event.type == KEYDOWN and event.key == K_n:
                regista_pontos(pontuacao(jogo)) #regista a pontuacao
                mensagem_cloud = escreve_registo()
                print(mensagem_cloud) 
                inicializa_semente(None)
                jogo = novo_jogo()
        
                regista_grelha_inicial(valor(jogo,1,1), valor(jogo,1,2), valor(jogo,1,3), valor(jogo,1,4),
                                       valor(jogo,2,1), valor(jogo,2,2), valor(jogo,2,3), valor(jogo,2,4),
                                       valor(jogo,3,1), valor(jogo,3,2), valor(jogo,3,3), valor(jogo,3,4),
                                       valor(jogo,4,1), valor(jogo,4,2), valor(jogo,4,3), valor(jogo,4,4))
                grelha()

            #função que verifica se existe 2048 na grelha 
            if ganhou_ou_perdeu(jogo)==True:
                janela.fill(Branco)
                font=pygame.font.Font(None,80)
                text=font.render('you win',10,Preto)
                janela.blit(background,(0,0))
                janela.blit(text,(100,200))

        #funcao verifica se o jogo terminou     
        if terminou(jogo):  
            regista_pontos(pontuacao(jogo)) #regista a pontuacao
            mensagem_cloud = escreve_registo()
            print(mensagem_cloud)
            regista_grelha_inicial(valor(jogo,1,1), valor(jogo,1,2), valor(jogo,1,3), valor(jogo,1,4),
                           valor(jogo,2,1), valor(jogo,2,2), valor(jogo,2,3), valor(jogo,2,4),
                           valor(jogo,3,1), valor(jogo,3,2), valor(jogo,3,3), valor(jogo,3,4),
                           valor(jogo,4,1), valor(jogo,4,2), valor(jogo,4,3), valor(jogo,4,4))
            font=pygame.font.Font(None,60)
            text=font.render('game over',20,Branco)  
            janela.blit(text,(100,70))
            
    pygame.display.update() #atualiza o pygame

regista_pontos(pontuacao(jogo)) 
mensagem_cloud = escreve_registo()
print(mensagem_cloud)
pygame.quit()


