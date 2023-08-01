class Movie():
    """
    Represents a Movie object with various attributes.

    Attributes:
        Title (str): The title of the movie.
        Rating (str): The movie's rating.
        Genre (str): The genre of the movie.
        Year (int): The release year of the movie.
        Price (str): The price of renting the movie.
        Tag (str): A tag associated with the movie.
        Description (str): A brief description of the movie.
        MovieId (int): An ID assigned to the movie.
        Ratings (str): The movie's ratings.

    Methods:
        getMovieDetails(): Returns a formatted string containing details about the movie.
        getPrice(): Returns the price of the movie as a floating-point number.
        __str__(): Returns a formatted string describing the movie.

    Note:
        The class uses properties to manage attributes with the naming convention,
        making them accessible as properties (e.g., movie.title).

    Example:
        movie = Movie("The Matrix", "PG-13", "Sci-Fi", 1999, "$3.99", "Action", 
                "A computer hacker learns the truth about reality.", 101, "8.7/10")
        print(movie.getMovieDetails())
    """

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

    """
    Represents a Customer object with various attributes.

    Attributes:
        CustomerId (int): An ID assigned to the customer.
        FirstName (str): The first name of the customer.
        LastName (str): The last name of the customer.
        Age (int): The age of the customer.
        Gender (str): The gender of the customer.
        Phone (str): The phone number of the customer.
        MoviePreferences (list): A list of movie preferences for the customer.
        ShoppingCart (list): A list of movies in the customer's shopping cart.

    Methods:
        getCustomerDetails(): Returns a tuple containing details about the customer.
        getFullName(): Returns the full name of the customer.
        addMoviePreference(*moviePreferences): Adds movie preferences to the customer's list.
        removeMoviePreference(moviePreference): Removes a movie preference from the list.
        getID(): Returns the customer's ID.
        getName(): Returns the full name of the customer.
        getMoviePreferences(): Returns the list of movie preferences.
        getDetails(): Returns a formatted string containing details about the customer.

    Example:
        customer = Customer("John", "Doe", 30, "Male", "555-1234", 101)
        customer.addMoviePreference("Action", "Adventure")
        print(customer.getDetails())
    """

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

    """
    Represents a Rental Store that manages movies, customers, and rentals.

    Attributes:
        Movies (list): A list of Movie objects in the store.
        Customers (list): A list of Customer objects in the store.
        RentalsDict (list): A list of rental records as dictionaries.

    Methods:
        addToStore(title, rating, genre, year, price, tag, description, movieid, ratings):
            Adds a new Movie to the store.
        removeFromStore(movie): Removes a Movie from the store.
        addCustomer(firstName, lastName, age, phone, customerid): Adds a new Customer to the store.
        removeCustomer(customer): Removes a Customer from the store.
        rentMovie(movie, customer, rent_duration): Records a rental transaction.
        add_bulk_movies(movies): Adds multiple movies to the store at once.
        returnMovie(movie, customer): Records the return of a movie (not fully implemented).
        getMovieDetails(): Prints details of all movies in the store.
        getCustomers(): Prints details of all customers in the store.
        get_total_number_of_movies(): Returns the total number of movies in the store.

    Note:
        The returnMovie() method is present but not fully implemented.

    Example:
        rental_store = RentalStore()
        rental_store.addToStore("The Matrix", "PG-13", "Sci-Fi", 1999, "$3.99", "Action", 
                                "A computer hacker learns the truth about reality.", 101, "8.7/10")
        print(rental_store.get_total_number_of_movies())
    """
     

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
