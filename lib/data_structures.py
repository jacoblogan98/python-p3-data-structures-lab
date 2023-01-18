spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [obj["name"] for obj in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [obj for obj in spicy_foods if obj["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for obj in spicy_foods:
        print(obj["name"] + " (" + obj["cuisine"] + ") | Heat Level: " + '🌶' * obj["heat_level"])

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for obj in spicy_foods:
        if obj["cuisine"] == cuisine:
            return obj

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    average = 0
    for food in spicy_foods:
        average += food["heat_level"]
    
    return average / len(spicy_foods)
