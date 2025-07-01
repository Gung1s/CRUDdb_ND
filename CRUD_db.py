import mysql.connector

DB_CONFIG = {
    'host': 'localhost',  # 127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3312,
    'user': 'root',
    'password': "****",
    'database': 'library'
}

def get_conn():
    return mysql.connector.connect(**DB_CONFIG)

headers = ["id", "name", "surname"]

def print_info():
    print("1. Parodyti autorių sąrašą")
    print("2. Įtraukti naują autorių")
    print("3. Redaguoti autorių")
    print("4. Ištrinti autorių")
    print("5. Išeiti iš programos")

def print_data(authors):
    print()
    print("Autoriai:")
    for a in authors:
        print(f"{a["id"]}. Vardas: {a["name"]}, Pavardė: {a["surname"]}")

def load_data():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM library")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    authors = []
    for row in rows:
        author = {}
        for i in range(len(headers)):
            author[headers[i]] = str(row[i])
        authors.append(author)
    return authors

def create_data(authors):
    print("Įtraukti naują autorių")
    print("Vardas")
    name = input()
    print("Pavardė")
    surname = input()

    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO authors (id, name, surname) VALUES (%s, %s, %s)",
                   (id, name, surname))
    conn.commit()

    cursor.close()
    conn.close()

def edit_data(authors):
    print(f"Redaguoti esamus autorius.",
          f"Įveskite id, kurį autorių norite redaguoti")
    id = input()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = %s", (id,))
    row = cursor.fetchone()

    if row:
        print(f"{row[0]}. Vardas: {row[1]}, Pavardė: {row[2]}")
        print("Įveskite vardą:")
        name = input()
        print("Įveskite pavardę:")
        surname = input()
        cursor.execute("UPDATE authors SET name = %s, surname = %s WHERE id = %s",
                       (name, surname, id))
        conn.commit()
    cursor.close()
    conn.close()

def delete_data(authors):
    print(f"Autoriaus pašalinimas iš sąrašo.",
          f"Pasirinkite ID kurį, norite pašalinti")
    id = input()

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM authors WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Atlikome šalinimo veiksmą")






