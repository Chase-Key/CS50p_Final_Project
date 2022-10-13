# Automated Ordering System for Coffee Shop
#### Video Demo:  <https://youtu.be/HrBX4G--21k>
#### Description:

This project acts as an ordering system for a coffee shop. You will be brought to a main menu, then from the user's input, decide what drink, side, and quantities of each that you would like to order. Once the user is finished deciding their order, they will then be able to checkout. The checkout function will print a receipt that displays accumulated total with tax and current time/date.

Libraries used:

- sys
- tabulate
- zoneinfo
- datetime

## How the project works?

Once the program runs, it brings you to a welcome screen. From that welcome screen, the user is then able to navigate either to the main menu, sides menu, or checkout screen. When viewing the main menu the user has the option to enter a order number, which corresponds to the type of coffee drink they would like to order, then the user is prompted to enter the amount they want for that specific drink. The user can order up to a maximum of 5 drinks of each specific item per customer. Once the user is done deciding which type of coffee drink they would like and quantity they want, the user can then navigate to a sides menu or to the checkout. In the sides menu, there are five different sides the user can choose from by entering a specific order number and then choosing the quantity of that item, 5 max per customer per item. When the user decides they are done ordering they can navigate to the checkout from the sides menu or navigate back to the main menu if they decide they want another drink. Once the checkout is enabled, a receipt with the total drink amount, sides amount, total price, price with tax, and date/time is outputted.

## Files contained within the project folder:

- project.py
- test_project.py
- store_menu.csv
- extras_menu.csv
- README.md
- requirements.txt

There are 6 files contained inside the project folder, including the project itself. The project.py file contains the program you will run, which is explained above. The test_project.py file uses pytest to test multiple functions within the project.py file. The store_menu.csv file contains the order number, name of each drink, and the price for each drink that the user can order from. The extras_menu.csv file contains the order number, name of each side, and the price for each side that the user can order. Both the main_menu and extras_menu is tabulated into a table format for the user. The README.md file contains the markdown script for the project. The requirements.txt file displays each library that is used for the project.

## Design decisions:

I chose to create each menu in a seperate .csv file so I could tabulate each menu in the effort of making each menu more user-friendly for the user to make choices. When writing the program, my functions do not take arguments, instead I imagined each function as a seperate section the user navigates to and within each section the user is able to stay and continue to make choices, until the user decides to move on. I chose to use integers for the user input to correspond to order numbers based on each menu. If the user does not input an integer, or inputs an integer out-of-range of the order numbers, the user is prompted to re-enter their choice.

### Thank you!