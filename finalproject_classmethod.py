import random

# DATA BASE
users = []
food_items = []
orders = []

class user:
    def __init__(self,Fullname,Phone_number,Email,Address,Password):
        self.user_id = random.randint(1000,9999) #generate a random user id
        self.Fullname = Fullname
        self.Phone_number = Phone_number
        self.Email = Email
        self.Address = Address
        self.Password = Password 
class food_item:
    def __init__(self,foodname,quantity,price,discount,stock):
        self.food_id = random.randint(100000,999999) # generate a random food id
        self.foodname = foodname
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
class order:
    def __init__(self,user_id,food_items_ids,total_prize):
        self.order_id =  random.randint(100000,999999)  # generate a random order id
        self.user_id = user_id
        self.food_items = food_items_ids
        self.total_prize = total_prize

# ADMIN FUNCTINALITIES 
def add_food_item():
    foodname = input('enter food item name:')
    quantity = input('enter quantity required:')
    price = float(input('enter the price:'))
    discount = float(input('enter discount:'))
    stock = int(input('enter stock amount:'))
    food_item_1 = food_item(foodname,quantity,price,discount,stock)
    food_items.append(food_item_1)
    print('food item has been added successfully!')

def edit_food_item():
    food_id = int(input('enter the food item id:'))
    food_item = find_food_item_by_id(food_id)
    if food_item:
        food_item.name = input('enter new name:')
        food_item.quantity = input('enter new quantity:')
        food_item.price = float(input('enter new price:'))
        food_item.discount = float(input('enter new discount:'))
        food_item.stock = int(input('enter new stock:'))
        print('food item updated successfully!')
    else:
        print('food item not found!')
def view_food_items():
    if len(food_items) > 0:
        for item in food_items:
            print(f"id: {item.food_id}, name: {item.name}, quantity: {item.quantity}, price: {item.price}")
    else:
        print('no food items available.')
def remove_food_item():
    food_id = int(input('enter food item id:'))
    food_item = find_food_item_by_id()
    if food_item:
        food_items.remove(food_item)
        print('food item has been removed successfully!')
    else:
        print('food item not found!')

#USER FUNCTIONALITIES
def register_user():
    Fullname = input('enter your fullname:')
    Phone_number = input('enter your phone number:')
    Email = input('enter your email id:')
    Address = input('enter the address:')
    Password = input('enter the password:')
    User = user(Fullname,Phone_number,Email,Address,Password)
    users.append(User)
    print('user registered successfully.')

def login():
    Email = input('enter email:')
    Password = input('enter the password:')
    User = find_user_by_email(Email)
    if User and User.Password == Password:
        print('login procees has susscessfully completed!')
        show_user_menu(User)
    else:
        print('invalid email or password.')
def place_new_order(User):
    view_food_items()
    selected_items = input('enter the food items you want to order(comma-separated): ')
    selected_ids = [int(id)for id in selected_items.split(',')]
    order_items = []
    total_price = 0
    for food_id in selected_ids:
        food_item = find_food_item_by_id(food_id)
        if food_item:
            order_items.append(food_item)
            total_price += (food_item.price - (food_item.price * food_item.discount / 100))
        if len(order_items) > 0:
            Order = order(User.user_id,selected_ids,total_price)
            orders.append(Order)
            print('order placed successfully.')
        else:
            print('no items are selected for order!')

def view_order_history(user):
    user_orders = find_orders_by_user_id(user.user_id)
    for order in user_orders:
        print(f"order id: {order.order_id}, food item id: {order.food_item_ids}, total price: {order.total_price}")

def update_profile(user):
    Fullname = input('enter new fullname:')
    Phone_number = input('enter new phone number:')
    Address = input('enter new address:')
    user.Fullname = Fullname
    user.Phone_number = Phone_number
    user.Address = Address
    print('profile updated successfully!')

# HELPER FUNCTIONS
def find_food_item_by_id(food_id):
    for item in food_items:
        if item.food_id == food_id:
            return item
        return None
def find_user_by_email(Email):
    for user in users:
        if user in user.Email == Email:
            return user
        return None
def find_orders_by_user_id(user_id):
    user_orders = []
    for order in orders:
        if order.user_id == user_id:
            user_orders.append(order)
    return user_orders

# MENU FUNCTION
def show_admin_menu():
    print('-------------ADMIN MENU--------------')
    print('1). Add new food item')
    print('2). Edit food item')
    print('3). View food items')
    print('4). Remove food items')
    print('-------------------------------------')

def show_user_menu(user):
    print('--------------USER MENU---------------')
    print('1). Place new order')
    print('2). Order history')
    print('3). Update profile')
    print('4). logut')
    print('--------------------------------------')

    choice = int(input('enter your choice:'))
    if choice == 1:
        place_new_order(user)
    elif choice == 2:
        view_order_history(user)
    elif choice == 3:
        update_profile(user)
    elif choice == 4:
        print('logged out successfully!')
        return
    else:
        print('invalid choice.')

# MAIN PROGRAM
def main():
    while True:
        print('---------FOOD ORDERING APP--------')
        print('1). Admin login')
        print('2). User login')
        print('3). User registration')
        print('4). Exit')
        print('----------------------------------')

        choice = int(input('enter your choice: '))
        if choice ==  1:
            admin_password = input('enter admin password:')
            if admin_password == 'admin123':
                show_admin_menu()
                admin_choice = int(input('enter your choice:'))
                if admin_choice == 1:
                    add_food_item()
                elif admin_choice == 2:
                    edit_food_item()
                elif admin_choice == 3:
                    view_food_items()
                elif admin_choice == 4:
                    remove_food_item()
                else:
                    print('invalid choice!')
            else:
                print('invalid admin password!')
        elif choice == 2:
            login()
        elif choice == 3:
            register_user()
        elif choice == 4:
            print('thank you for using food ordering app!')
            break
        else:
            print('invalid choice!')
if __name__ ==  "__main__":
    main()