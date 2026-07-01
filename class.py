class Fruit:
    def __init__(self, name, shape, color):
        self.name = name
        self.shape = shape
        self.color = color
        
    def display(self):
        print(f"This is {self.name}, it is {self.shape}, its color is {self.color}")
blueberry = Fruit("blueberry", "round", "purple")
blueberry.display()
blueberry.shape = "small and round"
blueberry.display()