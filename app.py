import sys
from tabulate import tabulate

class Movie():
    def __init__(self, title, rating, genre, year, price, tag, description, movieid,ratings):
        self.Title = title
        self.Rating = rating
        self.Genre = genre
        self.Year = year
        self.Price = price
        self.Tag = tag
        self.Description = description
        self.MovieId = movieid
        self.Ratings = ratings

    
    def getMovieDetails(self):
        return f"{self.Title} ,{ self.Rating },{self.Genre },{self.Year},{self.Price } ,{ self.Tag } ,{ self.Description }, {self.MovieId}"
    
    def getPrice(self):
        return float((self.Price[1:]))
    
    def __str__(self) -> str:
        return f"This is a movie with title: {self.title} from the genre:{self.Genre}"

class Customer():
    def __init__(self, first_name, last_name, age, gender,phone, customerid):
        self.CustomerId = customerid
        self.FirstName = first_name
        self.LastName = last_name
        self.Age = age
        self.Gender = gender
        self.Phone = phone
        self.MoviePreferences = []
        self.ShoppingCart = []

    def getCustomerDetails(self):
        return (self.CustomerId, self.FirstName, self.LastName, self.Age, self.Phone)

    def getFullName(self):
        return self.FirstName + " " + self.LastName

    def addMoviePreference(self, title,genre,year,rating):
        self.MoviePreferences.append({"title":title,"genre":genre,"year":year,"rating":rating})
    
    def removeMoviePreference(self,title):
        for movie in self.Movies_Store:
            if movie['title'] == title:
                self.MoviePreferences.remove(movie)
            else:
                print("Movie preference not found")

    def getID(self):
        return self.CustomerId 
    
    def getName(self):
        return self.FirstName + self.LastName
    
    def getMoviePrefences(self):
        return self.MoviePreferences

    def getDetails(self):
        return f"{self.FirstName},{ self.LastName} ,{str(self.Age)} , {self.Phone },{ self.CustomerId } ,{str(self.MoviePreferences)}"


class RentalStore():
    # stores all movies , customers and rentals
    def __init__(self,Movies=None):
        self.Movies_Store = []
        self.Customers = []
        self.RentalsDict = {}

    def addToStore(self, title = None, rating = None ,genre = None, year = None, price = None, tag = None, description = None, movieid = None ,ratings= None,movie=None,num_copies=None):
        if movie != None and num_copies != None:
            for i in range(num_copies):
                self.movies_available.append(movie)
            return
        else:
            movie = Movie(title, rating, genre, year, price, tag, description, movieid,ratings)
            self.Movies_Store.append(movie)

    def removeFromStore(self, movie):
        self.Movies_Store.remove(movie)

    def addCustomer(self, firstName, lastName, age,gender, phone, customerid):
        customer = Customer(firstName, lastName, age,gender, phone, customerid)
        self.Customers.append(customer)

    def removeCustomer(self, customer):
        self.Customers.remove(customer)

         # 
    def rent_movie(self, customer, movie):
        if movie in self.Movies_Store:
            self.Movies_Store.remove(movie)
            if customer in self.RentalsDict:
                self.RentalsDict[customer].append(movie)
            else:
                self.RentalsDict[customer] = [movie]
            return(f"{print(customer.getName)} rented '{movie.Title}' for '{movie.Price}' successfully!")
        else:
            return(f"'{movie.Title}' is not available for rent.")


    def return_movie(self, customer, movie_to_return):
        # Check if the customer has any movies rented
        if customer not in self.RentalsDict:
            print(f"No movies are currently rented by {customer}.")
            return

        elif customer in self.RentalsDict:
            # Find the returned movie in the rented movies list
            rented_movies = self.rented_movies[customer]
            found_copy = None
            for movie_copy in rented_movies:
                if movie_copy.Title == movie_to_return.Title:
                    found_copy = movie_copy
                    break

            if found_copy is not None:
                # Add the returned movie copy back to the available movies list
                self.movies_available.append(found_copy)
                # Remove the returned movie copy from the customer's rented movies
                rented_movies.remove(found_copy)
                print(f"{customer} returned '{found_copy.title}' successfully!")
            else:
                print(f"No movie with title '{movie_to_return.title}' is rented by {customer}.")
    def add_bulk_movies(self,movies):
        for movie in movies:
            self.Movies.append(movie)

    def getMovies(self):
        movie_data = []
        for movie in self.Movies_Store:
            movie_data.append([
                movie.Title,
                movie.Rating,
                movie.Genre,
                movie.Year,
                movie.Price,
                movie.Tag,
                movie.Description,
                movie.MovieId,
                movie.Ratings
            ])

        headers = [
            "Title",
            "Rating",
            "Genre",
            "Year",
            "Price",
            "Tag",
            "Description",
            "Movie ID",
            "Ratings"
        ]

        print(tabulate(movie_data, headers=headers))

    # def getCustomers(self):
    #     for customer in self.Customers:
    #         print(customer.getCustomerDetails())
    
    def getCustomers(self):
        customer_data = []
        for customer in self.Customers:
            customer_data.append([
                customer.CustomerId,
                customer.FirstName,
                customer.LastName,
                customer.Age,
                customer.Phone,
            ])

        headers = ["Customer ID", "First Name", "Last Name", "Age", "Phone"]

        print(tabulate(customer_data, headers=headers))

    
    def get_total_number_of_movies(self):
        return len(self.Movies)

# Create a rental store
RentMovies = RentalStore()

# Add movies to the store
RentMovies.addToStore('The Godfather','PG', 'Fantasy','2018','GH₵5.00','New','This is an old movie','1', '90%')
RentMovies.addToStore('Ariel','P', 'Fantasy','2018','GH₵10.00','New','This is a new movie','2', '9')
RentMovies.addToStore('Pulp Fiction','P', 'Adventure','2013','GH₵5.00','Old','This is an old movie','3', '9')
RentMovies.addToStore('The Shawshank Redemption','P', 'Adventure','2014','GH₵20.00','New','This is a new movie','4', '9')
RentMovies.addToStore('The Matrix','P', 'Romance','2013','GH₵10.00','New','This is an old movie','5', '9')
RentMovies.addToStore('Pulp Fiction','P', 'Adventure','2019','GH₵45.00','New','This is an old movie','6', '9')
RentMovies.addToStore('Ariel','P', 'Thriller','2015','GH₵20.00','Old','This is a new movie','7', '9')
RentMovies.addToStore('Pulp Fiction','P', 'Adventure','2016','GH₵30.00','New','This is a new movie','8', '9')
RentMovies.addToStore('Ariel','P', 'Action','2013','GH₵30.00','Old','This is an old movie','9', '9')
RentMovies.addToStore('Jungle Story','P', 'Crime','2014','GH₵50.00','New','This is an old movie','10', '9')
# Add customers to the store
RentMovies.addCustomer('Henry', 'Bernard','25','Male', '1129083552', 0)
RentMovies.addCustomer('Randy', 'Oscar','11','Male', '8675927194', 1)
RentMovies.addCustomer('Mandy', 'Penny','20','Male', '4607835889', 2)
RentMovies.addCustomer('Uma', 'Mandy','22','Male', '4607835889', 3)
RentMovies.addCustomer('Quincy', 'Hannah','25','Male', '1749762630', 4)
RentMovies.addCustomer('Grace', 'Oscar','19','Male', '1749762630', 5)
RentMovies.addCustomer('Quincy', 'Quincy','12','Male', '1393601684', 6)
RentMovies.addCustomer('David', 'Oscar','11','Female', '6977098783', 7)
RentMovies.addCustomer('Fiona', 'Nancy','17','Female', '1393601684', 8)
RentMovies.addCustomer('Mandy', 'Jenny','25','Male', '8675927194', 9)



def CustomerDisplay():
    print("Hello Customer, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    print("4. Add preference")
    print("5. Exit")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            RentMovie()
    elif userInput== 3:
            ReturnMovie()
    elif userInput== 4:
            AddPreference()
    elif userInput == 5:
         running1 = False
    

def adminDisplay():
    print("Hello Admin, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Display all customers")
    print("3. Add movies ")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            DisplayCustomers()

runing = 1
def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput


def DisplayMovies():
    print("Movie List:")
    RentMovies.getMovies()

def DisplayCustomers():
    print("Customer List:")
    RentMovies.getCustomers()

def RentMovie():
    print("Please select a movie from the list below")
    DisplayMovies()
    movieChoice = input("What is your choice: ")
    print("Please select a customer from the list below")
    RentMovies.getCustomers()
    customerChoice = int(input("What is your choice: "))

    # Find the selected movie in the list
    selected_movie = next((movie for movie in RentMovies.Movies_Store if movie.Title == movieChoice), None)
    if selected_movie is None:
        print(f"'{movieChoice}' not found in the movie list.")
        return
    #Find the selected customer in the list
    selected_customer = next((customer for customer in RentMovies.Customers if customer.CustomerId == customerChoice ), None)
    if selected_customer is None:
        print(f"'{customerChoice}' not found in the movie list.")
        return

    # Rent the selected movie to the selected customer with the movie's price
    print(RentMovies.rent_movie(selected_customer, selected_movie))
    print("Movie Rented")

def AddPreference():
    print("Please select a movie from the list below")
    RentMovies.getMovies()
    movieChoice = input("What is your choice: ")

    print("Please select a customer from the list below")
    RentMovies.getCustomers()
    customerChoice = int(input("What is your choice: "))

    # Find the customer with the specified customer ID
    customer = next((c for c in RentMovies.Customers if c.CustomerId == customerChoice), None)

    if customer is None:
        print("Customer not found.")
        return

    print("Please enter the rating of the movie")
    rating = input("What is the rating: ")
    print("Please enter the review of the movie")
    genre = input("What is the genre: ")
    print("Please enter the year of the movie")
    year = input("What is the year: ")

    # Add the movie preference to the customer
    customer.addMoviePreference(movieChoice, genre, year, rating)
    print("Preference added")

def ReturnMovie():
    print("Please select a movie from the list below")
    DisplayMovies()
    movieChoice = input("What is your choice: ")
    if movieChoice not in RentMovies.Movies:
        raise ValueError("Movie not found")
    print("Please select a customer from the list below")
    DisplayCustomers()
    customerChoice = input("What is your choice: ")
    if customerChoice not in RentMovies.Customers:
        raise ValueError("Customer not found")
    
    RentMovies.returnMovie(movieChoice,customerChoice)
    print("Movie Returned")

def exit(var,value):
     var = value 
     return var 

def main():
    InitialDisplay()

while running == True :
    
    def InitialDisplay():
        print("Hello , Welcome to CinemaHouseX2")
        type = chooseWhoYouAre()
        if type == 1:
            running1 = True
            while running1 == True:
                  CustomerDisplay()
        elif type == 2:
            adminDisplay()
        else:
            running == False

if __name__ == "__main__":
    main()
