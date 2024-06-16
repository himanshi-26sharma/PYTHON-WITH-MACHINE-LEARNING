#Define the menu of restuarant 
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80
}
#Greet
print("WELCOME TO PYHTON RESTUARANT")
print("pizza:Rs40\nPasta:Rs50\nBurger:Rs60\nSalad:Rs70\nCoffee:Rs80") 
order_total = 0
item_1 = input("enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ORDERED ITEM {item_1} IS NOT AVAIABLE YET")  
 
another_order = input("DO YOU WANT WANT TO ADD ANOTHER ITEM?(yes/no) ")
if another_order =="yes":
        item_2 = input("enter the name of second item =")
        if item_2 in menu:
            order_total += menu[item_2]
            print("item {item_2} has been added to order")
        else:
            print("ordered item{item_2} is not avaiable")
            
print(f"the total amount of items to pay is {order_total}")
