import random
from dishes_data import dishes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# TELEGRAM START

TOKEN = '6080214194:AAHvBwONC54vgXBJc8Idvq33FJHrVsb2m8o'
BOT_USERNAME = Final = 'BAnanan'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your dish recommender. Type /recommend to get a dish recommendation.')


async def recommend_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global excluded_categories
    global max_preparation_time

    main_dish_options = [dish for dish in dishes.keys() if
                         dishes[dish]['type'] == 'main' and
                         not any(ingredient in rejected_ingredients[dish] for ingredient in dishes[dish]['ingredients']) and
                         dishes[dish]['category'] not in excluded_categories and
                         (max_preparation_time is None or dishes[dish]['preparation_time'] <= max_preparation_time)]

    if not main_dish_options:
        await update.message.reply_text(
            "Sorry, no suitable main dishes available based on your current restrictions.")
        return

    dish = random.choice(main_dish_options)

    # Extract ingredients and preparation time for the chosen dish
    ingredients = ", ".join(dishes[dish]['ingredients'])
    preparation_time = dishes[dish]['preparation_time']

    # Send a message to the user with the recommended main dish, ingredients, and preparation time
    keyboard = [[InlineKeyboardButton("Yes", callback_data='yes'),
                 InlineKeyboardButton("No", callback_data='no')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    message_text = (
        f"Recommended main dish: {dish}\n"
        f"Ingredients: {ingredients}\n"
        f"Preparation time: {preparation_time} minutes\n"
        "Is this suitable?"
    )

    await update.message.reply_text(message_text, reply_markup=reply_markup)


async def button_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_response = query.data

    if user_response == 'yes':
        # User accepted the recommendation
        await query.edit_message_text("Great! Enjoy your meal.")
        # Continue with the rest of the code as needed
    elif user_response == 'no':
        # User declined the recommendation
        await query.edit_message_text("Okay, let me find another option.")

        # Add your logic here to generate another recommendation
        # You can use the logic from get_recommendation or customize it as needed
        main_dish_options = [dish for dish in dishes.keys() if
                             dishes[dish]['type'] == 'main' and
                             not any(ingredient in rejected_ingredients[dish] for ingredient in dishes[dish]['ingredients']) and
                             dishes[dish]['category'] not in excluded_categories and
                             (max_preparation_time is None or dishes[dish]['preparation_time'] <= max_preparation_time)]

        if not main_dish_options:
            await query.edit_message_text("Sorry, no suitable main dishes available based on your current restrictions.")
            return

        dish = random.choice(main_dish_options)

        # Extract ingredients and preparation time for the chosen dish
        ingredients = ", ".join(dishes[dish]['ingredients'])
        preparation_time = dishes[dish]['preparation_time']

        # Send a message to the user with the recommended main dish, ingredients, and preparation time
        keyboard = [[InlineKeyboardButton("Yes", callback_data='yes'),
                     InlineKeyboardButton("No", callback_data='no')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        message_text = (
            f"Recommended main dish: {dish}\n"
            f"Ingredients: {ingredients}\n"
            f"Preparation time: {preparation_time} minutes\n"
            "Is this suitable?"
        )

        await query.edit_message_text(message_text, reply_markup=reply_markup)
        # await handle_rejection(dish)


""" async def handle_rejection(dish):
    response = input("Is this suitable? (yes/no): ").lower()

    if response == "no":
        reason_options = [
            f"I would not like {dishes[dish]['category']} food now",
            f"There are no ingredients at home for the suggested {
                dishes[dish]['category']} dish",
            f"I don't have that much time",
        ]

        print("\nReason options:")
        for i, reason in enumerate(reason_options, start=1):
            print(f"{i}. {reason}")

        reason_index = int(
            input("Choose a reason by entering its number (1, 2, etc.): ")) - 1
        reason = reason_options[reason_index]

        if reason == f"There are no ingredients at home for the suggested {dishes[dish]['category']} dish":
            update_rejected_ingredients(dish)
        elif reason == f"I don't have that much time":
            max_preparation_time = int(
                input("Enter the maximum preparation time you have (in minutes): "))
        elif reason == f"I would not like {dishes[dish]['category']} food now":
            excluded_categories.add(dishes[dish]['category'])

    elif response == "yes":
        response_side = input("Do you want any side dish? (yes/no): ").lower()
        side_dish = None

        if response_side == "yes":
            # Filter available side dishes
            side_dishes = [d for d in dishes.keys() if dishes[d]
                           ['type'] == 'side_dish']

            if side_dishes:
                print("\nAvailable Side Dishes:")
                for i, s_dish in enumerate(side_dishes, start=1):
                    print(f"{i}. {s_dish}")

                chosen_side_dish = input(
                    "Choose a side dish (enter the number): ")
                side_dish = side_dishes[int(chosen_side_dish) - 1]
                print(f"You chose {side_dish} as a side dish.")
            else:
                print("No side dishes available.")

        response_soup = input("Do you want any soup? (yes/no): ").lower()
        soup = None

        if response_soup == "yes":
            # List all soups and let the user choose
            soups = [d for d in dishes.keys() if dishes[d]['type'] == 'soup']
            print("\nAvailable Soups:")
            for i, s in enumerate(soups, start=1):
                print(f"{i}. {s}")

            chosen_soup = input("Choose a soup (enter the number): ")
            soup = soups[int(chosen_soup) - 1]
            print(f"You chose {soup} as a soup.")

        print(f"\nRecipe for {dish}:")
        print(dishes[dish]['recipe'])

        if side_dish:
            print(f"\nRecipe for {side_dish}:")
            print(dishes[side_dish]['recipe'])

        if soup:
            print(f"\nRecipe for {soup}:")
            print(dishes[soup]['recipe']) """


def handle_response(text: str) -> str:
    processed = text.lower()

    if 'hello' in processed:
        return 'Hello, how are you today?'
    elif 'bye' in processed:
        return 'Goodbye! Have a great day.'

    else:
        return 'I didnt understand that.'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f' User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


# TELEGRAM END

# User's available ingredients
available_ingredients = set()

# Set to store rejected ingredients for each dish
rejected_ingredients = {dish: set() for dish in dishes}

# Set to store excluded categories
excluded_categories = set()

# Set to store maximum preparation time the user can spend
max_preparation_time = None


def get_recommendation():
    global excluded_categories
    global max_preparation_time

    main_dish_options = [dish for dish in dishes.keys() if
                         dishes[dish]['type'] == 'main' and
                         not any(ingredient in rejected_ingredients[dish] for ingredient in dishes[dish]['ingredients']) and
                         dishes[dish]['category'] not in excluded_categories and
                         (max_preparation_time is None or dishes[dish]['preparation_time'] <= max_preparation_time)]

    if not main_dish_options:
        print(
            "Sorry, no suitable main dishes available based on your current restrictions.")
        return

    dish = random.choice(main_dish_options)
    print(f"Recommended main dish: {dish}")

    ingredients = show_ingredients_info(dish)
    print(f"\nIngredients for {dish}:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"- {ingredient}")

    print(f"Preparation time: {dishes[dish]['preparation_time']} minutes")

    response = input("Is this suitable? (yes/no): ").lower()

    if response == "no":
        reason_options = [
            f"I would not like {dishes[dish]['category']} food now",
            f"There are no ingredients at home for the suggested {
                dishes[dish]['category']} dish",
            f"I don't have that much time",
        ]

        print("\nReason options:")
        for i, reason in enumerate(reason_options, start=1):
            print(f"{i}. {reason}")

        reason_index = int(
            input("Choose a reason by entering its number (1, 2, etc.): ")) - 1
        reason = reason_options[reason_index]

        if reason == f"There are no ingredients at home for the suggested {dishes[dish]['category']} dish":
            update_rejected_ingredients(dish)
        elif reason == f"I don't have that much time":
            max_preparation_time = int(
                input("Enter the maximum preparation time you have (in minutes): "))
        elif reason == f"I would not like {dishes[dish]['category']} food now":
            excluded_categories.add(dishes[dish]['category'])
    # Inside get_recommendation() function, after asking if the dish is suitable
    elif response == "yes":
        response_side = input("Do you want any side dish? (yes/no): ").lower()
        side_dish = None

        if response_side == "yes":
            # Filter available side dishes
            side_dishes = [d for d in dishes.keys() if dishes[d]
                           ['type'] == 'side_dish']

            if side_dishes:
                print("\nAvailable Side Dishes:")
                for i, s_dish in enumerate(side_dishes, start=1):
                    print(f"{i}. {s_dish}")

                chosen_side_dish = input(
                    "Choose a side dish (enter the number): ")
                side_dish = side_dishes[int(chosen_side_dish) - 1]
                print(f"You chose {side_dish} as a side dish.")
            else:
                print("No side dishes available.")

        response_soup = input("Do you want any soup? (yes/no): ").lower()
        soup = None

        if response_soup == "yes":
            # List all soups and let the user choose
            soups = [d for d in dishes.keys() if dishes[d]['type'] == 'soup']
            print("\nAvailable Soups:")
            for i, s in enumerate(soups, start=1):
                print(f"{i}. {s}")

            chosen_soup = input("Choose a soup (enter the number): ")
            soup = soups[int(chosen_soup) - 1]
            print(f"You chose {soup} as a soup.")

        print(f"\nRecipe for {dish}:")
        print(dishes[dish]['recipe'])

        if side_dish:
            print(f"\nRecipe for {side_dish}:")
            print(dishes[side_dish]['recipe'])

        if soup:
            print(f"\nRecipe for {soup}:")
            print(dishes[soup]['recipe'])


def show_ingredients_info(dish):
    all_ingredients = dishes[dish]['ingredients']
    return all_ingredients


def update_rejected_ingredients(dish):
    global rejected_ingredients

    all_ingredients = dishes[dish]['ingredients']

    ingredients = show_ingredients_info(dish)
    print(f"\nIngredients for {dish}:")
    for i, ingredient in enumerate(ingredients, start=1):
        print(f"[{i}] {ingredient}")

    rejected_indices_str = input(
        "Enter the numbers of ingredients not at home (comma-separated): ")
    rejected_indices = [
        int(index) - 1 for index in rejected_indices_str.split(",")]

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
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    # Add this line for the new command
    app.add_handler(CommandHandler('recommend', recommend_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(button_response))

    print('polling...')

    app.run_polling(poll_interval=3)
