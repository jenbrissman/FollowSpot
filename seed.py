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
                     casting_office="Karge + Ross",
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
                     project_title="Best Buy",
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
                     project_title="Empire",
                     industry="Television",
                     company="FOX",
                     casting_office="Karge + Ross",
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
                     agency="Stewart Talent")
#24
just_the_beginning_p = crud.create_project(user_id=1,
                     project_title="Noggin's Just The Beginning",
                     industry="Voiceover",
                     company="Noggin",
                     casting_office="New Games Productions",
                     agency="Stewart Talent")
#25
hometown_heroes_p = crud.create_project(user_id=1,
                     project_title="Nickelodeon's Hometown Heroes",
                     industry="Voiceover",
                     company="Nickelodeon",
                     casting_office="Lorena Gallego",
                     agency="Stewart Talent")

#26
and_now_shes_gone_p = crud.create_project(user_id=1,
                     project_title="And Now She's Gone",
                     industry="Film",
                     company="Gone LLC",
                     casting_office="Anthony DelNegro",
                     agency="Stewart Talent")
#27
project_m_p = crud.create_project(user_id=1,
                     project_title="Project M",
                     industry="Voiceover",
                     company="Project M",
                     casting_office="Pit Stop",
                     agency="Stewart Talent")

#28
boss_baby_p = crud.create_project(user_id=1,
                     project_title="Boss Baby",
                     industry="Voiceover",
                     company="Dreamworks",
                     casting_office="Dreamworks Casting",
                     agency="Stewart Talent")

#29
boss_baby2_p = crud.create_project(user_id=1,
                     project_title="Boss Baby",
                     industry="Voiceover",
                     company="Dreamworks",
                     casting_office="Dreamworks Casting",
                     agency="Stewart Talent")
#30
mean_girls_p = crud.create_project(user_id=1,
                     project_title="Mean Girls",
                     industry="Theatre",
                     company="Broadway",
                     casting_office="Telsey & Co.",
                     agency="Stewart Talent")
#31                    
trolls_p = crud.create_project(user_id=1,
                     project_title="Trolls",
                     industry="Voiceover",
                     company="Dreamworks",
                     casting_office="Katie Galvan",
                     agency="Stewart Talent")
#32                    
daily_harvest_p = crud.create_project(user_id=1,
                     project_title="Daily Harvest",
                     industry="Commercial",
                     company="Daily Harvest",
                     casting_office="Daily Harvest",
                     agency="STATE")
#33
kung_fu_panda_p = crud.create_project(user_id=1,
                     project_title="Kung Fu Panda",
                     industry="Voiceover",
                     company="Dreamworks",
                     casting_office="Dreamworks Casting",
                     agency="Stewart Talent")
 #34   
baskin_robbins_p = crud.create_project(user_id=1,
                     project_title="Baskin Robbins",
                     industry="Voiceover",
                     company="Baskin Robbins",
                     casting_office="Direct Booking",
                     agency="Stewart Talent")
#35
cherry_coke_p = crud.create_project(user_id=1,
                     project_title="Cherry Vanilla Coke",
                     industry="Voiceover",
                     company="Coca Cola",
                     casting_office="Sound and Fury",
                     agency="Stewart Talent")

#36
bobbi_brown_p = crud.create_project(user_id=1,
                     project_title="Bobbi Brown",
                     industry="Modeling",
                     company="Bobbi Brown",
                     casting_office="Direct Booking",
                     agency="STATE")
#37
kohls2_p = crud.create_project(user_id=1,
                     project_title="Kohl's Scott Living",
                     industry="Modeling",
                     company="Kohl's",
                     casting_office="Binder/RWS Studios",
                     agency="STATE")
#38
cover_girl_p = crud.create_project(user_id=1,
                     project_title="Cover Girl Foundation",
                     industry="Modeling",
                     company="Cover Girl",
                     casting_office="Direct Request",
                     agency="STATE")
#39
i_hate_new_years_p = crud.create_project(user_id=1,
                     project_title="I Hate New Years",
                     industry="Film",
                     company="Feature Film",
                     casting_office="Julie Gale",
                     agency="Stewart Talent")

#40
republic_of_sarah_p = crud.create_project(user_id=1,
                     project_title="The Republic of Sarah",
                     industry="Television",
                     company="The CW",
                     casting_office="Karge + Ross",
                     agency="Stewart Talent")                     

#############################AUDITION###########################################
#1
wicked_a = crud.create_audition(user_id=1,
                           project_id=1,
                           callback="no",
                           date="2021-03-16",
                        #    date="2019-11-18",
                           role="Nessa",
                           location="1400 Broadway",
                           notes="Went really well! I worked on the material for a while with the MD, and they put my audition on tape. I have a callback next week! I wore my floral black dress that I got at H&M in Hong Kong, and was asked to wear the same thing for the callback.")
#2
blue_bloods_a = crud.create_audition(user_id=1,
                           project_id=2,
                           callback="no",
                           date="2021-01-05",
                        #    date="2020-09-01",
                           role="Officer Jones",
                           location="Self Tape",
                           notes="I did the scene three times, was given notes to do three completely different takes. I took the note but probably could have made bigger choices. I wore button up white shirt. First time going in for Bowling Miscia Casting.")
#3
coca_cola_a = crud.create_audition(user_id=1,
                           project_id=3,
                           callback="no",
                           date="2020-12-01",
                           # date="2021-02-11",
                           role="Woman",
                           location="Self Record",
                           notes="No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.")
#4
chicago_pd_a = crud.create_audition(user_id=1,
                           project_id=4,
                           callback="no",
                           date="2020-12-17",
                           role="Young Reporter",
                           location="Self Record",
                           notes="Really wordy sides. I wore my black Theory dress and glasses. Using my cellphone as a recorder prop always helps.")
# 5
bull_a = crud.create_audition(user_id=1,
                           project_id=5,
                           callback="no",
                           date="2020-05-16",
                           #date="2021-02-28",
                           role="Rachel",
                           location="Self Record",
                           notes="Passed on this auditon because I was out of town, and Covid restrictions.")
# 6
chicago_fire2_a = crud.create_audition(user_id=1,
                           project_id=6,
                           callback="no",
                           date="2020-11-05",
                           role="Sydney",
                           location="Self Record",
                           notes="This felt like a GREAT fit! Character was trapped in car during the scene. Second time this casting office reached out in 2 days")
# 7
chicago_fire_a = crud.create_audition(user_id=1,
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
                           date="2021-03-15",
                        #    date="2020-09-15",
                           role="Yoga Woman",
                           location="Self Record",
                           notes="Favorite yoga pose: Shavasana. Lots of fun improv for this audition. Got to show a lot of my personality and some comedy chops.")
# 9
chilis_a = crud.create_audition(user_id=1,
                           project_id=9,
                           callback="no",
                           date="2020-01-13",
                           role="Waitress",
                           location="RWS Studios, 37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="National Commercial, woot! Got a callback!")
# 10
chilis2_a = crud.create_audition(user_id=1,
                           project_id=9,
                           callback="yes",
                           date="2020-01-15",
                           role="Waitress",
                           location="RWS Studios, 37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="Felt really good and they have put me on hold for the project. This would be my first national commercial.")
# 11
empire_a = crud.create_audition(user_id=1,
                           project_id=10,
                           callback="no",
                           # date="2020-02-03",
                           date="2020-03-03",
                           role="Kendra",
                           location="Self Tape",
                           notes="Breakdown said to dress the part and look sexy")
# 12
the_chair_a = crud.create_audition(user_id=1,
                           project_id=11,
                           callback="no",
                           date="2020-05-05",
                           # date="2021-01-12",
                           role="Sharon",
                           location="Self Tape",
                           notes="Passed on this audition due to requested nudity and not worth it")
# 13
behind_the_blur_a= crud.create_audition(user_id=1,
                           project_id=12,
                           callback="no",
                           date = "2019-01-15",
                           # date="2021-01-15",
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
                           notes="Industrial for storyboarding - Best Buy.")       
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
                           date="2020-04-16",
                        #    date="2019-10-29",
                           role="Nadine",
                           location="Self Tape",
                           notes="I tried to make myself look as homely as possible and wore zero makeup and a frumpy dress")                                
#23                                 
utopia_a = crud.create_audition(user_id=1,
                           project_id="22",
                           callback="no",
                           date="2020-05-13",
                        #    date="2019-10-29",
                           role="Bystander at Parade",
                           location="Self Tape",
                           notes="I had a lot of fun playing around with my sunglasses and cell phone as props. I gave them completely different takes")

#24
u3_video_game_a = crud.create_audition(user_id=1,
                           project_id="23",
                           callback="no",
                           date="2020-11-20",
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
                           date="2020-12-05",
                           # date="2020-10-02",
                           role="Lila Sheldon",
                           location="Self Tape",
                           notes="Did this tape from the Gasparini's condo in Squaw.  Poorly written script made me feel like a bad actress. It makes such a difference when the writing is good! I didn't really give this one my all.")                                      
#28
project_m_a = crud.create_audition(user_id=1,
                           project_id="27",
                           callback="no",
                           date="2019-01-02",
                        #    date="2020-12-14",
                           role="Jade McBride",
                           location="Self Record",
                           notes="This was perfect for me-- it was like Katniss Everdeen vibes. Natural, strong, contemp badass adventure brave girl. One of my best voiceover auditions yet")
#29
boss_baby_a = crud.create_audition(user_id=1,
                           project_id="28",
                           callback="no",
                           date="2019-12-16",
                           role="NannyCam No-Filter CEO Baby",
                           location="Self Record",
                           notes="I channeled Aziz Ansari's comedic style/delivery as Tom Haverford on Parks and Rec. Don't know why but it REALLY worked for me.")                                          

#30
boss_baby2_a = crud.create_audition(user_id=1,
                           project_id="29",
                           callback="no",
                           # date="2020-05-17",
                           date="2019-05-17",
                           role="Agent Brown",
                           location="Self Record",
                           notes="Dry comedy")
#31
mean_girls_a = crud.create_audition(user_id=1,
                           project_id="30",
                           callback="no",
                           date="2021-01-20",
                        #    date="2020-01-27",
                           role="Karen Smith",
                           location="1501 Broadway Floor 5 Suite 510 New York, NY 10036",
                           notes="Definitely more of a Cady. Fun material, but I knew I wouldn't be booking this." )
#32
trolls_a = crud.create_audition(user_id=1,
                           project_id="31",
                           callback="no",
                           date="2019-02-05",
                        #    date="2020-01-13",
                           role="Rose",
                           location="Self Record",
                           notes="Hard Rock Troll from the band BLAZE..." )
#33
daily_harvest_a = crud.create_audition(user_id=1,
                           project_id="32",
                           callback="no",
                           date="2021-01-10",
                        #    date="2020-01-13",
                           role="Nurse",
                           location="Self Record",
                           notes="Booked it!! They had me read for a Nurse and a Mom and I booked the Mom role.")
#34
kung_fu_panda_a = crud.create_audition(user_id=1,
                           project_id="33",
                           callback="no",
                           date="2019-03-16",
                        #    date="2020-04-22",
                           role="Wandering Blade",
                           location="Self Record",
                           notes="Female Brown Bear. Full British dialect. I channelled Brienne of Tarth from GOT and that is... NOT my voice type. But... did really well considering.")
#35
kung_fu_panda_a = crud.create_audition(user_id=1,
                           project_id="34",
                           callback="no",
                           date="2020-02-19",
                           role="Mermaid",
                           location="Self Record",
                           notes="PERFECT for  my voice type. This audition could literally go on my reel. Also, who doesn't want to voice a mermaid?")
#36
cherry_coke_a = crud.create_audition(user_id=1,
                           project_id="35",
                           callback="no",
                           date="2021-02-27",
                        #    date="2020-01-24",
                           role="Female",
                           location="Self Record",
                           notes="Recorded from the Lazerow's in Turks and Caicos on my iPhone without my VO setup. Sound quality pretty decent considering... this was a fun one. Turns out Piña Coladas help with making acting choices.")

#37
bobbi_brown_a = crud.create_audition(user_id=1,
                           project_id="36",
                           callback="no",
                           date="2021-02-14",
                        #    date="2019-08-06",
                           role="Model",
                           location="Spring Studios, 6 St. John's Lane, Studio 5, New York NY, 10014",
                           notes="I never love going on the subway totally bare faced to beauty auditions. They tone matched foundation on my cheek. I got to watch a few other models audition first which reminded me to really loosen up my body and be playful for the shoot. This job pays $40k!")
#38
kohls2_a = crud.create_audition(user_id=1,
                           project_id="37",
                           callback="no",
                           date="2019-06-10",
                           role="Model",
                           location="RWS Studios 37-12 35th St. Studio 6 Long Island City, NY 11101",
                           notes="For this audition, I had make, unmake and get into a bed with one of the hottest men I have ever met in the flesh. Hard to focus because of this. I was put on hold for this commercial.")
#39
cover_girl_a = crud.create_audition(user_id=1,
                           project_id="38",
                           callback="no",
                           date="2019-06-27",
                           role="Model",
                           location="Endeavor Studios 90 John Street, Suite 301, New York, NY 10038",
                           notes="I was at Endeavor for my Braava iRobot callback, and saw this beauty casting happening in the room next door. I got myself seen and then was avail checked for this job!")
#40
i_hate_new_years_a = crud.create_audition(user_id=1,
                           project_id="39",
                           callback="no",
                           date="2021-03-15",
                        #    date="2021-02-02",
                           role="Cassie",
                           location="Self Tape",
                           notes="Role had to be able to sing with a country style - I sang Confetti and Jolene. Highly emotional scenework. This tape took unusually long to make, but I was really proud of it. Shoots in Nashville & LA. ")
#41
republic_of_sarah_a = crud.create_audition(user_id=1,
                           project_id="40",
                           callback="no",
                           date="2021-03-16",
                        #    date="2021-02-02",
                           role="Sarah",
                           location="Self Tape",
                           notes='One of my favorite tapes ever. Such a fun role, and felt like a perfect fit for me. Rebelious high school history teacher in VT. Agent said this tape was "phenomenal", which felt great because feedback in general is kind of rare.')


############################MEDIA############################################

wicked_m = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Wicked Self Tape", link="http://res.cloudinary.com/followspotapp/image/upload/v1615944892/jtjxhgbc5qap7fsqkqox.png")

wicked_m = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Nessa Sides", link="http://res.cloudinary.com/followspotapp/image/upload/v1615944577/sisn7hrzdiz6a4mjrd61.png")

wicked_m = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="WWOTE Sheet Music", link="http://res.cloudinary.com/followspotapp/image/upload/v1615944564/jbxjqzqfcsyowukqubsb.png")

wicked_m = crud.create_media(audition_id="1",
                        user_id=jb.user_id,
                        media_title="Audio from ITR", link="http://res.cloudinary.com/followspotapp/video/upload/v1615944571/sdenwe1qpppddzwfyyre.m4a")

blue_bloods_m = crud.create_media(audition_id="2",
                       user_id=jb.user_id,
                       media_title="Officer Jones", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

coca_cola_m = crud.create_media(audition_id="3",
                        user_id=jb.user_id,
                        media_title="CocaCola Copy", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_pd_m = crud.create_media(audition_id="4",
                        user_id=jb.user_id,
                        media_title="Young Reporter Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

bull_m = crud.create_media(audition_id="5",
                        user_id=jb.user_id,
                        media_title="Bull Sides", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_fire_m = crud.create_media(audition_id="6",
                        user_id=jb.user_id,
                        media_title="Reporter Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chicago_fire2_m = crud.create_media(audition_id="7",
                        user_id=jb.user_id,
                        media_title="Sydney Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                        
google_m = crud.create_media(audition_id="8",
                        user_id=jb.user_id,
                        media_title="Yoga Self Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

google_m = crud.create_media(audition_id="8",
                        user_id=jb.user_id,
                        media_title="Requirements PDF", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

google_m = crud.create_media(audition_id="8",
                        user_id=jb.user_id,
                        media_title="Yoga Outfit Pic", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")




chilis_m = crud.create_media(audition_id="9",
                        user_id=1,
                        media_title="Chili's Copy", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

chilis2_m = crud.create_media(audition_id="10",
                        user_id=1,
                        media_title="Selfie of outfit", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

empire_m = crud.create_media(audition_id="11",
                        user_id=1,
                        media_title="Kendra Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")        

the_chair_m = crud.create_media(audition_id="12",
                        user_id=1,
                        media_title="Self Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

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
                        media_title="Self Tape", link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

miller_lite_m = crud.create_media(audition_id="17",
                        user_id=1,
                        media_title="Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")


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
                        media_title="Hometown Heroes VO",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                           
and_now_shes_gone_m = crud.create_media(audition_id="27",
                        user_id=1,
                        media_title="Lila Sheldon Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

project_m_m = crud.create_media(audition_id="28",
                        user_id=1,
                        media_title="Jade McBride Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                           
boss_baby_m = crud.create_media(audition_id="29",
                        user_id=1,
                        media_title="NannyCam CEO Baby",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

boss_baby2_m = crud.create_media(audition_id="30",
                        user_id=1,
                        media_title="Agent Brown Voiceover",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            
                                                                
mean_girls_m = crud.create_media(audition_id="31",
                        user_id=1,
                        media_title="Karen Smith Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

trolls_m = crud.create_media(audition_id="32",
                        user_id=1,
                        media_title="Trolls - ROSE",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

daily_harvest_m = crud.create_media(audition_id="33",
                        user_id=1,
                        media_title="Mom Sides PDF",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

daily_harvest_m = crud.create_media(audition_id="33",
                        user_id=1,
                        media_title="Nurse Sides PDF",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

daily_harvest_m = crud.create_media(audition_id="33",
                        user_id=1,
                        media_title="Selfie of What I Wore",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

kung_fu_panda_m = crud.create_media(audition_id="34",
                        user_id=1,
                        media_title="Kung Fu Panda VO",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

baskin_robbins_m = crud.create_media(audition_id="35",
                        user_id=1,
                        media_title="BR Mermaid VO",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

cherry_coke_m = crud.create_media(audition_id="36",
                        user_id=1,
                        media_title="Cherry Coke VO",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

bobbi_brown_m = crud.create_media(audition_id="37",
                        user_id=1,
                        media_title="Selfie",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

kohls2_m = crud.create_media(audition_id="38",
                        user_id=1,
                        media_title="Selfie of Outfit",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            
cover_girl_m = crud.create_media(audition_id="39",
                        user_id=1,
                        media_title="Selfie of Outfit",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

i_hate_new_years_m = crud.create_media(audition_id="40",
                        user_id=1,
                        media_title="Cassie Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

i_hate_new_years_m = crud.create_media(audition_id="40",
                        user_id=1,
                        media_title="Cassie Sides",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")                                            

republic_of_sarah_m = crud.create_media(audition_id="41",
                        user_id=1,
                        media_title="Sarah Sides",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")

republic_of_sarah_m = crud.create_media(audition_id="41",
                        user_id=1,
                        media_title="Sarah Self Tape",
                        link="https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png")
                                                                                                                                                 