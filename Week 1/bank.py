#get the greeting from the user.
greet = input("Greeting: ")
greet = greet.strip().lower()
#if the greeting is Hello no compensation.
if greet.startswith("hello"):
    print("$0")
#if the greeting starts from H the $20.
elif greet.startswith("h"):
    print("$20")
#for anything else its $100.
else:
    print("$100")