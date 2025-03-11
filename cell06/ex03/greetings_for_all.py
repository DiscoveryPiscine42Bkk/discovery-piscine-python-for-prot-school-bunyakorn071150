# Define the greetings method
def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

# Test the method with different arguments
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
