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

# json data file constant
FILE_NAME = "data.json"

# create new user
user = {
    "name"     : "Jaakko",
    "lastname" : "Simonen"
}

# get data from json file
data = get_data(FILE_NAME)

# save created user to json file
save_data(user,data,FILE_NAME)

