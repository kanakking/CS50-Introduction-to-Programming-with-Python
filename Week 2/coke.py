#assume he already ordered the coke now the due amount becomes 50 cents
d_amount = 50
print("Amount Due:", d_amount)

while d_amount > 0:
    i_coin = int(input("Insert Coin: "))

    # Check if the coin is valid (nickels, dimes, quarters)
    if i_coin in [5, 10, 25]:
        d_amount -= i_coin

        # If there's still an amount due, print it
        if d_amount > 0:
            print("Amount Due:", d_amount)
        else:
            # If the amount due is less than zero, print change owed
            print("Change Owed:", abs(d_amount))
    else:
        print("Amount Due:", d_amount)