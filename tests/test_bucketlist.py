from app import bucket, user
import unittest


class BucketlistTestCase(unittest.TestCase):

    def setUp(self):
        self.user = user.User()
        self.bucket = bucket

    def tearDown(self):
        pass

    # Test bucketlist is created correctly
    def test_create_bucket(self):
        email = "thuku.bonnie@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        user_id = self.user.get_userid(email)
        response = self.bucket.create_bucketlist("run wild", user_id)
        self.assertEqual(response, "Bucketlist Created")
