import sys

if len(sys.argv) != 2:
    print("none")
else:
    expected_word = sys.argv[1]
    user_word = input("What was the parameter? ")
    
    if user_word == expected_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
