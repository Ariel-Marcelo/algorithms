import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        # board será una matriz con las filas como arreglos de tamaño width
        # estará lleno de False
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        # mines guara tuplas de coordenadas de las minas
        # estas coordenadas se van añadiendo como true en la matriz board
        while len(self.mines) != mines:
            print()
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    # consulta si una posición es una mina
    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Devuelve el conjunto de todas las celdas de self.cells que se sabe que son minas. 
        """
        if len(self.cells) == self.count:
            return self.cells
        return set()

    def known_safes(self):
        """
        Devuelve el conjunto de todas las celdas de self.cells que se sabe que son seguras. 
        """
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """
        Actualiza la representación del conocimiento interno dado que
         se sabe que una celda es una mina. 
        """
        new_cells = set()
        for my_cell in self.cells:
            if my_cell != cell:
                new_cells.add(my_cell)
            else:
                self.count -= 1
        self.cells = new_cells

    def mark_safe(self, cell):
        """
        Actualiza la representación del conocimiento interno dado que
        se sabe que una celda es segura 
        """
        new_cells = set()
        for my_cell in self.cells:
            if my_cell != cell:
                new_cells.add(my_cell)
        self.cells = new_cells


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Se llama cuando el tablero Buscaminas nos dice, para una celda segura determinada, cuántas celdas vecinas tienen minas.
        
        """
        #1) marcar la celda como un movimiento que se ha realizado
        self.moves_made.add(cell)
        #2) marcar la celda como segura
        self.mark_safe(cell)
        #3) agregar una nueva oración a la base de conocimientos de la IA basado en el valor de `cell` y `count`
        cells=set()

        for i in range(cell[0]-1,cell[0]+2):
            if(0<=i<self.height):
                for j in range(cell[1]-1,cell[1]+2):
                    if(0<=j<self.width):
                        if (i,j) not in self.moves_made and (i,j)!=cell:
                            new_cell_visited=(i,j)
                            cells.add(new_cell_visited)

        if len(cells)!=0:
            self.knowledge.append(Sentence(cells,count))

        # 4) marcar cualquier celda adicional como segura o como mina si se puede concluir en base a la base de conocimientos de la IA
        for sentence in self.knowledge:

            if sentence.known_safes()!=None:
                for mycell in sentence.known_safes():
                    if mycell not in self.moves_made:
                        self.safes.add(mycell)
                        if sentence in self.knowledge:
                            self.knowledge.remove(sentence)

            if sentence.known_mines()!=None:
                for mycell in sentence.known_mines():
                    self.mines.add(mycell)
                    if sentence in self.knowledge:
                        self.knowledge.remove(sentence)
            
        for sentence in self.knowledge:
            for mine in self.mines:
                if mine in sentence.cells:
                    sentence.cells.remove(mine)
                    sentence.count-=1
                    
        #5) agregue cualquier oración nueva a la base de conocimiento de AI si se pueden inferir del conocimiento existente 

        for knowledge1 in self.knowledge:
            for knowledge2 in self.knowledge: 
                if knowledge2.cells.issubset(knowledge1.cells) and knowledge2 is not knowledge1:
                    knowledge1.cells -= knowledge2.cells
                    knowledge1.count -= knowledge2.count

       

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        for cell in self.safes:
            if(cell not in self.moves_made):
                self.safes.remove(cell)
                return cell

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        temp=True
        while(temp):
            i=random.randrange(self.height)
            j=random.randrange(self.width)
            if (i,j) not in self.moves_made and (i,j) not in self.mines:
                temp=False
                return (i,j)
