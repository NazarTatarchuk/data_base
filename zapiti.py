import sqlite3

conn =sqlite3.connect("football_players.db")
cursor = conn.cursor()

def execute_query(query, prams=()):
    try:
        cursor.execute(query, prams)
        rows = cursor.fetchall()
        for row  in rows:
            print(row)
    except Exception as e:
        print(f"Помилка при виконанні запиту: {e}")

print("\n Імена та прізвища футболістів в алфавітному порядку")

execute_query("""
    SELECT first_name, last_name
    FROM football_players
    ORDER BY first_name ASC
              """)

print("\n Імена та прізвища футболістів по кількості результативних дій")

execute_query("""
    SELECT first_name, last_name, goals, assists, (goals + assists) AS sum_ga
    FROM football_players
    ORDER BY sum_ga ASC
              """)

print("\n Імена та прізвища футболістів за національністю")

execute_query("""
    SELECT first_name, last_name, nationality
    FROM football_players
    ORDER BY nationality ASC
              """)

print("\n Імена та прізвища футболістів за трофеями")

execute_query("""
    SELECT first_name, last_name, trophies
    FROM football_players
    ORDER BY trophies ASC
              """)

print("\n Імена та прізвища футболістів в алфавітному порядку за їх клубом")

execute_query("""
    SELECT first_name, last_name, club,Nat
    FROM football_players
    ORDER BY club ASC
              """)

print("\n Імена та прізвища футболістів за національністю їх клубів")

execute_query("""
    SELECT first_name, last_name, club, club_nat
    FROM football_players
    ORDER BY club_nut ASC
              """)

print("\n Імена та прізвища футболістів за старшенством")

execute_query("""
    SELECT first_name, last_name, date_of_birth
    FROM football_players
    ORDER BY date_of_birth ASC
              """)

print("\n Імена та прізвища футболістів в алфавітному порядку")

execute_query("""
    SELECT first_name, last_name
    FROM football_players
    ORDER BY first_name DESC
              """)

print("\n Імена та прізвища футболістів по кількості результативних дій")

execute_query("""
    SELECT first_name, last_name, goals, assists, (goals + assists) AS sum_ga
    FROM football_players
    ORDER BY sum_ga DESC
              """)

print("\n Імена та прізвища футболістів за національністю")

execute_query("""
    SELECT first_name, last_name, nationality
    FROM football_players
    ORDER BY nationality DESC
              """)

print("\n Імена та прізвища футболістів за трофеями")

execute_query("""
    SELECT first_name, last_name, trophies
    FROM football_players
    ORDER BY trophies DESC
              """)

print("\n Імена та прізвища футболістів в алфавітному порядку за їх клубом")

execute_query("""
    SELECT first_name, last_name, club,Nat
    FROM football_players
    ORDER BY club DESC
              """)

print("\n Імена та прізвища футболістів за національністю їх клубів")

execute_query("""
    SELECT first_name, last_name, club, club_nat
    FROM football_players
    ORDER BY club_nut DESC
              """)

print("\n Імена та прізвища футболістів за старшенством")

execute_query("""
    SELECT first_name, last_name, date_of_birth
    FROM football_players
    ORDER BY date_of_birth DESC
              """)

