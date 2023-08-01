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

    def addCustomer(self, firstName, lastName, age,gender, phone, customerid):
        customer = Customer(firstName, lastName, age,gender, phone, customerid)
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

def InitialDisplay():
    print("Hello , Welcome to CinemaHouseX2")
    type = chooseWhoYouAre()
    if type == 1:
        CustomerDisplay()
        
    elif type == 2:
        adminDisplay()

    else:
        exit()


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
    exit()

def main():
    InitialDisplay()


if __name__ == "__main__":
    main()