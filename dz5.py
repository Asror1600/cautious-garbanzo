squares = [x**2 for x in range(1, 11)]

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

strings = ['hello', 'world', 'list', 'comprehension']
lengths = [len(s) for s in strings]

numbers = [1, 2, 3, 4, 4, 5, 5, 5, 6]
unique_numbers = list(set(numbers))

threshold = 10
numbers = [1, 2, 3, 15, 20, 5, 12]
filtered_numbers = [x for x in numbers if x > threshold]


words = ['hello', 'world', 'list', 'comprehension']
first_letters = [word[0] for word in words]


squares_of_evens = [x**2 for x in range(1, 11) if x % 2 == 0]