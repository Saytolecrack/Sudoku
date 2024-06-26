import time
import pygame
import sys
import sudokum 



class Case:
    
    def __init__(self, valeur, ligne, colonne,modifiable, couleur = (255, 255, 255)):
        self.valeur = valeur
        self.ligne = ligne
        self.colonne = colonne
        self.modifiable = modifiable
        self.couleur = couleur
    
    @property
    
    def valeur(self):
        return self.__valeur
    
    @valeur.setter
    
    def valeur(self, valeur):
        if valeur < 10 and valeur >= 0 and isinstance(valeur, int):
            self.__valeur = valeur
        else:
            raise ValueError("La valeur doit être comprise entre 1 et 9")
        
    @property
    
    def ligne(self):
        return self.__ligne
    
    @ligne.setter
    
    def ligne(self, ligne):
        if ligne < 10 and ligne >= 0 and isinstance(ligne, int):
            self.__ligne = ligne
        else:
            raise ValueError("La ligne doit être comprise entre 1 et 9")
        
    @property
    
    def colonne(self):
        return self.__colonne
    
    @colonne.setter
    
    def colonne(self, colonne):
        if colonne < 10 and colonne >= 0 and isinstance(colonne, int):
            self.__colonne = colonne
        else:
            raise ValueError("La colonne doit être comprise entre 1 et 9") 
    
    @property
    def couleur(self):
        return self.__couleur
    
    @couleur.setter
    def couleur(self, couleur):
        if isinstance(couleur, tuple):
            self.__couleur = couleur
        else:
            raise ValueError("La couleur doit être une tuple")      
        
    def __str__(self):
        return f"Case {self.ligne+1}, {self.colonne+1} valeur : {self.valeur} modifiable : {self.modifiable}" 

class sudokuIhm:
    
    def __init__(self, difficulty, controller):
        self.difficulty = difficulty
        self.tabCase = [[Case(0, i, j, True) for j in range(9)] for i in range(9)]
        self.caseTpm = None
        if self.difficulty == 1:            
            self.sudoku = sudokum.generate(0.4)
        elif self.difficulty == 2:
            self.sudoku = sudokum.generate(0.5)
        elif self.difficulty == 3:  
            self.sudoku = sudokum.generate(0.7)
            
        print(self.sudoku)
        self.button_x = 470
        self.button_y = 30
        self.button_width = 80
        self.button_height = 40

        self.button2_x = 470
        self.button2_y = 80
        self.button2_width = 120
        self.button2_height = 40

        self.btnSolve_x = 10
        self.btnSolve_y = 470
        self.btnSolve_width = 80
        self.btnSolve_height = 40

        self.btnValidate_x = 100
        self.btnValidate_y = 470
        self.btnValidate_width = 80
        self.btnValidate_height = 40
        
        self.btnNewGame_x = 470
        self.btnNewGame_y = 470
        self.btnNewGame_width = 120
        self.btnNewGame_height = 40
        
        self.screen = None
        self.controller = controller
        self.currentWindow = 0
        
    def SetDifficulty(self, difficulty):
        self.difficulty = difficulty
         
    def DrawLines(self) :
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 4
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (50 * i, 0), (50 * i, 450), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, 50 * i), (450, 50 * i), line_thickness)

    def initTableau(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j]  != 0:
                    self.tabCase[i][j].valeur = int(self.sudoku[i][j])
                    self.tabCase[i][j].modifiable = False
                    self.tabCase[i][j].couleur = (200,200,200)
                else:
                    self.tabCase[i][j].valeur = 0
                    self.tabCase[i][j].modifiable = True
                    
    def searchPossibleValues(self,i,j):
        # à faire : recursivité pour résouidre le sudoku
        possible_moves = [num for num in range(1, 10)]

        # Check numbers in the row
        for col in range(9):
            if self.tabCase[i][col].valeur in possible_moves:
                possible_moves.remove(self.tabCase[i][col].valeur)

        # Check numbers in the column
        for row in range(9):
            if self.tabCase[row][j].valeur in possible_moves:
                possible_moves.remove(self.tabCase[row][j].valeur)

        # Check numbers in the box
        for row in range(i // 3 * 3, i // 3 * 3 + 3):
            for col in range(j // 3 * 3, j // 3 * 3 + 3):
                if self.tabCase[row][col].valeur in possible_moves:
                    possible_moves.remove(self.tabCase[row][col].valeur)
        return possible_moves
    
    def DrawButton(self,name,x,y,w,h, color=(116, 208, 241), clicked = False):
        
        if clicked == False : 
            # Draw the button shadow
            shadow_rect = pygame.Rect(x + 2, y + 2, w, h)
            pygame.draw.rect(self.screen, (50, 50, 50), shadow_rect)
        else :
            shadow_rect = pygame.Rect( x + 2, y + 2, w, h)
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

    def DrawCase(self) :
        for j in range(9):
            for i in range(9):
                case = self.tabCase[i][j]
                if self.caseTpm is None:
                    if case.modifiable == True:
                        case.couleur = (255, 255, 255)
                pygame.draw.rect(self.screen, case.couleur, (j * 50, i * 50, 50, 50))
                if case.valeur  != 0 :
                    font = pygame.font.Font(None, 40)
                    text = font.render(str(case.valeur), 1, (0, 0, 0))
                    self.screen.blit(text, (case.colonne * 50 + 20, case.ligne * 50 + 10))
       
    def draw_timer(self, minutes, seconds):
        pygame.draw.rect(self.screen,(255,255,255),(470,10,80,20))
        font = pygame.font.Font(None, 16)
        text = font.render(f"Temps : {minutes:02}:{seconds:02}", True, (0, 0, 0))
        self.screen.blit(text, (470, 10))
                 
    def resetValue(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (470,140,130,300))
    
    def getEmptyCase(self):
        for i in range(9):
            for j in range(9):
                if self.tabCase[i][j].valeur == 0:
                    return self.tabCase[i][j]
        return None
    
    def checkValue(self,case, value):
        # Check numbers in the row
        tab = self.searchPossibleValues(case.ligne,case.colonne)
        if value in tab:
            return True
        else:
            return False
        
    def solveSudoku(self):
        
        case = self.getEmptyCase()
        if case is None:
            return True
        
        for i in range(1,10):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            case.valeur = i
            self.DrawCase()
            self.DrawLines()
            pygame.display.update((case.colonne * 50, case.ligne * 50, 50, 50))
            time.sleep(0.05)
            
            case.valeur = 0
            
            if not self.checkValue(case, i):
                case.valeur = 0
                continue
            case.valeur = i
                
            pygame.display.update((case.colonne * 50, case.ligne * 50, 50, 50))
            self.DrawCase()
            self.DrawLines()
            
            if self.solveSudoku():
                return True

        case.valeur = 0
        
        self.DrawCase()
        self.DrawLines()
        pygame.display.update((case.colonne * 50, case.ligne * 50, 50, 50))
        
        return False

    def verifieCase(self,case):
        value = case.valeur
        for i in range(9):
            if self.tabCase[i][case.colonne].valeur == value and i != case.ligne:
                return False
            if self.tabCase[case.ligne][i].valeur == value and i != case.colonne:
                return False
        for i in range(3):
            for j in range(3):
                if self.tabCase[(case.ligne//3)*3 + i][(case.colonne//3)*3 + j].valeur == value and (case.ligne//3)*3 + i != case.ligne and (case.colonne//3)*3 + j != case.colonne:
                    return False
        return True
    
    def Validate(self):
        if self.getEmptyCase() is not None:
            self.DrawButton("Sudoku Imcomplet ",self.btnValidate_x + 150 , self.btnValidate_y, self.btnValidate_width+80, self.btnValidate_height, (255, 0, 0))
            return False
        else:
            for row in range(9):
                for col in range(9):
                    if not self.verifieCase(self.tabCase[row][col]):
                        self.DrawButton("Sudoku Invalide ",self.btnValidate_x + 150 , self.btnValidate_y, self.btnValidate_width+80, self.btnValidate_height, (255, 0, 0))
                        return False
        self.DrawButton("Bravo ",self.btnValidate_x + 150 , self.btnValidate_y, self.btnValidate_width+80, self.btnValidate_height, (0, 255, 0))
        return True
    
    def play(self):
        pygame.init()
        self.currentWindow = 1
        self.screen = pygame.display.set_mode((600, 520))
        pygame.display.set_caption("Sudoku")
        self.screen.fill((255, 255, 255))
        if self.difficulty == 1:            
            self.sudoku = sudokum.generate(0.4)
        elif self.difficulty == 2:
            self.sudoku = sudokum.generate(0.5)
        elif self.difficulty == 3:  
            self.sudoku = sudokum.generate(0.7)

        self.initTableau()
        
        start_time = time.time()
        
        running = True
        sudokuOk = False
        
        while running:
            
            if not sudokuOk :
                current_time = int(time.time()- start_time)
                minutes = current_time // 60
                seconds = current_time % 60
            
            self.draw_timer(minutes,seconds)
            self.DrawCase()
            self.DrawLines()
            
            # Draw the button
            mouseX, mouseY = pygame.mouse.get_pos()
                
            if self.button_x < mouseX < self.button_x + self.button_width and self.button_y < mouseY < self.button_y + self.button_height:
                self.DrawButton("Reset",self.button_x, self.button_y, self.button_width, self.button_height, (1, 215, 88), True)
            else:
                self.DrawButton("Reset",self.button_x, self.button_y, self.button_width, self.button_height)
                
            if self.button2_x < mouseX < self.button2_x + self.button2_width and self.button2_y < mouseY < self.button2_y + self.button2_height:
                self.DrawButton("Search value",self.button2_x, self.button2_y, self.button2_width, self.button2_height, (1, 215, 88),True)
            else:
                self.DrawButton("Search value",self.button2_x, self.button2_y, self.button2_width, self.button2_height)
                
            if self.btnSolve_x < mouseX < self.btnSolve_x + self.btnSolve_width and self.btnSolve_y < mouseY < self.btnSolve_y + self.btnSolve_height:
                self.DrawButton("Solve",self.btnSolve_x, self.btnSolve_y, self.btnSolve_width, self.btnSolve_height, (1, 215, 88),True)
            else:
                self.DrawButton("Solve",self.btnSolve_x, self.btnSolve_y, self.btnSolve_width, self.btnSolve_height)
                
            if self.btnValidate_x < mouseX < self.btnValidate_x + self.btnValidate_width and self.btnValidate_y < mouseY < self.btnValidate_y + self.btnValidate_height:
                self.DrawButton("Validate",self.btnValidate_x, self.btnValidate_y, self.btnValidate_width, self.btnValidate_height, (1, 215, 88),True)
            else:
                self.DrawButton("Validate",self.btnValidate_x, self.btnValidate_y, self.btnValidate_width, self.btnValidate_height) 
                
            if self.btnNewGame_x < mouseX < self.btnNewGame_x + self.btnNewGame_width and self.btnNewGame_y < mouseY < self.btnNewGame_y + self.btnNewGame_height:
                self.DrawButton("New Game",self.btnNewGame_x, self.btnNewGame_y, self.btnNewGame_width, self.btnNewGame_height, (1, 215, 88),True)
            else:
                self.DrawButton("New Game",self.btnNewGame_x, self.btnNewGame_y, self.btnNewGame_width, self.btnNewGame_height) 
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP:
                    if self.caseTpm is not None and self.caseTpm.modifiable == True:
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 1
                        if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 2
                        if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 3
                        if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 4
                        if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 5
                        if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 6
                        if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 7
                        if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 8
                        if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 9
                        if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur = 0
                        if event.key ==pygame.K_RETURN:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].valeur != 0
                            self.caseTpm = None
                        self.DrawLines()
                        self.DrawCase()      
                # Obtention des coordonnées du clic
                                
                if event.type == pygame.MOUSEBUTTONDOWN:
                
                    # Calcul des indices de la case cliquée
                    clicked_row = mouseY // 50  # 50 est la hauteur d'une case
                    clicked_col = mouseX // 50  # 50 est la largeur d'une case
                    
                    if (clicked_row >= 0 and clicked_row < 9 and clicked_col >= 0 and clicked_col < 9):
                        if self.caseTpm is not None and self.tabCase[clicked_row][clicked_col].modifiable == True:
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].couleur = (255, 255, 255)
                            self.caseTpm = self.tabCase[clicked_row][clicked_col]
                            self.tabCase[self.caseTpm.ligne][self.caseTpm.colonne].couleur = (1, 215, 88)
                        elif self.tabCase[clicked_row][clicked_col].modifiable == True:
                            self.tabCase[clicked_row][clicked_col].couleur = (1, 215, 88)
                            self.caseTpm = self.tabCase[clicked_row][clicked_col]
                            
                        for i in range(9):
                            for j in range(9):
                                if self.caseTpm is not None :
                                    if self.tabCase[i][j] == self.caseTpm : 
                                        continue
                                    if (self.tabCase[i][j].ligne == self.caseTpm.ligne or self.tabCase[i][j].colonne == self.caseTpm.colonne or (i//3 == self.caseTpm.ligne//3 and j//3 == self.caseTpm.colonne//3)) and self.tabCase[i][j].modifiable == True:
                                        self.tabCase[i][j].couleur = (176, 242, 182)
                                    elif self.tabCase[i][j].modifiable == True :
                                        self.tabCase[i][j].couleur = (255, 255, 255)
                        self.DrawCase()
                        self.resetValue()
                        
                    if self.button_x < mouseX < self.button_x + self.button_width and self.button_y < mouseY < self.button_y + self.button_height:
                        # Clic détecté sur le bouton
                        self.caseTpm = None
                        self.initTableau()
                    if self.button2_x < mouseX < self.button2_x + self.button2_width and self.button2_y < mouseY < self.button2_y + self.button2_height:
                        if self.caseTpm is not None:
                            tab = self.searchPossibleValues(self.caseTpm.ligne,self.caseTpm.colonne)
                            self.resetValue()
                            y=0
                            for i in range(len(tab)):
                                font = pygame.font.Font(None, 40)
                                text = font.render(str(tab[i]), 1, (0, 0, 0))
                                self.DrawButton(str(tab[i]),470, 140 + y, 40, 40, (1, 215, 88))
                                y += 50
                            pygame.display.update()
                        else:
                            print("Veuillez selectionner une case")
                            
                    if self.btnSolve_x < mouseX < self.btnSolve_x + self.btnSolve_width and self.btnSolve_y < mouseY < self.btnSolve_y + self.btnSolve_height:
                        self.initTableau()
                        self.solveSudoku()
                        pygame.display.update()
                        print("fin")
                        
                    if self.btnValidate_x < mouseX < self.btnValidate_x + self.btnValidate_width and self.btnValidate_y < mouseY < self.btnValidate_y + self.btnValidate_height:
                        if self.Validate() :
                            sudokuOk = True
                        
                    # button new game
                    
                    if self.btnNewGame_x < mouseX < self.btnNewGame_x + self.btnNewGame_width and self.btnNewGame_y < mouseY < self.btnNewGame_y + self.btnNewGame_height:
                        if self.currentWindow == 1:
                            self.controller.lancer_accueil()

            # Dessin des lignes horizontales et verticales
            self.DrawLines()

            pygame.display.update()
        pygame.display.quit()
        pygame.quit()
 
    def close(self):
        pygame.display.quit()
        pygame.quit()
        