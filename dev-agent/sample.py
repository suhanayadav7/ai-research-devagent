import json

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

def load_users(filepath):
    f = open(filepath)
    data = json.load(f)
    return data["users"]

def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

def process_order(user_id, items, filepath):
    users = load_users(filepath)
    user = find_user(users, user_id)
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    if user["membership"] == "premium":
        total = calculate_discount(total, 20)
    return {"user": user["name"], "total": round(total, 2)}
