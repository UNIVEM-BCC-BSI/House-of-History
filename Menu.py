import pygame
import sys

# Inicialização
pygame.init()

# Configurações da tela
LARGURA = 1280
ALTURA = 751

TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("House of History")
mouse = pygame.mouse.get_pos()
clicou = False

# Cores
BRANCO = (255, 255, 255)
LARANJA_ESCURO = (194, 103, 0)
LARANJA_CLARO = (255, 178, 79)
PRETO = (0, 0, 0)
# Fonte
fonte = pygame.font.SysFont("comicsansms", 40)

# Carregar imagem de fundo
fundo = pygame.image.load("Img/fundo.jpg")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))
fase1 = pygame.image.load('Img/fase1.jpg')
fase1 = pygame.transform.scale(fase1, (LARGURA, ALTURA))

# Função para desenhar botão
def desenhar_botao(texto, x, y, largura, altura, cor_normal, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(TELA, cor_hover, (x, y, largura, altura), border_radius=12)
        if clique[0] == 1 and acao:
            acao()
    else:
        pygame.draw.rect(TELA, cor_normal, (x, y, largura, altura), border_radius=12)

    texto_superficie = fonte.render(texto, True, BRANCO)
    texto_ret = texto_superficie.get_rect(center=(x + largura // 2, y + altura // 2))
    TELA.blit(texto_superficie, texto_ret)

def ponto_interagivel(cena, x, y, larg, alt):
    mouse = pygame.mouse.get_pos()
    ret = pygame.Rect(x, y, larg, alt)

    if ret.collidepoint(mouse):
        cena = True
    else:
        cena = False

    return cena

def botao_invisivel_click(x, y, larg, alt):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    ret = pygame.Rect(x, y, larg, alt)
    if ret.collidepoint(mouse) and clique[0]:
        return True
    return False

def jogar():
    global clicou
    estado = "fase1"
    senha_digitada = ""



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

            imagemradio = ponto_interagivel(imagemradio,751, 539, 50, 50)
            imagemfolha = ponto_interagivel(imagemfolha, 1200, 600, 30, 65)
            imagemquadro = ponto_interagivel(imagemquadro,834,188,110,120)
            imagemmapa = ponto_interagivel(imagemmapa,1064,530,40,40)
            
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

            if botao_invisivel_click(48, 457, 100, 50):
                estado = "senha"
                senha_digitada = ""

        if estado == 'senha':
            cenasenha = pygame.image.load('img/cenasenha.jpg')
            cenasenha = pygame.transform.scale(cenasenha, (LARGURA, ALTURA))
            TELA.blit(cenasenha, (0, 0))

            if botao_invisivel_click(711, 456,160,50):
                estado = 'fase1'

                
            if estado == "senha":

                if evento.type == pygame.MOUSEBUTTONDOWN and not clicou:
                    x, y = evento.pos
                    clicou = True

        
                    if 450 <= x <= 525 and 330 <= y <= 375:
                        if len(senha_digitada) < 4:
                            senha_digitada += "1"

                    
                    elif 611 <= x <= 686 and 462 <= y <= 542:
                        if len(senha_digitada) < 4:
                            senha_digitada += "9"

                    
                    elif 450 <= x <= 525 and 395 <= y <= 475:
                        if len(senha_digitada) < 4:
                            senha_digitada += "4"

                    
                    elif 533 <= x <= 608 and 395 <= y <= 475:
                        if len(senha_digitada) < 4:
                            senha_digitada += "5"

                    
                    elif 711 <= x <= 871 and 350 <= y <= 400:
                        if senha_digitada == "1945":
                            estado = "fase2"
                        else:
                
                            senha_digitada = ""  

                elif evento.type == pygame.MOUSEBUTTONUP:
                    clicou = False  

                if(len(senha_digitada) == 1):
                    pygame.draw.circle(TELA, PRETO, (423, 283), radius = 25)

                elif(len(senha_digitada) == 2):
                    pygame.draw.circle(TELA, PRETO, (423, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (523, 283), radius = 25)

                elif(len(senha_digitada) == 3):
                    pygame.draw.circle(TELA, PRETO, (423, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (523, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (623, 283), radius = 25)

                elif(len(senha_digitada) == 4):
                    pygame.draw.circle(TELA, PRETO, (423, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (523, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (623, 283), radius = 25)
                    pygame.draw.circle(TELA, PRETO, (723, 283), radius = 25)


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


            imgpapiro = ponto_interagivel(imgpapiro,566, 480, 150, 20)
            imgpiramides = ponto_interagivel(imgpiramides, 1111, 436, 50, 30)
            imganubis = ponto_interagivel(imganubis, 39 ,238 , 40, 90)
            imgescaravelho = ponto_interagivel(imgescaravelho, 451, 441, 15, 35)
            imgesfingevazo = ponto_interagivel(imgesfingevazo, 1090, 620, 80, 70)
            imgesfingecama = ponto_interagivel(imgesfingecama, 308, 504 , 52, 86)
            if (botao_invisivel_click(20, 438, 50, 22)):
                estado = 'senha2'
                senha_digitada = ''
                fonte = pygame.font.Font(None, 48)
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

            
            if (botao_invisivel_click(767,367, 160, 50)):
                estado = 'fase2'


            if(botao_invisivel_click(408, 367, 160, 50)):
                if(texto_digitado.upper() == 'ESFINGE DE GIZE' or texto_digitado.upper() == 'ESFINGE DE GIZÉ'):

                    estado = 'fase3'
            print(texto_digitado)


        
            superficie_texto = fonte.render(texto_digitado, True, (0, 0, 0)) 
            TELA.blit(cenasenha2, (0 , 0))
            TELA.blit(superficie_texto, (425, 299))
        

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
            
            imgrio1 = ponto_interagivel(imgrio1, 895, 96, 50, 56)
            imgrio2 = ponto_interagivel(imgrio2, 956, 126, 70, 80)
            imgdomP = ponto_interagivel(imgdomP, 447, 52, 120, 150)
            imgenigma = ponto_interagivel(imgenigma, 523, 421 ,13, 30)
            imgband = ponto_interagivel(imgband, 874, 336, 35, 42)
            imgcavalo = ponto_interagivel(imgcavalo, 330, 193, 30, 30)

            
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


        pygame.display.update()
        print(estado)
    
        

def creditos():
    print("Autores do projeto...")

def sair():
    pygame.quit()
    sys.exit()

def menu():
    while True:
        TELA.blit(fundo, (0, 0))
        desenhar_botao("Jogar", 321, 332, 200, 60, LARANJA_ESCURO, LARANJA_CLARO, jogar)
        desenhar_botao("Créditos", 321, 406, 200, 60, LARANJA_ESCURO, LARANJA_CLARO, creditos)
        desenhar_botao("Sair", 321, 479, 200, 60, LARANJA_ESCURO, LARANJA_CLARO, sair)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

menu()
