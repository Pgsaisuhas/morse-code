from caci import code, code_inverse
run = True
while run:
    print("\nHey welcome!, to Morse encoder/decoder:\n1.Text to Morse\n2.Morse to text\n")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1: 

            def morse(string):
                str = ""
                for letters in string:
                    str = str + code[letters] + " "
                return str

            print(morse(input("enter a string: ").upper()))

        case 2:

            x = input("Enter the morse string: ").split()
            # print(x)
            y = ""
            for item in x:
                y = y+ code_inverse[item] 
            print(y, end="")
            print()
        
    runAgain = input("Do you want to run again?(Yes/No): ").lower()
    if runAgain == "yes":
        run = True
    else:
        run = False
