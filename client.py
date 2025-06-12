"""
Product Management System to manage products in the inventory
"""
import data

def user_create_product():
    """
    Create product to add product with name and price
    :return: None
    """
    product_name=input("Enter product name ")
    product_price=float(input("Enter price of product"))
    data.create_product(product_name,product_price)


def user_delete_product():
    """
    Delete product based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    data.delete_product(product_id)

def user_update_product():
    """
    Update product price based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    product_price = float(input("Enter price to update"))
    data.update_product(product_id, product_price)


def user_select_product():
    """
    To check whether product exists in inventory based on product id
    :return: None
    """
    product_id = float(input("Enter product id"))
    data.select_product(product_id)

def user_display_products():
    """
    Display all products from inventory
    :return: None
    """
    data.display_products()


SELECT_CHOICE="""
1. create product
2. delete product
3. update product
4. select product
5. display products
6. Quit
Enter your choice: 
"""


def menu():
    """
    Display menu options
    :return: None
    """
    choice = int(input(SELECT_CHOICE))
    while choice!=6:
        if choice==1:
            user_create_product()
        elif choice==2:
            user_delete_product()
        elif choice==3:
            user_update_product()
        elif choice==4:
            user_select_product()
        elif choice==5:
            user_display_products()
        choice = int(input(SELECT_CHOICE))

menu()

