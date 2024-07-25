from os import rmdir
from typing import runtime_checkable

#This is a coding system for hotel management from the guests' UI/UX

#defining room numbers/price

import random
rooms_1 = [101,102,103,104,105]
rooms_2 = [201,202,203,204,205]
rooms_3 = [301,302,303,304,305]
rooms_4 = [401,402,403,404,405]

guest = ""
rm_bill = 0
food_bill = 0
fin_bill = 0


#def booking
def booking(guest):
    print("We offer the following rooms: ")
    print("1. Single: $150/night")
    print("2. Double: $200/night")
    print("3. King: $275/night")
    print("4. Suite: $315/night")




    guest_room = int(input("Please choose the number that correlates with room type:"))
    nights = int(input("How many nights would you like to stay?: "))

    if(guest_room == 1):
      rm_bill = 150*nights
      check_name.append(guest_name)
      print("Thank you", check_name, "! You have booked a single. You will be billed $", rm_bill ,"at the end of your stay. We look forward to hosting you.")
      print("Your room number is: ",random.choice(rooms_1), ".")
    elif(guest_room == 2):
     check_name.append(guest_name)
     rm_bill = 200*nights
     print("Thank you", check_name, "! You have booked a double. You will be billed $",rm_bill,"at the end of your stay. We look forward to hosting you.")
     print("Your room number is: ",random.choice(rooms_2), ".")

    elif(guest_room == 3):
      check_name.append(guest_name)
      rm_bill = 275*nights
      print("Thank you", check_name, "! You have booked a king. You will be billed $",rm_bill,"at the end of your stay. We look forward to hosting you.")
      print("Your room number is: ",random.choice(rooms_3), ".")


    elif(guest_room == 4):
      check_name.append(guest_name)
      rm_bill = 315*nights
      print("Thank you", check_name, "! You have booked a suite. You will be billed $",rm_bill, "at the end of your stay. We look forward to hosting you.")
      print("Your room number is: ",random.choice(rooms_4), ".")


    else:
      guest_room = input("Invaild entry. Please try again: ")

def check_in_out():
    stay = input("Are you checking in or out: ")
    if stay == "in":
       name = input("Please confirm the name used in booking: ")
       if name in check_name:
          name = check_name.append(name)
          print("Thank you. You have succesfully checked in.")
       else:
          print("Please book first before checking in.")

    elif(stay == "out"):
         name = input("Please confirm the name used in booking: ")
         if name in check_name:
            print("Thank you. You have succesfully checked out.You have been billed",bill,". Please come and visit us again!")
         else:
            name = input("We're sorry. That name has not been checked in yet. Please try checking in or booking first.")



def room_service():
  order = input("Hello" + " " + guest_name + " " + "! What menu would you like to order from? ''\n'' Enter "" A"" for Appetizers '\n' Enter ""B"" for Brunch '\n' Enter ""L"" for Lunch '\n' Enter ""D"" for Dinner \n' Enter ""Dessert"" for Dessert \n' Enter ""Cancel"" to cancel order: ")

  if (order == "A"):
      food_bill = 10
      print("Thank you",guest_name, "! We have recieved your order. It will be delivered in about 15-20 minutes. You have been billed $",food_bill, ". We hope you enjoy!")


  elif(order == "B"):
      food_bill = 15
      print("Thank you",guest_name, "! We have recieved your order. It will be delivered  in about 15-20 minutes. You have been billed $",food_bill, ". We hope you enjoy!")

  elif(order == "L"):
      food_bill = 20
      print("Thank you",guest_name, "! We have recieved your order. It will be delivered in about 15-20 minutes. You have been billed $",food_bill, ". We hope you enjoy!")

  elif(order == "D"):
      food_bill = 25
      print("Thank you",guest_name, "! We have recieved your order. It will be delivered in about 15-20 minutes. You have been billed $",food_bill, ". We hope you enjoy!")

  elif(order == "Dessert"):
      food_bill = 10
      print("Thank you",guest_name, "! We have recieved your order. It will be delivered in about 15-20 minutes. You have been billed $",food_bill, ". We hope you enjoy!")

  elif(order == "Cancel"):
      quit = input("You have canceled your order.")
      pass

  else:
    invalid = input("We're sorry, that is not available please try again.")



def billing():
  print ("Room Total: $",rm_bill)
  print ("Food Service Total: $",food_bill)
  fin_bill = rm_bill + food_bill
  print("Your total is: $",fin_bill, ". You will be charged at the end of your stay.")



brunch = ""
lunch = ""
dinner = ""
app = ""
dessert = ""
guest_name = []
check_name =[]

#counter to keep track of rooms/lists

#Opulent Oasis offers four types of rooms: Single, Double Queen, King, and Suites
while True:
  guest_name = input("Please enter your first name and last intial: ")
  access = input("Hello" + " " + guest_name + " " + "! What action would you like to do? Main Menu: ''\n'' Enter "" 1"" for Check-in/out'\n' Enter ""2"" for Billing '\n' Enter ""3"" for Room Service '\n' Enter ""4"" for Booking \n' Enter ""5"" to Exit: ")

#if the room # is >= 100 count towards single, if the room # is >= 200 count towards double queen,if the room # is >= 300 count towards king,if the room # is >= 400 count towards suite
  if access == "1":
    check_in_out()

  elif access == "2":
    billing()

  elif access == "3":
    room_service()

  elif access == "4":
    booking(guest)

  elif access == "5":
    quit = input("Are you sure you want to quit? Enter yes or no: ")
    if quit == "no":
      print(access)

    if quit == "yes":
      print("You have ended the program.")
      break
 







         
        
        
