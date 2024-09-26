import json

from csv import DictReader

f_csv = "/Users/user/Desktop/books.csv"
f_json = "/Users/user/Desktop/users.json"


# создала функцию для фильтрации по ключам словаря, если нужно будет избавиться
# от некоторых данных(не знала нужно не нужно, не использовала пока что)
def find(dict_, *v):
    for key in list(dict_.keys()):
        if key.lower() not in v:
            dict_.pop(key)
    return dict_


# открываю файл cvs
# считаю всего кол-во книг
with open(f_csv, newline='') as f2:
    books = DictReader(f2)
    lst_books = list()
    n_of_books = 0
    for row in books:
        lst_books.append(row)
        n_of_books += 1


# считаю кол-во книг, с уникальными названиями
kl = set()
k_books = int()
for i in lst_books:
    kl.add(i["Title"])
k_books = len(kl)


# открываю файл json
# считаю кол-во юзеров n_of_use
with open(f_json, "r") as f:
    users = json.load(f)
    n_of_user = len(users)
    for user in users:
        user = find(user, "name", "gender", "address", "age")


# рассчитаываю, какое равное кол-во книг могу дать каждому юзеру
def n_b_for_user(a, b):
    return a // b


# прохожусь двумя циклами по списку из словарей с юзерами и книгами
# добавляю каждому юзеру по равному кол-ву книг - считается в функции n_b_for_user
names_books = list()
ll = list()
for user in users:
    step = 0
    ll = []
    for row in lst_books:
        if row["Title"] not in names_books:
            if step < n_b_for_user(n_of_books, n_of_user):
                names_books.append(row["Title"])
                ll.append(row)
                user["books"] = ll
                step += 1
            else:
                break
        else:
            continue


# прохожусь двумя циклами по списку из словарей с юзерами и книгами
# добавляю оставшиеся книги
for user in users:
    for row in lst_books:
        if row["Title"] not in names_books:
            names_books.append(row["Title"])
            user["books"].append(row)
            break
        else:
            continue


# создаю файл json
# записываю в файл словарь юзеры+книги
with open("result.json", "w") as f3:
    json.dump(users, f3, indent=4)