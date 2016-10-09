import json

def save_data(user, data, file_name):
    """Add user to users list and save to json file"""

    if user not in data["users"]:
        data["users"].append(user)
        with open(file_name, 'w') as data_file:
            json.dump(data, data_file)
        print("User {} successfully added to users".format(user))
    else:
        print('Cant add User {} to users, its already in users'.format(user))

def get_data(file_name):
    """Opens json file and returns the data"""

    with open(file_name) as data_file:
        data = json.load(data_file)
    return data

def login(file_name):
    username = input("Enter username: ")
    password = input("Enter password: ")
    data = get_data(file_name)
    find = any(user['username'] == username and user['password'] == password for user in data["users"])
    if find:
        userFound = next((user for user in data["users"] if user["username"] == username and user['password'] == password))
        return {"logged": True, "user": userFound}
    return {"logged": False, "user": None}

def get_balance(user):
    if user["logged"]:
        print("Your balance is {} EUR".format(user["user"]["balance"]))
    else:
        print("You are not logged in!")

# json data file constant
FILE_NAME = "data.json"

# create new user
user = {
    "name"     : "Erkki",
    "lastname" : "Matilainen",
    "username" : "erkmati",
    "password" : "myBank!2016",
    "balance"  : 30.40
}

# get data from json file
#data = get_data(FILE_NAME)
user = login(FILE_NAME)
get_balance(user)
# save created user to json file
#save_data(user,data,FILE_NAME)

