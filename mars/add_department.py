import datetime
from data.users import User
from flask import Flask
from data import db_session
from data.department import Depart

db_session.global_init("db/mars_explorer.db")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

job = Depart()
job.team_leader = 1
job.title = 'Покрасить забор завтра'
job.chief = 5
job.members = '1, 2, 3'
job.email = 'q@d'
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()


