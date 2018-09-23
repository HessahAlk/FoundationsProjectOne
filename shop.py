####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "The Cake Shop"
signature_flavors = ["tuna", "salmon", "red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu:")
    for aitem in menu:
    	print("-\"%s\": KD %s" % (aitem, menu[aitem]))



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    
    for aitem in original_flavors:
    	print("-\"%s\""% aitem)




def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    
    for aitem in signature_flavors:
    	print("-\"%s\""% aitem)


print("What is your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)\n")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order not in menu.keys() or order not in original_flavors or order not in signature_flavors:
    	return False
	print("Please Enter a Valid Order!")
    else:
    	return True


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    user_input = input("Type your order! (Type 'exit' when you Finish)\n")
    while user_input.lower() != "exit":
        if is_valid_order(user_input):
    	    order_list.oppened(user_input)
        else:
    	    print ("This order is not available in the menu!")


    user_input = input("> ")
    return order_list



def accept_credit_card(total):
	if total >= 5:
		print("Your order is eligible")


    """
    Return whether an order is eligible for credit card payment.
    """
   


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
    	if order in menu:
    		total += menu[item]
    	elif order in original_flavors:
    		total += original_price
    	elif order in signature_flavors:
    		total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")

    for order in order_list:
    	print("- \"%s\"" % order)

    	total_price = get_total_price(order_list)
    	print("Total price :  KD %s" % total_price)
	accept_credit_card(total_price)
	
	print("Thank you for choosing %s" % cupcake_shop_name)
    
