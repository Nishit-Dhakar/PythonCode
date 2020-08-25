a=5
b=0

try:
    b = int(input("Enter a number"))
    print(a/b)
except Exception as e:
    print("Hey, you can't divide by zero")
    print(e.__str__())
except ValueError as e:
    print(e.__str__())
except FileNotFoundError as e:
    print(e.__str__())

finally:
    print("Happy with what you entered?")