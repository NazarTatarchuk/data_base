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

print("\nІмена та прізвища футболістів в алфавітному порядку за ім'ям")
execute_query("""
    SELECT first_name, last_name
    FROM football_players
    ORDER BY first_name ASC
""")

print("\nІмена та прізвища футболістів в алфавітному порядку за прізвищем")
execute_query("""
    SELECT first_name, last_name
    FROM football_players
    ORDER BY last_name ASC
""")

print("\nФутболісти з більш ніж 10 голами")
execute_query("""
    SELECT first_name, last_name, goals
    FROM football_players
    WHERE goals > 10
    ORDER BY goals DESC
""")

print("\nФутболісти з більш ніж 10 асистами")
execute_query("""
    SELECT first_name, last_name, assists
    FROM football_players
    WHERE assists > 10
    ORDER BY assists DESC
""")

print("\nФутболісти з більш ніж 5 трофеями")
execute_query("""
    SELECT first_name, last_name, trophies
    FROM football_players
    WHERE trophies > 5
    ORDER BY trophies DESC
""")

print("\nФутболісти, які грають у клубі своєї країни")
execute_query("""
    SELECT first_name, last_name, club, club_nat, nationality
    FROM football_players
    WHERE club_nat = nationality
""")

print("\nКількість голів та асистів по клубах")
execute_query("""
    SELECT club, SUM(goals) AS total_goals, SUM(assists) AS total_assists
    FROM football_players
    GROUP BY club
    ORDER BY total_goals DESC
""")

print("\nФутболісти, народжені після 1990 року")
execute_query("""
    SELECT first_name, last_name, date_of_birth
    FROM football_players
    WHERE date_of_birth > '1990-01-01'
    ORDER BY date_of_birth ASC
""")

print("\nТоп 10 футболістів за сумою голів і асистів")
execute_query("""
    SELECT first_name, last_name, goals, assists, (goals + assists) AS contribution
    FROM football_players
    ORDER BY contribution DESC
    LIMIT 10
""")

print("\nФутболісти без жодного трофею")
execute_query("""
    SELECT first_name, last_name
    FROM football_players
    WHERE trophies = 0
""")

print("\nФутболісти на позиції нападника")
execute_query("""
    SELECT first_name, last_name, goals
    FROM football_players
    WHERE position = 'нападник'
    ORDER BY goals DESC
""")

print("\nФутболісти, які мають від 5 до 15 асистів")
execute_query("""
    SELECT first_name, last_name, assists
    FROM football_players
    WHERE assists BETWEEN 5 AND 15
    ORDER BY assists DESC
""")

print("\nФутболісти з найбільшою кількістю трофеїв")
execute_query("""
    SELECT first_name, last_name, trophies
    FROM football_players
    ORDER BY trophies DESC
    LIMIT 5
""")

print("\nФутболісти молодші 25 років")
execute_query("""
    SELECT first_name, last_name, date_of_birth
    FROM football_players
    WHERE date_of_birth > date('now', '-25 years')
    ORDER BY date_of_birth DESC
""")

print("\nКількість футболістів за національністю")
execute_query("""
    SELECT nationality, COUNT(*) AS players_count
    FROM football_players
    GROUP BY nationality
    ORDER BY players_count DESC
""")

print("\nКлуби з найбільшою кількістю гравців")
execute_query("""
    SELECT club, COUNT(*) AS players_count
    FROM football_players
    GROUP BY club
    ORDER BY players_count DESC
""")

print("\nФутболісти з мінімум 20 голами")
execute_query("""
    SELECT first_name, last_name, goals
    FROM football_players
    WHERE goals >= 20
    ORDER BY goals DESC
""")

print("\nФутболісти, народжені у 1995 році")
execute_query("""
    SELECT first_name, last_name, date_of_birth
    FROM football_players
    WHERE strftime('%Y', date_of_birth) = '1995'
""")

print("\nСередня кількість голів за національністю")
execute_query("""
    SELECT nationality, AVG(goals) AS avg_goals
    FROM football_players
    GROUP BY nationality
    ORDER BY avg_goals DESC
""")

print("\nФутболісти, які грають у клубі 'Barcelona'")
execute_query("""
    SELECT first_name, last_name, goals, assists
    FROM football_players
    WHERE club = 'Barcelona'
    ORDER BY goals DESC
""")
