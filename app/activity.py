from app.bucketlist import BucketList


class Activity(object):
    def add_activity(self, title, name):
        for bucketlist in BucketList.bucketlists:
            if bucketlist['name'] == title:
                bucket_activity = bucketlist["activities"]
                bucket_activity.append(name)

    def get_bucket_items(self, name):
        for bucketlist in BucketList.bucketlists:
            if bucketlist['name'] == name:
                bucket_items = bucketlist['activities']
                return bucket_items

    def remove_item(self, user_id, title):
        print(user_id, title)
        for bucketlist in BucketList.bucketlists:
            if bucketlist['user_id'] == user_id:
                bucket_activity = bucketlist["activities"]
                name=bucketlist['name']
                bucket_activity.remove(title)
        return name
