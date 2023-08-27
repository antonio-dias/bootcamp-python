import requests

class Post:

    def __init__(self):
        self.all_posts = requests.get("https://api.npoint.io/3a7586a2297d432db4ab").json()

    def get_all_posts(self):
        return self.all_posts

    def get_post(self, id):
        for post in self.all_posts:
            if post['id'] == id:
                return post
        return {"status": "Page not found!"}