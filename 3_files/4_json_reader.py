import json
from files import JSON_FILE_PATH

# Вот так лучше не делать "../files/example.json"
with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)
print(users)
users_list = users['users']
print(users_list)
for user in users_list:
    print(user)
