cars = ['BMW', 'Toyota', 'Honda', 'Audi']

new_list = sorted(cars)

print(f'''Original list: {cars} 
      New list 1: {new_list}''')

new_list2 = cars.copy().sort()


print(f'''Original list: {cars} 
      New list 2: {new_list2}''')

new_list3 = cars.copy()
new_list3.sort()

print(f'''Original list: {cars} 
      New list 3: {new_list3}''')