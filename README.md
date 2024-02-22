# Dish Recommendation Console App

This is a simple Python console application that recommends dishes based on your available ingredients and preferences. The program allows you to get dish recommendations, update ingredient availability, and exit the application.

## Features

- **Get Dish Recommendation:** Receive a random dish recommendation based on your available ingredients and preferences.
- **Update Ingredient Availability:** Update the list of available ingredients for more accurate recommendations.
- **Exit:** Close the application.

## How to Use

1. **Run the Program:**
   - Make sure you have Python installed on your machine.
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the command: `python your_script_name.py`

2. **Menu Options:**
   - **Get Dish Recommendation (Option 1):** Receive a random dish recommendation. Follow the prompts to accept or reject the recommendation.
   - **Update Ingredient Availability (Option 2):** Update the availability of ingredients in your kitchen.
   - **Exit (Option 3):** Close the application.

3. **Accept/Reject Recommendations:**
   - If a recommended dish is suitable, enter "yes."
   - If not suitable, enter "no" and choose a reason from the provided options.

4. **Update Ingredient Availability:**
   - Enter "2" to update ingredient availability.
   - Follow the prompts to indicate which ingredients are available.

## Additional Notes

- The program considers your available ingredients and preferences to provide suitable recommendations.
- Preferences include whether you want sweet or savory dishes.
- If a dish is rejected due to missing ingredients, it will be excluded from future recommendations in the same session.
- Restarting the program resets the exclusion list.

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests. Your feedback and ideas are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
