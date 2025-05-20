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

    imagens_locais = {
        "fase": pygame.image.load("img/fase1.jpg"),
        #"fase2": pygame.image.load("img/fase2.jpg"),
    }

    for chave in imagens_locais:
        imagens_locais[chave] = pygame.transform.scale(imagens_locais[chave], (LARGURA, ALTURA))

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
            imagemfolha = ponto_interagivel(imagemfolha, 1064, 530, 40, 40)
            imagemquadro = ponto_interagivel(imagemquadro,834,188,110,120)
            imagemmapa = ponto_interagivel(imagemmapa,1200,600,30,65)
            
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

        # Tecla 1 (x: 450, y: 330, largura: 75, altura: 45)
                    if 450 <= x <= 525 and 330 <= y <= 375:
                        if len(senha_digitada) < 4:
                            senha_digitada += "1"

                    # Tecla 9 (x: 611, y: 462, largura: 75, altura: 80)
                    elif 611 <= x <= 686 and 462 <= y <= 542:
                        if len(senha_digitada) < 4:
                            senha_digitada += "9"

                    # Tecla 4 (x: 450, y: 395, largura: 75, altura: 80)
                    elif 450 <= x <= 525 and 395 <= y <= 475:
                        if len(senha_digitada) < 4:
                            senha_digitada += "4"

                    # Tecla 5 (x: 533, y: 395, largura: 75, altura: 80)
                    elif 533 <= x <= 608 and 395 <= y <= 475:
                        if len(senha_digitada) < 4:
                            senha_digitada += "5"

                    # Confirmar (x: 711, y: 350, largura: 160, altura: 50)
                    elif 711 <= x <= 871 and 350 <= y <= 400:
                        if senha_digitada == "1945":
                            estado = "fase2"
                        else:
                
                            senha_digitada = ""  
                elif evento.type == pygame.MOUSEBUTTONUP:
                    clicou = False  

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


        elif estado in imagens_locais:
            TELA.blit(imagens_locais[estado], (0, 0))

        pygame.display.update()
        print(senha_digitada)
        print(pygame.mouse.get_pos())

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
