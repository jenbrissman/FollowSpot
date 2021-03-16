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
#1
wicked_p = crud.create_project(user_id=1,
                     project_title="Wicked",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey and Co.",
                     agency="Stewart Talent")

#2
blue_bloods_p = crud.create_project(user_id=1,
                     project_title="Blue Bloods",
                     industry="Television",
                     company="CBS",
                     casting_office="Bowling Miscia",
                     agency="Stewart Talent")
#3
coca_cola_p = crud.create_project(user_id=1,
                     project_title="Coca Cola Energy",
                     industry="Voiceover",
                     company="London Vision",
                     casting_office="London Vision",
                     agency="Stewart Talent")
#4
chicago_pd_p = crud.create_project(user_id=1,
                     project_title="Chicago P.D.",
                     industry="Television",
                     company="NBC",
                     casting_office="Claire Simon",
                     agency="10MGMT")
#5
bull_p = crud.create_project(user_id=1,
                     project_title="BULL",
                     industry="Television",
                     company="CBS",
                     casting_office="John Ort,Kathleen Chopin, Dennis Smith",
                     agency="Stewart Talent")
#6
chicago_fire_p = crud.create_project(user_id=1,
                     project_title="Chicago Fire",
                     industry="Television",
                     company="NBC",
                     casting_office="Claire Simon",
                     agency="10MGMT")

#7
chicago_fire2_p = crud.create_project(user_id=1,
                     project_title="Chicago Fire",
                     industry="Television",
                     company="NBC",
                     casting_office="Claire Simon",
                     agency="10MGMT")

#8
google_p = crud.create_project(user_id=1,
                     project_title="Google",
                     industry="Commercial",
                     company="Google",
                     casting_office="Donna Grossman Casting",
                     agency="10MGMT")
#9
chilis_p = crud.create_project(user_id=1,
                     project_title="Chili's",
                     industry="Commercial",
                     company="Chili's Commercial",
                     casting_office="RWS Studios/Binder Casting",
                     agency="10MGMT")
#10
empire_p = crud.create_project(user_id=1,
                     project_title="Empire",
                     industry="Television",
                     company="FOX",
                     casting_office="Karge + Ross Casting",
                     agency="10MGMT")
#11
the_chair_p = crud.create_project(user_id=1,
                     project_title="The Chair",
                     industry="Television",
                     company="Netflix",
                     casting_office="Donna Belajac",
                     agency="10MGMT")
#12
behind_the_blur_p = crud.create_project(user_id=1,
                     project_title="Behind The Blur",
                     industry="Voiceover",
                     company="Behind The Blur",
                     casting_office="Direct booking",
                     agency="10MGMT")
#13
oklahoma_obesity_prevention_p = crud.create_project(user_id=1,
                     project_title="Oklahoma Obesity Prevention",
                     industry="Voiceover",
                     company="OOP",
                     casting_office="Direct booking",
                     agency="10MGMT")       
#14
kohler_p = crud.create_project(user_id=1,
                     project_title="Kohler",
                     industry="Commercial",
                     company="Kohler",
                     casting_office="Tom Kermgard",
                     agency="10MGMT")                    
#15            
hallmark_p = crud.create_project(user_id=1,
                     project_title="Hallmark Keepsakes",
                     industry="Commercial",
                     company="Hallmark",
                     casting_office="Shine United",
                     agency="10MGMT")    
#16
miller_lite_p = crud.create_project(user_id=1,
                     project_title="Miller Lite",
                     industry="Commercial",
                     company="Miller Lite",
                     casting_office="direct booking",
                     agency="10MGMT")    
#17
kohls_p = crud.create_project(user_id=1,
                     project_title="Kohls",
                     industry="Commercial",
                     company="Kohls",
                     casting_office="direct booking",
                     agency="10MGMT")
#18
basil_hayden_p = crud.create_project(user_id=1,
                     project_title="Basil Hayden",
                     industry="Modeling",
                     company="Basil Hayden",
                     casting_office="Beam Suntory",
                     agency="10MGMT")
#19
makers_mark_hulu_p = crud.create_project(user_id=1,
                     project_title="Makers Mark / Hulu",
                     industry="Commercial",
                     company="Makers Mark /Hulu",
                     casting_office="Paskal Rudnicke",
                     agency="10MGMT")
#20
empire2_p = crud.create_project(user_id=1,
                     project_title="Makers Mark / Hulu",
                     industry="Television",
                     company="FOX",
                     casting_office="Karge + Ross Casting",
                     agency="10MGMT")
#21
fargo_p = crud.create_project(user_id=1,
                     project_title="Fargo",
                     industry="Television",
                     company="FX",
                     casting_office="Rachel Tenner",
                     agency="10MGMT")

#22
utopia_p = crud.create_project(user_id=1,
                     project_title="Utopia",
                     industry="Television",
                     company="Amazon",
                     casting_office="Paskal Rudnicke",
                     agency="10MGMT")
#23
u3_video_game_p = crud.create_project(user_id=1,
                     project_title="U3 Video Game",
                     industry="Voiceover",
                     company="U3",
                     casting_office="Direct Request",
                     agency="Stewart")
#24
just_the_beginning_p = crud.create_project(user_id=1,
                     project_title="Noggin's Just The Beginning",
                     industry="Voiceover",
                     company="Noggin",
                     casting_office="New Games Productions",
                     agency="Stewart")
#25
hometown_heroes_p = crud.create_project(user_id=1,
                     project_title="Nickelodeon's Hometown Heroes",
                     industry="Voiceover",
                     company="Nickelodeon",
                     casting_office="Lorena Gallego",
                     agency="Stewart")

#26
and_now_shes_gone_p = crud.create_project(user_id=1,
                     project_title="And Now She's Gone",
                     industry="Film",
                     company="Gone LLC",
                     casting_office="Anthony DelNegro",
                     agency="Stewart")
#27
project_m_p = crud.create_project(user_id=1,
                     project_title="Project M",
                     industry="Voiceover",
                     company="Project M",
                     casting_office="Pit Stop",
                     agency="Stewart")

#############################AUDITION###########################################
#1
wicked_a = crud.create_audition(user_id=1,
                           project_id=1,
                           callback="no",
                           date="2019-11-18",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="I wore my long sleeved black dress with flowers on it from H&M.")
#2
blue_bloods_a = crud.create_audition(user_id=1,
                           project_id=2,
                           callback="no",
                           date="2020-09-01",
                           role="Officer Jones",
                           location="Self Tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I wore button up white shirt")
#3
coca_cola_a = crud.create_audition(user_id=1,
                           project_id=3,
                           callback="no",
                           date="2021-02-11",
                           role="Woman",
                           location="Self Record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")
#4
chicago_pd_a = crud.create_audition(user_id=1,
                           project_id=4,
                           callback="no",
                           date="2021-02-25",
                           role="Young Reporter",
                           location="Self Record",
                           notes="Felt cute. Might delete later.")
# 5
bull_a = crud.create_audition(user_id=1,
                           project_id=5,
                           callback="no",
                           date="2021-02-28",
                           role="Rachel",
                           location="Self Record",
                           notes="Passed on this auditon because I was out of town, and Covid restrictions.")
# 6
chicago_fire_a = crud.create_audition(user_id=1,
                           project_id=6,
                           callback="no",
                           date="2020-11-03",
                           role="Sydney",
                           location="Self Record",
                           notes="This felt like a GREAT fit! Character was trapped in car during the scene. Second time this casting office reached out in 2 days")
# 7
chicago_fire2_a = crud.create_audition(user_id=1,
                           project_id=7,
                           callback="no",
                           date="2020-11-03",
                           role="Reporter",
                           location="Self Record",
                           notes="Typical reporter scene, pretty basic")
# 8
google_a = crud.create_audition(user_id=1,
                           project_id=8,
                           callback="no",
                           date="2020-09-15",
                           role="Yoga Woman",
                           location="Self Record",
                           notes="Passed on audition")
# 9
chilis_a = crud.create_audition(user_id=1,
                           project_id=9,
                           callback="no",
                           date="2020-01-13",
                           role="Waitress",
                           location="37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="Got a callback!")
# 10
chilis2_a = crud.create_audition(user_id=1,
                           project_id=9,
                           callback="yes",
                           date="2020-01-15",
                           role="Waitress",
                           location="37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="Felt really good and they have put me on hold for the project.")
# 11
empire_a = crud.create_audition(user_id=1,
                           project_id=10,
                           callback="no",
                           date="2020-02-03",
                           role="Kendra",
                           location="Self Tape",
                           notes="Breakdown said to dress the part and look sexy")
# 12
the_chair_a = crud.create_audition(user_id=1,
                           project_id=11,
                           callback="no",
                           date="2021-01-12",
                           role="Sharon",
                           location="Self Tape",
                           notes="Passed on this audition due to requested nudity and not worth it")
# 13
behind_the_blur_a= crud.create_audition(user_id=1,
                           project_id=12,
                           callback="no",
                           date="2021-01-15",
                           role="Female",
                           location="Self Record",
                           notes="Industrial - directions on how to procure Buccal sample")          
# 14               
oklahoma_obesity_prevention_a = crud.create_audition(user_id=1,
                           project_id=13,
                           callback="no",
                           date="2020-09-21",
                           role="Present and Future Teen - Female",
                           location="Self Record",
                           notes="Industrial for storyboard casting - telling someone to drink a glass of water instead of having a milkshake")       
# 15            
kohler_a = crud.create_audition(user_id=1,
                           project_id=14,
                           callback="no",
                           date="2020-08-20",
                           role="Woman",
                           location="Self Tape",
                           notes="This was a first - a self tape while showering! I honestly thought it was a great tape")
# 16
hallmark_a = crud.create_audition(user_id=1,
                           project_id=15,
                           callback="no",
                           date="2020-07-21",
                           role="Mom",
                           location="Self Tape",
                           notes="Passed because didn't feel like I fit the 30-35 mom age range we see on TV")

# 17
miller_lite_a = crud.create_audition(user_id=1,
                           project_id=16,
                           callback="no",
                           date="2020-06-22",
                           role="Young Woman",
                           location="Self Record",
                           notes="Passed on this audition, due too soon and we were on the road")   

#18
kohls_a = crud.create_audition(user_id=1,
                           project_id="17",
                           callback="no",
                           date="2019-10-18",
                           role="Woman",
                           location="Self Tape",
                           notes="This was so much fun to tape! I got to read funny reviews of products as if I was reading them for the first time. My favorite was elf on the shelf")  
#19
basil_hayden_a = crud.create_audition(user_id=1,
                           project_id="18",
                           callback="no",
                           date="2019-12-05",
                           role="Lifestyle Model",
                           location="Self Submit",
                           notes="Sent in photos and close ups of hands")


#TWENTY                           
makers_mark_hulu_a = crud.create_audition(user_id=1,
                           project_id="19",
                           callback="no",
                           date="2019-11-15",
                           role="Still Life Woman",
                           location="Self Tape",
                           notes="Sent in slate")
#21                                         
empire2_a = crud.create_audition(user_id=1,
                           project_id="20",
                           callback="no",
                           date="2019-11-11",
                           role="Bethany",
                           location="Self Tape",
                           notes="Had a semi hard time acting like a party girl and shorting invisible drugs off my hand...I got there, but I learned I really come off more innocent than I want when I'm trying to be edgy")
#22
fargo_a = crud.create_audition(user_id=1,
                           project_id="21",
                           callback="no",
                           date="2019-10-29",
                           role="Nadine",
                           location="Self Tape",
                           notes="I tried to make myself look as homely as possible and wore zero makeup and a frumpy dress")                                
#23                                 
utopia_a = crud.create_audition(user_id=1,
                           project_id="22",
                           callback="no",
                           date="2019-10-29",
                           role="Bystander at Parade",
                           location="Self Tape",
                           notes="I had a lot of fun playing around with my sunglasses and cell phone as props. I gave them completely different takes")

#24
u3_video_game_a = crud.create_audition(user_id=1,
                           project_id="23",
                           callback="no",
                           date="2020-12-14",
                           role="Laura",
                           location="Self Record",
                           notes="Lots of grunts, getting punched in the face, throwing punches. I had to actively try to NOT make gut punches sound like vomit noises. There's a fine line, but I found the balance")
                              
#25
just_the_beginning_a = crud.create_audition(user_id=1,
                           project_id="24",
                           callback="no",
                           date="2020-11-6",
                           role="Host",
                           location="Self Record",
                           notes="Noggin is the perfect style for my voice type")
#26
hometown_heroes_a = crud.create_audition(user_id=1,
                           project_id="25",
                           callback="no",
                           date="2020-11-13",
                           role="Blip",
                           location="Self Record",
                           notes="I love Blip! I feel like my voice is perfect for these kids shows....")
#27
and_now_shes_gone_a = crud.create_audition(user_id=1,
                           project_id="26",
                           callback="no",
                           date="2020-10-02",
                           role="Lila Sheldon",
                           location="Self Tape",
                           notes="Did this tape from the Gasparini's condo in Squaw.  Poorly written script made me feel like a bad actress. It makes such a difference when the writing is good! I didn't really give this one my all.")                                      
#28
project_m_a = crud.create_audition(user_id=1,
                           project_id="27",
                           callback="no",
                           date="2020-12-14",
                           role="Jade McBride",
                           location="Self Record",
                           notes="This was perfect for me-- it was like Katniss Everdeen vibes. Natural, strong, contemp badass adventure brave girl. One of my best voiceover auditions yet")
                                           
                                
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

empire_m = crud.create_media(audition_id="11",
                        user_id=1,
                        media_title="Kendra Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")        

the_chair_m = crud.create_media(audition_id="12",
                        user_id=1,
                        media_title="N/A", link="N/A")

behind_the_blur_m = crud.create_media(audition_id="13",
                        user_id=1,
                        media_title="Self Record", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

oklahoma_obesity_prevention_m = crud.create_media(audition_id="14",
                        user_id=1,
                        media_title="Self Record", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

kohler_m = crud.create_media(audition_id="15",
                        user_id=1,
                        media_title="Self Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

hallmark_m = crud.create_media(audition_id="16",
                        user_id=1,
                        media_title="N/A", link="N/A")

miller_lite_m = crud.create_media(audition_id="17",
                        user_id=1,
                        media_title="N/A",
                        link="N/A")


kohls_m = crud.create_media(audition_id="18",
                        user_id=1,
                        media_title="Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

basil_hayden_m = crud.create_media(audition_id="19",
                        user_id=1,
                        media_title="Hands Images",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                      
makers_mark_hulu_m = crud.create_media(audition_id="20",
                        user_id=1,
                        media_title="Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                  
empire2_m = crud.create_media(audition_id="21",
                        user_id=1,
                        media_title="Bethany Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

                                  
fargo_m = crud.create_media(audition_id="22",
                        user_id=1,
                        media_title="Nadine Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

utopia_m = crud.create_media(audition_id="23",
                        user_id=1,
                        media_title="Bystander Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

u3_video_game_m = crud.create_media(audition_id="24",
                        user_id=1,
                        media_title="Laura Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                       
just_the_beginning_m = crud.create_media(audition_id="25",
                        user_id=1,
                        media_title="Noggin Host Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

hometown_heroes_m = crud.create_media(audition_id="26",
                        user_id=1,
                        media_title="Nickelodeon Hometown Heroes Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                           
and_now_shes_gone_m = crud.create_media(audition_id="27",
                        user_id=1,
                        media_title="Lila Sheldon Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

project_m_m = crud.create_media(audition_id="28",
                        user_id=1,
                        media_title="Jade McBride Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                           
                                            
                                
