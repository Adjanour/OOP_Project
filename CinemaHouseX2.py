import sys


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
        self.Rating = ratings

    def _get_attr(self, attr_name):
        return getattr(self, '_' + attr_name)

    def _set_attr(self, attr_name, value):
        setattr(self, '_' + attr_name, value)

    def _del_attr(self, attr_name):
        delattr(self, '_' + attr_name)

    # Define properties using the common naming convention
    def _make_property(attr_name):
        return property(
            lambda self: self._get_attr(attr_name),
            lambda self, value: self._set_attr(attr_name, value),
            lambda self: self._del_attr(attr_name)
        )
    
    title = _make_property('title')
    rating = _make_property('rating')
    genre = _make_property('genre')
    year = _make_property('year')
    price = _make_property('price')
    tag = _make_property('tag')
    description = _make_property('description')
    movieid = _make_property('movieid')
    ratings = _make_property('ratings')

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

    def addMoviePreference(self, *moviePreferences):
        self.MoviePreferences.extend(moviePreferences)
    
    def removeMoviePreference(self,moviePreference):
        self.MoviePreferences.remove(moviePreference)

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
        self.Movies = []
        self.Customers = []
        self.RentalsDict = []

    def addToStore(self, title, rating,genre, year, price, tag, description, movieid,ratings):
        movie = Movie(title, rating, genre, year, price, tag, description, movieid,ratings)
        self.Movies.append(movie)

    def removeFromStore(self, movie):
        self.Movies.remove(movie)

    def addCustomer(self, firstName, lastName, age, phone, customerid):
        customer = Customer(firstName, lastName, age, phone, customerid)
        self.Customers.append(customer)

    def removeCustomer(self, customer):
        self.Customers.remove(customer)

    def rentMovie(self, movie, customer, rent_duration):
        self.RentalsDict.append( {
            'Movie': movie,
            'Customer': customer.getID(),
            'Price': movie.getPrice(),
            'Duration': rent_duration
        }
        )
    def add_bulk_movies(self,movies):
        for movie in movies:
            self.Movies.append(movie)
    
    def returnMovie(self, movie, customer):
        self.RentalDict = {}

    def getMovieDetails(self):
        for movie in self.Movies:
            print(movie.getMovieDetails())

    def getCustomers(self):
        for customer in self.Customers:
            print(customer.getCustomerDetails())
    
    def get_total_number_of_movies(self):
        return len(self.Movies)

# Create a rental store
RentMovies = RentalStore()

# Add movies to the store
RentMovies.addToStore(title ='The Dark Knight',rating ='18', genre ='Comedy',year ='2016',price='GH₵10.00',tag ='Old',description ='This is a new movie', movieid =1, ratings='100%')
RentMovies.addToStore(title ='Ariel',rating ='1', genre ='Action',year ='2017',price='GH₵20.00',tag ='New',description ='This is a new movie', movieid =2, ratings='%')
RentMovies.addToStore(title ='Jungle Story',rating ='1', genre ='Animation',year ='2015',price='GH₵30.00',tag ='New',description ='This is a new movie', movieid =3, ratings='%')
RentMovies.addToStore(title ='Fight Club',rating ='1', genre ='Action',year ='2014',price='GH₵10.00',tag ='New',description ='This is a new movie', movieid =4, ratings='%')
RentMovies.addToStore(title ='The Shawshank Redemption',rating ='1', genre ='Horror',year ='2015',price='GH₵20.00',tag ='Old',description ='This is a new movie', movieid =5, ratings='%')
RentMovies.addToStore(title ='The Shawshank Redemption',rating ='1', genre ='Drama',year ='2015',price='GH₵20.00',tag ='New',description ='This is an old movie', movieid =6, ratings='%')
RentMovies.addToStore(title ='The Dark Knight',rating ='1', genre ='Fantasy',year ='2017',price='GH₵40.00',tag ='New',description ='This is a new movie', movieid =7, ratings='%')
RentMovies.addToStore(title ='The Shawshank Redemption',rating ='1', genre ='Romance',year ='2016',price='GH₵40.00',tag ='New',description ='This is an old movie', movieid =8, ratings='%')
RentMovies.addToStore(title ='The Dark Knight',rating ='1', genre ='Fantasy',year ='2018',price='GH₵20.00',tag ='New',description ='This is a new movie', movieid =9, ratings='%')
RentMovies.addToStore(title ='The Matrix',rating ='1', genre ='Romance',year ='2019',price='GH₵35.00',tag ='New',description ='This is an old movie', movieid =10, ratings='%')

# Add customers to the store
RentMovies.addCustomer(first_name = 'Alice', last_name = 'Mandy',age ='16',gender = 'Female',phone_number = '8458092682',customer_id = 0)
RentMovies.addCustomer(first_name = 'Uma', last_name = 'Wendy',age ='24',gender = 'Female',phone_number = '7061293115',customer_id = 1)       
RentMovies.addCustomer(first_name = 'Isabel', last_name = 'Vicky',age ='23',gender = 'Female',phone_number = '2310456043',customer_id = 2)    
RentMovies.addCustomer(first_name = 'Alice', last_name = 'Yvonne',age ='14',gender = 'Female',phone_number = '7394355151',customer_id = 3)    
RentMovies.addCustomer(first_name = 'Xavier', last_name = 'Bernard',age ='15',gender = 'Male',phone_number = '7488790731',customer_id = 4)    
RentMovies.addCustomer(first_name = 'Ivan', last_name = 'Yvonne',age ='20',gender = 'Female',phone_number = '3342957117',customer_id = 5)     
RentMovies.addCustomer(first_name = 'Uma', last_name = 'Terry',age ='19',gender = 'Female',phone_number = '3342957117',customer_id = 6)       
RentMovies.addCustomer(first_name = 'Emma', last_name = 'Carter',age ='15',gender = 'Female',phone_number = '3342957117',customer_id = 7)     
RentMovies.addCustomer(first_name = 'Jenny', last_name = 'Uma',age ='19',gender = 'Female',phone_number = '8458092682',customer_id = 8)       
RentMovies.addCustomer(first_name = 'Xavier', last_name = 'Carter',age ='25',gender = 'Male',phone_number = '2310456043',customer_id = 9) 

def InitialDisplay():
    print("Hello , Welcome to CinemaHouseX2")
    type = chooseWhoYouAre()
    if type == 1:
        CustomerDisplay()
        
    elif type == 2:
        adminDisplay()

    else:
        sys.exit()


def CustomerDisplay():
    print("Hello Customer, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Rent a movie")
    print("3. Return a movie")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            RentMovie()
    elif userInput== 3:
            ReturnMovie()
    

def adminDisplay():
    print("Hello Admin, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all movies")
    print("2. Display all customers")
    userInput = int(input("What is your choice: "))
    if userInput == 1:
            DisplayMovies()
    elif userInput == 2:
            DisplayCustomers()

def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput

def DisplayMovies():
    RentMovies.getMovieDetails()

def DisplayCustomers():
    RentMovies.getCustomers()


def RentMovie():
    print("Please select a movie from the list below")
    DisplayMovies()
    movieChoice = input("What is your choice: ")
    print("Please select a customer from the list below")
    DisplayCustomers()
    customerChoice = input("What is your choice: ")
    print("Please enter the price of the movie")
    price = input("What is your choice: ")
    print("Please enter the duration of the rental")
    duration = input("What is your choice: ")
    RentMovies.rentMovie(movieChoice,customerChoice,price,duration)
    print("Movie Rented")

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

def exit():
    print("Goodbye")
    sys.exit()

def main():
    InitialDisplay()


if __name__ == "__main__":
    main()