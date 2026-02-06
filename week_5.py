
#starter code----------------------------------------------------------------------------------------------
inventory = {}
def add_item(d):
    item_id=int(input("Enter item id:"))
    item_name=input("ENter item name:")
    qty=int(input("Enter item quantity"))
    price=float(input("Enter item price"))
    d[item_id]=[item_name,qty,price]
    print("Item Added Successfully")

def update_quantity(d):
    up_id=int(input("ENter id of item to be updated :-"))
    up_qty=int(input("Enter Updated quantity:"))
    if up_id in d:
      d[up_id][1]=up_qty
      print("Item Quantity Updated Successfully ")
    
def search_item(d):
    search_id=int(input("Enter Id of item to be searched:-"))
    if search_id in d:
        print(d[search_id])

def display_items(d):
    print("-"*48)
    print(f"|{"ID":^5}| {"Name ":20}| {"Qty":>5} | {"price":>9}|")
    print("-"*48)
    for k,v in d.items():
        print(f"|{k:^5}| {v[0]:<20}|{v[1]:>5} | \u20B9{v[2]:>9}|")
        print("-"*48)
    print("-"*48)

def total_inventory_value(d):
    total=0
    for v in d.values():
       total=total+v[1]
    print(total)
    
def low_stock_items(d):
    for k,v in d.items():
       if v[1]<5:
          print(k,v)
# -------- MENU DRIVEN PROGRAM --------
while True:
 print("\nInventory Management System")
 print("1. Add Item")
 print("2. Update Quantity")
 print("3. Search by Item ID")
 print("4. Display All Items")
 print("5. Total Inventory Value")
 print("6. Low Stock Items")
 print("7. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
    add_item(inventory)
 elif choice == "2":
    update_quantity(inventory)
 elif choice == "3":
    search_item(inventory)
 elif choice == "4":
    display_items(inventory)
 elif choice == "5":
    total_inventory_value(inventory)
 elif choice == "6":
    low_stock_items(inventory)
 elif choice == "7":
    print("Exiting system.")
    break
 else:
    print("Invalid choice. Try again.")