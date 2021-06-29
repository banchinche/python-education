--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.1

-- Started on 2021-06-22 08:50:06 UTC

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

--
-- TOC entry 211 (class 1255 OID 17095)
-- Name: inserting_address_phone(integer); Type: PROCEDURE; Schema: public; Owner: admin
--

CREATE PROCEDURE public.inserting_address_phone(rows_count integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	temp_city VARCHAR := '';
	temp_street VARCHAR := '';
	temp_phone VARCHAR := '';
BEGIN
	FOR i IN 1..rows_count LOOP
		temp_city := 'city' || CAST(i AS VARCHAR);
		temp_street := 'street' || CAST(i AS VARCHAR);
		temp_phone := 'phone' || CAST(i AS VARCHAR);
		INSERT INTO address_telephone(city, street, house, telephone) 
		VALUES (temp_city, temp_street, i, temp_phone);
	END LOOP;
	COMMIT;
END;
$$;


ALTER PROCEDURE public.inserting_address_phone(rows_count integer) OWNER TO admin;

--
-- TOC entry 225 (class 1255 OID 17097)
-- Name: inserting_branch(integer); Type: PROCEDURE; Schema: public; Owner: admin
--

CREATE PROCEDURE public.inserting_branch(rows_count integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	count_addresses INT;
	second_part_addresses INT;
BEGIN
	SELECT COUNT(*) INTO count_addresses FROM address_telephone;
	second_part_addresses := count_addresses / 2 + 1;
	IF rows_count <= (count_addresses / 2) THEN
		FOR i IN second_part_addresses..(second_part_addresses + rows_count - 1) LOOP
			INSERT INTO branch(info_id, number) 
			VALUES (i, i - second_part_addresses + 1);
		END LOOP;
	ELSE
		RAISE EXCEPTION 'Dublicate addresses possible!';
	END IF;
	COMMIT;
END;
$$;


ALTER PROCEDURE public.inserting_branch(rows_count integer) OWNER TO admin;

--
-- TOC entry 227 (class 1255 OID 17098)
-- Name: inserting_car(integer); Type: PROCEDURE; Schema: public; Owner: admin
--

CREATE PROCEDURE public.inserting_car(rows_count integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	branches_count INT;
	temp_price MONEY;
	counter INT := 0;
	temp_brand VARCHAR := '';
	temp_model VARCHAR := '';
	temp_number VARCHAR := '';
	
BEGIN
	SELECT COUNT(*) INTO branches_count FROM branch;
	<<f_loop>>
	LOOP
		FOR i IN 1..branches_count LOOP
			counter := counter + 1;
			EXIT f_loop WHEN counter = rows_count + 1;
			temp_price := CAST((i * 100) AS MONEY);
			temp_brand := 'brand' || CAST(i AS VARCHAR);
			temp_model := 'model' || CAST(i AS VARCHAR);
			temp_number := 'number#' || CAST(i AS VARCHAR);
			INSERT INTO car(branch_id, brand, model, number, price)
			VALUES (i, temp_brand, temp_model, temp_number, temp_price);
		END LOOP;
	END LOOP;
END;
$$;


ALTER PROCEDURE public.inserting_car(rows_count integer) OWNER TO admin;

--
-- TOC entry 226 (class 1255 OID 17096)
-- Name: inserting_customer(integer); Type: PROCEDURE; Schema: public; Owner: admin
--

CREATE PROCEDURE public.inserting_customer(rows_count integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	count_addresses INT;
	temp_name VARCHAR := '';
	temp_surname VARCHAR := '';
BEGIN
	SELECT COUNT(*) INTO count_addresses FROM address_telephone;
	IF rows_count <= (count_addresses / 2) THEN
		FOR i IN 1..rows_count LOOP
			temp_name := 'first-name' || CAST(i AS VARCHAR);
			temp_surname := 'last-name' || CAST(i AS VARCHAR);
			INSERT INTO customer(info_id, first_name, last_name) 
			VALUES (i, temp_name, temp_surname);
		END LOOP;
	ELSE
		RAISE EXCEPTION 'Dublicate addresses possible!';
	END IF;
	COMMIT;
END;
$$;


ALTER PROCEDURE public.inserting_customer(rows_count integer) OWNER TO admin;

--
-- TOC entry 224 (class 1255 OID 17099)
-- Name: inserting_orders(integer); Type: PROCEDURE; Schema: public; Owner: admin
--

CREATE PROCEDURE public.inserting_orders(rows_count integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	car_count INT;
	temp_customer INT;
	temp_branch INT;
	temp_car INT;
	temp_days INT;
	temp_date TIMESTAMP;
BEGIN
	SELECT COUNT(*) INTO car_count FROM car;
	FOR i IN 1..car_count LOOP
		INSERT INTO orders(customer_id, car_id, renting_days, renting_date)
		VALUES (i, i, random_between(1, 6), random_date());
	END LOOP;
END;
$$;


ALTER PROCEDURE public.inserting_orders(rows_count integer) OWNER TO admin;

--
-- TOC entry 210 (class 1255 OID 17018)
-- Name: random_between(integer, integer); Type: FUNCTION; Schema: public; Owner: admin
--

CREATE FUNCTION public.random_between(low integer, high integer) RETURNS integer
    LANGUAGE plpgsql
    AS $$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$;


ALTER FUNCTION public.random_between(low integer, high integer) OWNER TO admin;

--
-- TOC entry 223 (class 1255 OID 17019)
-- Name: random_date(); Type: FUNCTION; Schema: public; Owner: admin
--

CREATE FUNCTION public.random_date() RETURNS timestamp without time zone
    LANGUAGE plpgsql
    AS $$
BEGIN
	SET datestyle TO DMY, SQL;
	RETURN date_trunc('day', NOW() + (random() * (interval '90 days')) + '30 days');
END;
$$;


ALTER FUNCTION public.random_date() OWNER TO admin;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 17212)
-- Name: address_telephone; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.address_telephone (
    at_id integer NOT NULL,
    city character varying,
    street character varying,
    house integer,
    telephone character varying
);


ALTER TABLE public.address_telephone OWNER TO admin;

--
-- TOC entry 200 (class 1259 OID 17210)
-- Name: address_telephone_at_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.address_telephone_at_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.address_telephone_at_id_seq OWNER TO admin;

--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 200
-- Name: address_telephone_at_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.address_telephone_at_id_seq OWNED BY public.address_telephone.at_id;


--
-- TOC entry 205 (class 1259 OID 17239)
-- Name: branch; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.branch (
    branch_id integer NOT NULL,
    info_id integer NOT NULL,
    number integer NOT NULL
);


ALTER TABLE public.branch OWNER TO admin;

--
-- TOC entry 204 (class 1259 OID 17237)
-- Name: branch_branch_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.branch_branch_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.branch_branch_id_seq OWNER TO admin;

--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 204
-- Name: branch_branch_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.branch_branch_id_seq OWNED BY public.branch.branch_id;


--
-- TOC entry 207 (class 1259 OID 17286)
-- Name: car; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.car (
    car_id integer NOT NULL,
    branch_id integer NOT NULL,
    brand character varying NOT NULL,
    model character varying NOT NULL,
    number character varying NOT NULL,
    price money NOT NULL
);


ALTER TABLE public.car OWNER TO admin;

--
-- TOC entry 206 (class 1259 OID 17284)
-- Name: car_car_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.car_car_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.car_car_id_seq OWNER TO admin;

--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 206
-- Name: car_car_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.car_car_id_seq OWNED BY public.car.car_id;


--
-- TOC entry 203 (class 1259 OID 17223)
-- Name: customer; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.customer (
    customer_id integer NOT NULL,
    info_id integer NOT NULL,
    first_name character varying,
    last_name character varying
);


ALTER TABLE public.customer OWNER TO admin;

--
-- TOC entry 202 (class 1259 OID 17221)
-- Name: customer_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.customer_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_customer_id_seq OWNER TO admin;

--
-- TOC entry 3007 (class 0 OID 0)
-- Dependencies: 202
-- Name: customer_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.customer_customer_id_seq OWNED BY public.customer.customer_id;


--
-- TOC entry 209 (class 1259 OID 17302)
-- Name: orders; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    customer_id integer NOT NULL,
    car_id integer NOT NULL,
    renting_days integer NOT NULL,
    renting_date timestamp(6) without time zone NOT NULL
);


ALTER TABLE public.orders OWNER TO admin;

--
-- TOC entry 208 (class 1259 OID 17300)
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_id_seq OWNER TO admin;

--
-- TOC entry 3008 (class 0 OID 0)
-- Dependencies: 208
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- TOC entry 2837 (class 2604 OID 17215)
-- Name: address_telephone at_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.address_telephone ALTER COLUMN at_id SET DEFAULT nextval('public.address_telephone_at_id_seq'::regclass);


--
-- TOC entry 2839 (class 2604 OID 17242)
-- Name: branch branch_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.branch ALTER COLUMN branch_id SET DEFAULT nextval('public.branch_branch_id_seq'::regclass);


--
-- TOC entry 2840 (class 2604 OID 17289)
-- Name: car car_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.car ALTER COLUMN car_id SET DEFAULT nextval('public.car_car_id_seq'::regclass);


--
-- TOC entry 2838 (class 2604 OID 17226)
-- Name: customer customer_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.customer ALTER COLUMN customer_id SET DEFAULT nextval('public.customer_customer_id_seq'::regclass);


--
-- TOC entry 2841 (class 2604 OID 17305)
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- TOC entry 2990 (class 0 OID 17212)
-- Dependencies: 201
-- Data for Name: address_telephone; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.address_telephone (at_id, city, street, house, telephone) FROM stdin;
1	city1	street1	1	phone1
2	city2	street2	2	phone2
3	city3	street3	3	phone3
4	city4	street4	4	phone4
5	city5	street5	5	phone5
6	city6	street6	6	phone6
7	city7	street7	7	phone7
8	city8	street8	8	phone8
9	city9	street9	9	phone9
10	city10	street10	10	phone10
11	city11	street11	11	phone11
12	city12	street12	12	phone12
13	city13	street13	13	phone13
14	city14	street14	14	phone14
15	city15	street15	15	phone15
16	city16	street16	16	phone16
17	city17	street17	17	phone17
18	city18	street18	18	phone18
19	city19	street19	19	phone19
20	city20	street20	20	phone20
21	city21	street21	21	phone21
22	city22	street22	22	phone22
23	city23	street23	23	phone23
24	city24	street24	24	phone24
25	city25	street25	25	phone25
26	city26	street26	26	phone26
27	city27	street27	27	phone27
28	city28	street28	28	phone28
29	city29	street29	29	phone29
30	city30	street30	30	phone30
31	city31	street31	31	phone31
32	city32	street32	32	phone32
33	city33	street33	33	phone33
34	city34	street34	34	phone34
35	city35	street35	35	phone35
36	city36	street36	36	phone36
37	city37	street37	37	phone37
38	city38	street38	38	phone38
39	city39	street39	39	phone39
40	city40	street40	40	phone40
41	city41	street41	41	phone41
42	city42	street42	42	phone42
43	city43	street43	43	phone43
44	city44	street44	44	phone44
45	city45	street45	45	phone45
46	city46	street46	46	phone46
47	city47	street47	47	phone47
48	city48	street48	48	phone48
49	city49	street49	49	phone49
50	city50	street50	50	phone50
51	city51	street51	51	phone51
52	city52	street52	52	phone52
53	city53	street53	53	phone53
54	city54	street54	54	phone54
55	city55	street55	55	phone55
56	city56	street56	56	phone56
57	city57	street57	57	phone57
58	city58	street58	58	phone58
59	city59	street59	59	phone59
60	city60	street60	60	phone60
61	city61	street61	61	phone61
62	city62	street62	62	phone62
63	city63	street63	63	phone63
64	city64	street64	64	phone64
65	city65	street65	65	phone65
66	city66	street66	66	phone66
67	city67	street67	67	phone67
68	city68	street68	68	phone68
69	city69	street69	69	phone69
70	city70	street70	70	phone70
71	city71	street71	71	phone71
72	city72	street72	72	phone72
73	city73	street73	73	phone73
74	city74	street74	74	phone74
75	city75	street75	75	phone75
76	city76	street76	76	phone76
77	city77	street77	77	phone77
78	city78	street78	78	phone78
79	city79	street79	79	phone79
80	city80	street80	80	phone80
81	city81	street81	81	phone81
82	city82	street82	82	phone82
83	city83	street83	83	phone83
84	city84	street84	84	phone84
85	city85	street85	85	phone85
86	city86	street86	86	phone86
87	city87	street87	87	phone87
88	city88	street88	88	phone88
89	city89	street89	89	phone89
90	city90	street90	90	phone90
91	city91	street91	91	phone91
92	city92	street92	92	phone92
93	city93	street93	93	phone93
94	city94	street94	94	phone94
95	city95	street95	95	phone95
96	city96	street96	96	phone96
97	city97	street97	97	phone97
98	city98	street98	98	phone98
99	city99	street99	99	phone99
100	city100	street100	100	phone100
101	city101	street101	101	phone101
102	city102	street102	102	phone102
103	city103	street103	103	phone103
104	city104	street104	104	phone104
105	city105	street105	105	phone105
106	city106	street106	106	phone106
107	city107	street107	107	phone107
108	city108	street108	108	phone108
109	city109	street109	109	phone109
110	city110	street110	110	phone110
111	city111	street111	111	phone111
112	city112	street112	112	phone112
113	city113	street113	113	phone113
114	city114	street114	114	phone114
115	city115	street115	115	phone115
116	city116	street116	116	phone116
117	city117	street117	117	phone117
118	city118	street118	118	phone118
119	city119	street119	119	phone119
120	city120	street120	120	phone120
121	city121	street121	121	phone121
122	city122	street122	122	phone122
123	city123	street123	123	phone123
124	city124	street124	124	phone124
125	city125	street125	125	phone125
126	city126	street126	126	phone126
127	city127	street127	127	phone127
128	city128	street128	128	phone128
129	city129	street129	129	phone129
130	city130	street130	130	phone130
131	city131	street131	131	phone131
132	city132	street132	132	phone132
133	city133	street133	133	phone133
134	city134	street134	134	phone134
135	city135	street135	135	phone135
136	city136	street136	136	phone136
137	city137	street137	137	phone137
138	city138	street138	138	phone138
139	city139	street139	139	phone139
140	city140	street140	140	phone140
141	city141	street141	141	phone141
142	city142	street142	142	phone142
143	city143	street143	143	phone143
144	city144	street144	144	phone144
145	city145	street145	145	phone145
146	city146	street146	146	phone146
147	city147	street147	147	phone147
148	city148	street148	148	phone148
149	city149	street149	149	phone149
150	city150	street150	150	phone150
151	city151	street151	151	phone151
152	city152	street152	152	phone152
153	city153	street153	153	phone153
154	city154	street154	154	phone154
155	city155	street155	155	phone155
156	city156	street156	156	phone156
157	city157	street157	157	phone157
158	city158	street158	158	phone158
159	city159	street159	159	phone159
160	city160	street160	160	phone160
161	city161	street161	161	phone161
162	city162	street162	162	phone162
163	city163	street163	163	phone163
164	city164	street164	164	phone164
165	city165	street165	165	phone165
166	city166	street166	166	phone166
167	city167	street167	167	phone167
168	city168	street168	168	phone168
169	city169	street169	169	phone169
170	city170	street170	170	phone170
171	city171	street171	171	phone171
172	city172	street172	172	phone172
173	city173	street173	173	phone173
174	city174	street174	174	phone174
175	city175	street175	175	phone175
176	city176	street176	176	phone176
177	city177	street177	177	phone177
178	city178	street178	178	phone178
179	city179	street179	179	phone179
180	city180	street180	180	phone180
181	city181	street181	181	phone181
182	city182	street182	182	phone182
183	city183	street183	183	phone183
184	city184	street184	184	phone184
185	city185	street185	185	phone185
186	city186	street186	186	phone186
187	city187	street187	187	phone187
188	city188	street188	188	phone188
189	city189	street189	189	phone189
190	city190	street190	190	phone190
191	city191	street191	191	phone191
192	city192	street192	192	phone192
193	city193	street193	193	phone193
194	city194	street194	194	phone194
195	city195	street195	195	phone195
196	city196	street196	196	phone196
197	city197	street197	197	phone197
198	city198	street198	198	phone198
199	city199	street199	199	phone199
200	city200	street200	200	phone200
201	city201	street201	201	phone201
202	city202	street202	202	phone202
203	city203	street203	203	phone203
204	city204	street204	204	phone204
205	city205	street205	205	phone205
206	city206	street206	206	phone206
207	city207	street207	207	phone207
208	city208	street208	208	phone208
209	city209	street209	209	phone209
210	city210	street210	210	phone210
211	city211	street211	211	phone211
212	city212	street212	212	phone212
213	city213	street213	213	phone213
214	city214	street214	214	phone214
215	city215	street215	215	phone215
216	city216	street216	216	phone216
217	city217	street217	217	phone217
218	city218	street218	218	phone218
219	city219	street219	219	phone219
220	city220	street220	220	phone220
221	city221	street221	221	phone221
222	city222	street222	222	phone222
223	city223	street223	223	phone223
224	city224	street224	224	phone224
225	city225	street225	225	phone225
226	city226	street226	226	phone226
227	city227	street227	227	phone227
228	city228	street228	228	phone228
229	city229	street229	229	phone229
230	city230	street230	230	phone230
231	city231	street231	231	phone231
232	city232	street232	232	phone232
233	city233	street233	233	phone233
234	city234	street234	234	phone234
235	city235	street235	235	phone235
236	city236	street236	236	phone236
237	city237	street237	237	phone237
238	city238	street238	238	phone238
239	city239	street239	239	phone239
240	city240	street240	240	phone240
241	city241	street241	241	phone241
242	city242	street242	242	phone242
243	city243	street243	243	phone243
244	city244	street244	244	phone244
245	city245	street245	245	phone245
246	city246	street246	246	phone246
247	city247	street247	247	phone247
248	city248	street248	248	phone248
249	city249	street249	249	phone249
250	city250	street250	250	phone250
251	city251	street251	251	phone251
252	city252	street252	252	phone252
253	city253	street253	253	phone253
254	city254	street254	254	phone254
255	city255	street255	255	phone255
256	city256	street256	256	phone256
257	city257	street257	257	phone257
258	city258	street258	258	phone258
259	city259	street259	259	phone259
260	city260	street260	260	phone260
261	city261	street261	261	phone261
262	city262	street262	262	phone262
263	city263	street263	263	phone263
264	city264	street264	264	phone264
265	city265	street265	265	phone265
266	city266	street266	266	phone266
267	city267	street267	267	phone267
268	city268	street268	268	phone268
269	city269	street269	269	phone269
270	city270	street270	270	phone270
271	city271	street271	271	phone271
272	city272	street272	272	phone272
273	city273	street273	273	phone273
274	city274	street274	274	phone274
275	city275	street275	275	phone275
276	city276	street276	276	phone276
277	city277	street277	277	phone277
278	city278	street278	278	phone278
279	city279	street279	279	phone279
280	city280	street280	280	phone280
281	city281	street281	281	phone281
282	city282	street282	282	phone282
283	city283	street283	283	phone283
284	city284	street284	284	phone284
285	city285	street285	285	phone285
286	city286	street286	286	phone286
287	city287	street287	287	phone287
288	city288	street288	288	phone288
289	city289	street289	289	phone289
290	city290	street290	290	phone290
291	city291	street291	291	phone291
292	city292	street292	292	phone292
293	city293	street293	293	phone293
294	city294	street294	294	phone294
295	city295	street295	295	phone295
296	city296	street296	296	phone296
297	city297	street297	297	phone297
298	city298	street298	298	phone298
299	city299	street299	299	phone299
300	city300	street300	300	phone300
301	city301	street301	301	phone301
302	city302	street302	302	phone302
303	city303	street303	303	phone303
304	city304	street304	304	phone304
305	city305	street305	305	phone305
306	city306	street306	306	phone306
307	city307	street307	307	phone307
308	city308	street308	308	phone308
309	city309	street309	309	phone309
310	city310	street310	310	phone310
311	city311	street311	311	phone311
312	city312	street312	312	phone312
313	city313	street313	313	phone313
314	city314	street314	314	phone314
315	city315	street315	315	phone315
316	city316	street316	316	phone316
317	city317	street317	317	phone317
318	city318	street318	318	phone318
319	city319	street319	319	phone319
320	city320	street320	320	phone320
321	city321	street321	321	phone321
322	city322	street322	322	phone322
323	city323	street323	323	phone323
324	city324	street324	324	phone324
325	city325	street325	325	phone325
326	city326	street326	326	phone326
327	city327	street327	327	phone327
328	city328	street328	328	phone328
329	city329	street329	329	phone329
330	city330	street330	330	phone330
331	city331	street331	331	phone331
332	city332	street332	332	phone332
333	city333	street333	333	phone333
334	city334	street334	334	phone334
335	city335	street335	335	phone335
336	city336	street336	336	phone336
337	city337	street337	337	phone337
338	city338	street338	338	phone338
339	city339	street339	339	phone339
340	city340	street340	340	phone340
341	city341	street341	341	phone341
342	city342	street342	342	phone342
343	city343	street343	343	phone343
344	city344	street344	344	phone344
345	city345	street345	345	phone345
346	city346	street346	346	phone346
347	city347	street347	347	phone347
348	city348	street348	348	phone348
349	city349	street349	349	phone349
350	city350	street350	350	phone350
351	city351	street351	351	phone351
352	city352	street352	352	phone352
353	city353	street353	353	phone353
354	city354	street354	354	phone354
355	city355	street355	355	phone355
356	city356	street356	356	phone356
357	city357	street357	357	phone357
358	city358	street358	358	phone358
359	city359	street359	359	phone359
360	city360	street360	360	phone360
361	city361	street361	361	phone361
362	city362	street362	362	phone362
363	city363	street363	363	phone363
364	city364	street364	364	phone364
365	city365	street365	365	phone365
366	city366	street366	366	phone366
367	city367	street367	367	phone367
368	city368	street368	368	phone368
369	city369	street369	369	phone369
370	city370	street370	370	phone370
371	city371	street371	371	phone371
372	city372	street372	372	phone372
373	city373	street373	373	phone373
374	city374	street374	374	phone374
375	city375	street375	375	phone375
376	city376	street376	376	phone376
377	city377	street377	377	phone377
378	city378	street378	378	phone378
379	city379	street379	379	phone379
380	city380	street380	380	phone380
381	city381	street381	381	phone381
382	city382	street382	382	phone382
383	city383	street383	383	phone383
384	city384	street384	384	phone384
385	city385	street385	385	phone385
386	city386	street386	386	phone386
387	city387	street387	387	phone387
388	city388	street388	388	phone388
389	city389	street389	389	phone389
390	city390	street390	390	phone390
391	city391	street391	391	phone391
392	city392	street392	392	phone392
393	city393	street393	393	phone393
394	city394	street394	394	phone394
395	city395	street395	395	phone395
396	city396	street396	396	phone396
397	city397	street397	397	phone397
398	city398	street398	398	phone398
399	city399	street399	399	phone399
400	city400	street400	400	phone400
401	city401	street401	401	phone401
402	city402	street402	402	phone402
403	city403	street403	403	phone403
404	city404	street404	404	phone404
405	city405	street405	405	phone405
406	city406	street406	406	phone406
407	city407	street407	407	phone407
408	city408	street408	408	phone408
409	city409	street409	409	phone409
410	city410	street410	410	phone410
411	city411	street411	411	phone411
412	city412	street412	412	phone412
413	city413	street413	413	phone413
414	city414	street414	414	phone414
415	city415	street415	415	phone415
416	city416	street416	416	phone416
417	city417	street417	417	phone417
418	city418	street418	418	phone418
419	city419	street419	419	phone419
420	city420	street420	420	phone420
421	city421	street421	421	phone421
422	city422	street422	422	phone422
423	city423	street423	423	phone423
424	city424	street424	424	phone424
425	city425	street425	425	phone425
426	city426	street426	426	phone426
427	city427	street427	427	phone427
428	city428	street428	428	phone428
429	city429	street429	429	phone429
430	city430	street430	430	phone430
431	city431	street431	431	phone431
432	city432	street432	432	phone432
433	city433	street433	433	phone433
434	city434	street434	434	phone434
435	city435	street435	435	phone435
436	city436	street436	436	phone436
437	city437	street437	437	phone437
438	city438	street438	438	phone438
439	city439	street439	439	phone439
440	city440	street440	440	phone440
441	city441	street441	441	phone441
442	city442	street442	442	phone442
443	city443	street443	443	phone443
444	city444	street444	444	phone444
445	city445	street445	445	phone445
446	city446	street446	446	phone446
447	city447	street447	447	phone447
448	city448	street448	448	phone448
449	city449	street449	449	phone449
450	city450	street450	450	phone450
451	city451	street451	451	phone451
452	city452	street452	452	phone452
453	city453	street453	453	phone453
454	city454	street454	454	phone454
455	city455	street455	455	phone455
456	city456	street456	456	phone456
457	city457	street457	457	phone457
458	city458	street458	458	phone458
459	city459	street459	459	phone459
460	city460	street460	460	phone460
461	city461	street461	461	phone461
462	city462	street462	462	phone462
463	city463	street463	463	phone463
464	city464	street464	464	phone464
465	city465	street465	465	phone465
466	city466	street466	466	phone466
467	city467	street467	467	phone467
468	city468	street468	468	phone468
469	city469	street469	469	phone469
470	city470	street470	470	phone470
471	city471	street471	471	phone471
472	city472	street472	472	phone472
473	city473	street473	473	phone473
474	city474	street474	474	phone474
475	city475	street475	475	phone475
476	city476	street476	476	phone476
477	city477	street477	477	phone477
478	city478	street478	478	phone478
479	city479	street479	479	phone479
480	city480	street480	480	phone480
481	city481	street481	481	phone481
482	city482	street482	482	phone482
483	city483	street483	483	phone483
484	city484	street484	484	phone484
485	city485	street485	485	phone485
486	city486	street486	486	phone486
487	city487	street487	487	phone487
488	city488	street488	488	phone488
489	city489	street489	489	phone489
490	city490	street490	490	phone490
491	city491	street491	491	phone491
492	city492	street492	492	phone492
493	city493	street493	493	phone493
494	city494	street494	494	phone494
495	city495	street495	495	phone495
496	city496	street496	496	phone496
497	city497	street497	497	phone497
498	city498	street498	498	phone498
499	city499	street499	499	phone499
500	city500	street500	500	phone500
\.


--
-- TOC entry 2994 (class 0 OID 17239)
-- Dependencies: 205
-- Data for Name: branch; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.branch (branch_id, info_id, number) FROM stdin;
1	251	1
2	252	2
3	253	3
4	254	4
5	255	5
6	256	6
7	257	7
8	258	8
9	259	9
10	260	10
11	261	11
12	262	12
13	263	13
14	264	14
15	265	15
16	266	16
17	267	17
18	268	18
19	269	19
20	270	20
21	271	21
22	272	22
23	273	23
24	274	24
25	275	25
26	276	26
27	277	27
28	278	28
29	279	29
30	280	30
31	281	31
32	282	32
33	283	33
34	284	34
35	285	35
36	286	36
37	287	37
38	288	38
39	289	39
40	290	40
41	291	41
42	292	42
43	293	43
44	294	44
45	295	45
46	296	46
47	297	47
48	298	48
49	299	49
50	300	50
51	301	51
52	302	52
53	303	53
54	304	54
55	305	55
56	306	56
57	307	57
58	308	58
59	309	59
60	310	60
61	311	61
62	312	62
63	313	63
64	314	64
65	315	65
66	316	66
67	317	67
68	318	68
69	319	69
70	320	70
71	321	71
72	322	72
73	323	73
74	324	74
75	325	75
76	326	76
77	327	77
78	328	78
79	329	79
80	330	80
81	331	81
82	332	82
83	333	83
84	334	84
85	335	85
86	336	86
87	337	87
88	338	88
89	339	89
90	340	90
91	341	91
92	342	92
93	343	93
94	344	94
95	345	95
96	346	96
97	347	97
98	348	98
99	349	99
100	350	100
101	351	101
102	352	102
103	353	103
104	354	104
105	355	105
106	356	106
107	357	107
108	358	108
109	359	109
110	360	110
111	361	111
112	362	112
113	363	113
114	364	114
115	365	115
116	366	116
117	367	117
118	368	118
119	369	119
120	370	120
121	371	121
122	372	122
123	373	123
124	374	124
125	375	125
126	376	126
127	377	127
128	378	128
129	379	129
130	380	130
131	381	131
132	382	132
133	383	133
134	384	134
135	385	135
136	386	136
137	387	137
138	388	138
139	389	139
140	390	140
141	391	141
142	392	142
143	393	143
144	394	144
145	395	145
146	396	146
147	397	147
148	398	148
149	399	149
150	400	150
151	401	151
152	402	152
153	403	153
154	404	154
155	405	155
156	406	156
157	407	157
158	408	158
159	409	159
160	410	160
161	411	161
162	412	162
163	413	163
164	414	164
165	415	165
166	416	166
167	417	167
168	418	168
169	419	169
170	420	170
171	421	171
172	422	172
173	423	173
174	424	174
175	425	175
176	426	176
177	427	177
178	428	178
179	429	179
180	430	180
181	431	181
182	432	182
183	433	183
184	434	184
185	435	185
186	436	186
187	437	187
188	438	188
189	439	189
190	440	190
191	441	191
192	442	192
193	443	193
194	444	194
195	445	195
196	446	196
197	447	197
198	448	198
199	449	199
200	450	200
\.


--
-- TOC entry 2996 (class 0 OID 17286)
-- Dependencies: 207
-- Data for Name: car; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.car (car_id, branch_id, brand, model, number, price) FROM stdin;
1	1	brand1	model1	number#1	$100.00
2	2	brand2	model2	number#2	$200.00
3	3	brand3	model3	number#3	$300.00
4	4	brand4	model4	number#4	$400.00
5	5	brand5	model5	number#5	$500.00
6	6	brand6	model6	number#6	$600.00
7	7	brand7	model7	number#7	$700.00
8	8	brand8	model8	number#8	$800.00
9	9	brand9	model9	number#9	$900.00
10	10	brand10	model10	number#10	$1,000.00
11	11	brand11	model11	number#11	$1,100.00
12	12	brand12	model12	number#12	$1,200.00
13	13	brand13	model13	number#13	$1,300.00
14	14	brand14	model14	number#14	$1,400.00
15	15	brand15	model15	number#15	$1,500.00
16	16	brand16	model16	number#16	$1,600.00
17	17	brand17	model17	number#17	$1,700.00
18	18	brand18	model18	number#18	$1,800.00
19	19	brand19	model19	number#19	$1,900.00
20	20	brand20	model20	number#20	$2,000.00
21	21	brand21	model21	number#21	$2,100.00
22	22	brand22	model22	number#22	$2,200.00
23	23	brand23	model23	number#23	$2,300.00
24	24	brand24	model24	number#24	$2,400.00
25	25	brand25	model25	number#25	$2,500.00
26	26	brand26	model26	number#26	$2,600.00
27	27	brand27	model27	number#27	$2,700.00
28	28	brand28	model28	number#28	$2,800.00
29	29	brand29	model29	number#29	$2,900.00
30	30	brand30	model30	number#30	$3,000.00
31	31	brand31	model31	number#31	$3,100.00
32	32	brand32	model32	number#32	$3,200.00
33	33	brand33	model33	number#33	$3,300.00
34	34	brand34	model34	number#34	$3,400.00
35	35	brand35	model35	number#35	$3,500.00
36	36	brand36	model36	number#36	$3,600.00
37	37	brand37	model37	number#37	$3,700.00
38	38	brand38	model38	number#38	$3,800.00
39	39	brand39	model39	number#39	$3,900.00
40	40	brand40	model40	number#40	$4,000.00
41	41	brand41	model41	number#41	$4,100.00
42	42	brand42	model42	number#42	$4,200.00
43	43	brand43	model43	number#43	$4,300.00
44	44	brand44	model44	number#44	$4,400.00
45	45	brand45	model45	number#45	$4,500.00
46	46	brand46	model46	number#46	$4,600.00
47	47	brand47	model47	number#47	$4,700.00
48	48	brand48	model48	number#48	$4,800.00
49	49	brand49	model49	number#49	$4,900.00
50	50	brand50	model50	number#50	$5,000.00
51	51	brand51	model51	number#51	$5,100.00
52	52	brand52	model52	number#52	$5,200.00
53	53	brand53	model53	number#53	$5,300.00
54	54	brand54	model54	number#54	$5,400.00
55	55	brand55	model55	number#55	$5,500.00
56	56	brand56	model56	number#56	$5,600.00
57	57	brand57	model57	number#57	$5,700.00
58	58	brand58	model58	number#58	$5,800.00
59	59	brand59	model59	number#59	$5,900.00
60	60	brand60	model60	number#60	$6,000.00
61	61	brand61	model61	number#61	$6,100.00
62	62	brand62	model62	number#62	$6,200.00
63	63	brand63	model63	number#63	$6,300.00
64	64	brand64	model64	number#64	$6,400.00
65	65	brand65	model65	number#65	$6,500.00
66	66	brand66	model66	number#66	$6,600.00
67	67	brand67	model67	number#67	$6,700.00
68	68	brand68	model68	number#68	$6,800.00
69	69	brand69	model69	number#69	$6,900.00
70	70	brand70	model70	number#70	$7,000.00
71	71	brand71	model71	number#71	$7,100.00
72	72	brand72	model72	number#72	$7,200.00
73	73	brand73	model73	number#73	$7,300.00
74	74	brand74	model74	number#74	$7,400.00
75	75	brand75	model75	number#75	$7,500.00
76	76	brand76	model76	number#76	$7,600.00
77	77	brand77	model77	number#77	$7,700.00
78	78	brand78	model78	number#78	$7,800.00
79	79	brand79	model79	number#79	$7,900.00
80	80	brand80	model80	number#80	$8,000.00
81	81	brand81	model81	number#81	$8,100.00
82	82	brand82	model82	number#82	$8,200.00
83	83	brand83	model83	number#83	$8,300.00
84	84	brand84	model84	number#84	$8,400.00
85	85	brand85	model85	number#85	$8,500.00
86	86	brand86	model86	number#86	$8,600.00
87	87	brand87	model87	number#87	$8,700.00
88	88	brand88	model88	number#88	$8,800.00
89	89	brand89	model89	number#89	$8,900.00
90	90	brand90	model90	number#90	$9,000.00
91	91	brand91	model91	number#91	$9,100.00
92	92	brand92	model92	number#92	$9,200.00
93	93	brand93	model93	number#93	$9,300.00
94	94	brand94	model94	number#94	$9,400.00
95	95	brand95	model95	number#95	$9,500.00
96	96	brand96	model96	number#96	$9,600.00
97	97	brand97	model97	number#97	$9,700.00
98	98	brand98	model98	number#98	$9,800.00
99	99	brand99	model99	number#99	$9,900.00
100	100	brand100	model100	number#100	$10,000.00
\.


--
-- TOC entry 2992 (class 0 OID 17223)
-- Dependencies: 203
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.customer (customer_id, info_id, first_name, last_name) FROM stdin;
1	1	first-name1	last-name1
2	2	first-name2	last-name2
3	3	first-name3	last-name3
4	4	first-name4	last-name4
5	5	first-name5	last-name5
6	6	first-name6	last-name6
7	7	first-name7	last-name7
8	8	first-name8	last-name8
9	9	first-name9	last-name9
10	10	first-name10	last-name10
11	11	first-name11	last-name11
12	12	first-name12	last-name12
13	13	first-name13	last-name13
14	14	first-name14	last-name14
15	15	first-name15	last-name15
16	16	first-name16	last-name16
17	17	first-name17	last-name17
18	18	first-name18	last-name18
19	19	first-name19	last-name19
20	20	first-name20	last-name20
21	21	first-name21	last-name21
22	22	first-name22	last-name22
23	23	first-name23	last-name23
24	24	first-name24	last-name24
25	25	first-name25	last-name25
26	26	first-name26	last-name26
27	27	first-name27	last-name27
28	28	first-name28	last-name28
29	29	first-name29	last-name29
30	30	first-name30	last-name30
31	31	first-name31	last-name31
32	32	first-name32	last-name32
33	33	first-name33	last-name33
34	34	first-name34	last-name34
35	35	first-name35	last-name35
36	36	first-name36	last-name36
37	37	first-name37	last-name37
38	38	first-name38	last-name38
39	39	first-name39	last-name39
40	40	first-name40	last-name40
41	41	first-name41	last-name41
42	42	first-name42	last-name42
43	43	first-name43	last-name43
44	44	first-name44	last-name44
45	45	first-name45	last-name45
46	46	first-name46	last-name46
47	47	first-name47	last-name47
48	48	first-name48	last-name48
49	49	first-name49	last-name49
50	50	first-name50	last-name50
51	51	first-name51	last-name51
52	52	first-name52	last-name52
53	53	first-name53	last-name53
54	54	first-name54	last-name54
55	55	first-name55	last-name55
56	56	first-name56	last-name56
57	57	first-name57	last-name57
58	58	first-name58	last-name58
59	59	first-name59	last-name59
60	60	first-name60	last-name60
61	61	first-name61	last-name61
62	62	first-name62	last-name62
63	63	first-name63	last-name63
64	64	first-name64	last-name64
65	65	first-name65	last-name65
66	66	first-name66	last-name66
67	67	first-name67	last-name67
68	68	first-name68	last-name68
69	69	first-name69	last-name69
70	70	first-name70	last-name70
71	71	first-name71	last-name71
72	72	first-name72	last-name72
73	73	first-name73	last-name73
74	74	first-name74	last-name74
75	75	first-name75	last-name75
76	76	first-name76	last-name76
77	77	first-name77	last-name77
78	78	first-name78	last-name78
79	79	first-name79	last-name79
80	80	first-name80	last-name80
81	81	first-name81	last-name81
82	82	first-name82	last-name82
83	83	first-name83	last-name83
84	84	first-name84	last-name84
85	85	first-name85	last-name85
86	86	first-name86	last-name86
87	87	first-name87	last-name87
88	88	first-name88	last-name88
89	89	first-name89	last-name89
90	90	first-name90	last-name90
91	91	first-name91	last-name91
92	92	first-name92	last-name92
93	93	first-name93	last-name93
94	94	first-name94	last-name94
95	95	first-name95	last-name95
96	96	first-name96	last-name96
97	97	first-name97	last-name97
98	98	first-name98	last-name98
99	99	first-name99	last-name99
100	100	first-name100	last-name100
101	101	first-name101	last-name101
102	102	first-name102	last-name102
103	103	first-name103	last-name103
104	104	first-name104	last-name104
105	105	first-name105	last-name105
106	106	first-name106	last-name106
107	107	first-name107	last-name107
108	108	first-name108	last-name108
109	109	first-name109	last-name109
110	110	first-name110	last-name110
111	111	first-name111	last-name111
112	112	first-name112	last-name112
113	113	first-name113	last-name113
114	114	first-name114	last-name114
115	115	first-name115	last-name115
116	116	first-name116	last-name116
117	117	first-name117	last-name117
118	118	first-name118	last-name118
119	119	first-name119	last-name119
120	120	first-name120	last-name120
121	121	first-name121	last-name121
122	122	first-name122	last-name122
123	123	first-name123	last-name123
124	124	first-name124	last-name124
125	125	first-name125	last-name125
126	126	first-name126	last-name126
127	127	first-name127	last-name127
128	128	first-name128	last-name128
129	129	first-name129	last-name129
130	130	first-name130	last-name130
131	131	first-name131	last-name131
132	132	first-name132	last-name132
133	133	first-name133	last-name133
134	134	first-name134	last-name134
135	135	first-name135	last-name135
136	136	first-name136	last-name136
137	137	first-name137	last-name137
138	138	first-name138	last-name138
139	139	first-name139	last-name139
140	140	first-name140	last-name140
141	141	first-name141	last-name141
142	142	first-name142	last-name142
143	143	first-name143	last-name143
144	144	first-name144	last-name144
145	145	first-name145	last-name145
146	146	first-name146	last-name146
147	147	first-name147	last-name147
148	148	first-name148	last-name148
149	149	first-name149	last-name149
150	150	first-name150	last-name150
151	151	first-name151	last-name151
152	152	first-name152	last-name152
153	153	first-name153	last-name153
154	154	first-name154	last-name154
155	155	first-name155	last-name155
156	156	first-name156	last-name156
157	157	first-name157	last-name157
158	158	first-name158	last-name158
159	159	first-name159	last-name159
160	160	first-name160	last-name160
161	161	first-name161	last-name161
162	162	first-name162	last-name162
163	163	first-name163	last-name163
164	164	first-name164	last-name164
165	165	first-name165	last-name165
166	166	first-name166	last-name166
167	167	first-name167	last-name167
168	168	first-name168	last-name168
169	169	first-name169	last-name169
170	170	first-name170	last-name170
171	171	first-name171	last-name171
172	172	first-name172	last-name172
173	173	first-name173	last-name173
174	174	first-name174	last-name174
175	175	first-name175	last-name175
176	176	first-name176	last-name176
177	177	first-name177	last-name177
178	178	first-name178	last-name178
179	179	first-name179	last-name179
180	180	first-name180	last-name180
181	181	first-name181	last-name181
182	182	first-name182	last-name182
183	183	first-name183	last-name183
184	184	first-name184	last-name184
185	185	first-name185	last-name185
186	186	first-name186	last-name186
187	187	first-name187	last-name187
188	188	first-name188	last-name188
189	189	first-name189	last-name189
190	190	first-name190	last-name190
191	191	first-name191	last-name191
192	192	first-name192	last-name192
193	193	first-name193	last-name193
194	194	first-name194	last-name194
195	195	first-name195	last-name195
196	196	first-name196	last-name196
197	197	first-name197	last-name197
198	198	first-name198	last-name198
199	199	first-name199	last-name199
200	200	first-name200	last-name200
\.


--
-- TOC entry 2998 (class 0 OID 17302)
-- Dependencies: 209
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.orders (order_id, customer_id, car_id, renting_days, renting_date) FROM stdin;
1	1	1	1	2021-09-08 00:00:00
2	2	2	1	2021-09-11 00:00:00
3	3	3	3	2021-10-12 00:00:00
4	4	4	1	2021-08-17 00:00:00
5	5	5	4	2021-09-05 00:00:00
6	6	6	5	2021-09-30 00:00:00
7	7	7	6	2021-08-22 00:00:00
8	8	8	1	2021-07-31 00:00:00
9	9	9	6	2021-08-18 00:00:00
10	10	10	6	2021-09-01 00:00:00
11	11	11	5	2021-08-15 00:00:00
12	12	12	4	2021-09-03 00:00:00
13	13	13	2	2021-08-22 00:00:00
14	14	14	4	2021-08-03 00:00:00
15	15	15	5	2021-08-01 00:00:00
16	16	16	3	2021-08-17 00:00:00
17	17	17	6	2021-08-19 00:00:00
18	18	18	6	2021-08-08 00:00:00
19	19	19	1	2021-07-28 00:00:00
20	20	20	5	2021-09-03 00:00:00
21	21	21	5	2021-09-29 00:00:00
22	22	22	1	2021-07-26 00:00:00
23	23	23	3	2021-09-22 00:00:00
24	24	24	4	2021-09-25 00:00:00
25	25	25	1	2021-08-07 00:00:00
26	26	26	5	2021-08-26 00:00:00
27	27	27	1	2021-10-17 00:00:00
28	28	28	5	2021-09-20 00:00:00
29	29	29	2	2021-09-22 00:00:00
30	30	30	4	2021-08-07 00:00:00
31	31	31	5	2021-09-28 00:00:00
32	32	32	2	2021-08-03 00:00:00
33	33	33	3	2021-10-18 00:00:00
34	34	34	6	2021-09-21 00:00:00
35	35	35	3	2021-08-11 00:00:00
36	36	36	5	2021-08-27 00:00:00
37	37	37	3	2021-08-06 00:00:00
38	38	38	3	2021-09-08 00:00:00
39	39	39	3	2021-10-10 00:00:00
40	40	40	1	2021-09-14 00:00:00
41	41	41	4	2021-09-02 00:00:00
42	42	42	1	2021-09-11 00:00:00
43	43	43	6	2021-08-14 00:00:00
44	44	44	1	2021-09-06 00:00:00
45	45	45	5	2021-08-22 00:00:00
46	46	46	6	2021-08-22 00:00:00
47	47	47	5	2021-10-18 00:00:00
48	48	48	2	2021-10-01 00:00:00
49	49	49	4	2021-08-09 00:00:00
50	50	50	3	2021-08-18 00:00:00
51	51	51	6	2021-09-12 00:00:00
52	52	52	6	2021-09-21 00:00:00
53	53	53	6	2021-10-07 00:00:00
54	54	54	2	2021-10-04 00:00:00
55	55	55	6	2021-09-09 00:00:00
56	56	56	1	2021-08-01 00:00:00
57	57	57	6	2021-08-15 00:00:00
58	58	58	4	2021-08-10 00:00:00
59	59	59	1	2021-09-12 00:00:00
60	60	60	5	2021-08-30 00:00:00
61	61	61	3	2021-08-25 00:00:00
62	62	62	4	2021-09-25 00:00:00
63	63	63	2	2021-08-09 00:00:00
64	64	64	6	2021-08-10 00:00:00
65	65	65	5	2021-09-13 00:00:00
66	66	66	2	2021-08-10 00:00:00
67	67	67	6	2021-07-21 00:00:00
68	68	68	1	2021-07-30 00:00:00
69	69	69	6	2021-09-16 00:00:00
70	70	70	1	2021-08-18 00:00:00
71	71	71	4	2021-09-19 00:00:00
72	72	72	2	2021-09-08 00:00:00
73	73	73	5	2021-08-07 00:00:00
74	74	74	5	2021-09-12 00:00:00
75	75	75	6	2021-08-05 00:00:00
76	76	76	1	2021-09-21 00:00:00
77	77	77	1	2021-10-03 00:00:00
78	78	78	3	2021-08-11 00:00:00
79	79	79	1	2021-10-19 00:00:00
80	80	80	2	2021-10-10 00:00:00
81	81	81	3	2021-09-18 00:00:00
82	82	82	2	2021-08-10 00:00:00
83	83	83	4	2021-08-13 00:00:00
84	84	84	1	2021-09-16 00:00:00
85	85	85	1	2021-09-29 00:00:00
86	86	86	4	2021-08-24 00:00:00
87	87	87	5	2021-07-24 00:00:00
88	88	88	5	2021-08-10 00:00:00
89	89	89	3	2021-10-08 00:00:00
90	90	90	4	2021-10-16 00:00:00
91	91	91	1	2021-07-29 00:00:00
92	92	92	3	2021-07-27 00:00:00
93	93	93	1	2021-10-05 00:00:00
94	94	94	3	2021-09-10 00:00:00
95	95	95	4	2021-07-30 00:00:00
96	96	96	4	2021-07-24 00:00:00
97	97	97	4	2021-09-17 00:00:00
98	98	98	3	2021-09-25 00:00:00
99	99	99	5	2021-08-30 00:00:00
100	100	100	4	2021-09-14 00:00:00
\.


--
-- TOC entry 3009 (class 0 OID 0)
-- Dependencies: 200
-- Name: address_telephone_at_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.address_telephone_at_id_seq', 500, true);


--
-- TOC entry 3010 (class 0 OID 0)
-- Dependencies: 204
-- Name: branch_branch_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.branch_branch_id_seq', 200, true);


--
-- TOC entry 3011 (class 0 OID 0)
-- Dependencies: 206
-- Name: car_car_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.car_car_id_seq', 100, true);


--
-- TOC entry 3012 (class 0 OID 0)
-- Dependencies: 202
-- Name: customer_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.customer_customer_id_seq', 200, true);


--
-- TOC entry 3013 (class 0 OID 0)
-- Dependencies: 208
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 100, true);


--
-- TOC entry 2843 (class 2606 OID 17220)
-- Name: address_telephone address_telephone_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.address_telephone
    ADD CONSTRAINT address_telephone_pkey PRIMARY KEY (at_id);


--
-- TOC entry 2847 (class 2606 OID 17244)
-- Name: branch branch_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.branch
    ADD CONSTRAINT branch_pkey PRIMARY KEY (branch_id);


--
-- TOC entry 2849 (class 2606 OID 17294)
-- Name: car car_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_pkey PRIMARY KEY (car_id);


--
-- TOC entry 2845 (class 2606 OID 17231)
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);


--
-- TOC entry 2853 (class 2606 OID 17307)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- TOC entry 2850 (class 1259 OID 24850)
-- Name: idx_renting_date; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_renting_date ON public.orders USING btree (renting_date);


--
-- TOC entry 2851 (class 1259 OID 24849)
-- Name: idx_renting_days; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX idx_renting_days ON public.orders USING btree (renting_days);


--
-- TOC entry 2855 (class 2606 OID 17245)
-- Name: branch branch_info_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.branch
    ADD CONSTRAINT branch_info_id_fkey FOREIGN KEY (info_id) REFERENCES public.address_telephone(at_id);


--
-- TOC entry 2856 (class 2606 OID 17295)
-- Name: car car_branch_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.car
    ADD CONSTRAINT car_branch_id_fkey FOREIGN KEY (branch_id) REFERENCES public.branch(branch_id);


--
-- TOC entry 2854 (class 2606 OID 17232)
-- Name: customer customer_info_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_info_id_fkey FOREIGN KEY (info_id) REFERENCES public.address_telephone(at_id);


--
-- TOC entry 2858 (class 2606 OID 17313)
-- Name: orders orders_car_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_car_id_fkey FOREIGN KEY (car_id) REFERENCES public.car(car_id);


--
-- TOC entry 2857 (class 2606 OID 17308)
-- Name: orders orders_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


-- Completed on 2021-06-22 08:50:06 UTC

--
-- PostgreSQL database dump complete
--

