import pygame


class AccueilIHM :  

    def __init__(self,controller):
        self.controller = controller
        self.difficulty = 3
        #self.sudoku = sudokuIhm(self.difficulty,self)

    def drawTitle(self) :
        
        # Initialisation du texte
        text = "BINVENUE DANS LE JEU SUDOKU"
        text2 = "Veuillez choisir une difficulté :"
        # Initialisation de la couleur du texte
        textcolor = (0, 0, 0)
        # Initialisation de la police du texte
        font = pygame.font.Font(None, 36)
        # Initialisation de la surface du texte
        text_surface = font.render(text, True, textcolor)
        text_surface2 = font.render(text2, True, textcolor)
        
        textrect = text_surface.get_rect()
        textrect2 = text_surface2.get_rect()
        
        # Initialisation de la position du texte
        text_X = (self.windos_width - textrect.width ) //2
        text_Y = 100
        text_X2 =  (self.windos_width - textrect2.width ) //2
        text_Y2 = 150
        # Affichage du texte
        self.screen.blit(text_surface, (text_X, text_Y))
        self.screen.blit(text_surface2, (text_X2, text_Y2))
        
    def DrawButton(self,name,x,y,w,h, color=(116, 208, 241),clicked = False):
    
        if clicked == False :
            # Draw the button shadow
            shadow_rect = pygame.Rect(x + 2, y + 2, w, h)
            pygame.draw.rect(self.screen, (50, 50, 50), shadow_rect)
        else :
            # Draw the button shadow
            shadow_rect = pygame.Rect(x + 2, y + 2, w, h)
            pygame.draw.rect(self.screen, (255,255,255), shadow_rect)

        # Draw the button background
        button_rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.screen, color, button_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)

        # Draw the button text
        font = pygame.font.Font(None, 24)
        text = font.render(name, True, (0,0,0))
        text_rect = text.get_rect(center=button_rect.center)
        self.screen.blit(text, text_rect)
        
    def initAccueil(self) :
        pygame.init()
        pygame.display.init()
        self.windos_width = 600
        self.windos_height = 520
        
        self.difficulty = 0
        self.btnEasy_y = 200
        self.btnEasy_w = 100
        self.btnEasy_h = 50
        self.btnEasy_x = (self.windos_width  - self.btnEasy_w ) //2

        self.btnMedium_y = 275
        self.btnMedium_w = 100
        self.btnMedium_h = 50
        self.btnMedium_x = (self.windos_width  - self.btnMedium_w ) //2
        
        self.btnHard_y = 350
        self.btnHard_w = 100
        self.btnHard_h = 50
        self.btnHard_x = (self.windos_width  - self.btnHard_w ) //2
        
        self.btnPlay_y = 425
        self.btnPlay_w = 100
        self.btnPlay_h = 50
        self.btnPlay_x = (self.windos_width  - self.btnPlay_w ) //2
        
        self.screen = pygame.display.set_mode((self.windos_width, self.windos_height)) 
        
        self.screen = pygame.display.set_mode((600, 520))
        pygame.display.set_caption("Accueil")
        
        self.screen.fill((255, 255, 255))
        
        self.drawTitle()

        running = True
        
        while running:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()    
            
            if (self.btnEasy_x <= mouse_x <= self.btnEasy_x + self.btnEasy_w and self.btnEasy_y <= mouse_y <= self.btnEasy_y + self.btnEasy_h) or self.difficulty == 1:
                self.DrawButton("Easy",self.btnEasy_x,self.btnEasy_y,self.btnEasy_w,self.btnEasy_h,(0, 255, 0),True)
            else :
                self.DrawButton("Easy",self.btnEasy_x,self.btnEasy_y,self.btnEasy_w,self.btnEasy_h)
                
            if (self.btnMedium_x <= mouse_x <= self.btnMedium_x + self.btnMedium_w and self.btnMedium_y <= mouse_y <= self.btnMedium_y + self.btnMedium_h) or self.difficulty == 2:
                self.DrawButton("Medium",self.btnMedium_x,self.btnMedium_y,self.btnMedium_w,self.btnMedium_h,(255, 255, 0),True)
            else :
                self.DrawButton("Medium",self.btnMedium_x,self.btnMedium_y,self.btnMedium_w,self.btnMedium_h)
                
            if (self.btnHard_x <= mouse_x <= self.btnHard_x + self.btnHard_w and self.btnHard_y <= mouse_y <= self.btnHard_y + self.btnHard_h) or self.difficulty == 3:
                self.DrawButton("Hard",self.btnHard_x,self.btnHard_y,self.btnHard_w,self.btnHard_h,(255, 0, 0),True)
            else :
                self.DrawButton("Hard",self.btnHard_x,self.btnHard_y,self.btnHard_w,self.btnHard_h)
                
            if self.btnPlay_x <= mouse_x <= self.btnPlay_x + self.btnPlay_w and self.btnPlay_y <= mouse_y <= self.btnPlay_y + self.btnPlay_h :
                self.DrawButton("Play",self.btnPlay_x,self.btnPlay_y,self.btnPlay_w,self.btnPlay_h,(1, 215, 88),True)
            else :
                self.DrawButton("Play",self.btnPlay_x,self.btnPlay_y,self.btnPlay_w,self.btnPlay_h)    
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN :
                
                    if self.btnEasy_x <= mouse_x <= self.btnEasy_x + self.btnEasy_w and self.btnEasy_y <= mouse_y <= self.btnEasy_y + self.btnEasy_h :
                        self.difficulty = 1
                    if self.btnMedium_x <= mouse_x <= self.btnMedium_x + self.btnMedium_w and self.btnMedium_y <= mouse_y <= self.btnMedium_y + self.btnMedium_h :
                        self.difficulty = 2
                    if self.btnHard_x <= mouse_x <= self.btnHard_x + self.btnHard_w and self.btnHard_y <= mouse_y <= self.btnHard_y + self.btnHard_h :
                        self.difficulty = 3
                    if self.btnPlay_x <= mouse_x <= self.btnPlay_x + self.btnPlay_w and self.btnPlay_y <= mouse_y <= self.btnPlay_y + self.btnPlay_h :
                        if self.difficulty == 1 :
                            self.controller.lancer_sudoku(1)
                        elif self.difficulty == 2 or self.difficulty == 0 :
                            self.controller.lancer_sudoku(2)
                        elif self.difficulty == 3 :
                            self.controller.lancer_sudoku(3)
                                      
            pygame.display.update()
        pygame.quit()
        
        
    def close(self):
        pygame.display.quit()
        pygame.quit()