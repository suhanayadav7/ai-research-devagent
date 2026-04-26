```python
# tests.py
import pytest
import json
from your_module import calculate_discount, load_users, find_user, process_order  # replace 'your_module' with the actual name of your module

def test_calculate_discount():
    # Test case 1: Normal discount calculation
    price = 100
    discount_percent = 20
    expected_discount = 20
    expected_final_price = 80
    assert calculate_discount(price, discount_percent) == expected_final_price

    # Test case 2: Zero discount
    price = 100
    discount_percent = 0
    expected_final_price = 100
    assert calculate_discount(price, discount_percent) == expected_final_price

    # Test case 3: 100% discount
    price = 100
    discount_percent = 100
    expected_final_price = 0
    assert calculate_discount(price, discount_percent) == expected_final_price

    # Test case 4: Negative price
    price = -100
    discount_percent = 20
    with pytest.raises(ValueError):
        calculate_discount(price, discount_percent)

    # Test case 5: Negative discount
    price = 100
    discount_percent = -20
    with pytest.raises(ValueError):
        calculate_discount(price, discount_percent)

def test_load_users():
    # Test case 1: Valid JSON file
    with open('test_users.json', 'w') as f:
        json.dump({'users': [{'id': 1, 'name': 'John'}]}, f)
    users = load_users('test_users.json')
    assert len(users) == 1
    assert users[0]['id'] == 1
    assert users[0]['name'] == 'John'

    # Test case 2: Invalid JSON file
    with open('test_users.json', 'w') as f:
        f.write('Invalid JSON')
    with pytest.raises(json.JSONDecodeError):
        load_users('test_users.json')

    # Test case 3: File not found
    with pytest.raises(FileNotFoundError):
        load_users('non_existent_file.json')

def test_find_user():
    # Test case 1: User found
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    user_id = 1
    user = find_user(users, user_id)
    assert user['id'] == user_id
    assert user['name'] == 'John'

    # Test case 2: User not found
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    user_id = 3
    user = find_user(users, user_id)
    assert user is None

def test_process_order():
    # Test case 1: Normal order processing
    user_id = 1
    items = [{'price': 10, 'qty': 2}, {'price': 20, 'qty': 1}]
    with open('test_users.json', 'w') as f:
        json.dump({'users': [{'id': user_id, 'name': 'John', 'membership': 'premium'}]}, f)
    result = process_order(user_id, items, 'test_users.json')
    assert result['user'] == 'John'
    assert result['total'] == 36.0

    # Test case 2: Non-premium user
    user_id = 1
    items = [{'price': 10, 'qty': 2}, {'price': 20, 'qty': 1}]
    with open('test_users.json', 'w') as f:
        json.dump({'users': [{'id': user_id, 'name': 'John', 'membership': 'basic'}]}, f)
    result = process_order(user_id, items, 'test_users.json')
    assert result['user'] == 'John'
    assert result['total'] == 40.0

    # Test case 3: User not found
    user_id = 2
    items = [{'price': 10, 'qty': 2}, {'price': 20, 'qty': 1}]
    with open('test_users.json', 'w') as f:
        json.dump({'users': [{'id': 1, 'name': 'John', 'membership': 'premium'}]}, f)
    with pytest.raises(KeyError):
        process_order(user_id, items, 'test_users.json')

    # Test case 4: Invalid file
    user_id = 1
    items = [{'price': 10, 'qty': 2}, {'price': 20, 'qty': 1}]
    with pytest.raises(FileNotFoundError):
        process_order(user_id, items, 'non_existent_file.json')
```

Note: Make sure to replace `'your_module'` with the actual name of your module in the import statement. Also, the `test_users.json` file is created and deleted during the test, so make sure to run the tests in a directory where you have write permission.