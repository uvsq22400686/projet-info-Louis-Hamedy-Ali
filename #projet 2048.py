#projet 2048
import tkinter as tk
import random
racine = tk.Tk() # Création de la fenêtre racine
racine.title("2048")
#canvas = tk.Canvas(racine,text="2048", font=("helvetica","20"))
#WIDTH=500
#HEIGHT=500
case_taille=100
canvas_grid=4
marge=4
background_color="beige"
case_vide_color="gray"
couleur_block={2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179", 16: "#F59563",
    32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72", 256: "#EDCC61",
    512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E"}
couleur_texte = {2: "#776E65", 4: "#776E65", 8: "#F9F6F2"}
#largeur_case = WIDTH // 4
#hauteur_case = HEIGHT // 4

#canvas=tk.Canvas(racine,background="beige",width=WIDTH,height=HEIGHT)
#canvas.grid(row=1,column=1,rowspan=3)
#canvas.create_rectangle((100, 100), (450, 450))
#canvas.grid()
#for i in range(8):
    #for j in range(8):
        #if (i+j) % 2 == 0:
            #color = "gray80"
        #else:
            #color = "gray80"
        #canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                #((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)
        
class Game2048:
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.title("2048")
        self.racine.resizable(False, False)
        self.grid = [[0] * canvas_grid for _ in range(canvas_grid)]
        self.init_ui()
        self.cree_block()
        self.cree_block()
        self.racine.bind("<Key>", self.key_press)
        self.update_ui()
        self.racine.mainloop()


def init_ui(self):
        """ Initialise l'interface graphique """
        self.canvas = tk.Canvas(self.root, width=canvas_grid * case_taille, height=canvas_grid * case_taille, bg=background_color)
        self.canvas.pack()


def cree_block(self):
        """ Ajoute un nouveau block (2 ou 4) à un emplacement vide """
        case_vide = [(i, j) for i in range(canvas_grid) for j in range(canvas_grid) if self.grid[i][j] == 0]
        if case_vide:
            i, j = random.choice(case_vide)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4


def interface(self):
        """ Met à jour l'affichage du plateau """
        self.canvas.delete("all")
        for i in range(canvas_grid):
            for j in range(canvas_grid):
                value = self.grid[i][j]
                x0, y0 = j * case_taille + marge, i * case_taille + marge
                x1, y1 = x0 + case_taille - marge * 2, y0 + case_taille - marge * 2
                color = couleur_block.get(value, case_vide_color)
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
                if value:
                    couleur_texte = couleur_texte.get(value, "#F9F6F2")
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(value), font=("Arial", 24, "bold"), fill=couleur_texte)

def touches(self, event):
        """ Gère les déplacements selon la touche pressée """
        if event.keysym in ("haut", "bas", "gauche", "droite"):
            moved = self.move(event.keysym)
            if moved:
                self.cree_block()
                self.interface()
                if self.check_game_over():
                    self.game_over()

def deplacement(self, direction):
        """ Déplace et fusionne les blocks selon la direction """
        def compress(row):
            new_row = [v for v in row if v != 0]
            new_row += [0] * (canvas_grid - len(new_row))
            return new_row

        def merge(row):
            for i in range(canvas_grid - 1):
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] *= 2
                    row[i + 1] = 0
            return row

        def move_row_left(row):
            return compress(merge(compress(row)))

        rotated = False
        if direction in ("haut", "bas"):
            self.grid = [list(x) for x in zip(*self.grid)]
            rotated = True

        moved = False
        for i in range(canvas_grid):
            original = self.grid[i][:]
            self.grid[i] = move_row_left(self.grid[i] if direction in ("gauche", "haut") else self.grid[i][::-1])
            if direction in ("droite", "bas"):
                self.grid[i].reverse()
            if self.grid[i] != original:
                moved = True

        if rotated:
            self.grid = [list(x) for x in zip(*self.grid)]

        return moved

def check_game_over(self):
        """ Vérifie si le jeu est terminé """
        for row in self.grid:
            if 0 in row:
                return False
        for i in range(canvas_grid):
            for j in range(canvas_grid - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        for j in range(canvas_grid):
            for i in range(canvas_grid - 1):
                if self.grid[i][j] == self.grid[i + 1][j]:
                    return False
        return True

def game_over(self):
        """ Affiche un message de fin de partie """
        self.canvas.create_text(canvas_grid * case_taille / 2, canvas_grid * case_taille / 2, text="Game Over", font=("Arial", 32, "bold"), fill="red")

if __name__ == "__main__":
    Game2048()
#racine.mainloop()