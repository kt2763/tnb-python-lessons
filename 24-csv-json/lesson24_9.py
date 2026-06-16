import csv

users = [
    {"name": "太郎", "age": 30, "email": "taro@example.com"},
    {"name": "彩花", "age": 25, "email": "ayaka@example.com"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age", "email"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)
