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

# sm = crud.create_user(first_name="Sean",
#                       last_name="Montgomery",
#                       email="seandmontgomery@gmail.com",
#                       password="password2",
#                       phone="+15202482392"
#                       )

# sg = crud.create_user(first_name="Spencer",
#                       last_name="Glass",
#                       email="sglass724@gmail.com",
#                       password="password3",
#                       phone="+15164451174"
#                       )


###########################PROJECT#############################################

wicked_p = crud.create_project(user_id=1,
                     project_title="Wicked",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey and Co.",
                     agency="Stewart Talent")


blue_bloods_p = crud.create_project(user_id=1,
                     project_title="Blue Bloods",
                     industry="Television",
                     company="CBS",
                     casting_office="Bowling Miscia",
                     agency="Stewart Talent")

coca_cola_p = crud.create_project(user_id=1,
                     project_title="Coca Cola Energy",
                     industry="Voiceover",
                     company="London Vision",
                     casting_office="London Vision",
                     agency="Stewart Talent")

chicago_pd_p = crud.create_project(user_id=1,
                     project_title="Chicago P.D.",
                     industry="Television",
                     company="NBC",
                     casting_office="Claire Simon",
                     agency="10MGMT")

bull_p = crud.create_project(user_id=1,
                     project_title="BULL",
                     industry="Television",
                     company="CBS",
                     casting_office="John Ort,Kathleen Chopin, Dennis Smith",
                     agency="Stewart Talent")

chicago_fire_p = crud.create_project(user_id=1,
                     project_title="Chicago Fire",
                     industry="Television",
                     company="NBC",
                     casting_office="Claire Simon",
                     agency="10MGMT")

google_p = crud.create_project(user_id=1,
                     project_title="Google",
                     industry="Commercial",
                     company="Google",
                     casting_office="Donna Grossman Casting",
                     agency="10MGMT")

chilis_p = crud.create_project(user_id=1,
                     project_title="Chili's",
                     industry="Commercial",
                     company="Chili's Commercial",
                     casting_office="RWS Studios/Binder Casting",
                     agency="10MGMT")

empire_p = crud.create_project(user_id=1,
                     project_title="Empire",
                     industry="Television",
                     company="FOX",
                     casting_office="Karge + Ross Casting",
                     agency="10MGMT")

the_chair_p = crud.create_project(user_id=1,
                     project_title="The Chair",
                     industry="Television",
                     company="Netflix",
                     casting_office="Donna Belajac",
                     agency="10MGMT")

behind_the_blur_p = crud.create_project(user_id=1,
                     project_title="Behind The Blur",
                     industry="Voiceover",
                     company="Behind The Blur",
                     casting_office="Direct booking",
                     agency="10MGMT")

oklahoma_obesity_prevention_p = crud.create_project(user_id=1,
                     project_title="Oklahoma Obesity Prevention",
                     industry="Voiceover",
                     company="OOP",
                     casting_office="Direct booking",
                     agency="10MGMT")       

kohler_p = crud.create_project(user_id=1,
                     project_title="Kohler",
                     industry="Commercial",
                     company="Kohler",
                     casting_office="Tom Kermgard",
                     agency="10MGMT")                    
             
hallmark_p = crud.create_project(user_id=1,
                     project_title="Hallmark Keepsakes",
                     industry="Commercial",
                     company="Hallmark",
                     casting_office="Shine United",
                     agency="10MGMT")    

miller_lite_p = crud.create_project(user_id=1,
                     project_title="Miller Lite",
                     industry="Commercial",
                     company="Miller Lite",
                     casting_office="direct booking",
                     agency="10MGMT")    

kohls_p = crud.create_project(user_id=1,
                     project_title="Kohls",
                     industry="Commercial",
                     company="Kohls",
                     casting_office="direct booking",
                     agency="10MGMT")    

#############################AUDITION###########################################

wicked_a = crud.create_audition(user_id=1,
                           project_id=1,
                           callback="no",
                           date="2019-11-18",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="I wore my long sleeved black dress with flowers on it from H&M.")

blue_bloods_a = crud.create_audition(user_id=1,
                           project_id=2,
                           callback="no",
                           date="2020-09-01",
                           role="Officer Jones",
                           location="Self Tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I wore button up white shirt")

coca_cola_a = crud.create_audition(user_id=1,
                           project_id=3,
                           callback="no",
                           date="2021-02-11",
                           role="Woman",
                           location="Self Record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")

chicago_pd_a = crud.create_audition(user_id=1,
                           project_id=4,
                           callback="no",
                           date="2021-02-25",
                           role="Young Reporter",
                           location="Self Record",
                           notes="Felt cute. Might delete later.")

bull_a = crud.create_audition(user_id=1,
                           project_id=5,
                           callback="no",
                           date="2021-02-28",
                           role="Rachel",
                           location="Self Record",
                           notes="Passed on this auditon because I was out of town, and Covid restrictions.")

chicago_fire_a = crud.create_audition(user_id=1,
                           project_id=6,
                           callback="no",
                           date="2020-11-03",
                           role="Sydney",
                           location="Self Record",
                           notes="This felt like a GREAT fit! Character was trapped in car during the scene. Second time this casting office reached out in 2 days")

chicago_fire2_a = crud.create_audition(user_id=1,
                           project_id=6,
                           callback="no",
                           date="2020-11-03",
                           role="Reporter",
                           location="Self Record",
                           notes="Typical reporter scene, pretty basic")

google_a = crud.create_audition(user_id=1,
                           project_id=7,
                           callback="no",
                           date="2020-09-15",
                           role="Yoga Woman",
                           location="Self Record",
                           notes="Passed on audition")

chilis_a = crud.create_audition(user_id=1,
                           project_id=8,
                           callback="yes",
                           date="2020-01-13",
                           role="Waitress",
                           location="37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="Got a callback!")

chilis2_a = crud.create_audition(user_id=1,
                           project_id=8,
                           callback="yes",
                           date="2020-01-15",
                           role="Waitress",
                           location="37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="Felt really good and they have put me on hold for the project.")

empire_a = crud.create_audition(user_id=1,
                           project_id=9,
                           callback="no",
                           date="2020-02-03",
                           role="Kendra",
                           location="Self Tape",
                           notes="Breakdown said to dress the part and look sexy")

the_chair_a = crud.create_audition(user_id=1,
                           project_id=10,
                           callback="no",
                           date="2021-01-12",
                           role="Sharon",
                           location="Self Tape",
                           notes="Passed on this audition due to requested nudity and not worth it")

behind_the_blur_a= crud.create_audition(user_id=1,
                           project_id=11,
                           callback="no",
                           date="2021-01-15",
                           role="Female",
                           location="Self Record",
                           notes="Industrial - directions on how to procure Buccal sample")          
                
oklahoma_obesity_prevention_a = crud.create_audition(user_id=1,
                           project_id=12,
                           callback="no",
                           date="2020-09-21",
                           role="Present and Future Teen - Female",
                           location="Self Record",
                           notes="Industrial for storyboard casting - telling someone to drink a glass of water instead of having a milkshake")       
            
kohler_a = crud.create_audition(user_id=1,
                           project_id=13,
                           callback="no",
                           date="2020-08-20",
                           role="Woman",
                           location="Self Tape",
                           notes="This was a first - a self tape while showering! I honestly thought it was a great tape")   

miller_lite_a = crud.create_audition(user_id=1,
                           project_id=14,
                           callback="no",
                           date="2020-06-22",
                           role="Young Woman",
                           location="Self Record",
                           notes="Passed on this audition, due too soon and we were on the road")   

#17 
kohls_a = crud.create_audition(user_id=1,
                           project_id=15,
                           callback="no",
                           date="2019-10-18",
                           role="Woman",
                           location="Self Tape",
                           notes="This was so much fun to tape! I got to read funny reviews of products as if I was reading them for the first time. My favorite was elf on the shelf")  


############################MEDIA############################################

wicked_m = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Nessa Audition", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
            
   
blue_bloods_m = crud.create_media(audition_id="2",
                       user_id=jb.user_id,
                       media_title="Officer Jones", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

coca_cola_m = crud.create_media(audition_id="3",
                        user_id=jb.user_id,
                        media_title="CocaCola", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_pd_m = crud.create_media(audition_id="4",
                        user_id=jb.user_id,
                        media_title="Self tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

bull_m = crud.create_media(audition_id="5",
                        user_id=jb.user_id,
                        media_title="Self tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_fire_m = crud.create_media(audition_id="6",
                        user_id=jb.user_id,
                        media_title="Self tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_fire2_m = crud.create_media(audition_id="7",
                        user_id=jb.user_id,
                        media_title="Self tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                        
google_m = crud.create_media(audition_id="8",
                        user_id=jb.user_id,
                        media_title="Self tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chilis_m = crud.create_media(audition_id="9",
                        user_id=1,
                        media_title="Commercial Copy", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chilis2_m = crud.create_media(audition_id="10",
                        user_id=1,
                        media_title="Selfie of outfit", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

the_chair_m = crud.create_media(audition_id="11",
                        user_id=1,
                        media_title="N/A", link="N/A")

behind_the_blur_m = crud.create_media(audition_id="12",
                        user_id=1,
                        media_title="Self Record", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

oklahoma_obesity_prevention_m = crud.create_media(audition_id="13",
                        user_id=1,
                        media_title="Self Record", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

kohler_m = crud.create_media(audition_id="14",
                        user_id=1,
                        media_title="Self Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

hallmark_m = crud.create_media(audition_id="15",
                        user_id=1,
                        media_title="N/A", link="N/A")

miller_lite_m = crud.create_media(audition_id="16",
                        user_id=1,
                        media_title="N/A",
                        link="N/A")


kohls_m = crud.create_media(audition_id="17",
                        user_id=1,
                        media_title="Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")




