class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def __repr__(self):
        return f"objektas-> cpu: {self.cpu}, ram: {self.ram}"

    def display(self):
        print("HEllo")

    def __display(self):
        print("HEllo")


msi = Computer("Intel i7", "2gb")

msi.display()


msi.__display()
print(msi)
