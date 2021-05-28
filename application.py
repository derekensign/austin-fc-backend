import os
from flask import Flask, request
from flask_cors import CORS
import sqlalchemy
app = Flask(__name__)
CORS(app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

import jwt

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
import models
models.db.init_app(app)

def roster_load():
  stanley = models.Player(
    name = 'Aedan Stanley',
    number = 4,
    age = 21,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Stanley.png'
  )
  berhalter = models.Player(
    name = 'Sebastian Berhalter',
    number = 6,
    age = 20,
    position = 'Midfielder',
    nationality = 'USA',
    image = '/roster-pics/Berhalter.png'
  )
  besler = models.Player(
    name = 'Matt Besler',
    number = 5,
    age = 34,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Besler.png'
  )
  cascante = models.Player(
    name = 'Julio Cascante',
    number = 18,
    age = 27,
    position = 'Defender',
    nationality = 'Costa Rica',
    image = '/roster-pics/Cascante.png'
  )
  dominguez = models.Player(
    name = 'Cecilio Dominguez',
    number = 10,
    age = 26,
    position = 'Forward',
    nationality = 'Paraguay',
    image = '/roster-pics/Dominguez.png'
  )
  fagundez = models.Player(
    name = 'Diego Fagundez',
    number = 14,
    age = 26,
    position = 'Midfielder',
    nationality = 'USA',
    image = '/roster-pics/Fagundez.png'
  )
  gallagher = models.Player(
    name = 'Jon Gallagher',
    number = 17,
    age = 25,
    position = 'Forward',
    nationality = 'Ireland',
    image = '/roster-pics/Gallagher.png'
  )
  hoesen = models.Player(
    name = 'Danny Hoesen',
    number = 9,
    age = 30,
    position = 'Forward',
    nationality = 'Netherlands',
    image = '/roster-pics/Hoesen.png'
  )
  jimenez = models.Player(
    name = 'Hector Jimenez',
    number = 16,
    age = 32,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Jimenez.png'
  )
  kolmanic = models.Player(
    name = 'Zan Kolmanic',
    number = 21,
    age = 21,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Kolmanic.png'
  )
  kleeman = models.Player(
    name = 'Freddy Kleemann',
    number = 19,
    age = 22,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Kleemann.png'
  )
  lima = models.Player(
    name = 'Nick Lima',
    number = 24,
    age = 26,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Lima.png'
  )
  manneh = models.Player(
    name = 'Kekuta Manneh',
    number = 23,
    age = 26,
    position = 'Forward',
    nationality = 'Bakau',
    image = '/roster-pics/Manneh.png'
  )
  pereira = models.Player(
    name = 'Daniel Pereira',
    number = 15,
    age = 20,
    position = 'Midfielder',
    nationality = 'Venezuela',
    image = '/roster-pics/Pereira.png'
  )
  pochettino = models.Player(
    name = 'Tomas Pochettino',
    number = 7,
    age = 25,
    position = 'Midfielder',
    nationality = 'Argentina',
    image = '/roster-pics/Pochettino.png'
  )
  pulisic = models.Player(
    name = 'William Pulisic',
    number = 34,
    age = 23,
    position = 'Goalkeeper',
    nationality = 'USA',
    image = '/roster-pics/Pulisic.png'
  )
  redes = models.Player(
    name = 'Rodney Redes',
    number = 11,
    age = 21,
    position = 'Forward',
    nationality = 'Paraguay',
    image = '/roster-pics/Redes.png'
  )
  ring = models.Player(
    name = 'Alex Ring',
    number = 8,
    age = 30,
    position = 'Midfielder',
    nationality = 'Finland',
    image = '/roster-pics/Ring.png'
  )
  romana = models.Player(
    name = 'Jhohan Romana',
    number = 3,
    age = 22,
    position = 'Defender',
    nationality = 'Colombia',
    image = '/roster-pics/Romana.png'
  )
  schoenfeld = models.Player(
    name = 'Aaron Schoenfeld',
    number = 13,
    age = 31,
    position = 'Forward',
    nationality = 'USA',
    image = '/roster-pics/Schoenfeld.png'
  )
  scott = models.Player(
    name = 'Brady Scott',
    number = 28,
    age = 21,
    position = 'Goalkeeper',
    nationality = 'USA',
    image = '/roster-pics/Scott.png'
  )
  segura = models.Player(
    name = 'Ulises Segura',
    number = 12,
    age = 27,
    position = 'Midfielder',
    nationality = 'Costa Rica',
    image = '/roster-pics/Segura.png'
  )
  stroud = models.Player(
    name = 'Jared Stroud',
    number = 20,
    age = 24,
    position = 'Midfielder',
    nationality = 'USA',
    image = '/roster-pics/Stroud.png'
  )
  stuver = models.Player(
    name = 'Brad Stuver',
    number = 41,
    age = 30,
    position = 'Goalkeeper',
    nationality = 'USA',
    image = '/roster-pics/Stuver.png'
  )
  sweat = models.Player(
    name = 'Ben Sweat',
    number = 22,
    age = 29,
    position = 'Defender',
    nationality = 'USA',
    image = '/roster-pics/Sweat.png'
  )
  tarbell = models.Player(
    name = 'Andrew Tarbell',
    number = 31,
    age = 27,
    position = 'Goalkeeper',
    nationality = 'USA',
    image = '/roster-pics/Tarbell.png'
  )

  models.db.session.add(berhalter)
  models.db.session.add(besler)
  models.db.session.add(cascante)
  models.db.session.add(dominguez)
  models.db.session.add(fagundez)
  models.db.session.add(gallagher)
  models.db.session.add(hoesen)
  models.db.session.add(jimenez)
  models.db.session.add(kleeman)
  models.db.session.add(kolmanic)
  models.db.session.add(lima)
  models.db.session.add(manneh)
  models.db.session.add(pereira)
  models.db.session.add(pochettino)
  models.db.session.add(pulisic)
  models.db.session.add(redes)
  models.db.session.add(ring)
  models.db.session.add(romana)
  models.db.session.add(schoenfeld)
  models.db.session.add(scott)
  models.db.session.add(segura)
  models.db.session.add(stanley)
  models.db.session.add(stroud)
  models.db.session.add(stuver)
  models.db.session.add(sweat)
  models.db.session.add(tarbell)
  models.db.session.commit()

  return 'roster db updated'

def get_roster():
  players = models.Player.query.all()
  return {
    "roster": [p.to_json() for p in players]
  }

def root():
  return 'ok'

def create_user():
  existing_user = models.User.query.filter_by(email=request.json["email"]).first()
  if existing_user:
    return { "message": "Email must be present and unique" }, 400
  
  hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
  user = models.User(
    email=request.json["email"],
    name=request.json["name"],
    password=hashed_pw,
  )

  models.db.session.add(user)
  models.db.session.commit()

  # encrypted_id = jwt.encode({ "user_id": user.id }, os.environ.get('JWT_SECRET'), algorithm="HS256")
  return { "user": user.to_json(), "user_id": user.id}
app.route('/users', methods=["POST"])(create_user)

def login():
  user = models.User.query.filter_by(email=request.json["email"]).first()
  if not user:
    return { "message": "User not found" }, 404


  if bcrypt.check_password_hash(user.password, request.json["password"]):
    # encrypted_id = jwt.encode({ "user_id": user.id }, os.environ.get('JWT_SECRET'), algorithm="HS256")
    return { "user": user.to_json(), "user_id": user.id}
  else:
    return { "message": "Password incorrect" }, 401
app.route('/users/login', methods=["POST"])(login)

def verify_user():
  # decrypted_id = jwt.decode(request.headers["Authorization"], os.environ.get('JWT_SECRET'), algorithms=["HS256"])["user_id"]
  user = models.User.query.filter_by(id=id).first()
  if not user:
    return { "message": "user not found" }, 404
  return { "user": user.to_json(), "user_id": user.id}
app.route('/users/verify', methods=["GET"])(verify_user)

# def add_fixture():

app.route('/', methods=["GET"])(root)
app.route('/roster', methods=["POST"])(roster_load)
app.route('/roster', methods=["GET"])(get_roster)

if __name__ == '__main__':
  port = int(os.environ.get('PORT')) or 5000
  app.run('0.0.0.0', port=port, debug=True)