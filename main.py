import random

# Sample data
dishes = {
    "Spaghetti Bolognese": {
        "ingredients": ["pasta", "minced meat", "tomato sauce", "onion", "garlic"],
        "category": "savory"
    },
    "Chicken Stir-Fry": {
        "ingredients": ["chicken", "vegetables", "soy sauce", "ginger"],
        "category": "savory"
    },
    "Chocolate Cake": {
        "ingredients": ["flour", "sugar", "chocolate", "eggs", "butter"],
        "category": "sweet"
    },
    "Caesar Salad": {
        "ingredients": ["lettuce", "chicken", "croutons", "parmesan", "Caesar dressing"],
        "category": "savory"
    },
    "Fruit Salad": {
        "ingredients": ["apple", "banana", "grapes", "orange", "honey"],
        "category": "sweet"
    },
    "Grilled Salmon": {
        "ingredients": ["salmon", "lemon", "olive oil", "herbs", "garlic"],
        "category": "savory"
    },
    "Pancakes": {
        "ingredients": ["flour", "milk", "eggs", "baking powder", "maple syrup"],
        "category": "sweet"
    },
    "Mushroom Risotto": {
        "ingredients": ["arborio rice", "mushrooms", "onion", "white wine", "parmesan"],
        "category": "savory"
    },
    "Cheesecake": {
        "ingredients": ["cream cheese", "sugar", "eggs", "vanilla extract", "graham cracker crust"],
        "category": "sweet"
    },
    "Caprese Salad": {
        "ingredients": ["tomatoes", "mozzarella", "basil", "balsamic glaze", "olive oil"],
        "category": "savory"
    }
    # Add more dishes and their ingredients with categories
}

# User's available ingredients
available_ingredients = set()

# Set to store rejected ingredients for each dish
rejected_ingredients = {dish: set() for dish in dishes}


def get_recommendation():
    dish_options = [dish for dish in dishes.keys() if not any(
        ingredient in rejected_ingredients[dish] for ingredient in dishes[dish]['ingredients'])]
    if not dish_options:
        print("Sorry, no suitable dishes available based on your current restrictions.")
        return

    dish = random.choice(dish_options)
    print(f"Recommended dish: {dish}")
    response = input("Is this suitable? (yes/no): ").lower()

    if response == "no":
        reason_options = [
            "I don't have sweet food",
            "I would not like savory food now",
            "There are no ingredients at home for the suggested dish",
            # Add more predefined reasons
        ]

        print("\nReason options:")
        for i, reason in enumerate(reason_options, start=1):
            print(f"{i}. {reason}")

        reason_index = int(
            input("Choose a reason by entering its number (1, 2, etc.): ")) - 1
        reason = reason_options[reason_index]

        if reason == "There are no ingredients at home for the suggested dish":
            show_ingredients_info(dish)
            update_rejected_ingredients(dish)


def show_ingredients_info(dish):
    print(f"\nIngredients for {dish}:")
    for i, ingredient in enumerate(dishes[dish]['ingredients'], start=1):
        print(f"[{i}] {ingredient}")

    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(available_ingredients, start=1):
        print(f"[{i}] {ingredient}")

    print(f"\nCategory: {dishes[dish]['category']}")


def update_rejected_ingredients(dish):
    global rejected_ingredients

    all_ingredients = dishes[dish]['ingredients']
    rejected_indices = input(
        "Enter the numbers of ingredients not at home (comma-separated): ").split(", ")
    rejected_ingredients[dish].update(
        all_ingredients[int(index) - 1] for index in rejected_indices)

    print(f"Rejected ingredients for {dish} updated: {
          rejected_ingredients[dish]}")


def update_available_ingredients():
    global available_ingredients
    print("Update available ingredients:")
    for ingredient in dishes.values():
        available = input(
            f"Is {ingredient['ingredients']} available? (yes/no): ").lower()
        if available == "yes":
            available_ingredients.add(ingredient['ingredients'])


def main():
    while True:
        print("\n1. Get Dish Recommendation\n2. Update Ingredient Availability\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            get_recommendation()
        elif choice == "2":
            update_available_ingredients()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
