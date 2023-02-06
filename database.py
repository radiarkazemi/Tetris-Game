import sqlite3


def create_database():
    # Connect to database or create it if it doesn't exist
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            username text,
            score integer
        )
    ''')


def new_insert(name, score):
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    username = name

    # Get score
    score = score

    # Insert the new score into the database
    cursor.execute('INSERT INTO scores (username, score) VALUES (?, ?)', (username, score))
    conn.commit()


def check_name(name: str, new_score: int):
    create_database()
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores WHERE username=?", (name,))
    record = cursor.fetchone()
    if record:
        # name exists, check if new score is bigger
        if new_score > record[1]:
            cursor.execute('UPDATE scores SET score = ? WHERE username = ?', (new_score, name))
            conn.commit()
    else:
        new_insert(name, new_score)


def get_scores():
    scores = {}
    conn = sqlite3.connect('game_scores.db')
    cursor = conn.cursor()
    create_database()
    cursor.execute('SELECT * FROM scores ORDER BY score DESC LIMIT 10')
    top_scores = cursor.fetchall()

    # Print the top 10 scores
    for i, score in enumerate(top_scores):
        scores[score[0]] = score[1]

    # Close the database connection
    conn.close()
    return scores


print(get_scores())
