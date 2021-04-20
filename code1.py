print("""
************** ------------------ **************

            WELCOME TO OUR RESTURANT
            
************** ------------------ **************         

Please take a look at our menu and place your order:
  
  _________________________________________________
  | S/No.  | Items               | Price per item |
  |________|_____________________|________________|
  | 1.     | Coke                | 1.50           |
  | 2.     | Sprite              | 1.50           |
  | 3.     | Water               | 1.00           |
  | 4.     | Ham Burger          | 4.00           |
  | 5.     | Cheese Burger       | 5.00           |
  | 6.     | Hotdog              | 3.00           |
  | 7.     | Fries               | 2.50           |
  | 8.     | Cheese Fries        | 3.50           |
  |________|_____________________|________________|
  
  
""")
serial_list = [1,2,3,4,5,6,7,8]
items_list = ["Coke", "Sprite", "Water", "Ham Burger", "Cheese Burger", "Hot dog","Fries", "Cheese Fries"]
price_list = [1.50, 1.50, 1.00, 4.00, 5.00, 3.00, 2.50, 3.50]

items_selected = []
selected_item_nums = []
items_total_price = []

state = True
while state: 
  user_choice = int(input("Please enter S/No. of the item of your choice: "))
  while user_choice < serial_list[0] or user_choice > serial_list[-1]:
    print("Entered S/No. not in menu, please try again.")
    user_choice = int(input("Please enter S/No. of the item of your choice: "))
  num = int(input(f"Please enter the quantity of {items_list[user_choice-1]} you want to order(in numbers): "))
  print(f"{items_list[user_choice-1]} order accepted.")
  print()
  print("Do you want to order something else? ")
  print("Enter 'Y' to choose anything else, 'n' to print the receipt and place the order.")
  
  item = items_list[user_choice-1]
  item_price = num * price_list[user_choice-1]
  items_selected.append(item)
  selected_item_nums.append(num)
  items_total_price.append(item_price)
  
  choice = input("Y/n? ")
  while not (choice == "Y" or choice == "n"):
    choice = input("Y/n? ")
  if choice == "Y":
    state = True
  elif choice == "n":
    state = False
    
print()
print("------------------------------")
print("Itemized Order List Receipt")
print("------------------------------")
print()
for i in range(len(items_selected)):
  print(f'{items_selected[i]} - {selected_item_nums[i]} items - Price: {items_total_price[i]} ')
print()
print("------------------------------")
print()
print(f'Total number of items: {sum(selected_item_nums)}')
print(f'Grand Total: {sum(items_total_price)} ')
print()
print("------------------------------")
print()
print("Thanks for placing your order. \nYou will be served soon.")

