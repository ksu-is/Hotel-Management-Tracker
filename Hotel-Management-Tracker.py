#This is a coding system for hotel management from the guests' UI/UX 

#Hotel menus
brunch_menu = ["Pancakes", "Shrimp & Grits", "All-Star Breakfast", "Omelette"]
lunch_menu = ["Cesar Salad", "Club Snadwich", "1/3 lb. Beef Burger w/ Fries", "Fish Tacos"]
dinner_menu = ["Steak & Frites", "Fish & Chips", "1/3 lb. Beef Burger w/ Fries", "Short Ribs with Mashed Potatoes"]
appetizer_menu = ["Spinach & Artichoke Dip", "Pretzel Bites", "Garden Salad", "Hummus"]

#counter to keep track of rooms/lists
menu = []
rooms = []
attempts = 0
rooms_taken = 0
single_avail = 100
double_avail = 75
kings_avail = 50
suites_avail  = 25
date = []


#Opulent Oasis offers four types of rooms: Single Queen, Double Queen, King, and Suites
#Use "guest_name" for username and "guest_room" for password
guest_name = input("Please enter your first name and last intial: ")
guest_room = input("Please enter your room number: ")

#login
user_name = input("Enter username: ")
password = input("Enter password: ")
   
for entry in range(3):
    
    if user_name == guest_name and password == guest_room:
        access = input("Access Granted! Main Menu ''\n'' Enter "" 1"" for Check-in/out'\n' Enter ""2"" for Billing '\n' Enter ""3"" for Room Service '\n' Enter ""4"" for Booking \n' Enter ""5"" to Exit: ")
        attempts += 1
        break
    else:
        home = input("Access Denied, try again. Password: ")
        attempts += 1
    if attempts == 3:
        print("You have exceeded the amount of attempts allowed. Please try again later. Goodbye.")
        break
#charge customers accordingly based on room number
#
#if the room # is >= 100 count towards single, if the room # is >= 200 count towards double queen,if the room # is >= 300 count towards king,if the room # is >= 400 count towards suite
if access == "1":
   stay = input("Are you checking in or out")
      if stay == "checking in".capitalize or "in".capitalize
         stay = input("Please confirm the room number confirmed with your stay: ")
            if stay in rooms
               stay = input("That room number is not valid. Please try again.")

      if stay == "checking out".capitalize or "out".capitalize
          guest_room = input("Please confirm your room number: ")
            if stay in rooms
               stay = input("Thank you for confirming. You have successfully checked out. Please visit us again!")
          if guest_room >= 100 
              print("Thank you, your bill for a queen single is $125 and has been charged to your card. Thank you for staying at Opulet Oasis! Please come again!")
          if guest_room >= 200 
              print("Thank you, your bill for a queen double is $250 and has been charged to your card. Thank you for staying at Opulet Oasis! Please come again!")
          if guest_room >= 300
              print("Thank you, your bill for a king is $315 and has been charged to your card. Thank you for staying at Opulet Oasis! Please come again!")
         if guest_room >= 400
              print("Thank you, your bill for a suite is $405 and has been charged to your card. Thank you for staying at Opulet Oasis! Please come again!")


if access == "2":
   billing = input("Thank you, you have accessed our billing menu. Would you like to view your bill?")
   if billing == "yes".capiatlize
      billing = input("Please enter your room number: ")
if access == "3":
    menu = input("Which menu would you like to order from? For breakfast: enter 'B', for lunch: enter 'L', for dinner:  enter 'D',for appetizers: enter 'A': ")
   if menu.capitalize == "B":
                   print(brunch_menu)
                   order_brunch = input("What would the guest like to order?")
                   if order_brunch is in brunch_menu:
                      print("Thank you",guest_name, "! Your order:" ,order_brunch, "has been placed with an estimated arrival time of 15 minutes.")
                      
   if menu.capitalize == "L":
                   print(lunch_menu)
                   room = input("Please enter the room number you are currently staying in: ")
                   order_lunch = input("What would the guest like to order?")
                   if order_lunch is in lunch_menu:
                       print("Thank you",guest_name, "! Your order:" ,order_lunch, "has been placed with an estimated arrival time of 15 minutes. You have been billed for your order")
   
   if menu.capitalize == "D":
                   print(dinner_menu)
                   order_dinner = input("What would the guest like to order?")
                   if order_dinner is in dinner_menu:
                       print("Thank you",guest_name, "! Your order:" ,order_dinner, "has been placed with an estimated arrival time of 15 minutes. You have been billed for your order.") 
           
   if menu.capitalize == "D":
                   print(dinner_menu)
                   order_dinner = input("What would the guest like to order?")
                   if order_dinner is in dinner_menu:
                       print("Thank you",guest_name, "! Your order:" ,order_dinner, "has been placed with an estimated arrival time of 15 minutes. You have been billed for your order.") 
           
   if menu.capitalize == "A":
                   print(dinner_menu)
                   order_app = input("What would the guest like to order?")
                   if order_app is in appetizer_menu_menu:
                       print("Thank you",guest_name, "! Your order:" ,order_app, "has been placed with an estimated arrival time of 15 minutes. You have been billed for your order") 

if access == "4":
   date = input("Thank you for choosing to stay with Opulent Oasis. When would you check-in? (MM/DD/YY"))
   date_2 = input("Thank you for choosing to stay with Opulent Oasis. When would you check-out? (MM/DD/YY"))
   booking = input("Which type of room would you like to book? Enter Single, Double, King, or Suite")
   if booking == "Single"
         print("Thank you! You have booked with Opulent Oasis on:" , date, "to", date_2, ". We look forward to seeing you soon!")
         date = date.append()
         date_2 = date.append()
   if booking == "Double"
         print("Thank you! You have booked with Opulent Oasis on:" , date, "to", date_2, ". We look forward to seeing you soon!")
         date = date.append()
         date_2 = date.append()
   if booking == "Single"
         print("Thank you! You have booked with Opulent Oasis on:" , date, "to", date_2, ". We look forward to seeing you soon!")
         date = date.append()
         date_2 = date.append()
   if booking == "King"
            print("Thank you! You have booked with Opulent Oasis on:" , date, "to", date_2, ". We look forward to seeing you soon!")
            date = date.append()
            date_2 = date.append()
   if booking == "Suite"
            print("Thank you! You have booked with Opulent Oasis on:" , date, "to", date_2, ". We look forward to seeing you soon!")
            date = date.append()
            date_2 = date.append()
if access == "5":
   quit = input("Are you sure you want to quit? Enter 'yes' or 'no'")
      if quit == "no". capitalize():
         return access
      if quit == "yes". capitalize():
         print("You have ended the program. Thank you.")
      else: 
         quit = input("Entry invalid. Please enter 'yes' or 'no'")



   


         
        
        
