import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT,
    deleted INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books_archive (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT
)
""")

connection.commit()


def add_book(title: str, author: str):
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    connection.commit()

def get_all_books(show_deleted=False):
    if show_deleted:
        cursor.execute("SELECT * FROM books")
    else:
        cursor.execute("SELECT * FROM books WHERE deleted = 0")
    return cursor.fetchall()

def update_book_title(book_id: int, new_title: str):
    cursor.execute("UPDATE books SET title = ? WHERE id = ?", (new_title, book_id))
    connection.commit()

def soft_delete(book_id: int):
    cursor.execute("UPDATE books SET deleted = 1 WHERE id = ?", (book_id,))
    cursor.execute("SELECT title, author FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("INSERT INTO books_archive (title, author) VALUES (?, ?)", book)
    connection.commit()

def hard_delete(book_id: int):
    cursor.execute("DELETE FROM books WHERE id = ? AND deleted = 1", (book_id,))
    connection.commit()

if __name__ == "__main__":
    add_book("War and Peace", "Leo Tolstoy")
    add_book("Pride and Prejudice", "Jane Austen")
    add_book("1984", "George Orwell")

    print("Все книги после добавления:")
    for book in get_all_books():
        print(book)

    update_book_title(2, "Pride & Prejudice")
    print("\nКниги после изменения названия id=2:")
    for book in get_all_books():
        print(book)

    soft_delete(3)
    print("\nКниги после soft_delete id=3:")
    for book in get_all_books():
        print(book)

    hard_delete(3)
    print("\nКниги после hard_delete id=3:")
    for book in get_all_books(show_deleted=True):
        print(book)