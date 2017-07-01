"""
Test bucketlist class
"""
import unittest
from app import app


class AppTestCase(unittest.TestCase):
    """
    Check response data in routes
    """

    # check flask is set correctly
    def test_index(self):
        """
        The login page
        """
        tester = app.test_client(self)
        respose = tester.get('/login', content_type='html/text')
        self.assertEqual(respose.status_code, 200)

    # ensure login words correctly if user is not registered
    def test_login(self):
        """
        Login without registration
        """
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(email='ebso24vi@gmail.com', password='root'), follow_redirects=True)
        print(response.data)
        self.assertIn(b'Email does not exist. Please sign up', response.data)

    # ensure that you can not access dashboard if not signed in
    def test_main_route_requires_login(self):
        """
        Trying to acces dashboard without permission
        """
        tester = app.test_client(self)
        response = tester.get('/dashboard', follow_redirects=True)
        self.assertTrue(b'You need to login first' in response.data)


if __name__ == '__main__':
    unittest.main()
