"""
Test Bucketlist class
"""
import unittest
from models.bucketlist import BucketList
from models.user import User


class BucketlistTestCase(unittest.TestCase):
    """
    Test various functions in bucketlist class
    """

    def setUp(self):
        self.user = User()
        self.bucket = BucketList()

    def tearDown(self):
        pass

    # Test bucketlist is created correctly
    def test_create_bucket(self):
        """
        Create a bucketlist
        """
        email = "thuku.bonnie@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        user_id = self.user.get_userid(email)
        response = self.bucket.create_bucketlist("run wild", user_id)
        self.assertEqual(response, "Bucketlist Created")
    # test rename bucketlist

    def test_rename_bucket(self):
        """
        Rename a bucketlist
        """
        email = "thuku.bonnie@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        user_id = self.user.get_userid(email)
        self.bucket.create_bucketlist("run wild", user_id)
        response = self.bucket.rename("run wild", "run slow")
        self.assertEqual(response, "Bucket renamed")

    def test_bucketlist_exists(self):
        """
        Test for existence of a bucketlist
        """
        response = self.bucket.check_if_bucketlist_exists("run wild")
        self.assertEqual(response, False)

    def test_delete_bucket(self):
        """
        Delete a bucket
        """
        self.test_create_bucket()
        response = self.bucket.delete("run wild")
        self.assertEqual(response, "Bucket removed")

    def test_mark_as_complete(self):
        """
        Test mark a bucket as complete
        """
        self.test_create_bucket()
        response = self.bucket.mark_as_complete("run wild")
        self.assertEqual(response, "Bucket complete")

    def test_get_users_buckets(self):
        """
        Get all buckets for a given user
        """
        email = "thuku@gmail.com"
        password = "password"
        self.user.create_user(email, password)
        user_id = self.user.get_userid(email)
        self.bucket.create_bucketlist("run wild", user_id)
        buckets = self.bucket.get_users_buckets(user_id)
        self.assertEqual(buckets, [
                         {'id': 2, 'user_id': 3, 'name': 'run wild', 'activities': [], 'status': 'Inprogress'}])

    def test_latest_bucket(self):
        """
        Test to get latest buckets for a user
        """
        email = "thuku@gmail.com"
        user_id = self.user.get_userid(email)
        latest = self.bucket.latest_bucketlists(user_id)
        length_latest = len(latest)
        self.assertEqual(length_latest, 1)

    def test_completed_bucketlist(self):
        """
        Test for completed bucketlist
        """
        email = "thuku@gmail.com"
        user_id = self.user.get_userid(email)
        result = self.bucket.completed_bucketlist(user_id)
        completed = len(result)
        self.assertEqual(completed, 0)

    def test_inprogress_bucketlist(self):
        """
        Test for bucketlists in progress
        """
        email = "thuku@gmail.com"
        user_id = self.user.get_userid(email)
        result = self.bucket.inprogress_bucketlist(user_id)
        inprogress = len(result)
        self.assertEqual(inprogress, 1)
