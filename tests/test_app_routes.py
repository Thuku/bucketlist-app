from app import app
from app import views
import unittest


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_root_page_accessible(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        response = self.app.post('/signup')
        self.assertEqual(response.status_code, 400)
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_create_bucket_route(self):
        response = self.app.post('/create')
        self.assertEqual(response.status_code, 302)

    def test_dashboard(self):
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 302)
