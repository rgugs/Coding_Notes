class Animal:
    type = 'pig'
    name = 'Wilbur'

animal_1 = Animal()
print(f'Type: {animal_1.type}')
print(f'Name: {animal_1.name}')

# Change properties by assigning new ones

animal_1.type = 'goat'
print(f'New Type: {animal_1.type}')

# Add new properties to the object the same way
animal_1.age = 1
print(f'Age: {animal_1.age}')