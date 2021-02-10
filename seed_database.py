from model import *
import os
import server

os.system('dropdb qtestdb')
os.system('createdb qtestdb')

connect_to_db(server.app)
dc.create_all()

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
