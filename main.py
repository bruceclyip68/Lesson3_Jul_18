class IkeaFurniture:

    def __init__(self, name, dimensions, material, price):
        self.name = name
        self.dimensions = dimensions
        self.material = material
        self.price = price
        
Sample = IkeaFurniture('bookcase', (80, 200, 30), 'particle board', 199.99)

