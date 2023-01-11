import csv


all_customers = []

class Customers:
    def __init__(self, file):
        self.file = file
        self.all_customers = []
        
        with open(file, 'r', newline='') as c_file:
            reader = csv.DictReader(c_file)

            for row in reader:
                all_customers.append(row)
        
        self.all_customers = all_customers

    # Show customer_id and name for each customer in the store.
    def view_all_customers(self):
        print("\n=== Customers ===\n")
        for person in self.all_customers:
            customer_id = person['id']
            first_name = person['first_name']
            last_name = person['last_name']
            customer = f"Name: {first_name} {last_name}\nCustomer ID#: {customer_id}\n"
            print(customer)
        return 
    
    # Take in a customer_id from the user and show the current rented videos for that customer.
    # Each title should be listed separately.
    def view_customer_rentals(self, customer_id):
        for person in self.all_customers:
            if person['id'] == customer_id:

                # video rentals will either be an empty string if starting with no movies or 
                # None if customer had movies but movies were deleted resulting in "None" from the "return a movie" method
                if person['current_video_rentals'] == '' or person['current_video_rentals'] == None:
                    print('No current rentals.')
                    return person['current_video_rentals']
                
                # Current Video Rentals turned into a list after a movie is added, so this conditional takes that into account:
                elif type(person['current_video_rentals']) == list:
                    print(', '.join(person['current_video_rentals']))
                    return person['current_video_rentals']
                else: 
                    person['current_video_rentals'] = (person['current_video_rentals']).replace("/", '\n')
                    person['current_video_rentals'] = person['current_video_rentals'].splitlines()
                    print(', '.join(person['current_video_rentals']))
                    return person['current_video_rentals']
    
    # A newly created customer should not have any rentals.
    def add_a_customer(self, first_name, last_name, account_type):
        print("\n=== Adding New Customer ===\n")
        new_customer = {}

        # Prevent duplicate IDs
        for person in all_customers:
            new_id = int(person['id']) + 1
        
        new_customer['id'] = str(new_id)
        new_customer['first_name'] = first_name
        new_customer['last_name'] = last_name
        new_customer['account_type'] = account_type
        new_customer['current_video_rentals'] = '' 

        print(f"New customer added successfully.\n\nEmployee Account Information:\n\nID Number: {new_customer['id']}\nFirst Name: {new_customer['first_name']}\nLast Name: {new_customer['last_name']}\nAccount Type: {new_customer['account_type']}\nNo current rentals.\n")
        return all_customers.append(new_customer)
    

# TESTS
# customers = Customers('./data/customers.csv')
# customers.view_all_customers(customers.all_customers)
# customers.view_customer_rentals('2')
# customers.add_a_customer(first_name='Kayla', last_name='Nicole', account_type='sx')
# print(customers.all_customers)
# customers.add_a_customer(first_name='Jane', last_name='Doe', account_type='sx')
# print(customers.all_customers)
# customers.add_a_customer(first_name='John', last_name='Doe', account_type='sx')
# print(customers.all_customers)