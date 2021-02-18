"""Script to seed database"""

import os
import json
from datetime import datetime

import crud
from model import *
import server

os.system('dropdb followspot')
os.system('createdb followspot')

connect_to_db(server.app)
db.create_all()

########################################################################


bb = crud.create_media(media_title="Officer Jones", link="www.link.com")
cce = crud.create_media(
    media_title="CocaCola Jen Brissman", link="www.link1.com")
wkm = crud.create_media(media_title="Nessa Audition", link="www.link2.com")

########################################################################

jb = crud.create_user(first_name="Jen",
                      last_name="Brissman",
                      email="brissman514@gmail.com",
                      password="password1"
                      )

sm = crud.create_user(first_name="Sean",
                      last_name="Montgomery",
                      email="seandmontgomery@gmail.com",
                      password="password2"
                      )

sg = crud.create_user(first_name="Spencer",
                      last_name="Glass",
                      email="sglass724@gmail.com",
                      password="password3"
                      )

########################################################################

wk = crud.create_job(project_title="Wicked",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey",
                     agency="Stewart Talent")

bb = crud.create_job(project_title="Blue Bloods",
                     industry="TV",
                     company="CBS",
                     casting_office="Bowling Miscia",
                     agency="CGF")

cc = crud.create_job(project_title="Coca Cola Energy",
                     industry="Voiceover",
                     company="London Vision",
                     casting_office="Jenny Brightman",
                     agency="Nicolosi")

########################################################################

wka = crud.create_audition(user_id=1,
                           job_id=1,
                           callback=True,
                           date="11-18-19",
                           time="3:00pm",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="I wore my long sleeved black dress with flowers on it from H&M.")

bba = crud.create_audition(user_id=1,
                           job_id=1,
                           callback=False,
                           date="09-01-20",
                           time="11:15am",
                           role="Officer Jones",
                           location="self tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I wore button up white shirt")

cca = crud.create_audition(user_id=1,
                           job_id=1,
                           callback=False,
                           date="02-11-21",
                           time="N/A",
                           role="Woman",
                           location="self record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")


# I wore black heels and had my hair down. I sang from the show, but also had 'Safer' from First Date prepared in my book. Lisa Leguillo wasn't in the room. I auditioned for Dan the music director - he worked with me a lot in the room, and even had me come back in for more after I had left. I recorded the audition on my iPhone and is uploaded in the media files. I used my more serious Justin Patterson headshot. The sides and sheet music are also uploaded in the media files.
