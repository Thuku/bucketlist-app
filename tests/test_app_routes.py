"""
Test routes response
"""
import unittest
from app import app


class FlaskAppTestCase(unittest.TestCase):
    """
    This class tests routes to ensure flask is setup correctly
    """

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_root_page_accessible(self):
        """
        Checks the root page is setup correctly
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        """
        check sign up page
        """
        response = self.app.post('/signup')
        self.assertEqual(response.status_code, 400)
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_create_bucket_route(self):
        """
        Check create is setup
        """
        response = self.app.post('/create')
        self.assertEqual(response.status_code, 302)

    def test_dashboard(self):
        """
        check for dashboard page
        """
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 302)
