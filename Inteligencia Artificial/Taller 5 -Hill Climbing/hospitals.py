import random


class Space():

    def __init__(self, height, width, num_hospitals):
        """Crear un nuevo estado con las dimensiones dadas."""
        # Definir las dimensiones del espacio y el número de hospitales
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set() # Conjunto vácio de casas
        self.hospitals = set()  # Conjunto vácio de hospitales

    def add_house(self, row, col):
        """Añadir a una casa una locación especifica en el espacio."""
        # Guardar una casa representada por su posición en el espacio
        self.houses.add((row, col))

    def available_spaces(self):
        """Devolver todas las celdas en vacías."""

        # Conjunto de todas las celdas en el espacio en todas las posiciones posibles
        candidates = set(
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
        )

        # Remover todas las casas y hospitales
        # Elimina cualquier posición ya ocuapada por una casa
        for house in self.houses:
            candidates.remove(house)
        for hospital in self.hospitals:
            candidates.remove(hospital)
        return candidates

    # Hill Climbing normal , se envia log = True para ver el estado de cada iteracion
    # y el image_prefix para guardar las imagenes de cada iteracion
    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        """Performs hill-climbing to find a solution."""
        count = 0

        # la ubicación de los hospitales iniciales son aleatorios
        self.hospitals = set()
        for i in range(self.num_hospitals):
            # añade posiciones aleatorias para los hospitales
            self.hospitals.add(random.choice(list(self.available_spaces())))
        if log:
            # Imprime el estado inicial y su costo
            print("Initial state: cost", self.get_cost(self.hospitals))
        if image_prefix:
            # Genera una imagen del estado inicial
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

        # Repita hasta llegar a un número mázimo de iteraciones o hasta que el estado no cambie
        while maximum is None or count < maximum:
            count += 1
            best_neighbors = []
            best_neighbor_cost = None

            # Considere todos los hospitales a mover
            for hospital in self.hospitals:

                # Considere todos los vecinos de un hospital que no sean una casa u otro hospital
                for replacement in self.get_neighbors(*hospital):
                    
                    # Generar un conjunto vecino de hospitales
                    neighbor = self.hospitals.copy() # copia todo el conjunto de hospitales
                    neighbor.remove(hospital) # remueve el hospital actual que se esta analizando
                    neighbor.add(replacement) # añade uno de los vecinos de ese hospital

                    # Compruebo que vecino es mejor
                    cost = self.get_cost(neighbor) # costo de la distancia de un vecion al resto de vecinos
                    if best_neighbor_cost is None or cost < best_neighbor_cost: # si se encuentra un costo más corto
                        best_neighbor_cost = cost # se actualiza el mejor costo
                        best_neighbors = [neighbor] # nueva lista de mejores vecinos
        
                    elif best_neighbor_cost == cost: # si el costo es igual guarda este vecino en la lista de mejores vecinos
                        best_neighbors.append(neighbor)

            # Si ninguno de los vecionos es mejor que el estado actual 
            if best_neighbor_cost >= self.get_cost(self.hospitals):
                return self.hospitals

            # Mudarse a un vecino de mayor valor
            else:
                if log:
                    print(f"Found better neighbor: cost {best_neighbor_cost}")
                self.hospitals = random.choice(best_neighbors)

            # Generar lmagen
            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

    def random_restart(self, maximum, image_prefix=None, log=False):
        """Repeats hill-climbing multiple times."""
        best_hospitals = None
        best_cost = None

        # Repite la escalada un número fijo de veces 
        for i in range(maximum):
            hospitals = self.hill_climb()
            cost = self.get_cost(hospitals)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_hospitals = hospitals
                if log:
                    print(f"{i}: Found new best state: cost {cost}")
            else:
                if log:
                    print(f"{i}: Found state: cost {cost}")

            if image_prefix:
                self.output_image(f"{image_prefix}{str(i).zfill(3)}.png")

        return best_hospitals

    def get_cost(self, hospitals):
        """Calcual la suma de distancias desde las casas a los hospitales más cercanos."""
        cost = 0
        for house in self.houses:
            # Para cada casa se escoje la mínima distancia al comparar con cada hosptial en el espacio
            cost += min(
                abs(house[0] - hospital[0]) + abs(house[1] - hospital[1])
                for hospital in hospitals
            )
        return cost

    def get_neighbors(self, row, col):
        """Dame la posición de los vecinos q no son una casa u hospital."""
        candidates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]
        neighbors = []
        for r, c in candidates:
            if (r, c) in self.houses or (r, c) in self.hospitals:
                continue
            if 0 <= r < self.height and 0 <= c < self.width:
                neighbors.append((r, c))
        return neighbors

    def output_image(self, filename):
        """Generates image with all houses and hospitals."""
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        house = Image.open("assets/images/House.png").resize(
            (cell_size, cell_size)
        )
        hospital = Image.open("assets/images/Hospital.png").resize(
            (cell_size, cell_size)
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # Draw cell
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], hospital)

        # Add cost
        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: {self.get_cost(self.hospitals)}",
            fill="white",
            font=font
        )

        img.save(filename)


# Crear un nuevo espacio y añadir cassas randomicamente
s = Space(height=10, width=20, num_hospitals=3)
for i in range(15):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

# Use local search to determine hospital placement
hospitals = s.hill_climb(image_prefix="hospitals", log=True)

# Use local search to determine hospital placementhospitals = s.random_restart(20,image_prefix="hospitals", log = True)#
#hospitals = s.random_restart(200,image_prefix="hospitals", log = True)