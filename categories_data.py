"""
Contains the predefined categories, templates and descriptions for the dataset generator.
Separating this data makes the main script more maintainable and easier to update.
"""

CATEGORIES = [
    "Python Basics",
    "Pythonic Logic", 
    "Testing and Debugging",
    "Data Structures",
    "Algorithmic Thinking",
    "Python Libraries"
]

PROMPT_TEMPLATES = {
    "Python Basics": [
        "How can I sort a list in Python?",
        "How do I create a class in Python?",
        "How do I handle exceptions in Python using try and except?",
        "What is the difference between a tuple and a list in Python?",
        "How do I work with strings in Python?",
        "What are Python's built-in data types?",
        "How do I use if-else statements in Python?",
        "How do I write a for loop in Python?",
        "What is the purpose of the __init__ method?",
        "How do I read and write files in Python?"
    ],
    "Pythonic Logic": [
        "How can I use a list comprehension to filter even numbers from a list?",
        "What is a decorator in Python?",
        "How can I merge two dictionaries in Python?",
        "How do I use list slicing to reverse a list in Python?",
        "What are generator expressions in Python?",
        "How do I use the ternary operator in Python?",
        "What is the difference between map() and filter()?",
        "How do I use *args and **kwargs?",
        "What are context managers in Python?",
        "How do I implement method chaining?"
    ],
    "Testing and Debugging": [
        "How can I test a Python function using unittest?",
        "How do I debug a Python script?",
        "What is the purpose of logging in Python?",
        "How can I measure the execution time of a Python function?",
        "What is test-driven development in Python?",
        "How do I use pytest fixtures?",
        "What is mocking in Python testing?",
        "How do I use the Python debugger (pdb)?",
        "What are assertion statements used for?",
        "How do I profile Python code performance?"
    ],
    "Data Structures": [
        "How do I use a stack in Python?",
        "How can I implement a queue in Python?",
        "What is a dictionary comprehension?",
        "How do I create and use a set in Python?",
        "What is a linked list in Python?",
        "How do I implement a binary tree?",
        "What are Python's built-in data structures?",
        "How do I use defaultdict from collections?",
        "What is the difference between lists and tuples?",
        "How do I implement a hash table?"
    ],
    "Algorithmic Thinking": [
        "How do I write a function that returns the factorial of a number?",
        "How do I implement a binary search algorithm in Python?",
        "How do I find the greatest common divisor (GCD) in Python?",
        "How can I optimize a sorting algorithm?",
        "How do I implement merge sort?",
        "What is dynamic programming in Python?",
        "How do I solve the fibonacci sequence?",
        "How do I implement breadth-first search?",
        "What is the time complexity of common operations?",
        "How do I implement depth-first search?"
    ],
    "Python Libraries": [
        "What is the use of the map() function in Python?",
        "How do I use the pandas library to manipulate data?",
        "How can I use the requests library in Python?",
        "What is the purpose of the itertools module?",
        "How do I use numpy arrays?",
        "What is the datetime module used for?",
        "How do I use regular expressions in Python?",
        "What is the purpose of the collections module?",
        "How do I use the json module?",
        "What is the sqlite3 module used for?"
    ]
}

DESCRIPTIONS = {
    "Python Basics": "Fundamental Python concepts including basic syntax, data types, control structures, functions, and file operations.",
    "Pythonic Logic": "Advanced Python programming practices focusing on idiomatic code, efficiency, and language-specific features.",
    "Testing and Debugging": "Methods and tools for testing Python code, debugging issues, and ensuring code quality.",
    "Data Structures": "Implementation and usage of various data structures in Python, from built-in types to custom implementations.",
    "Algorithmic Thinking": "Problem-solving approaches, algorithm implementation, and optimization techniques in Python.",
    "Python Libraries": "Usage and understanding of Python's standard library and popular third-party packages."
}
