class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.posts = []

    def create_post(self, content ):
        post = Post(content, self)
        return self.posts.append(post)

    def comment_on_post(self, post, content):
        comment = Comment(content, self)
        return post.add_comment(comment)


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []

    def add_comment(self, comment):
        return self.comments.append(comment)

class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author


# Example usage:
user1 = User(1, "John")
user2 = User(2, "Peter")

user1.create_post("Hello, this is my first post!")
user1.create_post("Hello, this is my second post!")
user1.create_post("Hello, this is my third post!")
user2.create_post("Nice weather today!")
user2.create_post("Nice weather tommorrow!")
user2.create_post("Nice weather yesterday too!")

user1.comment_on_post(user2.posts[0], "I agree, it's lovely outside.")
user1.comment_on_post(user2.posts[1], "Are you sure about that?")
user1.comment_on_post(user2.posts[2], "Definitely true.")
user2.comment_on_post(user1.posts[0], "Welcome to social Tweet.")
user2.comment_on_post(user1.posts[1], "Hope you know your way around.")
user2.comment_on_post(user1.posts[2], "I hope you are enjoying this social media.")

for post in user1.posts + user2.posts:
    print(f"{post.author.username} posted: {post.content}")
    for comment in post.comments:
        print(f"  {comment.author.username} commented: {comment.content}")

