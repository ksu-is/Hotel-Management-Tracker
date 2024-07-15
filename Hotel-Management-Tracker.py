attempts = 0
brunch_menu = ["Pancakes", "Shrimp & Grits", "All-Star Breakfast", "Omelett"]
lunch_menu = ["Cesar Salad", "Club Snadwich", "1/3 lb. Beef Burger w/ Fries", "Fish Tacos"]
dinner_menu = ["Steak & Frites", "Fish & Chips", "1/3 lb. Beef Burger w/ Fries", "Short Ribs with Mashed Potatoes"]
appetizer_menu = ["Spinach & Artichoke Dip", "Pretzel Bites", "Garden Salad", "Hummus"]


user_name = input("Enter username: ")
password = input("Enter password: ")
    
for entry in range(3):
    
    if user_name == "hotel_admin" and password == "Opulent Oasis":
        access= input("Access Granted! Main Menu ''\n'' Enter "" 1"" for Billing '\n' Enter ""2"" for Check-in '\n' Enter ""3"" for Room Service: ")
        attempts += 1
        break
    else:
        access = input("Access Denied, try again. Password: ")
        attempts += 1
    if attempts == 3:
        print("You have exceeded the amount of attempts allowed. Please try again later. Goodbye.")
        break
if access == "1":
    billing = input("What room type do you want to bill?")
if access == "3":
    menu_? = input("Which menu would you like to order from? For breakfast: enter 'B', for lunch: enter 'L', for dinner:  enter 'D',for appetizers: enter 'A'")
        if menu_?.capitalize = "B"
            print(brunch_menu)
 
        
