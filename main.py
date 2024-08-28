from models import Session, User

session = Session()

# Add a new user
new_user = User(name="John Doe", email="john.doe@example.com")
session.add(new_user)
session.commit()

# Query users
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
