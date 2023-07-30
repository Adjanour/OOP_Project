import random
import string

first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabel", "John","Issabella","Bernard","James","Syrus","Andy","Bobby","Cindy","Derek","Ethan","Fiona","Gavin","Hannah","Ivan","Jenny","Kenny","Linda","Mandy","Nancy","Oscar","Penny","Quincy","Randy","Sandy","Terry","Uma","Vicky","Wendy","Xavier","Yvonne","Zack"]
last_names = ["Katamanso","Bernard","Carter","Davids","Ethan","Fisher","Gavin","Hannah","Ivan","Jenny","Kenny","Linda","Mandy","Nancy","Oscar","Penny","Quincy","Randy","Sandy","Terry","Uma","Vicky","Wendy","Xavier","Yvonne","Zack"]
genders = ["Male", "Female"]
ages = range(10, 26)

# Generate a list of phone numbers
phone_numbers = []
for i in range(10):
    phone_number = ''.join(random.choices(string.digits, k=10))
    phone_numbers.append(phone_number)

# Generate a list of dictionaries with the data
data = []
for i in range(10):
    first_name = random.choice(first_names) 
    last_name = random.choice(last_names)
    age = random.choice(ages)
    gender = random.choice(genders)
    phone_number = random.choice(phone_numbers)
    customer_id = i
    print(f"RentMovies.addCustomer(first_name = '{first_name}', last_name = '{last_name}',age ='{age}',gender = '{gender}',phone_number = '{phone_number}',customer_id = {customer_id})")
    data.append({"name":first_name + last_name, "age":age, "gender":gender , "phone_number":phone_number, "customer_id":customer_id})

for customer in data:
    print("Name:",customer['name'])
    print("Age:",customer['age'])
    print("Gender:",customer['gender'])
    print("Phone Number:",customer['phone_number'])
    print("Customer ID:",customer['customer_id'])
    print("")