"""
This module deals with all tasks performed on a bucketlist
"""


class BucketList(object):
    """
    Bucketlist class
    """
    bucketlists = []

    def create_bucketlist(self, name, user_id):
        """
        Create bucketlist
        """
        # initialize bucketlist activity to an empty list
        activity = []

        # initialize status to inprogress
        status = "Inprogress"

        # Bucketlist id
        bl_id = len(self.bucketlists) + 1

        # create new bucketlist
        new_bucket = {"id": bl_id, "user_id": user_id,
                      "name": name, "activities": activity, "status": status}
        self.bucketlists.append(new_bucket)
        print(self.bucketlists)
        return "Bucketlist Created"

    def check_if_bucketlist_exists(self, name):
        """
        Check if a similar bucketlist already exists
        """
        # loop through all bucketlists
        # check if bucketlist already exists
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == name:
                return True

        return False

    def get_users_buckets(self, user_id):
        """
        Get user's buckets using their ID
        """
        # create a list of bucketlists with a given user id
        users_buckets = []
        for bucketlist in self.bucketlists:
            if bucketlist["user_id"] == user_id:
                users_buckets.append(bucketlist)
        return users_buckets

    def delete(self, title):
        """
        delete a bucketlist
        """
        # delete a given bucketlist
        for i, bucketlist in enumerate(self.bucketlists):
            if bucketlist['name'] == title:
                self.bucketlists.pop(i)
                return "Bucket removed"

    def mark_as_complete(self, name):
        """
        Mark a bucketlist as complete
        """
        # Change a bucketlist to status
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == name:
                bucketlist.update([("status", "Complete")])
                return "Bucket complete"

    def inprogress_bucketlist(self, user_id):
        """
        Get all inprogress bucketlist for a given user
        """
        # create a list of user's bucketlist whose status is inprogress
        inprogress = []
        for bucketlist in self.bucketlists:
            if bucketlist["status"] == "Inprogress":
                if bucketlist["user_id"] == user_id:
                    inprogress.append(bucketlist)
        return inprogress

    def latest_bucketlists(self, user_id):
        """
        Get the latest bucket based on users ID
        """
        # Create a list of a user's last 3 bucklists
        users_buckets = []
        for bucketlist in self.bucketlists:
            if bucketlist["user_id"] == user_id:
                users_buckets.append(bucketlist)
        latest = users_buckets[-3:]
        return latest

    def completed_bucketlist(self, user_id):
        """
        get completed bucketlist for a user
        """
        # create a list of user's bucketlist whose status is complete
        completed = []
        for bucketlist in self.bucketlists:
            if bucketlist["status"] == "Complete":
                if bucketlist["user_id"] == user_id:
                    completed.append(bucketlist)
        return completed

    def rename(self, title, name):
        """
        Rename bucketlist
        """
        # rename bucketlist
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == title:
                bucketlist.update([("name", name)])
                return "Bucket renamed"
