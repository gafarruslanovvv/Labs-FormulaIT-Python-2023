users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']


dict_ = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

unique_users = set(users)
count_users = len(users)

dict_["Общее количество"] = count_users
dict_["Уникальные посещения"] = len(unique_users)

print(dict_)