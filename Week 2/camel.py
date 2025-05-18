def main():
    #here we will just take input from the user.
    c_case = input("camelCase : ")
    #suppose i have a function that canverts came case to snake case.
    snake_case(c_case)


def snake_case(c_case):
    snake_case = ""
    for c in c_case:
         #program it in such a way that it identifies the capital letter in the string and appends it with _ and lower() the character.
         if c.isupper():
            snake_case += "_" + c.lower()
         else:
            snake_case += c

    print("snake_case: ", snake_case)



if __name__ == "__main__":
    main()
