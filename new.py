class Movie:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

    def get_details(self):
        return f"Title: {self.title}\nGenre: {self.genre}\nRelease Year: {self.release_year}"


class RentalStore:
    def __init__(self):
        self.movies_available = []  # List to store available movie copies
        self.rented_movies = {}  # Dictionary to track rented movies

    def add_movie(self, movie, num_copies=1):
        for _ in range(num_copies):
            self.movies_available.append(movie)
        # end of admin section
    def rent_movie(self, customer_name, movie_title):
        # Check if the movie is available for rent
        # Checks and finds all copies of the movie and appends them to the  avaiable_copies list
        available_copies = [movie for movie in self.movies_available if movie.title == movie_title]
        if available_copies:
            self.movies_available.remove(available_copies[0])
            if customer_name in self.rented_movies:
                self.rented_movies[customer_name].append(available_copies[0])
            else:
                self.rented_movies[customer_name] = [available_copies[0]]
            print(f"{customer_name} rented '{movie_title}' successfully!")
        else:
            print(f"'{movie_title}' is not available for rent.")

    def return_movie(self, customer_name, movie_to_return):
        # Check if the customer has any movies rented
        if customer_name not in self.rented_movies:
            print(f"No movies are currently rented by {customer_name}.")
            return

        elif customer_name in self.rented_movies:
            # Find the returned movie in the rented movies list
            rented_movies = self.rented_movies[customer_name]
            found_copy = None
            for movie_copy in rented_movies:
                if movie_copy.title == movie_to_return.title:
                    found_copy = movie_copy
                    break

            if found_copy is not None:
                # Add the returned movie copy back to the available movies list
                self.movies_available.append(found_copy)
                # Remove the returned movie copy from the customer's rented movies
                rented_movies.remove(found_copy)
                print(f"{customer_name} returned '{found_copy.title}' successfully!")
            else:
                print(f"No movie with title '{movie_to_return.title}' is rented by {customer_name}.")


class Customer:
    def __init__(self, name, email, movie_preferences=None):
        self.name = name
        self.email = email
        self.movie_preferences = movie_preferences if movie_preferences is not None else []

    def add_preference(self, new_preference):
        if new_preference not in self.movie_preferences:
            self.movie_preferences.append(new_preference)

    def remove_preference(self, to_remove):
        if type(to_remove) == list:
            for x in to_remove:
                if x in self.movie_preferences:
                    self.movie_preferences.remove(x)
        else:
            if to_remove in self.movie_preferences:
                self.movie_preferences.remove(to_remove)

    def display_preferences(self):
        print("Movie Preferences:")
        for preference in self.movie_preferences:
            print(preference)

    def rent_movie(self, rental_store):
        movie_title = input("Enter the title of the movie you want to rent: ")
        rental_store.rent_movie(self.name, movie_title)

    def return_movie(self, rental_store):
        movie_title = input("Enter the title of the movie you want to return: ")
        rental_store.return_movie(self.name, Movie(movie_title, "", 0))


# Example usage:

store = RentalStore()

# Add movies with multiple copies
while True:
    title = input("Enter the title of the movie (or 'exit' to stop adding movies): ")
    if title.lower() == 'exit':
        break
    genre = input("Enter the genre of the movie: ")
    release_year = int(input("Enter the release year of the movie: "))
    num_copies = int(input("Enter the number of copies available for rent: "))
    movie = Movie(title, genre, release_year)
    store.add_movie(movie, num_copies)

# Rent movies
customer_name = input("Enter your name: ")
email = input("Enter your email address: ")
customer = Customer(customer_name, email)
customer.rent_movie(store)

# Return movies
customer.return_movie(store)

# Display customer preferences
customer.add_preference(genre)
customer.display_preferences()
