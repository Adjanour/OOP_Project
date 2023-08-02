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

    def rent_movie(self, customer_name, movie_title, num_copies):
        # Check if the movie is available for rent
        available_copies = [movie for movie in self.movies_available if movie.title == movie_title]

        if not available_copies:
            print(f"'{movie_title}' is not available for rent or doesn't exist in the store.")
            return

        if len(available_copies) < num_copies:
            print(f"Insufficient copies of '{movie_title}' available. Only {len(available_copies)} copy(s) left.")
            return

        rented_copies = available_copies[:num_copies]
        for copy in rented_copies:
            self.movies_available.remove(copy)

        if customer_name in self.rented_movies:
            self.rented_movies[customer_name].extend(rented_copies)
        else:
            self.rented_movies[customer_name] = rented_copies

        if len(available_copies) == num_copies:
            print(f"All copies of '{movie_title}' have been rented. Movie is finished.")

        print(f"{customer_name} rented {num_copies} copy(ies) of '{movie_title}' successfully!")

    def return_movie(self, customer_name, movie_to_return):
        if customer_name not in self.rented_movies:
            print(f"No movies are currently rented by {customer_name}.")
            return

        elif customer_name in self.rented_movies:
            rented_movies = self.rented_movies[customer_name]
            found_copy = None
            for movie_copy in rented_movies:
                if movie_copy.title == movie_to_return.title:
                    found_copy = movie_copy
                    break

            if found_copy is not None:
                self.movies_available.append(found_copy)
                rented_movies.remove(found_copy)
                print(f"{customer_name} returned '{found_copy.title}' successfully!")
            else:
                print(f"No movie with title '{movie_to_return.title}' is rented by {customer_name}.")

    def getMovieDetails(self):
        for movie in self.movies_available:
            print(movie.get_details())


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
        print("Available Movies:")
        rental_store.getMovieDetails()

        movie_title = input("Enter the title of the movie you want to rent: ")
        num_copies = int(input("How many copies do you want to rent? "))

        rental_store.rent_movie(self.name, movie_title, num_copies)

    def return_movie(self, rental_store):
        print("Movies Currently Rented:")
        if self.name in rental_store.rented_movies:
            for movie in rental_store.rented_movies[self.name]:
                print(movie.get_details())
        else:
            print(f"No movies are currently rented by {self.name}.")

        movie_title = input("Enter the title of the movie you want to return: ")
        movie_to_return = [movie for movie in rental_store.rented_movies[self.name] if movie.title == movie_title]

        if movie_to_return:
            rental_store.return_movie(self.name, movie_to_return[0])
        else:
            print(f"No movie with title '{movie_title}' is rented by {self.name}.")


def main():
    rental_store = RentalStore()

    # Add movies with multiple copies
    movie1 = Movie("Movie1", "Action", 2022)
    movie2 = Movie("Movie2", "Comedy", 2021)
    movie3 = Movie("Movie3", "Drama", 2020)

    rental_store.add_movie(movie1, 3)
    rental_store.add_movie(movie2, 2)
    rental_store.add_movie(movie3, 1)

    while True:
        user_type = input("Are you an admin or user? (Type 'admin' or 'user', or 'exit' to quit): ")

        if user_type.lower() == 'admin':
            # Administrator Section
            while True:
                title = input("Enter the title of the movie (or 'exit' to stop adding movies): ")
                if title.lower() == 'exit':
                    break
                genre = input("Enter the genre of the movie: ")
                release_year = int(input("Enter the release year of the movie: "))
                num_copies = int(input("Enter the number of copies available for rent: "))
                movie = Movie(title, genre, release_year)
                rental_store.add_movie(movie, num_copies)

        elif user_type.lower() == 'user':
            # User Section
            customer_name = input("Enter your name: ")
            email = input("Enter your email address: ")
            customer = Customer(customer_name, email)

            while True:
                print("Please select an option:")
                print("1. Rent a movie")
                print("2. Return a movie")
                print("3. Display movie preferences")
                print("4. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    customer.rent_movie(rental_store)
                elif choice == 2:
                    customer.return_movie(rental_store)
                elif choice == 3:
                    customer.display_preferences()
                elif choice == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif user_type.lower() == 'exit':
            print("Goodbye!")
            break

        else:
            print("Invalid user type. Please enter either 'admin' or 'user', or 'exit' to quit.")


if __name__ == "__main__":
    main()
