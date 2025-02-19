
from flaskblog import User, Post, app, db

# NOTE: You have to run everything in the app app_context

# Create the tables and database
with app.app_context():
    db.create_all()


# How to add a user
with app.app_context():
    user1 = User(username='meh', email='meh@b.com', password='123')
    user2 = User(username='bhoomi', email='bhoomi@b.com', password='123')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()


# Get all the users and print it.
with app.app_context():
    users = User.query.all()
    print(users)


# Add a post
with app.app_context():
    user = User.query.first()
    post = Post(title="My Post", content="My Content", user_id=user.id)
    db.session.add(post)
    db.session.commit()

# List posts by some user
with app.app_context():
    user1 = User.query.first()
    print(user1.posts)
