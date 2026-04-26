```python
import json

def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The percentage of the discount to be applied.

    Returns:
        float: The final price after applying the discount.

    Notes:
        The discount is calculated as a percentage of the original price.
        The final price is then calculated by subtracting the discount from the original price.
    """
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

def load_users(filepath: str) -> list:
    """
    Load a list of users from a JSON file.

    Args:
        filepath (str): The path to the JSON file containing the user data.

    Returns:
        list: A list of user dictionaries.

    Raises:
        FileNotFoundError: If the file at the specified filepath does not exist.
        json.JSONDecodeError: If the file at the specified filepath is not valid JSON.

    Notes:
        The JSON file is expected to have a "users" key containing a list of user dictionaries.
    """
    f = open(filepath)
    data = json.load(f)
    return data["users"]

def find_user(users: list, user_id: int) -> dict:
    """
    Find a user by their ID in a list of users.

    Args:
        users (list): A list of user dictionaries.
        user_id (int): The ID of the user to find.

    Returns:
        dict: The user dictionary with the matching ID, or None if no user is found.

    Notes:
        The function iterates over the list of users and checks the "id" key of each user dictionary.
    """
    for user in users:
        if user["id"] == user_id:
            return user

def process_order(user_id: int, items: list, filepath: str) -> dict:
    """
    Process an order for a user.

    Args:
        user_id (int): The ID of the user placing the order.
        items (list): A list of item dictionaries, each containing "price" and "qty" keys.
        filepath (str): The path to the JSON file containing the user data.

    Returns:
        dict: A dictionary containing the user's name and the total cost of the order.

    Notes:
        The function loads the list of users from the JSON file, finds the user with the matching ID,
        calculates the total cost of the order, and applies a discount if the user has a premium membership.
    """
    users = load_users(filepath)
    user = find_user(users, user_id)
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    if user["membership"] == "premium":
        total = calculate_discount(total, 20)
    return {"user": user["name"], "total": round(total, 2)}
```