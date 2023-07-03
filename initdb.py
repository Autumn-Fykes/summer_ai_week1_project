import pathlib
pathlib.Path('./data/app.db').unlink(missing_ok=True)

from models import db, User, Msg

db.connect()
db.create_tables([User, Msg])

users = [
    {"name":"Serdar"},
    {"name":"Spike"},
    {"name":"Jet"},
    {"name":"Faye"},
    {"name":"Ed"},
]

msgs = [
    {"user":"Serdar","message":"Hello world."},
    {"user":"Spike","message":"Hola."},
    {"user":"Jet","message":"What's up."},
    {"user":"Faye","message":"I hate pizza."},
    {"user":"Ed","message":"im here rn."},
]

for user in users:
    User.create(**user)

for msg in msgs:
    Msg.create(
        user = User.get(name=msg['user']),
        message = msg['message']
    )

for msg in Msg.select():
    print (f'{msg.user.name}: "{msg.message}"')

