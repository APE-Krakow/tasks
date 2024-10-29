plants = [
    "Aloe Vera", "Snake Plant", "Spider Plant", "Peace Lily", "ZZ Plant", 
    "Monstera Deliciosa", "Pothos", "Philodendron", "Rubber Plant", "Bird's Nest Fern", 
    "Boston Fern", "Chinese Money Plant", "Jade Plant", "Fiddle Leaf Fig", "Areca Palm", 
    "Dracaena", "Calathea", "Peperomia", "Dieffenbachia", "English Ivy", 
    "Cast Iron Plant", "Swiss Cheese Plant", "Croton", "String of Pearls", "Elephant Ear", 
    "Dumb Cane", "Oxalis", "Heartleaf Philodendron", "Golden Pothos", "Anthurium", 
    "Prayer Plant", "Air Plant", "Hoya", "Kentia Palm", "Christmas Cactus", 
    "Dwarf Banana Plant", "Rex Begonia", "Asparagus Fern", "Bromeliad", "Zebra Plant", 
    "Umbrella Plant", "Arrowhead Plant", "African Violet", "Maranta", "Parlor Palm", 
    "Rubber Tree", "Lady Palm", "Alocasia", "Chinese Evergreen", "Kalanchoe", 
    "Silver Queen", "Lucky Bamboo", "Peace Lily", "Variegated Rubber Plant", "Bird of Paradise", 
    "Moth Orchid", "Corn Plant", "Guzmania", "Lipstick Plant", "Golden Barrel Cactus", 
    "Crown of Thorns", "Baby Rubber Plant", "Silver Satin Pothos", "Rattlesnake Plant", 
    "Echeveria", "Pilea", "Spiderwort", "Ming Aralia", "Succulent Mix", 
    "Fatsia Japonica", "Indian Fern", "Yucca", "Flamingo Lily", "Fishbone Cactus", 
    "Desert Rose", "Split Leaf Philodendron", "Golden Cane Palm", "Blue Star Fern", 
    "Coral Cactus", "White Bird of Paradise", "Senecio", "Money Tree", "Snake Plant Laurentii", 
    "Chinese Fan Palm", "Velvet Leaf Philodendron", "Chain of Hearts", "Silver Nerve Plant", 
    "Staghorn Fern", "Purple Passion Plant", "String of Bananas", "Kangaroo Paw Fern", 
    "Wax Plant", "Grape Ivy", "Watermelon Peperomia", "Olive Plant", 
    "Crassula Ovata", "Tiger Aloe", "Arrowhead Vine", "Moses in the Cradle", 
    "Pink Anthurium", "Green Shamrock Plant", "Dwarf Umbrella Tree", "Sago Palm"
]

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

plants = [plant.lower() for plant in plants]

plants_for_a_number = len([plant for plant in plants if plant[0] == 'a'])
print(f"Na liście roślin jest {plants_for_a_number} roślin na literę a.")

plants_for_vowel = [plant for plant in plants if plant[0] in vowels]
print("Rośliny których nazwa zaczyna się od samogłoski:")
print(sorted(plants_for_vowel))

biggest_length = 0
longest_name = ""

for plant in plants:
    if len(plant) > biggest_length:
        biggest_length = len(plant)
        longest_name = plant
print(f"Roślina o najdłuższej nazwie to {longest_name}.")

tested_plant = input("Podaj nazwę rośliny\n")
if tested_plant in plants:
    print("Twoja roślina znajduje się na liście")
else:
    print("Twojej rośliny nie ma na liście")
