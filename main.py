import csv
import json


def read_books(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def read_users(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def distribute_books(books, users):
    result = []

    if not users and books:
        raise ValueError("Нет пользователей для распределения книг")

    for user in users:
        result.append({
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        })

    for index, book in enumerate(books):
        user_index = index % len(result)

        result[user_index]["books"].append({
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        })
    return result


def write_result(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    books = read_books("books.csv")
    users = read_users("users.json")
    result = distribute_books(books, users)
    write_result("result.json", result)


if __name__ == "__main__":
    main()