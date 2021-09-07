from copy import deepcopy
from jsonschema import validate


DEFAULT_USER_LIST = [
{
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]


class UserExistError(Exception):

    def __str__(self):
        return "User is already exist"


class UserNotFoundError(Exception):

    def __str__(self):
        return "User not found"


USER_LIST = deepcopy(DEFAULT_USER_LIST)


class Users:

    def __init__(self):
        self.reset_user()

    @staticmethod
    def reset_user():
        USER_LIST.clear()
        USER_LIST.extend(deepcopy(DEFAULT_USER_LIST))

    @staticmethod
    def add_user(user_data):
        USER_LIST.extend(user_data)

    @staticmethod
    def get_users():
        return [*USER_LIST]

    @staticmethod
    def get_user(field_name, field_value):
        return next((user for user in USER_LIST if user[field_name] == field_value), None)

    def remove_user(self, user_id):
        self.validate_user_not_found(user_id)
        USER_LIST.clear()
        USER_LIST.extend(user for user in USER_LIST if user["id"] != user_id)

    def add_user(self, user_data):
        self.validate_user_data(user_data)
        user_id = user_data["id"]
        self.validate_user_exist(user_id)
        USER_LIST.append(user_data)

    def get_user_by_id(self, user_id):
        return self.get_user("id", user_id)

    def get_user_by_username(self, username):
        return self.get_user("username", username)

    def update_user(self, user_id, updated_field):
        self.validate_user_not_found(user_id)
        self.validate_user_data({**updated_field, "id" : user_id})

        user = self.get_user_by_id(user_id)
        user.update(updated_field)
        return user

    def is_user_exist(self, user_id):
        return self.get_user_by_id(user_id)

    @staticmethod
    def validate_user_data(user_data):
        schema = {
            "type": "object",
            "properties": {
                # In real life, id is generated on the backend side when user created
                "id": {"type": "number"},
                "username": {"type": "string"},
                "firstName": {"type": "string"},
                "lastName": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string"},
            },
            "required": ["id", "username", "firstName", "email", "password"]
        }

        validate(instance=user_data, schema=schema)

    def validate_user_exist(self, user_id):
        if self.is_user_exist(user_id):
            raise UserExistError

    def validate_user_not_found(self, user_id):
        if not self.is_user_exist(user_id):
            raise UserNotFoundError
