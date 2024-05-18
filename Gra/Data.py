
import pygame, time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
blockC = pygame.Rect((20,475,50,50))
blockD = pygame.Rect((20,400,50,50))
blockE = pygame.Rect((20,325,50,50))
blockF = pygame.Rect((20,250,50,50))
blockG = pygame.Rect((20,175 ,50,50))
blockA = pygame.Rect((20,100,50,50))
blockB = pygame.Rect((20,25,50,50))
list_of_blocks = [blockC, blockD, blockE, blockF, blockG, blockA, blockB]
nuty_krowa ={"c": "Sounds/cow/cow_c.mp3", "d":"Sounds/cow/cow_d.mp3", "e": "Sounds/cow/cow_e.mp3", "f": "Sounds/cow/cow_f.mp3","g":"Sounds/cow/cow_g.mp3","a": "Sounds/cow/cow_a.mp3", "b": "Sounds/cow/cow_b.mp3" }
podklady = {"1":"Sounds/backgroundMusic/never gonna.mp3"}
dict_of_ramka = {"C": 'Graphics/BUTTONC.png', "D": 'Graphics/BUTTOND.png', "E": 'Graphics/BUTTONE.png', "F": 'Graphics/BUTTONF.png', "G": 'Graphics/BUTTONG.png', "A": 'Graphics/BUTTONA.png', "B": 'Graphics/BUTTONB.png'," ": 'Graphics/frame.png', "fast": 'Graphics/frame1.png'}
list_of_Notes = [" "," "," "," "," "," "," "," ","E", "G"," "," ","F"," ","A"," "," "," ","D"," "," ","E"," "," ","B","A"," "," "," "," "," ","E", "G"," "," ","F"," ","A"," "," "," ","D"," "," ","F"," "," ","B","A"," "," "," "," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F","G"," "," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," "," ","B","A"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," ","B","A"," "," ","F","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F","G"," "," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," "," ","B","A"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," ","B","A"," ","D","D"," ","E"," "," ","B","A"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," ","B","A"," "," ","F","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F","G"," "," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," ","F"," "," "," "," "," "," ","G","G"," "," "," ","E","E"," "," "," ","F","F"," ","G"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," "," ","B","A"," "," ","E"," "," ","G"," "," "," ","F"," "," ","A"," "," "," "," ","D","D"," ","E"," ","B","A"]








