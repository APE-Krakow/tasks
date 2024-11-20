ingredients = {
    "ser": 2,
    "ananas": 3,
    "kukurydza": 7,
    "pomidor": 2,
    "brokuł": 3,
    "papryka": 100,
}
emojis = {
    "ser": "🧀",
    "ananas": "🍍",
    "kukurydza": "🌽",
    "pomidor": "🍅",
    "brokuł": "🥦",
    "papryka": "🌶️",
}

while True:
    pizza = "🍕"
    for ingredient in ingredients:
        if ingredients[ingredient] > 0:
            answer = input(f"Czy chcesz dodać {ingredient} do pizzy? T/n ")
            if answer != "n":
                ingredients[ingredient] -= 1
                pizza += emojis[ingredient]

    print("Oto twoja pizza" + pizza)
    decision = input("Czy chcesz przygotować następną? t/N ")
    if decision != "t":
        break
