from model import *
import os
import server

os.system('dropdb followspot')
os.system('createdb followspot')

connect_to_db(server.app)
db.create_all()

jb = User(first_name="Jen",
          last_name="Brissman",
          email="brissman514@gmail.com",
          password="password1"
          )

sm = User(first_name="Sean",
          last_name="Montgomery",
          email="seandmontgomery@gmail.com",
          password="password2"
          )

sg = User(first_name="Spencer",
          last_name="Glass",
          email="sglass724@gmail.com",
          password="password3"
          )
