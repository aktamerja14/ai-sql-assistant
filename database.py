import sqlite3

def create_database():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            salary REAL,
            experience INTEGER
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM employees")

    if cursor.fetchone()[0] == 0:
        employees = [
            ("Rahul", "IT", 50000, 2),
            ("Priya", "HR", 40000, 3),
            ("Amit", "IT", 65000, 5),
            ("Neha", "Finance", 55000, 4),
            ("Karan", "Sales", 35000, 1),
        ]

        cursor.executemany("""
            INSERT INTO employees
            (name, department, salary, experience)
            VALUES (?, ?, ?, ?)
        """, employees)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
