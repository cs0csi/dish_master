import random
from dishes_data import dishes

# User's available ingredients
available_ingredients = set()

# Set to store rejected ingredients for each dish
rejected_ingredients = {dish: set() for dish in dishes}

# Set to store excluded categories
excluded_categories = set()


def get_recommendation():
    global excluded_categories

    # Filter dishes based on available ingredients and excluded categories
    dish_options = [dish for dish in dishes.keys() if not any(
        ingredient in rejected_ingredients[dish] for ingredient in dishes[dish]['ingredients']) and dishes[dish]['category'] not in excluded_categories]

    if not dish_options:
        print("Sorry, no suitable dishes available based on your current restrictions.")
        return

    # Randomly choose a dish from the available options
    dish = random.choice(dish_options)
    print(f"Recommended dish: {dish}")

    # Display ingredients for the recommended dish
    ingredients = show_ingredients_info(dish)
    print(f"\nIngredients for {dish}:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"- {ingredient}")

    # Prompt user for suitability
    response = input("Is this suitable? (yes/no): ").lower()

    if response == "no":
        # Provide reasons for user rejection
        reason_options = [
            f"I would not like {dishes[dish]['category']} food now",
            f"There are no ingredients at home for the suggested {
                dishes[dish]['category']} dish",
        ]

        print("\nReason options:")
        for i, reason in enumerate(reason_options, start=1):
            print(f"{i}. {reason}")

        # Prompt user to choose a reason and handle accordingly
        reason_index = int(
            input("Choose a reason by entering its number (1, 2, etc.): ")) - 1
        reason = reason_options[reason_index]

        if reason == f"There are no ingredients at home for the suggested {dishes[dish]['category']} dish":
            update_rejected_ingredients(dish)
        elif reason == f"I would not like {dishes[dish]['category']} food now":
            excluded_categories.add(dishes[dish]['category'])
    # Inside get_recommendation() function, after asking if the dish is suitable
    elif response == "yes":
        response_side = input("Do you want any side dish? (yes/no): ").lower()
        if response_side == "yes":
            # Filter available side dishes
            side_dishes = [dish for dish in dishes.keys(
            ) if dishes[dish]['type'] == 'side_dish']

            if side_dishes:
                print("\nAvailable Side Dishes:")
                for i, side_dish in enumerate(side_dishes, start=1):
                    print(f"{i}. {side_dish}")

                chosen_side_dish = input(
                    "Choose a side dish (enter the number): ")
                print(f"You chose {
                      side_dishes[int(chosen_side_dish) - 1]} as a side dish.")
            else:
                print("No side dishes available.")

        response_soup = input("Do you want any soup? (yes/no): ").lower()
        if response_soup == "yes":
            # List all soups and let the user choose
            soups = [dish for dish in dishes.keys() if dishes[dish]
                     ['type'] == 'soup']
            print("\nAvailable Soups:")
            for i, soup in enumerate(soups, start=1):
                print(f"{i}. {soup}")

            chosen_soup = input("Choose a soup (enter the number): ")
            print(f"You chose {soups[int(chosen_soup) - 1]} as a soup.")


def show_ingredients_info(dish):
    all_ingredients = dishes[dish]['ingredients']
    return all_ingredients


def update_rejected_ingredients(dish):
    global rejected_ingredients

    all_ingredients = dishes[dish]['ingredients']

    # Display ingredients and prompt user to select rejected ones
    ingredients = show_ingredients_info(dish)
    print(f"\nIngredients for {dish}:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"[{i}] {ingredient}")

    # Prompt user to enter numbers of rejected ingredients
    rejected_indices_str = input(
        "Enter the numbers of ingredients not at home (comma-separated): ")

    # Convert user input into a list of indices
    rejected_indices = [
        int(index) - 1 for index in rejected_indices_str.split(",")]

    # Update rejected ingredients for the chosen dish
    rejected_ingredients[dish].update(
        all_ingredients[index] for index in rejected_indices)

    print(f"Rejected ingredients for {dish} updated: {
          rejected_ingredients[dish]}")


def main():
    while True:
        print("\n1. Get Dish Recommendation\n2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            get_recommendation()
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
