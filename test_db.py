from models import db, User
# ------- CREATE USER/s
users = [
    User(
        name="Steve Peters",
        email="stpets@biddaddaybezos.com",
        bio="Cranky, but cool and caring"
    )
]
users.append(User(
    name="Mike Schull",
    email="mikey.boi@prettyokay.dev",
    bio="The reddest raddest dev in town"
))
bb = User(
    name="Brandi Butler",
    email="brandi@butler.com",
    bio="Cats and computers are my jam"
)
users.append(bb)

db.session.add_all(users)
db.session.commit()