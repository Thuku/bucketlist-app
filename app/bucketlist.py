class BucketList(object):
    bucketlists = []

    def create_bucketlist(self, name, user_id):
        activity = []
        status = "Inprogress"
        bl_id = len(self.bucketlists) + 1
        new_bucketlist = {"id": bl_id, "user_id": user_id,
                          "name": name, "activities": activity, "status": status}
        self.bucketlists.append(new_bucketlist)
        print(self.bucketlists)
        return "Bucketlist Created"

    def check_if_bucketlist_exists(self, name):
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == name:
                return True
        else:
            return False

    def get_users_buckets(self, user_id):
        users_buckets = []
        for bucketlist in self.bucketlists:
            if bucketlist["user_id"] == user_id:
                users_buckets.append(bucketlist)
        return users_buckets

    def delete(self, title):
        for i, bucketlist in enumerate(self.bucketlists):
            if bucketlist['name'] == title:
                self.bucketlists.pop(i)
                break

    def mark_as_complete(self, name):
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == name:
                bucketlist.update([("status", "Complete")])

    def inprogress_bucketlist(self, user_id):
        inprogress = []
        for bucketlist in self.bucketlists:
            if bucketlist["status"] == "Inprogress":
                if bucketlist["user_id"] == user_id:
                    inprogress.append(bucketlist)
        return inprogress

    def latest_bucketlists(self, user_id):
        users_buckets = []
        for bucketlist in self.bucketlists:
            if bucketlist["user_id"] == user_id:
                users_buckets.append(bucketlist)
        latest = users_buckets[-3:]
        return latest

    def completed_bucketlist(self, user_id):
        completed = []
        for bucketlist in self.bucketlists:
            if bucketlist["status"] == "Complete":
                if bucketlist["user_id"] == user_id:
                    completed.append(bucketlist)
        return completed

    def rename(self, title, name):
        for bucketlist in self.bucketlists:
            if bucketlist["name"] == title:
                bucketlist.update([("name", name)])
