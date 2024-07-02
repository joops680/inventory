from tabulate import tabulate
#========The beginning of the class==========

class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
#         '''
#         Add the code to return the cost of the shoe in this method.
#         '''

    def get_quantity(self):
        return self.quantity
#         '''
#         Add the code to return the quantity of the shoes.
#         '''

    def __str__(self):
        return f"{self.country} {self.code} {self.product}  ${self.cost} {self.quantity}"

        #  '''
        #  Add a code to returns a string representation of a class.
        #  '''


# #=============Shoe list===========
# '''
# The list will be used to store a list of objects of shoes.
# '''
shoe_list = []
# #==========Functions outside the class==============
def read_shoes_data():
    try:

        with open   ("inventory.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe_data = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe_data)
                except ValueError as e:
                    print(f"Error line not processing '{line.strip()}': {e}")
    except FileNotFoundError:
        print(" file not found")

#     '''
#     This function will open the file inventory.txt
#     and read the data from this file, then create a shoes object with this data
#     and append this object into the shoes list. One line in this file represents
#     data to create one object of shoes. You must use the try-except in this function
#     for error handling. Remember to skip the first line using your code.
#     '''
def capture_shoes():

    user_data = {}
    user_data["country"] = input("What country is the shoe from? ")
    user_data["code"] = input("What is the code of the shoe? ")
    user_data["product"] = input("What is the brand name? ")
    user_data["cost"] = input("How much is the shoe? ")
    user_data["quantity"] = input("How many shoes do you want? ")
    with open ("inventory.txt", "a") as file:
        file.write(f"\n{user_data["country"]},{user_data["code"]},{user_data["product"]},{user_data["cost"]},{user_data["quantity"]}")
    
    shoe_capture = Shoe(user_data["country"], user_data["code"], user_data["product"], user_data["cost"], user_data["quantity"])
    shoe_list.append(shoe_capture)

    return user_data

#     '''
#     This function will allow a user to capture data
#     about a shoe and use this data to create a shoe object
#     and append this object inside the shoe list.
#     '''

def view_all(shoe_list):
    empty_shoe_lst = []
    for Shoe in shoe_list:
        empty_shoe_lst.append([Shoe.country, Shoe.code, Shoe.product, Shoe.cost, Shoe.quantity])

    shoe_L = ["country", "code", "product", "cost", "quantity"]
    print(tabulate(empty_shoe_lst, headers=shoe_L, tablefmt='grid'))
#     '''
#     This function will iterate over the shoes list and
#     print the details of the shoes returned from the __str__
#     function. Optional: you can organise your data in a table format
#     by using Python’s tabulate module.
#     '''

def re_stock():
    shoe_list1 = []
    with open ("inventory.txt","r") as file:
        lines = file.readlines()

        for line in lines[1:]:
            data_shoe = line.strip().split(",")
            shoe_object = Shoe(data_shoe[0],data_shoe[1],data_shoe[2],data_shoe[3],data_shoe[4])
            shoe_list1.append(shoe_object)
    print(shoe_list1)
    
    if len(shoe_list1) == 0:
        print("no shoes in stock or inventory")
        return
    lowest_quantity = shoe_list1[0]
    for shoe in shoe_list1[1:]:
        try:
            shoe_quantity = float(shoe.quantity) 
        except ValueError:
            continue
        if shoe_quantity < float(lowest_quantity.quantity):
            lowest_quantity = shoe
    
    print("lowest shoe quantity")
    print(",".join([lowest_quantity.country, lowest_quantity.code, lowest_quantity.product, lowest_quantity.cost, lowest_quantity.quantity]))
    print(f"quantity: {lowest_quantity.quantity}")

    stock_reload = input("How many do you want to restock? ")
    try:
        stock_reload = int(stock_reload)
        if stock_reload < 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity, enter correct quantity")
        return

    lowest_quantity.quantity = str(int(lowest_quantity.quantity) + stock_reload)

    with open("inventory.txt", "w") as file:
        file.write("country,code,product,cost,quantity\n")
        for shoe in shoe_list1:
            file.write(",".join([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]) + "\n")


#     '''
#     This function will find the shoe object with the lowest quantity,
#     which is the shoes that need to be re-stocked. Ask the user if they
#     want to add this quantity of shoes and then update it.
#     This quantity should be updated on the file for this shoe.
#     '''

def seach_shoe(product):
    with open ("inventory.txt","r") as file:
        for line in file:
            if product.lower() in line.lower():
                print(f"{product} was found.")
                return
            print(f"{product} was not found")               
#     '''
#      This function will search for a shoe from the list
#      using the shoe code and return this object so that it will be printed.
#     '''

def value_per_item():
    with open ("inventory.txt","r") as file:
        lines_2 = file.readlines()
        shoe_3 = lines_2[0].strip().split(",")
        table_data = []
        for line in lines_2[1:]:
            shoe_data2 = line.strip().split(",")
            if len(shoe_data2) >= 5:
                cost = float(shoe_data2[3].replace("$", " "))
                quantity = int(shoe_data2[4])
                value = cost * quantity
                shoe_data2.append(f"${value}")
                table_data.append(shoe_data2)
        print(tabulate(table_data,headers=shoe_3 + ["Value"], tablefmt='grid'))
#     '''
#     This function will calculate the total value for each item.
#     Please keep the formula for value in mind: value = cost * quantity.
#     Print this information on the console for all the shoes.
#     '''

def highest_qty():
    quantity_max = 0
    max_shoe = None

    with open ("inventory.txt","r") as file:
        lines_3 = file.readlines()
        shoe_4 = lines_3[0].strip().split(",")
        for line in lines_3[1:]:
            shoe_data3 = line.strip().split(",")
            if len(shoe_data3) >= 5:
                quantity = int(shoe_data3[4])
                if quantity > quantity_max:
                    quantity_max = quantity
                    max_shoe = shoe_data3
    if max_shoe:
        print("for sale")
        print(",".join(shoe_4))
        print(",".join(max_shoe))
    else:
        print("no shoes are for sale.")
#     '''
#     Write code to determine the product with the highest quantity and
#     print this shoe as being for sale.
#     '''
# #==========Main Menu=============
# '''
# Create a menu that executes each function above.
# This menu should be inside the while loop. Be creative!
# '''
read_shoes_data()

while True:
    menu = input ('''Select one of the following options:
    cs - capture shoes
    va - view all shoes
    rs - restock
    ss - search shoe
    vs - value of shoes
    hq - highest quantity                                                 
    e - exit
    : ''').lower()

# If user chooses 'cs' it will let the user add their own shoes to the inventory.txt 
    if menu == 'cs':
        capture_shoes()
    # If user chooses 'va' it will then view all shoes in a tble format. 
    elif menu == 'va':
        view_all(shoe_list)
    # If user choose rs it will restock the shoes .
    elif menu == 'rs':
        re_stock()
        # quantity = int(input("Enter the quantity to restock: "))
        # re_stock(quantity)
        # print(f"the shoe has been restocked by {quantity}")
    # If user choose ss it will search the shoes the user is looking for
    elif menu == 'ss':
        product = input("what shoes are you looking for?")
        seach_shoe(product)
    # this will show the cost of the shoe
    elif menu == 'vs':
        value_per_item()   
    # this will show the highest quantity of the shoe list
    elif menu == 'hq':
        highest_qty()

     #If user choose e it just exits the program.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:               
        print("You have entered an invalid input. Please try again")