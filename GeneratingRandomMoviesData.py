import random
from string import Template
from currency_symbols import CurrencySymbols


# Format the price to 2 decimal places and add the currency symbol
cedis = CurrencySymbols.get_symbol('GHS')
print(f"{cedis}50.0")

def format_Price(price, currency,decimal_places=2):
    """
    Format the price to 2 decimal places and add the currency symbol
    parameters: price, currency,decimal_places=2
    return: Price2
    """
    Price2 = []
    
    # loop through the price list and format the price
    for prices in price:
        money_format = Template(f"{currency}{prices:,.{decimal_places}f}")
        formatted_amount = "{:,.{}f}".format(prices, decimal_places)
        formatted_money = money_format.substitute(currencys = currency,prices=formatted_amount)
        Price2.append(formatted_money)
    return Price2
    
# Generate random data for the movies

titles = ["The Matrix", "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Fight Club","Ariel","The Irish Man","Jungle Story"]
genres = ["Action", "Drama", "Crime", "Comedy", "Animation", "Adventure", "Fantasy", "Horror", "Thriller", "Romance"]
years = ["2019", "2018", "2017", "2016", "2015", "2014", "2013"]
rating = ["PG", "18", "15", "12", "U"]
ratings = ["50%", "60%", "70%", "80%", "90%", "100%"]
descriptions = ["This is a new movie", "This is an old movie"]
tags = ["New", "Old"]
prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
prices2 = format_Price(prices, cedis ,2)

Movies = []

# Generate 10 random movies and add them to the Movies list
for i in range(1,11):
    title = random.choice(titles)
    genre = random.choice(genres)
    year = random.choice(years)
    rating = random.choice(rating)
    description = random.choice(descriptions)
    tag = random.choice(tags)
    price = random.choice(prices2)
    ratings = random.choice(ratings)
    movieid = i
    Movies.append({"Title":title,"Ratings":ratings,"Rating":rating,"Genre":genre,"Year":year,"Price":price,"Tag":tag,"Description":description,"MovieId":movieid})
    print(f"RentMovies.addToStore(title ='{title}',rating ='{rating}', genre ='{genre}',year ='{year}',price='{price}',tag ='{tag}',description ='{description}', movieid ={movieid}, ratings='{ratings}')")

for movie in Movies:
    print("Title:",movie['Title'])
    print("Rating:",movie['Rating'])
    print("Ratings:",movie['Ratings'])
    print("Price:",movie['Price'])
    print("Genre:",movie['Genre'])
    print("Year:",movie['Year'])
    print("Tag:",movie['Tag'])
    print("Description:",movie['Description'])
    print("MovieId:",movie['MovieId'])
    print("")