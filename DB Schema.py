import psycopg2

conn = psycopg2.connect(host="elmer.db.elephantsql.com",database="mxywyuox", user="mxywyuox", password="vpK0uG4-H1k1JJM4E1TNVfdbEVNCN1Mq")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute('Drop Table CAR_MAKE')
cur.execute('Drop Table CAR_MODEL')
cur.execute('''CREATE TABLE CAR_MAKE
      (ID SERIAL  PRIMARY KEY,
      NAME           	CHAR(100)    NULL,
      MAKE       	 	char(100)    NULL,
      PRIORITY       	CHAR(100)	NULL,
      PARENT_CATEGORY 	CHAR(50)	NULL,
      image 			CHAR(100)	NULL,
      logo_Image		CHAR(100) 	NULL

             );''')


cur.execute('''CREATE TABLE CAR_MODEL
      (ID SERIAL PRIMARY KEY ,
      NAME           		CHAR(200)    NULL,
      MAKE       	 		char(200)    NULL,
      PRIORITY       		CHAR(500)	NULL,
      PARENT_CATEGORY	 	CHAR(500)	NULL,
      image 				CHAR(200)	NULL,
      MAKE_ID 				CHAR(200)	NULL,
      CAR_SERIES			CHAR(200)	NULL,
      FEUL_TYPE 			CHAR(200)	NULL,
      GEARBOX 				CHAR(200)	NULL,
      DOOR_TYPE 			CHAR(200)	NULL,
      CAR_MODEL 			CHAR(200)	NULL,
      CONTENT				CHAR(200)	NULL,
      STATUS 				CHAR(200)	NULL,
      FILE					CHAR(200)	NULL,
      DISPLAY_DATE			CHAR(200)	NULL,
      START_PRICE			CHAR(200)	NULL,
      END_PRICE				CHAR(200)	NULL,
      MOTOR					CHAR(200)	NULL,
      PHB					CHAR(200)	NULL,
      SUBTITLE				CHAR(200)	NULL,
      CAR_COLOR				CHAR(200)	NULL,
      CAR_TRIM 				CHAR(200)	NULL,
      CAR_PACK				CHAR(200)	NULL,
      CAR_WHEEL				CHAR(200)	NULL,
      DRIVER_CON			CHAR(200)	NULL,
      EXTERIOR_FEATURE		CHAR(200)	NULL,
      ENTERTAINMENT			CHAR(200)	NULL,
      interior_features 	CHAR(200)	NULL,
      technical 			CHAR(200)	NULL,
      security 				CHAR(200)	NULL, 
      safety				CHAR(200)	NULL,
      mod_desc				CHAR(200)	NULL,
      body_type  CHAR(200)	NULL,
      co2 CHAR(200)	NULL,
      annual_road_tax CHAR(200)	NULL,
      rrp CHAR(200)	NULL,
      vrt_band CHAR(200)	NULL ,
      engine_cc CHAR(200) NULL


      


      )
      ;''')
print ('Table created successfully')




conn.commit()
conn.close()
