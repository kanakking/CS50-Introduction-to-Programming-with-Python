#take the input from the user.
fruit = input("item: ")
# we will make a dictionary with all it's keys and value, where key's are fruit and values are calories.
fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "water melon": "80"
    }
#Now we take the input from the user on whose calorie they want to know about
if fruit.lower() in fruits:
    print(f"Calories: {fruits[fruit.lower()]}")
