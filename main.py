import pygame, Data, time, Functions
pygame.init()
pygame.font.init()
piosenka_gra=False
index_of_Note = 0

m = 475
my_font = pygame.font.SysFont('Brush Script MT', 30)
screen = pygame.display.set_mode((Data.SCREEN_WIDTH, Data.SCREEN_HEIGHT))

image = pygame.image.load('Graphics/cow.png').convert()
main_zdjecie= image.get_rect()
image2 = pygame.image.load('Graphics/Logo.png').convert()
logo_zdjecie= image2.get_rect()
image3 = pygame.image.load('Graphics/radio.png').convert()
radio= image3.get_rect()
image4 = pygame.image.load('Graphics/frame.png').convert()
ramka= image4.get_rect()
image5 = pygame.image.load('Graphics/letters.png').convert()
liter = image5.get_rect()
screen.blit(image4, ramka)

run = True
j = 0
inputt=""
main_zdjecie.center = (550, 300)
logo_zdjecie.center = (455, 60)
radio.center = (1000, 560)
ramka.center = (400, 435)
liter.center = (100, 280)

c = 0



wynik = 0
Nazwa = input("Podaj swoją nazwę, aby wprowadzić wynik do tabeli: ")
while run:
    screen.fill((0,0,0))
    screen.blit(image, main_zdjecie)
    screen.blit(image2, logo_zdjecie)
    screen.blit(image5, liter)
    for i in Data.list_of_blocks:

        pygame.draw.rect(screen, (255, 0, 0), i)



    key = pygame.key.get_pressed()
    if key[pygame.K_p] == True:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(Data.podklady["1"]))
        pygame.mixer.Channel(0).set_volume(0.4)
        piosenka_gra=True
    elif key[pygame.K_a] == True:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(Data.nuty_krowa["c"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[0])
        inputt = "C"
    elif key[pygame.K_s] == True:
        pygame.mixer.Channel(2).play(pygame.mixer.Sound(Data.nuty_krowa["d"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[1])
        inputt = "D"
    elif key[pygame.K_d] == True:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound(Data.nuty_krowa["e"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[2])
        inputt = "E"
    elif key[pygame.K_f] == True:
        pygame.mixer.Channel(4).play(pygame.mixer.Sound(Data.nuty_krowa["f"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[3])
        inputt = "F"
    elif key[pygame.K_g] == True:
        pygame.mixer.Channel(5).play(pygame.mixer.Sound(Data.nuty_krowa["g"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[4])
        inputt = "G"
    elif key[pygame.K_h] == True:
        pygame.mixer.Channel(6).play(pygame.mixer.Sound(Data.nuty_krowa["a"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[5])
        inputt = "A"
    elif key[pygame.K_j] == True:
        pygame.mixer.Channel(7).play(pygame.mixer.Sound(Data.nuty_krowa["b"]))
        pygame.draw.rect(screen, (255, 255, 255), Data.list_of_blocks[6])
        inputt = "B"
    elif key[pygame.K_ESCAPE] == True:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if piosenka_gra:
        if Functions.Click(Data.list_of_Notes, inputt, wynik, j):
            wynik += 1
        text_surface = my_font.render(
            f"Wynik: {wynik}",
            False, (255, 255, 255))
        screen.blit(text_surface, (358, 480))
        screen.blit(image3, radio)
        radio.move_ip(-10,0)
        time.sleep(0.05)
        ramka.center = (400, 435)
        screen.blit(image4, ramka)
        image4 = pygame.image.load(Functions.Queue(Data.dict_of_ramka, Data.list_of_Notes, j)).convert()
        ramka = image4.get_rect()
        inputt=""
        c += 1
        if Functions.Queue(Data.dict_of_ramka, Data.list_of_Notes, j) == 'Graphics/frame.png':
            if c % 5 == 0:
                j += 1
        elif Functions.Queue(Data.dict_of_ramka, Data.list_of_Notes, j) == 'Graphics/frame1.png':
            if c % 3 == 0:
                j += 1
        else:
            if c % 18 == 0:
                j += 1
        if j == len(Data.list_of_Notes) - 1:
            Data.list_of_Notes.append(" ")
    pygame.display.update()
pygame.quit()
if wynik != 0:
    file = open("Results", "a")
    file.write(f"\n{Nazwa}: {wynik}\n")
    file.close()
    Functions.Tabela()
