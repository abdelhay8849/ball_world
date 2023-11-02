print("Sandwich Shop menu:[halal]")

sandwiches_dict = {
   1:"Chicken",
   2:"Beef",
   3:"Lamb",
   4:"Falafel"
   }





for x,y in sandwiches_dict.items():
  print(x,y)
chosen_sandwich =int( input("choose your sandwich: "))
print(sandwiches_dict[chosen_sandwich])


bread_dict = {
   1:"white",
   2:"whole",
   3:"gluten"
   }
for x,y in bread_dict.items():
    print(x,y)
chosen_bread = int(input("choose a type of bread: "))
print(sandwiches_dict[chosen_bread])

toppings_dict = {
   1:"Lettuce",
   2:"cucumber", 
   3:"Onion",
   4:"Pickles",
   5:"Olives"
   }
for x,y in toppings_dict.items():
    print(x,y)
chosen_toppings = int(input("choose what toppings you want: "))
print(toppings_dict[chosen_toppings])
price = 
customer_order = 












print("Thank you for shopping at the sandwich shop!!!")