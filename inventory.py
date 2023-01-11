import csv
from customers import Customers

all_inventory = []

class Inventory:
    
    def __init__(self, file):
        self.file = file
        self.all_inventory = []

        with open(file, 'r', newline='') as i_file:
            reader = csv.DictReader(i_file)
            
            for row in reader:
                all_inventory.append(row)
        
        self.all_inventory = all_inventory
        
    def view_current_inventory(self):
        print("\n=== Current Inventory ===\n")
        for movie in all_inventory:
            print(f"Title: {movie['title']}\nCopies Available: {movie['copies_available']}\n")
        return
        
    def rent_a_video(self, customer_id, first_name, account_type, movie_title):
        customers = Customers('./data/customers.csv')
        current_rentals = []
        rentals_list = []
        unrestricted_by_ratings = ['sx', 'px']
        restricted_ratings = ['sf', 'pf']

        max_one_rental = ['sx', 'sf']
        max_three_rentals = ['px', 'pf']
        
        customer_rentals = customers.view_customer_rentals(customer_id=customer_id)

        if customer_rentals == None: # customer has no rentals, so they can rent something based on their account type

            if account_type in unrestricted_by_ratings: # customer can rent available movies
                for movie in all_inventory: 
                    if movie['title'] == movie_title and int(movie['copies_available']) > 0: # change the value of available copies when the customer rents and add the movie to their current rentals
                        movie['copies_available'] = int(movie['copies_available']) - 1 # change the number of available copies since renting to customer
                
                        for customer in customers.all_customers:
                            if customer['id'] == customer_id: # find the customer
                                customer['current_video_rentals'] = rentals_list
                                customer['current_video_rentals'].append(movie['title']) # add the movie to their empty current rentals     
                                print("\n=== NEW MOVIE ADDED TO RENTALS ===\n")
                                print(f"\n'{movie_title}' successfully added to {first_name}'s rentals.\n")
                                return customer['current_video_rentals']
                        return movie['copies_available']

                    elif movie['title'] == movie_title and int(movie['copies_available']) == 0: # customer can't rent because no available copies
                        print(f"\n=== ALERT: NO COPIES OF '{movie_title}' AVAILABLE ===\n")
                        print(f"\nSorry, {first_name}! No copies available.\n")
                        
            elif account_type in restricted_ratings: # customer can rent available movies if not rated R
                
                for movie in all_inventory:
                    if movie['title'] == movie_title and movie['rating'] != 'R': # customer can rent because movie not rated R
                        if int(movie['copies_available']) > 0: # change the value of available copies when the customer rents and add the movie to their current rentals
                            movie['copies_available'] = int(movie['copies_available']) - 1

                            for customer in customers.all_customers:
                                if customer['id'] == customer_id:
                                    customer['current_video_rentals'] = rentals_list
                                    customer['current_video_rentals'].append(movie['title'])
                                    print("\n=== NEW MOVIE ADDED TO RENTALS ===\n")
                                    print(f"\n'{movie_title}' successfully added to {first_name}'s rentals.\n")
                                    return customer['current_video_rentals']
                            return movie['copies_available']
                        
                        elif int(movie['copies_available']) == 0: # no copies available, so cannot rent
                            print(f"\n=== ALERT: NO COPIES OF '{movie_title}' AVAILABLE ===\n")
                            print(f"\nSorry, {first_name}! No copies available.\n")
                    
                    elif movie['title'] == movie_title and movie['rating'] == 'R': # customer cant rent because movie is rated r
                        print(f"\n=== ALERT: UNACCEPTED RATING FOR ACCOUNT ===\n")
                        print(f"\n{first_name} ineligible to rent movie due to R rating.\n")
        
        else: # customer has rentals, so they may be restricted to renting based on their amount of rentals
            
            current_rentals.append(customer_rentals)
            
            # this condition checks for new-line characters; if a customer does not have newline characters present in their current rentals, 
            # the customer has gone through the process of renting a movie and the formatting of their current video rentals has changed
            # this conditional avoids conflict when checking a customers amount of rentals based on if they've recently rented or not
            if '\n' not in current_rentals:
                rentals_list = [movie for movie in current_rentals[0]]
                amount_of_rentals = len(rentals_list)
            else:
                rentals_list = [movie for movie in current_rentals[0].splitlines()]
                amount_of_rentals = len(rentals_list)
            
            if account_type in max_one_rental and amount_of_rentals == 1: # customer cannot rent because they met their max
                print("\n=== MAX RENTAL LIMIT REACHED. ===\n")
                print(f"\n{first_name} cannot rent. Max rental limit met.\n")
            
            elif account_type in max_three_rentals and amount_of_rentals == 3: # customer cannot rent because they met their max
                print("\n=== MAX RENTAL LIMIT REACHED. ===\n")
                print(f"\n{first_name} cannot rent. Max rental limit met.\n")
            
            else:
                
                if account_type in unrestricted_by_ratings: # customer can rent any available movie 
                    
                    for movie in all_inventory:
                        if movie['title'] == movie_title and int(movie['copies_available']) > 0: # change the value of available copies when the customer rents and add the movie to their current rentals
                            movie['copies_available'] = int(movie['copies_available']) - 1

                            for customer in customers.all_customers:
                                if customer['id'] == customer_id:
                                    customer['current_video_rentals'] = rentals_list
                                    customer['current_video_rentals'].append(movie['title'])
                                    print("\n=== NEW MOVIE ADDED TO RENTALS ===\n")
                                    print(f"\n'{movie_title}' successfully added to {first_name}'s rentals.\n")
                                    return customer['current_video_rentals']
                            return movie['copies_available']

                        elif movie['title'] == movie_title and int(movie['copies_available']) == 0: # customer can't rent because no available copies
                            print(f"\n=== ALERT: NO COPIES OF '{movie_title}' AVAILABLE ===\n")
                            print(f"\nSorry, {first_name}! No copies available.\n")
                
                elif account_type in restricted_ratings: # customer can rent any available movie that is not rated R.
                    
                    for movie in all_inventory:
                        if movie['title'] == movie_title and movie['rating'] != 'R': # customer can rent because movie not rated R
                            if int(movie['copies_available']) > 0: # change the value of available copies when the customer rents and add the movie to their current rentals
                                movie['copies_available'] = int(movie['copies_available']) - 1

                                for customer in customers.all_customers: # WORK ON JOHN'S CASE
                                    if customer['id'] == customer_id:
                                        customer['current_video_rentals'] = rentals_list
                                        customer['current_video_rentals'].append(movie['title'])
                                        print("\n=== NEW MOVIE ADDED TO RENTALS ===\n")
                                        print(f"\n'{movie_title}' successfully added to {first_name}'s rentals.\n")
                                        return customer['current_video_rentals']
                                return movie['copies_available']

                            elif int(movie['copies_available']) == 0: # no copies available, so cannot rent
                                print(f"\n=== ALERT: NO COPIES OF '{movie_title}' AVAILABLE ===\n")
                                print(f"\nSorry, {first_name}! No copies available.\n")
                        
                        elif movie['title'] == movie_title and movie['rating'] == 'R': # customer cant rent because movie is rated r
                            print(f"\n=== ALERT: UNACCEPTED RATING FOR ACCOUNT ===\n")
                            print(f"\n{first_name} ineligible to rent movie due to R rating.\n")
    

    def return_a_video(self, customer_id, movie_title):
        customers = Customers('./data/customers.csv')

        for customer in customers.all_customers:
            if customer['id'] == customer_id:
                curr_rentals_list = customer['current_video_rentals']
                curr_rentals_list = curr_rentals_list.remove(movie_title)
                customer['current_video_rentals'] = curr_rentals_list

                for movie in self.all_inventory:
                    if movie['title'] == movie_title:   
                        movie['copies_available'] = str(int(movie['copies_available']) + 1)   
                        print("\n=== MOVIE SUCCESSFULLY REMOVED ===\n")
                        print(f"\n'{movie_title}' has been removed from {customer['first_name']}'s video rentals.\n")
                        return



# TESTS                   
# inventory = Inventory('./data/inventory.csv')
# inventory.rent_a_video(customer_id='1', first_name='Monica', account_type='sx', movie_title='Toy Story')
# inventory.rent_a_video(customer_id='2', first_name='Chandler', account_type='px', movie_title='WALL-E')
# inventory.rent_a_video(customer_id='3', first_name='Rachel', account_type='pf', movie_title='Up')
# inventory.rent_a_video(customer_id='4', first_name='Ross', account_type='sx', movie_title='Inside Out')
# inventory.rent_a_video(customer_id='5', first_name='Phoebe', account_type='sf', movie_title='The Godfather')
# inventory.rent_a_video(customer_id='6', first_name='Joey', account_type='px', movie_title='Deadpool')
# inventory.rent_a_video(customer_id='7', first_name='Billy', account_type='sf', movie_title='Deadpool')
# inventory.rent_a_video(customer_id='8', first_name='Jane', account_type='sf', movie_title='Inside Out')
# inventory.rent_a_video(customer_id='9', first_name='John', account_type='sf', movie_title='Intersteller')
# inventory.rent_a_video(customer_id='10', first_name='Ella', account_type='pf', movie_title='Intersteller')





