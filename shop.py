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
    for aitem in menu.items():
    	print('_"{}" (KD {})'.format(aitem[0],aitem[1]))

print_menue()


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    
    for aitem in original_flavors:
    	print('_"{}"'.format(aitem))

  print_originals()


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    
    for aitem in signature_flavors:
    	print('_"{}"'.format(aitem))

print_signatures()


print("What is your order? (Enter the exact spelling of the item you want. Type 'Exit' to end your order.)\n")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order not in menu.keys() and order not in original_flavors and order not in signature_flavors:
    	print("Please Enter a Valid Order!")
    	return get_order()
    else:
    	global order_list
    	order_list.append(order)
    	return get_order()


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    
    order = input()
    if order != "Exit":
    	is_valid_order(order)

    return order_list

get_order()


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
