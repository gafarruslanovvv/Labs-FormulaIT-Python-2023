import json


def sum_of_products(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    sum_of_products = 0
    for item in data:
        score = item['score']
        weight = item['weight']
        product = score * weight
        sum_of_products += product

    return round(sum_of_products, 3)


file_path = 'input.json'  # путь к файлу JSON
result = sum_of_products(file_path)
print(result)



