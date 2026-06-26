from app.models.user_model import User

users = [
    User(
        id=1,
        name="John",
        email="john@example.com",
        age=25
    ),
    User(
        id=2,
        name="Mike",
        email="mike@example.com",
        age=30
    )
]

def get_users():
    return users

def get_user_by_id(user_id: int):
    return next(
        (user for user in users if user.id == user_id),
        None
    )

def create_user(user: User):
    users.append(user)
    return user

def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user

    return None

def delete_user(user_id: int):

    global users

    before = len(users)

    users = [
        user for user in users
        if user.id != user_id
    ]

    return len(users) < before