class Animal:
    def __init__(self, name):
        self.name = name    # public attribute
        self._species = "pig"     # "protected" attribute
        self.__accommodation = "barn" # "private" attribute


wilbur = Animal("Wilbur")
print(wilbur.name)      # Output: Wilbur
print(wilbur._species)  # Output: pig

print(wilbur.__accommodation)   # AttributeError: 'Animal' object has no attribute '__accommodation'

print(wilbur.__dict__)  # Output: {'name': 'Wilbur', '_species': 'pig', '_Animal__accommodation': 'barn'}
print(wilbur._Animal__accommodation)    # Output: barn