#ask the user for What is the Answer to the Great Question of Life, the Universe, and Everything?
ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
fans = ans.strip().lower()
#get the output from the user.
if fans == "42" or fans == "forty-two" or fans == "forty two":
#the answer should be 42 only, could be in any form but should be 42 only.
    print("Yes")
else:
#for anything other than 42 print No.
    print("No")