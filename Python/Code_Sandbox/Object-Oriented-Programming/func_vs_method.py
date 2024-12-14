cars = ['BMW', 'Toyota', 'Honda', 'Audi']

new_list = sorted(cars)

print(f'Original list: {cars}')    # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 1: {new_list}')    # New list 1: ['Audi', 'BMW', 'Honda', 'Toyota']

new_list2 = cars.copy().sort()

print(f'Original list: {cars}')     # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 2: {new_list2}')   # None

new_list3 = cars.copy()
new_list3.sort()

print(f'Original list: {cars}')     # Original list: ['BMW', 'Toyota', 'Honda', 'Audi']
print(f'New list 3: {new_list3}')   # New list 3: ['Audi', 'BMW', 'Honda', 'Toyota']