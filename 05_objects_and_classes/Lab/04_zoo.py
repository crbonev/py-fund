class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'birds':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            print(f'Mammals in {self.name}: {", ".join(self.mammals)}')
        elif species == 'fish':
            print(f'Fishes in {self.name}: {", ".join(self.fish)}')
        elif species == 'bird':
            print(f'Birds in {self.name}: {", ".join(self.birds)}')
        # result = f'Total animals: {Zoo.__animals}'
        print(f'Total animals: {Zoo.__animals}')


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for i in range(count):
    animal = input().split(' ')
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

info = input()
zoo.get_info(info)
