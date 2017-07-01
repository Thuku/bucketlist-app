"""
User controller
"""


class User(object):
    """
    User class
    """

    users = []

    # Create a new user
    def create_user(self, email, password):
        """
        Creates a new user
        """
        user_id = len(self.users) + 1
        new_user = {"user_id": user_id, "email": email, "password": password}
        self.users.append(new_user)
        print(self.users)
        return True

    # Check if a user exists
    def check_user_exists(self, email):
        """
        Checks if a user with similar email already exists.
        """
        for user in self.users:
            if user["email"] == email:
                print(type(user["email"]))
                print(type(email))
                return True
            else:
                return False

    # Check if a password is alphanumeric
    def check_password_is_alphnum(self, password):
        """
        Check if password is alphanumeric
        """
        return password.isalnum()

    def get_userid(self, email):
        """
        Get user id
        """
        for user in self.users:
            if user["email"] == email:
                return user["user_id"]

    # login a user
    def login(self, email, password):
        """
        Login a user
        """
        for user in self.users:
            if email in dict.values(user):
                if password == user["password"]:
                    return True
                else:
                    return False
