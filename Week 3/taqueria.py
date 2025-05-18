def main():
    total_amount = 0.0
    while True:
        try:
            total_amount += u_input()
            print(f"Total: ${total_amount:.2f}")
        except EOFError:
            print("\n")
            break


def u_input():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    while True:
        item = input("Item: ").title()
        if item in menu:
            return menu[item]
        else:
            continue

if __name__ == "__main__":
    main()
