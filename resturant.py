# resturant 
menue ={ #dictinory creating
    'Chai'   : '40', 
    'pratha' : '50',
    'Anda'   : '50',
    'Chola'  : '60',}
print("Welcome to hotel")
print("Any thing you want to Order ")


# ye menue ko unpack krdega 2 hisso me ik item or dusra price me to neechy hm f k sath item lgayngy curly bracket me or phir price likhgngy
for item, price in menue.items():
    print(f"{item}: Rs {price}")


Order_amount = 0


order_01 = input("Enter your order : ")
if order_01 in menue: # check krega k hn ya ni order_01
    Order_amount+= int(menue[order_01])# it will add the amount    
else:
    print(f"this {order_01} is not availble \n Please order from menue :")
other_order = input("Do you want to order something else : (Y/N)").lower() # every entry become lower case

# second order
order_02 =None # none krrahy hn taky agr add na bhi kry to issue na ho
if other_order in ["y","yes"]:
    order_02 = input("Enter another item: ")
    if order_02 in menue:
        print(f"Your order {order_02} has been added")
        Order_amount+=int(menue[order_02]) # adding the amount
    else:
        print(f"{order_02} is not availble : ")

# If order_02 exists, print it
if order_02:  
    print(f"The total amount of your order(s) ({order_01} and {order_02}) is Rs {Order_amount}")
else:  # If only one item was ordered
    print(f"The total amount of your order ({order_01}) is Rs {Order_amount}")

print("Thanks for comming")
# print(f"The total amount of : {Order_amount} \n of {order_01} and {order_02}")