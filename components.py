# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        return self.__name
        """
        Initializes a new store with a name.
        """
    

    def add_product(self, product):
        return self.__product
        """
        Adds a product to the list of products in this store.
        """
    

    def print_products(self):
        return self.__product
        """
        Prints all the products of this store in a nice readable format.
        """



class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.__name = name
        self.__description = description
        self.__price = price

    def __str__(self):
        return self


class Cart():
    def __init__(self):
        self.__cartlist = {}
        self.__cartlist[0] = cart()
        """
        Initializes a new cart with an empty list of products.
        """
    

    def add_to_cart(self, product):
        self.__cartlist[len(self.__product)]= cart()
        """
        Adds a product to this cart.
        """


    def get_total_price(self):
        self.__cartlist[cartindex][product.name()][1]+= price
        """
        Returns the total price of all the products in this cart.
        """
        

    def print_receipt(self):
        print "name \t description \t price"
        for a in range(0, list + 1):
            print name[a], "\t\t" , description[a], "\t\t 3", price[a]

        print "\t\t\t", "KD" , total
        print " Thank you for shopping with us" 


    while 1:
        name()
        Price()
        if finished:
            print_receipt()
        else:
            continue
        """
        Prints the receipt in a nice readable format.
        """


    def checkout(self):
        print "Successful!"
        

        """
        Does the checkout.
        """
        
