import sqlite3
import json
from datetime import datetime



def parse_data_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str,"%Y-%m-%d").date()
    except ValueError:
        return None

conn =sqlite3.connect("football_players.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foregn_keys =ON")

cursor.execute("""CREATE TABLE IF NOT EXISTS players(
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    date_of_birth DATE,
    club TEXT,
    club_nat TEXT,
    nationality TEXT,
    goals INTEGER,
    assists INTEGER,
    trophies INTEGER);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS players(
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    clubcareer_id TEXT PRIMARY KEY AUROINCREMENT,
   club_name TEXT,
   club_nat TEXT,
    FOREIGN KEY(player_id) REFERECES players(player_id) ON DELETE CASCADE           
    );
    """)

with open("-", 'r', encoding='utf-8') as f:
    students = json.load(f)

for player in players:
    cursor.execute("""
    INSERT INTO students(
    first_name, last_name, date_of_birth, nationality, club, club_nat, goals, assists, trophies)
    )
    VALUES(?, ?, ?, ?, ?, ?, ?)
    """, (
        player['first_name']
        player['last_name']
        parse_data_safe(player['date_of_birth'])
        player['nationality']
        player['club']
        player['club_nat']
        player['goals']
        player['assists']
        player['trophies']
    ))
 player_id = cursor.lastrowid

 cursor.execute("""
                INSERT INTO clubcareer(player_id, clubcareer_date, retirment_date)
                VALUES(?, ?, ?)
                """,(
                    player_id,
                     parse_data_safe(player.get("clubcareer_date"))
                     parse_data_safe(player.get("retirment_date"))
                ))   

conn.commit()
conn.close()
print("data was sucsessfully added")