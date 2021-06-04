# DROP TABLES

songplay_table_drop = "DROP table songplay_table"
user_table_drop = "DROP table user_table"
song_table_drop = "DROP table song_table"
artist_table_drop = "DROP table artist_table"
time_table_drop = "DROP table time_table"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay_table (
songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMP, user_id INT, 
level VARCHAR, song_id VARCHAR, artist_id VARCHAR, session_id INT, location 
VARCHAR, user_agent VARCHAR)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user_table (user_id INT 
PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, gender VARCHAR(1), 
level VARCHAR)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song_table (song_id 
VARCHAR PRIMARY KEY, title VARCHAR, artist_id VARCHAR, year INT, duration 
REAL""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist_table
(artist_id VARCHAR PRIMARY KEY, name VARCHAR, location VARCHAR, latitude REAL, 
longitude REAL
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time_table
(start_time TIMESTAMP, hour INT, day VARCHAR, week INT, month INT, year INT, 
weekday VARCHAR
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]