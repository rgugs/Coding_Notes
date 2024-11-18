num_list = [1, 8, 4, 9, 2, 0, 10, 22, -4, -22]

low_letters = ['d', 'k', 'q', 'i', 'a']

cap_letters = ['Y', 'K', 'A', 'M', 'B']

mix_letters = ['r', 'k', 'A', 'h', 'S', 'M']

mix_num_letters = ['d', 'k', 'q', 0, 10, 22, 'K', 'A',]

# Numbers
print('Numbers are sorted numerically')
print(' ')

print(f'Before: {num_list}')
num_list.sort()
print(f'Standard: {num_list}')
num_list.sort(reverse=True)
print(f'Reversed: {num_list}')
print(' ')

# Letters
print('Letters are sorted alphabetically, but captial letters will come first.')
print(' ')

print(f'Before: {low_letters}')
low_letters.sort()
print(f'Lower Sorted: {low_letters}')
print(' ')

print(f'Before: {cap_letters}')
cap_letters.sort()
print(f'Upper Sorted: {cap_letters}')
print(' ')

print(f'Before: {mix_letters}')
mix_letters.sort()
print(f'Mixed Sorted: {mix_letters}')
print(' ')

# Mixed Numbers and Letters
print("Lists can have a mix of letters and numbers, but you can't sort these lists. It will throw the following error: TypeError: '<' not supported between instances of 'int' and 'str'.")
