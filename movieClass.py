class Movie:
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

    def get_details(self):
        return f"Title: {self.title}\nGenre: {self.genre}\nRelease Year: {self.release_year}"


class RentalStore:
    def __init__(self):
        self.movies_available = []
        self.rented_movies = {}

    def add_movie(self, movie):
        self.movies_available.append(movie)

    def rent_movie(self, customer_name, movie_title):
        for i in range(len(self.movies_available)):
            if self.movies_available[i].title == movie_title:
                self.rented_movies[customer_name] = [self.movies_available.pop(i)]
                print(f"{customer_name} rented '{movie_title}' successfully!")
                return

        print(f"'{movie_title}' is not available for rent.")

    def return_movie(self, customer_name, movie_to_return):
        # Check if the customer has any movies rented
        if customer_name not in self.rented_movies:
            print(f"No movies are currently rented by {customer_name}.")
            return

        # Find the index of the returned movie
        found_index = -1
        for i in range(len(self.rented_movies[customer_name])):
            if self.rented_movies[customer_name][i].title == movie_to_return.title:
                found_index = i

        # If the returned movie was found, remove it from the list and add it back to inventory
        if found_index != -1:
            self.movies_available.append(self.rented_movies[customer_name].pop(found_index))
            print(f"{customer_name} returned '{movie_to_return.title}' successfully!")
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

# Add movies
while True:
    title = input("Enter the title of the movie (or 'exit' to stop adding movies): ")
    if title.lower() == 'exit':
        break
    genre = input("Enter the genre of the movie: ")
    release_year = int(input("Enter the release year of the movie: "))
    movie = Movie(title, genre, release_year)
    store.add_movie(movie)

# Rent movies
customer_name = input("Enter your name: ")
email = input("Enter your email address: ")
customer = Customer(customer_name, email)
customer.rent_movie(store)

# Return movies
customer.return_movie(store)

# Display customer preferences
customer.add_preference("Comedy")
customer.display_preferences()
