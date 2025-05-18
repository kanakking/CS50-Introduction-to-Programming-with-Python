def main():
    level = lvl()
    print(level)

def lvl():
    fraction = fract()
    if fraction <= 1:
        return "E"
    elif fraction >= 99:
        return "F"
    else:
        return f"{fraction:.0f}%"

def fract():
    while True:
        try:
            frac = input("Fraction: ")
            x,y = map(int, frac.split("/"))
            if x > y:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            fracti = x/y * 100
            return fracti
        except (ValueError, ZeroDivisionError):
            pass



if __name__ == "__main__":
    main()
