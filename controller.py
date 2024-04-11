from AccueilIhm import AccueilIHM

from sudokuIhm import sudokuIhm

class Controller:
    
    def __init__(self):
        self.accueil = None
        self.sudoku = None
    
    def lancer_accueil(self):
    # Code pour lancer l'interface utilisateur d'accueil
        if self.sudoku != None:
            self.sudoku.close()
            print("Fermeture de l'interface utilisateur du Sudoku")
            self.sudoku = None
            print (self.sudoku)
        self.accueil = AccueilIHM(self)
        self.accueil.initAccueil()

    def lancer_sudoku(self,difficulte):
        # Code pour lancer l'interface utilisateur du Sudoku en fonction de la difficulté sélectionnée
        if self.accueil != None:
            self.accueil.close()
            print("Fermeture de l'interface utilisateur de l'accueil")
            self.accueil = None
            
        self.sudoku = sudokuIhm(difficulte,self)
        
        self.sudoku.play()
    

if __name__ == "__main__":
    controller = Controller()
    controller.lancer_accueil()
    