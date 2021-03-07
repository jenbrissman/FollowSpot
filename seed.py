import os
import json
from datetime import datetime

import crud
import model
import server

os.system('dropdb followspot')
os.system('createdb followspot')

model.connect_to_db(server.app)
model.db.create_all()

########################################################################

jb = crud.create_user(first_name="Jen",
                      last_name="Brissman",
                      email="brissman514@gmail.com",
                      password="password1",
                      phone="+16507735818"
                      )

sm = crud.create_user(first_name="Sean",
                      last_name="Montgomery",
                      email="seandmontgomery@gmail.com",
                      password="password2",
                      phone="+15202482392"
                      )

sg = crud.create_user(first_name="Spencer",
                      last_name="Glass",
                      email="sglass724@gmail.com",
                      password="password3",
                      phone="+15164451174"
                      )

########################################################################

wkp = crud.create_project(user_id=1,
                     project_title="Wicked",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey",
                     agency="Stewart Talent")


bbp = crud.create_project(user_id=1,
                     project_title="Blue Bloods",
                     industry="Television",
                     company="CBS",
                     casting_office="Bowling Miscia",
                     agency="CGF")

ccp = crud.create_project(user_id=1,
                     project_title="Coca Cola Energy",
                     industry="Voiceover",
                     company="London Vision",
                     casting_office="Jenny Brightman",
                     agency="Nicolosi")

########################################################################

wka = crud.create_audition(user_id=jb.user_id,
                           project_id=1,
                           callback="no",
                           date="2019-11-18",
                           time="15:00",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="I wore my long sleeved black dress with flowers on it from H&M.")

bba = crud.create_audition(user_id=jb.user_id,
                           project_id=2,
                           callback="no",
                           date="2020-09-01",
                           time="11:15",
                           role="Officer Jones",
                           location="Self Tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I wore button up white shirt")

cca = crud.create_audition(user_id=jb.user_id,
                           project_id=3,
                           callback="no",
                           date="2021-02-11",
                           time="N/A",
                           role="Woman",
                           location="Self Record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")
########################################################################


ccm = crud.create_media(audition_id="3",
                        user_id=jb.user_id,
                        media_title="CocaCola", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                        
bbm = crud.create_media(audition_id="2",
                       user_id=jb.user_id,
                       media_title="Officer Jones", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

wkm = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Nessa Audition", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
