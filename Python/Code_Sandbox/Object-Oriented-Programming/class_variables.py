class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Bob', 'Jones', 40000)
emp2 = Employee('Susan', 'Smith', 50000)
emp3 = Employee('Kelly', 'Stone', 60000)

print('Before Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}')
print(f'{emp2.fullname()} pay: {emp2.pay}')
print(f'{emp3.fullname()} pay: {emp3.pay}')
print(' ')

# Set individual raise amount
emp1.raise_amount = 1.03
emp2.raise_amount = 1.05
emp3.raise_amount = 1.04

# End of year raise
emp1.apply_raise()
emp2.apply_raise()
emp3.apply_raise()

print('After Raise:')
print(f'{emp1.fullname()} pay: {emp1.pay}')
print(f'{emp2.fullname()} pay: {emp2.pay}')
print(f'{emp3.fullname()} pay: {emp3.pay}')