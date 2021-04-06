--
-- PostgreSQL database dump
--

-- Dumped from database version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE ONLY public.projects DROP CONSTRAINT projects_user_id_fkey;
ALTER TABLE ONLY public.media DROP CONSTRAINT media_user_id_fkey;
ALTER TABLE ONLY public.media DROP CONSTRAINT media_audition_id_fkey;
ALTER TABLE ONLY public.auditions DROP CONSTRAINT auditions_user_id_fkey;
ALTER TABLE ONLY public.auditions DROP CONSTRAINT auditions_project_id_fkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
ALTER TABLE ONLY public.users DROP CONSTRAINT users_email_key;
ALTER TABLE ONLY public.projects DROP CONSTRAINT projects_pkey;
ALTER TABLE ONLY public.media DROP CONSTRAINT media_pkey;
ALTER TABLE ONLY public.auditions DROP CONSTRAINT auditions_pkey;
ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
ALTER TABLE public.projects ALTER COLUMN project_id DROP DEFAULT;
ALTER TABLE public.media ALTER COLUMN media_id DROP DEFAULT;
ALTER TABLE public.auditions ALTER COLUMN audition_id DROP DEFAULT;
DROP SEQUENCE public.users_user_id_seq;
DROP TABLE public.users;
DROP SEQUENCE public.projects_project_id_seq;
DROP TABLE public.projects;
DROP SEQUENCE public.media_media_id_seq;
DROP TABLE public.media;
DROP SEQUENCE public.auditions_audition_id_seq;
DROP TABLE public.auditions;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auditions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auditions (
    audition_id integer NOT NULL,
    user_id integer,
    project_id integer,
    callback character varying(5),
    date date,
    location character varying,
    role character varying,
    notes character varying
);


--
-- Name: auditions_audition_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auditions_audition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auditions_audition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auditions_audition_id_seq OWNED BY public.auditions.audition_id;


--
-- Name: media; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.media (
    media_id integer NOT NULL,
    user_id integer,
    audition_id integer,
    media_title character varying,
    link character varying
);


--
-- Name: media_media_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.media_media_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: media_media_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.media_media_id_seq OWNED BY public.media.media_id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.projects (
    project_id integer NOT NULL,
    user_id integer,
    industry character varying(20),
    project_title character varying,
    company character varying(20),
    casting_office character varying,
    agency character varying(20)
);


--
-- Name: projects_project_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.projects_project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: projects_project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.projects_project_id_seq OWNED BY public.projects.project_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    email character varying(40) NOT NULL,
    password character varying(20) NOT NULL,
    phone character varying(20) NOT NULL
);


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: auditions audition_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auditions ALTER COLUMN audition_id SET DEFAULT nextval('public.auditions_audition_id_seq'::regclass);


--
-- Name: media media_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.media ALTER COLUMN media_id SET DEFAULT nextval('public.media_media_id_seq'::regclass);


--
-- Name: projects project_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects ALTER COLUMN project_id SET DEFAULT nextval('public.projects_project_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: auditions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.auditions (audition_id, user_id, project_id, callback, date, location, role, notes) FROM stdin;
1	1	1	no	2021-03-16	1400 Broadway	Nessa	Went really well! I worked on the material for a while with the MD, and they put my audition on tape. I have a callback next week! I wore my floral black dress that I got at H&M in Hong Kong, and was asked to wear the same thing for the callback.
2	1	2	no	2021-01-05	Self Tape	Officer Jones	I did the scene three times, was given notes to do three completely different takes. I took the note but probably could have made bigger choices. I wore button up white shirt. First time going in for Bowling Miscia Casting.
3	1	3	no	2020-12-01	Self Record	Woman	No response from submission, but felt like this project was a really good fit for me. The final submitted mp3 is attached.
4	1	4	no	2020-12-17	Self Record	Young Reporter	Really wordy sides. I wore my black Theory dress and glasses. Using my cellphone as a recorder prop always helps.
5	1	5	no	2020-05-16	Self Record	Rachel	Passed on this auditon because I was out of town, and Covid restrictions.
6	1	6	no	2020-11-05	Self Record	Sydney	This felt like a GREAT fit! Character was trapped in car during the scene. Second time this casting office reached out in 2 days
7	1	7	no	2020-11-03	Self Record	Reporter	Typical reporter scene, pretty basic
8	1	8	no	2021-03-15	Self Record	Yoga Woman	Favorite yoga pose: Shavasana. Lots of fun improv for this audition. Got to show a lot of my personality and some comedy chops.
9	1	9	no	2020-01-13	RWS Studios, 37-12 35th St. Studio 6 Long Island City, NY 11101	Waitress	National Commercial, woot! Got a callback!
10	1	9	yes	2020-01-15	RWS Studios, 37-12 35th St. Studio 6 Long Island City, NY 11101	Waitress	Felt really good and they have put me on hold for the project. This would be my first national commercial.
11	1	10	no	2020-03-03	Self Tape	Kendra	Breakdown said to dress the part and look sexy
12	1	11	no	2020-05-05	Self Tape	Sharon	Passed on this audition due to requested nudity and not worth it
13	1	12	no	2019-01-15	Self Record	Female	Industrial - directions on how to procure Buccal sample
14	1	13	no	2020-09-21	Self Record	Present and Future Teen - Female	Industrial for storyboarding - Best Buy.
15	1	14	no	2020-08-20	Self Tape	Woman	This was a first - a self tape while showering! I honestly thought it was a great tape
16	1	15	no	2020-07-21	Self Tape	Mom	Passed because didn't feel like I fit the 30-35 mom age range we see on TV
17	1	16	no	2020-06-22	Self Record	Young Woman	Passed on this audition, due too soon and we were on the road
18	1	17	no	2019-10-18	Self Tape	Woman	This was so much fun to tape! I got to read funny reviews of products as if I was reading them for the first time. My favorite was elf on the shelf
19	1	18	no	2019-12-05	Self Submit	Lifestyle Model	Sent in photos and close ups of hands
20	1	19	no	2019-11-15	Self Tape	Still Life Woman	Sent in slate
21	1	20	no	2019-11-11	Self Tape	Bethany	Had a semi hard time acting like a party girl and shorting invisible drugs off my hand...I got there, but I learned I really come off more innocent than I want when I'm trying to be edgy
22	1	21	no	2020-04-16	Self Tape	Nadine	I tried to make myself look as homely as possible and wore zero makeup and a frumpy dress
23	1	22	no	2020-05-13	Self Tape	Bystander at Parade	I had a lot of fun playing around with my sunglasses and cell phone as props. I gave them completely different takes
24	1	23	no	2020-11-20	Self Record	Laura	Lots of grunts, getting punched in the face, throwing punches. I had to actively try to NOT make gut punches sound like vomit noises. There's a fine line, but I found the balance
25	1	24	no	2020-11-06	Self Record	Host	Noggin is the perfect style for my voice type
26	1	25	no	2020-11-13	Self Record	Blip	I love Blip! I feel like my voice is perfect for these kids shows....
27	1	26	no	2020-12-05	Self Tape	Lila Sheldon	Did this tape from the Gasparini's condo in Squaw.  Poorly written script made me feel like a bad actress. It makes such a difference when the writing is good! I didn't really give this one my all.
28	1	27	no	2019-01-02	Self Record	Jade McBride	This was perfect for me-- it was like Katniss Everdeen vibes. Natural, strong, contemp badass adventure brave girl. One of my best voiceover auditions yet
29	1	28	no	2019-12-16	Self Record	NannyCam No-Filter CEO Baby	I channeled Aziz Ansari's comedic style/delivery as Tom Haverford on Parks and Rec. Don't know why but it REALLY worked for me.
30	1	29	no	2019-05-17	Self Record	Agent Brown	Dry comedy
31	1	30	no	2021-01-20	1501 Broadway Floor 5 Suite 510 New York, NY 10036	Karen Smith	Definitely more of a Cady. Fun material, but I knew I wouldn't be booking this.
32	1	31	no	2019-02-05	Self Record	Rose	Hard Rock Troll from the band BLAZE...
33	1	32	no	2021-01-10	Self Record	Nurse	Booked it!! They had me read for a Nurse and a Mom and I booked the Mom role.
34	1	33	no	2019-03-16	Self Record	Wandering Blade	Female Brown Bear. Full British dialect. I channelled Brienne of Tarth from GOT and that is... NOT my voice type. But... did really well considering.
35	1	34	no	2020-02-19	Self Record	Mermaid	PERFECT for  my voice type. This audition could literally go on my reel. Also, who doesn't want to voice a mermaid?
36	1	35	no	2021-02-27	Self Record	Female	Recorded from the Lazerow's in Turks and Caicos on my iPhone without my VO setup. Sound quality pretty decent considering... this was a fun one. Turns out Piña Coladas help with making acting choices.
37	1	36	no	2021-02-14	Spring Studios, 6 St. John's Lane, Studio 5, New York NY, 10014	Model	I never love going on the subway totally bare faced to beauty auditions. They tone matched foundation on my cheek. I got to watch a few other models audition first which reminded me to really loosen up my body and be playful for the shoot. This job pays $40k!
38	1	37	no	2019-06-10	RWS Studios 37-12 35th St. Studio 6 Long Island City, NY 11101	Model	For this audition, I had make, unmake and get into a bed with one of the hottest men I have ever met in the flesh. Hard to focus because of this. I was put on hold for this commercial.
39	1	38	no	2019-06-27	Endeavor Studios 90 John Street, Suite 301, New York, NY 10038	Model	I was at Endeavor for my Braava iRobot callback, and saw this beauty casting happening in the room next door. I got myself seen and then was avail checked for this job!
40	1	39	no	2021-03-15	Self Tape	Cassie	Role had to be able to sing with a country style - I sang Confetti and Jolene. Highly emotional scenework. This tape took unusually long to make, but I was really proud of it. Shoots in Nashville & LA. 
41	1	40	no	2021-03-16	Self Tape	Sarah	One of my favorite tapes ever. Such a fun role, and felt like a perfect fit for me. Rebelious high school history teacher in VT. Agent said this tape was "phenomenal", which felt great because feedback in general is kind of rare.
42	1	42	no	2021-04-02	Deschutes Brewery Bend Public House, Northwest Bond Street, Bend, OR, USA	ddd	ddd
43	1	43	no	2021-04-07	Farewell Bend Park, Southwest Reed Market Road, Bend, OR, USA	fff	fff
44	1	44	no	2021-04-07	Farewell Bend Park, Southwest Reed Market Road, Bend, OR, USA	fff	fff
\.


--
-- Data for Name: media; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.media (media_id, user_id, audition_id, media_title, link) FROM stdin;
1	1	1	Wicked Self Tape	http://res.cloudinary.com/followspotapp/image/upload/v1615944892/jtjxhgbc5qap7fsqkqox.png
2	1	1	Nessa Sides	http://res.cloudinary.com/followspotapp/image/upload/v1615944577/sisn7hrzdiz6a4mjrd61.png
3	1	1	WWOTE Sheet Music	http://res.cloudinary.com/followspotapp/image/upload/v1615944564/jbxjqzqfcsyowukqubsb.png
4	1	1	Audio from ITR	http://res.cloudinary.com/followspotapp/video/upload/v1615944571/sdenwe1qpppddzwfyyre.m4a
5	1	2	Officer Jones	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
6	1	3	CocaCola Copy	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
7	1	4	Young Reporter Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
8	1	5	Bull Sides	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
9	1	6	Reporter Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
10	1	7	Sydney Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
11	1	8	Yoga Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
12	1	8	Requirements PDF	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
13	1	8	Yoga Outfit Pic	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
14	1	9	Chili's Copy	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
15	1	10	Selfie of outfit	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
16	1	11	Kendra Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
17	1	12	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
18	1	13	Self Record	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
19	1	14	Self Record	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
20	1	15	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
21	1	16	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
22	1	17	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
23	1	18	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
24	1	19	Hands Images	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
25	1	20	Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
26	1	21	Bethany Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
27	1	22	Nadine Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
28	1	23	Bystander Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
29	1	24	Laura Voiceover	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
30	1	25	Noggin Host Voiceover	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
31	1	26	Hometown Heroes VO	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
32	1	27	Lila Sheldon Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
33	1	28	Jade McBride Voiceover	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
34	1	29	NannyCam CEO Baby	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
35	1	30	Agent Brown Voiceover	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
36	1	31	Karen Smith Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
37	1	32	Trolls - ROSE	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
38	1	33	Mom Sides PDF	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
39	1	33	Nurse Sides PDF	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
40	1	33	Selfie of What I Wore	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
41	1	34	Kung Fu Panda VO	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
42	1	35	BR Mermaid VO	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
43	1	36	Cherry Coke VO	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
44	1	37	Selfie	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
45	1	38	Selfie of Outfit	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
46	1	39	Selfie of Outfit	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
47	1	40	Cassie Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
48	1	40	Cassie Sides	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
49	1	41	Sarah Sides	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
50	1	41	Sarah Self Tape	https://res.cloudinary.com/followspotapp/image/upload/v1614959677/rdyzor4hqil3v946lafa.png
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.projects (project_id, user_id, industry, project_title, company, casting_office, agency) FROM stdin;
1	1	Theatre	Wicked	Broadway	Telsey and Co.	Stewart Talent
2	1	Television	Blue Bloods	CBS	Bowling Miscia	Stewart Talent
3	1	Voiceover	Coca Cola Energy	London Vision	London Vision	Stewart Talent
4	1	Television	Chicago P.D.	NBC	Claire Simon	10MGMT
5	1	Television	BULL	CBS	John Ort,Kathleen Chopin, Dennis Smith	Stewart Talent
6	1	Television	Chicago Fire	NBC	Claire Simon	10MGMT
7	1	Television	Chicago Fire	NBC	Claire Simon	10MGMT
8	1	Commercial	Google	Google	Donna Grossman Casting	10MGMT
9	1	Commercial	Chili's	Chili's Commercial	RWS Studios/Binder Casting	10MGMT
10	1	Television	Empire	FOX	Karge + Ross	10MGMT
11	1	Television	The Chair	Netflix	Donna Belajac	10MGMT
12	1	Voiceover	Behind The Blur	Behind The Blur	Direct booking	10MGMT
13	1	Voiceover	Best Buy	OOP	Direct booking	10MGMT
14	1	Commercial	Kohler	Kohler	Tom Kermgard	10MGMT
15	1	Commercial	Hallmark Keepsakes	Hallmark	Shine United	10MGMT
16	1	Commercial	Miller Lite	Miller Lite	direct booking	10MGMT
17	1	Commercial	Kohls	Kohls	direct booking	10MGMT
18	1	Modeling	Basil Hayden	Basil Hayden	Beam Suntory	10MGMT
19	1	Commercial	Makers Mark / Hulu	Makers Mark /Hulu	Paskal Rudnicke	10MGMT
20	1	Television	Empire	FOX	Karge + Ross	10MGMT
21	1	Television	Fargo	FX	Rachel Tenner	10MGMT
22	1	Television	Utopia	Amazon	Paskal Rudnicke	10MGMT
23	1	Voiceover	U3 Video Game	U3	Direct Request	Stewart Talent
24	1	Voiceover	Noggin's Just The Beginning	Noggin	New Games Productions	Stewart Talent
25	1	Voiceover	Nickelodeon's Hometown Heroes	Nickelodeon	Lorena Gallego	Stewart Talent
26	1	Film	And Now She's Gone	Gone LLC	Anthony DelNegro	Stewart Talent
27	1	Voiceover	Project M	Project M	Pit Stop	Stewart Talent
28	1	Voiceover	Boss Baby	Dreamworks	Dreamworks Casting	Stewart Talent
29	1	Voiceover	Boss Baby	Dreamworks	Dreamworks Casting	Stewart Talent
30	1	Theatre	Mean Girls	Broadway	Telsey & Co.	Stewart Talent
31	1	Voiceover	Trolls	Dreamworks	Katie Galvan	Stewart Talent
32	1	Commercial	Daily Harvest	Daily Harvest	Daily Harvest	STATE
33	1	Voiceover	Kung Fu Panda	Dreamworks	Dreamworks Casting	Stewart Talent
34	1	Voiceover	Baskin Robbins	Baskin Robbins	Direct Booking	Stewart Talent
35	1	Voiceover	Cherry Vanilla Coke	Coca Cola	Sound and Fury	Stewart Talent
36	1	Modeling	Bobbi Brown	Bobbi Brown	Direct Booking	STATE
37	1	Modeling	Kohl's Scott Living	Kohl's	Binder/RWS Studios	STATE
38	1	Modeling	Cover Girl Foundation	Cover Girl	Direct Request	STATE
39	1	Film	I Hate New Years	Feature Film	Julie Gale	Stewart Talent
40	1	Television	The Republic of Sarah	The CW	Karge + Ross	Stewart Talent
41	1	Voiceover	qqq	qqq	qqq	qqq
42	1	Dance	ddd	ddd	ddd	ddd
43	1	Instrumental	fff	fff	fff	fff
44	1	Instrumental	fff	fff	fff	fff
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (user_id, first_name, last_name, email, password, phone) FROM stdin;
1	Jen	Brissman	brissman514@gmail.com	password1	+16507735818
\.


--
-- Name: auditions_audition_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.auditions_audition_id_seq', 44, true);


--
-- Name: media_media_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.media_media_id_seq', 50, true);


--
-- Name: projects_project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.projects_project_id_seq', 44, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, true);


--
-- Name: auditions auditions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auditions
    ADD CONSTRAINT auditions_pkey PRIMARY KEY (audition_id);


--
-- Name: media media_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.media
    ADD CONSTRAINT media_pkey PRIMARY KEY (media_id);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (project_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: auditions auditions_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auditions
    ADD CONSTRAINT auditions_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.projects(project_id);


--
-- Name: auditions auditions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auditions
    ADD CONSTRAINT auditions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: media media_audition_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.media
    ADD CONSTRAINT media_audition_id_fkey FOREIGN KEY (audition_id) REFERENCES public.auditions(audition_id);


--
-- Name: media media_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.media
    ADD CONSTRAINT media_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: projects projects_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

