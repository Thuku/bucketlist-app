"""
Bucketlist Activity controller
"""
from models.bucketlist import BucketList


class Activity(object):
    """
    Activity class
    """
    def add_activity(self, title, name):
        """
        This method adds an activity to a bucketlist
        """
        for bucketlist in BucketList.bucketlists:
            if bucketlist['name'] == title:
                bucket_activity = bucketlist["activities"]
                bucket_activity.append(name)

    def get_bucket_items(self, name):
        """
        This method gets activities(items) of a bucketlist
        """
        for bucketlist in BucketList.bucketlists:
            if bucketlist['name'] == name:
                bucket_items = bucketlist['activities']
                return bucket_items

    def remove_item(self, user_id, title):
        """
        Remove an item from a bucketlist
        """
        print(user_id, title)
        for bucketlist in BucketList.bucketlists:
            if bucketlist['user_id'] == user_id:
                bucket_activity = bucketlist["activities"]
                name = bucketlist['name']
                bucket_activity.remove(title)
        return name
