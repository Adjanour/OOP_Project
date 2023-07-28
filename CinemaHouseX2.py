class Movie():
    def __init__(self, title, rating, genre, year, price, tag, description, movieid):
        self.Title = title
        self.Rating = rating
        self.Genre = genre
        self.Year = year
        self.Price = price
        self.Tag = tag
        self.Description = description
        self.MovieId = movieid

    def getMovieDetails(self):
        return f"{self.Title} ,{ self.Rating },{self.Genre },{self.Year},{self.Price } ,{ self.Tag } ,{ self.Description }, {self.MovieId}"

    def __str__(self) -> str:
        return f"This is a movie with title: {self.title} genre:{self.Genre}"

class Customer():
    def __init__(self, firstName, lastName, age, phone, customerid):
        self.CustomerId = customerid
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age
        self.Phone = phone
        self.MoviePreferences = []

    def getCustomerDetails(self):
        return (self.CustomerId, self.FirstName, self.LastName, self.Age, self.Phone)

    def getFullName(self):
        return self.FirstName + " " + self.LastName

    def addMoviePreference(self, *moviePreferences):
        self.MoviePreferences.extend(moviePreferences)
    
    def removeMoviePreference(self,moviePreference):
        self.MoviePreferences.remove(moviePreference)

    def getDetails(self):
        return f"{self.FirstName},{ self.LastName} ,{str(self.Age)} , {self.Phone },{ self.CustomerId } ,{str(self.MoviePreferences)}"


class RentalStore():
    # stores all movies , customers and rentals
    def __init__(self):
        self.Movies = []
        self.Customers = []
        self.RentalDict = []

    def addToStore(self, title, rating, genre, year, price, tag, description, movieid):
        movie = Movie(title, rating, genre, year, price, tag, description, movieid)
        self.Movies.append(movie)

    def removeFromStore(self, movie):
        self.Movies.remove(movie)

    def addCustomer(self, firstName, lastName, age, phone, customerid):
        customer = Customer(firstName, lastName, age, phone, customerid)
        self.Customers.append(customer)

    def removeCustomer(self, customer):
        self.Customers.remove(customer)

    def rentMovie(self, movie, customer, price, duration):
        self.RentalDict .append( {
            'Movie': movie,
            'Customer': customer,
            'Price': price,
            'Duration': duration
        }
        )
   

    def returnMovie(self, movie, customer):
        self.RentalDict = {}

    def getMovieDetails(self):
        for movie in self.Movies:
            print(movie.getMovieDetails())

    def getCustomers(self):
        for customer in self.Customers:
            print(customer.getCustomerDetails())


RentMovies = RentalStore()
RentMovies.addToStore("JamesTown", "50%", "Action", "2019", 5, "New", "This is a new movie", "1")
RentMovies.addCustomer("John", "Doe", "25", "1234567890", "1")
RentMovies.addCustomer("Jane", "Doe", "25", "1234567890", "2")
RentMovies.addCustomer("Jack", "Doe", "25", "1234567890", "3")
RentMovies.addCustomer("Jill", "Doe", "25", "1234567890", "4")
RentMovies.getCustomers()
RentMovies.rentMovie("JamesTown", "John", 5, 2)
RentMovies.rentMovie("JamesTown", "Jane", 5, 2)
print(RentMovies.RentalDict)

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