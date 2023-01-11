from customers import Customers
from inventory import Inventory

customers = Customers('./data/customers.csv')
inventory = Inventory('./data/inventory.csv')


class Interface:

    def __init__(self):
        self.main_menu = self.main_menu()
        

    def main_menu(self):
        print("\n=== C.P. Video Interface ===\n")
        options = ['1. View Store Video Inventory', '2. View Store Customers', '3. View Customer Rented Videos', '4. Add New Customer', '5. Rent Video', '6. Return Video', '7. Exit\n']
        for choice in options:
            print(choice)

        selected_choice = input('Please enter a number to select a menu option: ')

        if selected_choice == str(1): 
            self.view_inventory()
        elif selected_choice == str(2):  
            self.view_customers()
        elif selected_choice == str(3): 
            self.view_customer_rentals()
            return self.main_menu() 
        elif selected_choice == str(4): 
            self.add_customer()
            return self.main_menu() 
        elif selected_choice == str(5):  
            self.rent_video()
            return self.main_menu() 
        elif selected_choice == str(6):
            self.return_video()
        elif selected_choice == str(7):  
            print('Exiting C.P.V. Interface. Goodbye!')
            return exit()
        else:
            print("Invalid selection. Please try again.")
            return self.main_menu()

    def view_inventory(self):
        inventory.view_current_inventory()
        return self.main_menu()

    def view_customers(self):
        customers.view_all_customers()
        return self.main_menu()
  
    def view_customer_rentals(self):
        print("\n=== Enter Customer Credentials ===\n")
        customer_id = input("\nCustomer ID#: ")
        for customer in customers.all_customers:
            if customer['id'] == customer_id:
                print(f"\n=== {customer['first_name']}'s Current Video Rentals ===\n")
                customers.view_customer_rentals(customer_id=customer_id)
        return self.main_menu()
        
    def add_customer(self):
        print("\n=== Enter Customer Credentials ===\n")
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        account_type = input('Account Type: (sx = Standard, px = Premium, sf = Standard Family, pf = Premium Family) ')
        customers.add_a_customer(first_name=first_name, last_name=last_name, account_type=account_type)
        return self.main_menu()
        
    def rent_video(self):
        print("\n=== Enter Customer Credentials ===\n") 
        customer_id = input("Customer ID#: ")
        first_name = input("First Name: ")
        account_type = input("Account Type: ")
        movie_title = input("Movie Title: ")
        inventory.rent_a_video(customer_id=customer_id, first_name=first_name, account_type=account_type, movie_title=movie_title)
        return self.main_menu()

    def return_video(self):
        print("\n=== Enter Customer Credentials ===\n")
        customer_id = input("Customer ID#: ")
        print("\n=== Current Video Rentals ===\n")
        customers.view_customer_rentals(customer_id=customer_id)
        movie_title = input("\nEnter title of movie to return: ")
        inventory.return_a_video(customer_id=customer_id, movie_title=movie_title)
        return self.main_menu()
