import pygame
import sys
import time


pygame.init()


info = pygame.display.Info()
LARGURA = info.current_w
ALTURA = info.current_h

TELA = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("House of History")
mouse = pygame.mouse.get_pos()
clicou = False
comeca_conta = 0
jogo_começou = False


BRANCO = (255, 255, 255)
LARANJA_ESCURO = (194, 103, 0)
LARANJA_CLARO = (255, 178, 79)
PRETO = (0, 0, 0)


fonte = pygame.font.SysFont("comicsansms", int((ALTURA / 751) * 40))
clock = pygame.time.Clock()
pont = pygame.font.SysFont("comicsansms", int((ALTURA / 500) * 40))

ORIGINAL_LARGURA = 1280
ORIGINAL_ALTURA = 751
estado = 'Menu'


fundo = pygame.image.load("Img/fundo.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
fase1 = pygame.image.load('Img/fase1.jpg')
fase1 = pygame.transform.scale(fase1, (LARGURA, ALTURA))


def desenhar_botao(texto, x_ratio, y_ratio, largura_ratio, altura_ratio, cor_normal, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    
    x = int(x_ratio * LARGURA)
    y = int(y_ratio * ALTURA)
    largura = int(largura_ratio * LARGURA)
    altura = int(altura_ratio * ALTURA)

    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(TELA, cor_hover, (x, y, largura, altura), border_radius=12)
        if clique[0] == 1 and acao:
            acao()
    else:
        pygame.draw.rect(TELA, cor_normal, (x, y, largura, altura), border_radius=12)

    texto_superficie = fonte.render(texto, True, BRANCO)
    texto_ret = texto_superficie.get_rect(center=(x + largura // 2, y + altura // 2))
    TELA.blit(texto_superficie, texto_ret)

def ponto_interagivel(cena, x_ratio, y_ratio, larg_ratio, alt_ratio):
    mouse = pygame.mouse.get_pos()
    x = int(x_ratio * LARGURA)
    y = int(y_ratio * ALTURA)
    larg = int(larg_ratio * LARGURA)
    alt = int(alt_ratio * ALTURA)
    ret = pygame.Rect(x, y, larg, alt)

    if ret.collidepoint(mouse):
        cena = True
    else:
        cena = False

    return cena

def botao_invisivel_click(x_ratio, y_ratio, larg_ratio, alt_ratio):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    x = int(x_ratio * LARGURA)
    y = int(y_ratio * ALTURA)
    larg = int(larg_ratio * LARGURA)
    alt = int(alt_ratio * ALTURA)

    ret = pygame.Rect(x, y, larg, alt)
    if ret.collidepoint(mouse) and clique[0]:
        return True
    return False

def jogar():
    global clicou, jogo_começou, comeca_conta
    estado = "fase1"
    senha_digitada = ""
    comeca_conta = time.time()
    jogo_começou = True

    imagemradio = False
    imagemfolha = False
    imagemquadro = False
    imagemmapa = False
    imgpapiro = False
    imgpiramides = False
    imganubis = False
    imgescaravelho = False
    imgesfingecama = False
    imgesfingevazo = False
    imgrio1 = False
    imgrio2 = False
    imgdomP = False
    imgcavalo = False
    imgband = False
    imgenigma = False
   
    rodando = True
    while rodando:
        ultimo_clique = 0
        tempo_atual = pygame.time.get_ticks()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if(jogo_começou):
            cronometro = time.time() - comeca_conta

        if estado == "fase1":
            
            fase1 = pygame.image.load("img/fase1.jpg")
            fase1 = pygame.transform.scale(fase1,(LARGURA, ALTURA))
            cenafolha = pygame.image.load('img/cenafolha.jpg')
            cenafolha = pygame.transform.scale(cenafolha, (LARGURA, ALTURA))
            cenaquadro = pygame.image.load('img/cenaquadro.jpg')
            cenaquadro = pygame.transform.scale(cenaquadro, (LARGURA, ALTURA))
            cenaradio = pygame.image.load('img/cenaradio.jpg')
            cenaradio = pygame.transform.scale(cenaradio, (LARGURA, ALTURA))
            cenamapa = pygame.image.load('img/imagemmapa.jpg')
            cenamapa = pygame.transform.scale(cenamapa,(LARGURA, ALTURA))

            
            imagemradio = ponto_interagivel(imagemradio, 751/ORIGINAL_LARGURA, 539/ORIGINAL_ALTURA, 50/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA)
            imagemfolha = ponto_interagivel(imagemfolha, 1200/ORIGINAL_LARGURA, 600/ORIGINAL_ALTURA, 30/ORIGINAL_LARGURA, 65/ORIGINAL_ALTURA)
            imagemquadro = ponto_interagivel(imagemquadro, 834/ORIGINAL_LARGURA, 188/ORIGINAL_ALTURA, 110/ORIGINAL_LARGURA, 120/ORIGINAL_ALTURA)
            imagemmapa = ponto_interagivel(imagemmapa, 1064/ORIGINAL_LARGURA, 530/ORIGINAL_ALTURA, 40/ORIGINAL_LARGURA, 40/ORIGINAL_ALTURA)
            
            if imagemradio:
                TELA.blit(cenaradio, (0,0))
            elif imagemfolha:
                TELA.blit(cenafolha, (0, 0))
            elif imagemquadro:
                TELA.blit(cenaquadro, (0, 0))
            elif imagemmapa:
                TELA.blit(cenamapa, (0, 0))
            else:
                TELA.blit(fase1,(0,0))

            if botao_invisivel_click(48/ORIGINAL_LARGURA, 457/ORIGINAL_ALTURA, 100/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA):
                estado = "senha"
                senha_digitada = ""

        if estado == 'senha':
            cenasenha = pygame.image.load('img/cenasenha.jpg')
            cenasenha = pygame.transform.scale(cenasenha, (LARGURA, ALTURA))
            TELA.blit(cenasenha, (0, 0))

            if botao_invisivel_click(711/ORIGINAL_LARGURA, 456/ORIGINAL_ALTURA, 160/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA):
                estado = 'fase1'
            if botao_invisivel_click(711/ORIGINAL_LARGURA, 385/ORIGINAL_ALTURA, 160/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA):
                senha_digitada = ''


           
                
            btn1_x = int(450/ORIGINAL_LARGURA * LARGURA)
            btn1_y = int(330/ORIGINAL_ALTURA * ALTURA)
            btn1_width = int(75/ORIGINAL_LARGURA * LARGURA)
            btn1_height = int(45/ORIGINAL_ALTURA * ALTURA)

            btn9_x = int(611/ORIGINAL_LARGURA * LARGURA)
            btn9_y = int(462/ORIGINAL_ALTURA * ALTURA)
            btn9_width = int(75/ORIGINAL_LARGURA * LARGURA)
            btn9_height = int(80/ORIGINAL_ALTURA * ALTURA)

            btn4_x = int(450/ORIGINAL_LARGURA * LARGURA)
            btn4_y = int(395/ORIGINAL_ALTURA * ALTURA)
            btn4_width = int(75/ORIGINAL_LARGURA * LARGURA)
            btn4_height = int(80/ORIGINAL_ALTURA * ALTURA)

            btn5_x = int(533/ORIGINAL_LARGURA * LARGURA)
            btn5_y = int(395/ORIGINAL_ALTURA * ALTURA)
            btn5_width = int(75/ORIGINAL_LARGURA * LARGURA)
            btn5_height = int(80/ORIGINAL_ALTURA * ALTURA)

            btn_confirm_x = int(711/ORIGINAL_LARGURA * LARGURA)
            btn_confirm_y = int(350/ORIGINAL_ALTURA * ALTURA)
            btn_confirm_width = int(160/ORIGINAL_LARGURA * LARGURA)
            btn_confirm_height = int(50/ORIGINAL_ALTURA * ALTURA)


            if evento.type == pygame.MOUSEBUTTONDOWN and not clicou:
                    x, y = evento.pos
                    clicou = True
        
                    if btn1_x <= x <= btn1_x + btn1_width and btn1_y <= y <= btn1_y + btn1_height:
                        if len(senha_digitada) < 4:
                            senha_digitada += "1"

                    elif btn9_x <= x <= btn9_x + btn9_width and btn9_y <= y <= btn9_y + btn9_height:
                        if len(senha_digitada) < 4:
                            senha_digitada += "9"

                    elif btn4_x <= x <= btn4_x + btn4_width and btn4_y <= y <= btn4_y + btn4_height:
                        if len(senha_digitada) < 4:
                            senha_digitada += "4"

                    elif btn5_x <= x <= btn5_x + btn5_width and btn5_y <= y <= btn5_y + btn5_height:
                        if len(senha_digitada) < 4:
                            senha_digitada += "5"

                    elif btn_confirm_x <= x <= btn_confirm_x + btn_confirm_width and btn_confirm_y <= y <= btn_confirm_y + btn_confirm_height:
                        if senha_digitada == "1945":
                            estado = "fase2"
                            
                        else:
                            senha_digitada = ""  

            elif evento.type == pygame.MOUSEBUTTONUP:
                    clicou = False  

                
            circle_radius = int(25/ORIGINAL_ALTURA * ALTURA)
            circle_y = int(283/ORIGINAL_ALTURA * ALTURA)

            if(len(senha_digitada) >= 1):
                    pygame.draw.circle(TELA, PRETO, (int(423/ORIGINAL_LARGURA * LARGURA), circle_y), radius = circle_radius)
            if(len(senha_digitada) >= 2):
                    pygame.draw.circle(TELA, PRETO, (int(523/ORIGINAL_LARGURA * LARGURA), circle_y), radius = circle_radius)
            if(len(senha_digitada) >= 3):
                    pygame.draw.circle(TELA, PRETO, (int(623/ORIGINAL_LARGURA * LARGURA), circle_y), radius = circle_radius)
            if(len(senha_digitada) >= 4):
                    pygame.draw.circle(TELA, PRETO, (int(723/ORIGINAL_LARGURA * LARGURA), circle_y), radius = circle_radius)


        if estado == 'fase2':
            imgfase2 = pygame.image.load('img/imgfase2.jpg')
            imgfase2 = pygame.transform.scale(imgfase2, (LARGURA, ALTURA))   
            
            cenapapiro = pygame.image.load('img/cenapapiro.jpg')
            cenapapiro = pygame.transform.scale(cenapapiro, (LARGURA,ALTURA))
            cenapiramides = pygame.image.load('img/cenapiramides.jpg')
            cenapiramides = pygame.transform.scale(cenapiramides, (LARGURA, ALTURA))
            cenaanubis = pygame.image.load('img/cenaanubis.jpg')
            cenaanubis = pygame.transform.scale(cenaanubis, (LARGURA, ALTURA))
            cenaescaravelho = pygame.image.load('img/cenaescaravelho.jpg')
            cenaescaravelho = pygame.transform.scale(cenaescaravelho, (LARGURA, ALTURA))
            cenaesfingevazo = pygame.image.load('img/cenaesfingevazo.jpg')
            cenaesfingevazo = pygame.transform.scale(cenaesfingevazo, (LARGURA, ALTURA))
            cenaesfingecama = pygame.image.load('img/cenaesfingecama.jpg')
            cenaesfingecama = pygame.transform.scale(cenaesfingecama, (LARGURA, ALTURA))

           
            imgpapiro = ponto_interagivel(imgpapiro, 566/ORIGINAL_LARGURA, 480/ORIGINAL_ALTURA, 150/ORIGINAL_LARGURA, 20/ORIGINAL_ALTURA)
            imgpiramides = ponto_interagivel(imgpiramides, 1111/ORIGINAL_LARGURA, 436/ORIGINAL_ALTURA, 50/ORIGINAL_LARGURA, 30/ORIGINAL_ALTURA)
            imganubis = ponto_interagivel(imganubis, 39/ORIGINAL_LARGURA, 238/ORIGINAL_ALTURA, 40/ORIGINAL_LARGURA, 90/ORIGINAL_ALTURA)
            imgescaravelho = ponto_interagivel(imgescaravelho, 451/ORIGINAL_LARGURA, 441/ORIGINAL_ALTURA, 15/ORIGINAL_LARGURA, 35/ORIGINAL_ALTURA)
            imgesfingevazo = ponto_interagivel(imgesfingevazo, 1090/ORIGINAL_LARGURA, 620/ORIGINAL_ALTURA, 80/ORIGINAL_LARGURA, 70/ORIGINAL_ALTURA)
            imgesfingecama = ponto_interagivel(imgesfingecama, 308/ORIGINAL_LARGURA, 504/ORIGINAL_ALTURA, 52/ORIGINAL_LARGURA, 86/ORIGINAL_ALTURA)
            
            if (botao_invisivel_click(20/ORIGINAL_LARGURA, 438/ORIGINAL_ALTURA, 50/ORIGINAL_LARGURA, 22/ORIGINAL_ALTURA)):
                estado = 'senha2'
                
                
                fonte = pygame.font.Font(None, int((ALTURA / 751) * 48))
                texto_digitado = ""

            if(imgpapiro):
                TELA.blit(cenapapiro, (0,0))
            elif(imgpiramides):
                TELA.blit(cenapiramides, (0,0))
            elif(imganubis):
                TELA.blit(cenaanubis, (0,0))
            elif(imgescaravelho):
                TELA.blit(cenaescaravelho, (0,0))
            elif(imgesfingevazo):
                TELA.blit(cenaesfingevazo, (0,0))
            elif(imgesfingecama):
                TELA.blit(cenaesfingecama, (0,0))
            else:
                TELA.blit(imgfase2, (0,0))

        if(estado == 'senha2'):
            cenasenha2 = pygame.image.load('img/cenasenha2.jpg')
            cenasenha2 = pygame.transform.scale(cenasenha2, (LARGURA, ALTURA))
            for evento in pygame.event.get():
                 if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                            texto_digitado = texto_digitado[:-1]
                    else:
                            texto_digitado += evento.unicode

            
            if (botao_invisivel_click(767/ORIGINAL_LARGURA, 367/ORIGINAL_ALTURA, 160/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA)):
                estado = 'fase2'
            
            if botao_invisivel_click(583/ORIGINAL_LARGURA, 352/ORIGINAL_ALTURA, 160/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA):
                texto_digitado = ''

            if(botao_invisivel_click(408/ORIGINAL_LARGURA, 367/ORIGINAL_ALTURA, 160/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA)):
                if(texto_digitado.upper() == 'ESFINGE DE GIZE' or texto_digitado.upper() == 'ESFINGE DE GIZÉ'):
                    estado = 'fase3'
            print(texto_digitado)
        
            superficie_texto = fonte.render(texto_digitado, True, (0, 0, 0)) 
            TELA.blit(cenasenha2, (0 , 0))
           
            TELA.blit(superficie_texto, (int(425/ORIGINAL_LARGURA * LARGURA), int(299/ORIGINAL_ALTURA * ALTURA)))
        
        if(estado == 'fase3'):
            imgfase3 = pygame.image.load('img/fase3.jpg')
            imgfase3 = pygame.transform.scale(imgfase3, (LARGURA, ALTURA))

            cenario1 = pygame.image.load('img/cena_rio1.jpg')
            cenario1 = pygame.transform.scale(cenario1, (LARGURA, ALTURA))
            cenario2 = pygame.image.load('img/cena_rio2.jpg')
            cenario2 = pygame.transform.scale(cenario2, (LARGURA, ALTURA))
            cenadomP = pygame.image.load('img/cenadompedro.jpg')
            cenadomP = pygame.transform.scale(cenadomP, (LARGURA, ALTURA))
            cenaenigma2 = pygame.image.load('img/cenaenigma2.jpg')
            cenaenigma2 = pygame.transform.scale(cenaenigma2, (LARGURA, ALTURA))
            cenaband = pygame.image.load('img/cenaband.jpg')
            cenaband = pygame.transform.scale(cenaband, (LARGURA, ALTURA))
            cenacavalo = pygame.image.load('img/cenacavalo.jpg')
            cenacavalo = pygame.transform.scale(cenacavalo, (LARGURA, ALTURA))

            imgrio1 = ponto_interagivel(imgrio1, 895/ORIGINAL_LARGURA, 96/ORIGINAL_ALTURA, 50/ORIGINAL_LARGURA, 56/ORIGINAL_ALTURA)
            imgrio2 = ponto_interagivel(imgrio2, 956/ORIGINAL_LARGURA, 126/ORIGINAL_ALTURA, 70/ORIGINAL_LARGURA, 80/ORIGINAL_ALTURA)
            imgdomP = ponto_interagivel(imgdomP, 447/ORIGINAL_LARGURA, 52/ORIGINAL_ALTURA, 120/ORIGINAL_LARGURA, 150/ORIGINAL_ALTURA)
            imgenigma = ponto_interagivel(imgenigma, 523/ORIGINAL_LARGURA, 421/ORIGINAL_ALTURA, 13/ORIGINAL_LARGURA, 30/ORIGINAL_ALTURA)
            imgband = ponto_interagivel(imgband, 874/ORIGINAL_LARGURA, 336/ORIGINAL_ALTURA, 35/ORIGINAL_LARGURA, 42/ORIGINAL_ALTURA)
            imgcavalo = ponto_interagivel(imgcavalo, 330/ORIGINAL_LARGURA, 193/ORIGINAL_ALTURA, 30/ORIGINAL_LARGURA, 30/ORIGINAL_ALTURA)
            
            if(botao_invisivel_click(981/ORIGINAL_LARGURA, 308/ORIGINAL_ALTURA, 100/ORIGINAL_LARGURA, 50/ORIGINAL_ALTURA)):
                estado = 'senha3'
                texto_digitado = ''
                fonte = pygame.font.Font(None, int((ALTURA / 751) * 48))

            if(imgrio1):
                TELA.blit(cenario1, (0,0))

            elif(imgrio2):
                TELA.blit(cenario2, (0,0))

            elif(imgdomP):
                TELA.blit(cenadomP, (0,0))

            elif(imgenigma):
                TELA.blit(cenaenigma2, (0,0))

            elif(imgband):
                TELA.blit(cenaband, (0,0))

            elif(imgcavalo):
                TELA.blit(cenacavalo, (0,0))

            else:
                TELA.blit(imgfase3, (0,0))

        if(estado == 'senha3'):
            cenasenha3 = pygame.image.load('img/cenasenha3.jpg')
            cenasenha3 = pygame.transform.scale(cenasenha3, (LARGURA, ALTURA))
            for evento in pygame.event.get():
                 if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                            texto_digitado = texto_digitado[:-1]
                    else:
                            texto_digitado += evento.unicode

            
            superficie_texto = fonte.render(texto_digitado, True, (0, 0, 0)) 
            TELA.blit(cenasenha3, (0 , 0))
           


           
            TELA.blit(superficie_texto, (int(302/ORIGINAL_LARGURA * LARGURA), int(315/ORIGINAL_ALTURA * ALTURA)))

            if(botao_invisivel_click(278/ORIGINAL_LARGURA, 377/ORIGINAL_ALTURA, 230/ORIGINAL_LARGURA, 67/ORIGINAL_ALTURA)):
                if(texto_digitado.upper() == 'RIO IPIRANGA'):
                    estado = 'FINAL'
                    tempo = f'{cronometro:.3f}'
                    pontuação = 10000 - (cronometro * 1.2)
                    pontos = f'{pontuação:.0f}'

            if (botao_invisivel_click(772/ORIGINAL_LARGURA, 377/ORIGINAL_ALTURA, 230/ORIGINAL_LARGURA, 67/ORIGINAL_ALTURA)):
                estado = 'fase3'
            

            if botao_invisivel_click(519/ORIGINAL_LARGURA, 377/ORIGINAL_ALTURA, 230/ORIGINAL_LARGURA, 67/ORIGINAL_ALTURA):
                texto_digitado = ''

            if(len(texto_digitado) == 15):
                texto_digitado =''

        if(estado == 'FINAL'):
            
            if(cronometro< 360):
                final3 = pygame.image.load('img/FINAL3.jpg')
                final3 = pygame.transform.scale(final3, (LARGURA, ALTURA))
                TELA.blit(final3, (0, 0))
                
            elif(cronometro> 360 and cronometro<420):
                final2 = pygame.image.load('img/FINAL2.jpg')
                final2 = pygame.transform.scale(final2, (LARGURA, ALTURA))
                TELA.blit(final2, (0, 0))
                
            elif(cronometro> 420 and cronometro<480):
                final1 = pygame.image.load('img/FINAL1.jpg')
                final1 = pygame.transform.scale(final1, (LARGURA, ALTURA))
                TELA.blit(final1, (0, 0))

            tempodemorou = pont.render(tempo,True,PRETO)
            pontou = pont.render(pontos, True, PRETO)
            TELA.blit(tempodemorou, (int((635/ORIGINAL_LARGURA) * LARGURA), int((450/ORIGINAL_ALTURA) * ALTURA)))
            TELA.blit(pontou, (int((635/ORIGINAL_LARGURA) * LARGURA), int((345/ORIGINAL_ALTURA) * ALTURA)))

            if botao_invisivel_click(599/ORIGINAL_LARGURA, 540/ORIGINAL_ALTURA, 80/ORIGINAL_LARGURA, 80/ORIGINAL_ALTURA):
                menu()

                
        pygame.display.update()
        
        clock.tick(60)
        if(jogo_começou):
            cronometro = time.time() - comeca_conta
        print(pygame.mouse.get_pos())
           

def creditos():
    while True:
       
        cenacredito = pygame.image.load('img/cenacredito.jpg')
        cenacredito = pygame.transform.scale(cenacredito, (LARGURA, ALTURA))

        TELA.blit(cenacredito, (0, 0))
        desenhar_botao('Voltar', 917/ORIGINAL_LARGURA , 654/ORIGINAL_ALTURA,  200/ORIGINAL_LARGURA, 60/ORIGINAL_ALTURA, LARANJA_ESCURO,LARANJA_CLARO, menu)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

        print(pygame.mouse.get_pos())
             

        pygame.display.update()

    
    
def sair(): 
    pygame.quit()
    sys.exit()

def menu():
    while True:
       if(estado == 'Menu'):

        TELA.blit(fundo, (0, 0))
        desenhar_botao("Jogar", 321/ORIGINAL_LARGURA, 332/ORIGINAL_ALTURA, 200/ORIGINAL_LARGURA, 60/ORIGINAL_ALTURA, LARANJA_ESCURO, LARANJA_CLARO, jogar)
        desenhar_botao("Créditos", 321/ORIGINAL_LARGURA, 406/ORIGINAL_ALTURA, 200/ORIGINAL_LARGURA, 60/ORIGINAL_ALTURA, LARANJA_ESCURO, LARANJA_CLARO, creditos)
        desenhar_botao("Sair", 321/ORIGINAL_LARGURA, 479/ORIGINAL_ALTURA, 200/ORIGINAL_LARGURA, 60/ORIGINAL_ALTURA, LARANJA_ESCURO, LARANJA_CLARO, sair)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

        pygame.display.update()
menu()