from caci import code

code_inverse = {value: key for key, value in code.items()}

while True:
  print("1. Text to Morse\n2. Morse to text\n")
  y = int(input("Enter your choice: "))

  if y == 1:
    def morse(string):
      str = ""
      for letter in string:
        str += code[letter] + ' '
      return str
    print(morse(input("Enter a string: ").upper()))

  elif y == 2:
    x = input("Enter a string: ").split()
    for item in x:
      print(code_inverse[item], end="")
    print()

  x = input("Do you want to run again? (Yes/No): ").lower()
  if x != "yes":
    break
