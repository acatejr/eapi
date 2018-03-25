--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tiger; Type: SCHEMA; Schema: -; Owner: eapi
--

CREATE SCHEMA tiger;


ALTER SCHEMA tiger OWNER TO eapi;

--
-- Name: tiger_data; Type: SCHEMA; Schema: -; Owner: eapi
--

CREATE SCHEMA tiger_data;


ALTER SCHEMA tiger_data OWNER TO eapi;

--
-- Name: topology; Type: SCHEMA; Schema: -; Owner: eapi
--

CREATE SCHEMA topology;


ALTER SCHEMA topology OWNER TO eapi;

--
-- Name: SCHEMA topology; Type: COMMENT; Schema: -; Owner: eapi
--

COMMENT ON SCHEMA topology IS 'PostGIS Topology schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';


--
-- Name: postgis_tiger_geocoder; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder WITH SCHEMA tiger;


--
-- Name: EXTENSION postgis_tiger_geocoder; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_tiger_geocoder IS 'PostGIS tiger geocoder and reverse geocoder';


--
-- Name: postgis_topology; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS postgis_topology WITH SCHEMA topology;


--
-- Name: EXTENSION postgis_topology; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis_topology IS 'PostGIS topology spatial types and functions';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: eapi
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO eapi;

--
-- Name: srer_precipevents; Type: TABLE; Schema: public; Owner: eapi
--

CREATE TABLE public.srer_precipevents (
    id integer NOT NULL,
    raingage_id integer,
    year integer,
    month integer,
    precip numeric(15,5),
    created timestamp with time zone DEFAULT now(),
    updated timestamp with time zone
);


ALTER TABLE public.srer_precipevents OWNER TO eapi;

--
-- Name: srer_precipevents_id_seq; Type: SEQUENCE; Schema: public; Owner: eapi
--

CREATE SEQUENCE public.srer_precipevents_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.srer_precipevents_id_seq OWNER TO eapi;

--
-- Name: srer_precipevents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eapi
--

ALTER SEQUENCE public.srer_precipevents_id_seq OWNED BY public.srer_precipevents.id;


--
-- Name: srer_raingages; Type: TABLE; Schema: public; Owner: eapi
--

CREATE TABLE public.srer_raingages (
    id integer NOT NULL,
    code character varying,
    name character varying,
    created timestamp with time zone DEFAULT now(),
    latitude numeric(15,5),
    longitude numeric(15,5),
    updated timestamp with time zone
);


ALTER TABLE public.srer_raingages OWNER TO eapi;

--
-- Name: srer_raingages_id_seq; Type: SEQUENCE; Schema: public; Owner: eapi
--

CREATE SEQUENCE public.srer_raingages_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.srer_raingages_id_seq OWNER TO eapi;

--
-- Name: srer_raingages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eapi
--

ALTER SEQUENCE public.srer_raingages_id_seq OWNED BY public.srer_raingages.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.srer_precipevents ALTER COLUMN id SET DEFAULT nextval('public.srer_precipevents_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.srer_raingages ALTER COLUMN id SET DEFAULT nextval('public.srer_raingages_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: eapi
--

COPY public.alembic_version (version_num) FROM stdin;
8ecf3246265b
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: eapi
--

COPY public.spatial_ref_sys  FROM stdin;
\.


--
-- Data for Name: srer_precipevents; Type: TABLE DATA; Schema: public; Owner: eapi
--

COPY public.srer_precipevents (id, raingage_id, year, month, precip, created, updated) FROM stdin;
\.


--
-- Name: srer_precipevents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eapi
--

SELECT pg_catalog.setval('public.srer_precipevents_id_seq', 1, false);


--
-- Data for Name: srer_raingages; Type: TABLE DATA; Schema: public; Owner: eapi
--

COPY public.srer_raingages (id, code, name, created, latitude, longitude, updated) FROM stdin;
96	DESST	Desert Station	2018-03-25 03:55:22.933159+00	31.88012	-110.89980	\N
97	NE	Northeast	2018-03-25 03:55:22.940213+00	31.90731	-110.83300	\N
98	LIMST	Limestone	2018-03-25 03:55:22.942385+00	31.87796	-110.81360	\N
99	FAGAN	Fagan	2018-03-25 03:55:22.945402+00	31.91734	-110.79638	\N
100	GRARI	Gravelly Ridge	2018-03-25 03:55:22.94834+00	31.83891	-110.95128	\N
101	MUHLE	Muhlenbergia	2018-03-25 03:55:22.95138+00	31.84393	-110.87849	\N
102	RODEN	Rodent	2018-03-25 03:55:22.953909+00	31.81090	-110.88403	\N
103	ROAD	Road	2018-03-25 03:55:22.956185+00	31.79524	-110.88460	\N
104	131	Encl. No. 131	2018-03-25 03:55:22.958369+00	31.79904	-110.89844	\N
105	AMADO	Amado	2018-03-25 03:55:22.960647+00	31.80618	-110.94593	\N
106	41	Enclosure 41	2018-03-25 03:55:22.962988+00	31.78200	-110.91099	\N
107	WHITE	Whitehouse	2018-03-25 03:55:22.965425+00	31.76784	-110.88719	\N
108	DESRI	Desert Rim	2018-03-25 03:55:22.967814+00	31.87489	-110.84960	\N
109	HUERF	Huerfano	2018-03-25 03:55:22.970177+00	31.85663	-110.82287	\N
110	RUELA	Ruelas	2018-03-25 03:55:22.97239+00	31.82946	-110.80701	\N
111	ERIOP	Eriopoda	2018-03-25 03:55:22.974503+00	31.83774	-110.84289	\N
112	45	Enclosure 45	2018-03-25 03:55:22.976482+00	31.81804	-110.86139	\N
113	BOX	Box	2018-03-25 03:55:22.978439+00	31.81009	-110.84188	\N
114	ROBIN	Robinson	2018-03-25 03:55:22.980384+00	31.79873	-110.80782	\N
115	DESGR	Desert Grassland	2018-03-25 03:55:22.98229+00	31.78399	-110.86055	\N
116	PARKE	Parker	2018-03-25 03:55:22.98408+00	31.78438	-110.82535	\N
117	FORES	Forest	2018-03-25 03:55:22.985977+00	31.77145	-110.84927	\N
118	FLORI	Florida	2018-03-25 03:55:22.987887+00	31.76120	-110.84625	\N
119	NW	Northwest	2018-03-25 03:55:22.989816+00	31.89701	-110.90080	\N
120	164	Enclosure 164	2018-03-25 03:55:22.991706+00	31.89066	-110.87110	\N
121	JOHNS	Johnson Ranch	2018-03-25 03:55:22.994043+00	31.89963	-110.78525	\N
122	191	191	2018-03-25 03:55:22.996664+00	31.89900	-110.80954	\N
123	192	192	2018-03-25 03:55:23.000062+00	31.89177	-110.80494	\N
124	CHOLL	Cholla	2018-03-25 03:55:23.002403+00	31.89097	-110.84299	\N
125	SCS#1	SCS #1	2018-03-25 03:55:23.004509+00	31.90945	-110.89650	\N
126	SCS5N	SCS-5N	2018-03-25 03:55:23.006888+00	31.88534	-110.90124	\N
127	163	163	2018-03-25 03:55:23.009522+00	31.88218	-110.88032	\N
128	161	161	2018-03-25 03:55:23.012039+00	31.86322	-110.89474	\N
129	PAST3	Pasture 3	2018-03-25 03:55:23.014953+00	31.85595	-110.91818	\N
130	HUGHE	Hughes	2018-03-25 03:55:23.017454+00	31.85540	-110.91223	\N
131	155	155	2018-03-25 03:55:23.019679+00	31.83851	-110.91862	\N
132	149	149	2018-03-25 03:55:23.021749+00	31.85240	-110.85078	\N
133	120	120	2018-03-25 03:55:23.023843+00	31.84187	-110.84020	\N
134	117	117	2018-03-25 03:55:23.025929+00	31.83636	-110.85753	\N
135	205	Enclosure 205	2018-03-25 03:55:23.028107+00	31.83352	-110.84937	\N
136	118	118	2018-03-25 03:55:23.030356+00	31.83296	-110.84761	\N
137	222	222	2018-03-25 03:55:23.032386+00	31.82851	-110.86749	\N
138	169	169	2018-03-25 03:55:23.034474+00	31.84648	-110.80948	\N
139	119	119	2018-03-25 03:55:23.036535+00	31.83263	-110.83233	\N
140	166	166	2018-03-25 03:55:23.038606+00	31.82884	-110.82764	\N
141	NRNCH	North Ranch	2018-03-25 03:55:23.040607+00	31.83187	-110.80150	\N
142	124	124	2018-03-25 03:55:23.042701+00	31.81563	-110.81136	\N
143	18	Enclosure 18	2018-03-25 03:55:23.044796+00	31.81363	-110.81046	\N
144	123	123	2018-03-25 03:55:23.047033+00	31.80848	-110.81274	\N
145	121	121	2018-03-25 03:55:23.049295+00	31.79790	-110.81002	\N
146	122	122	2018-03-25 03:55:23.051425+00	31.79071	-110.81943	\N
147	AIRST	Airstrip	2018-03-25 03:55:23.05354+00	31.80206	-110.82918	\N
148	IBP	IBP	2018-03-25 03:55:23.055554+00	31.79940	-110.83219	\N
149	152	152	2018-03-25 03:55:23.057622+00	31.79957	-110.83430	\N
150	115	115	2018-03-25 03:55:23.059713+00	31.80392	-110.84662	\N
151	223	223	2018-03-25 03:55:23.061731+00	31.80665	-110.85118	\N
152	130	130	2018-03-25 03:55:23.063711+00	31.80714	-110.85796	\N
153	116	116	2018-03-25 03:55:23.065785+00	31.81346	-110.85405	\N
154	114	114	2018-03-25 03:55:23.067779+00	31.79909	-110.87440	\N
155	113	113	2018-03-25 03:55:23.069785+00	31.80325	-110.88620	\N
156	140	140	2018-03-25 03:55:23.071695+00	31.80545	-110.89781	\N
157	SW	Southwest	2018-03-25 03:55:23.073685+00	31.81558	-110.91398	\N
158	187	187	2018-03-25 03:55:23.075647+00	31.80641	-110.92939	\N
159	188	188	2018-03-25 03:55:23.077594+00	31.82515	-110.96153	\N
160	185	185	2018-03-25 03:55:23.079499+00	31.78953	-110.90943	\N
161	125	125	2018-03-25 03:55:23.081448+00	31.77987	-110.91041	\N
162	184	184	2018-03-25 03:55:23.083384+00	31.77293	-110.90146	\N
163	WATRE	Water Retention	2018-03-25 03:55:23.085316+00	31.79244	-110.88237	\N
164	228	228	2018-03-25 03:55:23.087195+00	31.78763	-110.87463	\N
165	111	111	2018-03-25 03:55:23.089152+00	31.78864	-110.87292	\N
166	PA11A	Pasture 11A	2018-03-25 03:55:23.091027+00	31.78243	-110.87477	\N
167	110	110	2018-03-25 03:55:23.092925+00	31.78430	-110.87025	\N
168	112	112	2018-03-25 03:55:23.094851+00	31.78582	-110.86138	\N
169	229	229	2018-03-25 03:55:23.096833+00	31.78051	-110.83206	\N
170	MCGIB	McGibbon	2018-03-25 03:55:23.098828+00	31.77343	-110.81320	\N
\.


--
-- Name: srer_raingages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eapi
--

SELECT pg_catalog.setval('public.srer_raingages_id_seq', 170, true);


--
-- Data for Name: geocode_settings; Type: TABLE DATA; Schema: tiger; Owner: eapi
--

COPY tiger.geocode_settings  FROM stdin;
\.


--
-- Data for Name: pagc_gaz; Type: TABLE DATA; Schema: tiger; Owner: eapi
--

COPY tiger.pagc_gaz  FROM stdin;
\.


--
-- Data for Name: pagc_lex; Type: TABLE DATA; Schema: tiger; Owner: eapi
--

COPY tiger.pagc_lex  FROM stdin;
\.


--
-- Data for Name: pagc_rules; Type: TABLE DATA; Schema: tiger; Owner: eapi
--

COPY tiger.pagc_rules  FROM stdin;
\.


--
-- Data for Name: topology; Type: TABLE DATA; Schema: topology; Owner: eapi
--

COPY topology.topology  FROM stdin;
\.


--
-- Data for Name: layer; Type: TABLE DATA; Schema: topology; Owner: eapi
--

COPY topology.layer  FROM stdin;
\.


--
-- Name: alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: srer_precipevents_pkey; Type: CONSTRAINT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.srer_precipevents
    ADD CONSTRAINT srer_precipevents_pkey PRIMARY KEY (id);


--
-- Name: srer_raingages_pkey; Type: CONSTRAINT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.srer_raingages
    ADD CONSTRAINT srer_raingages_pkey PRIMARY KEY (id);


--
-- Name: srer_precipevents_raingage_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: eapi
--

ALTER TABLE ONLY public.srer_precipevents
    ADD CONSTRAINT srer_precipevents_raingage_id_fkey FOREIGN KEY (raingage_id) REFERENCES public.srer_raingages(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

