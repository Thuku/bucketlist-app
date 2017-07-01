"""
Test User model
"""
import unittest
from app import app
from models.user import User


class UserTestcase(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        pass
    # create user and check if user exists

    def test_user_exists(self):
        """
        Check of existence of a given user
        """
        email = "thuku.bonnie@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        response = self.user.check_user_exists(email)
        self.assertEqual(response, True)

    # check if user's password is alphanumeric
    def test_password_is_alphanumeric(self):
        """
        Test for password content
        """
        password = "password"
        response = self.user.check_password_is_alphnum(password)
        self.assertEqual(response, True)

    def test_login(self):
        """
        Test for login
        """
        email = "thuku.bonnie@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        result = self.user.login(email, password)
        self.assertEqual(result, True)
