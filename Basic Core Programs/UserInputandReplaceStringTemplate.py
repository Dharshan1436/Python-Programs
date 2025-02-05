def input_and_replace():
    name = input("Enter your name (minimum 3 characters): ")
    while len(name) < 3:
        name = input("Name must have at least 3 characters. Please re-enter: ")
    print(f"Hello {name}, How are you?")
input_and_replace()