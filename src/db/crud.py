from db import cur, con
from db.exceptions import (
    UserWithThisEmailAlreadyPresented,
    NotesNotPresented,
    PasswordNotMatched,
    UserNotPresented
)


def get_user_by_email(email: str) -> tuple | None:
    cur.execute(f"SELECT id, name, email, pwd  FROM users WHERE email = '{email}'")
    user = cur.fetchone()
    return user


def get_user_with_auth(email: str, password: str) -> tuple | None:
    user = get_user_by_email(email)

    if user is None:
        raise UserNotPresented

    if user[3] != password:
        raise PasswordNotMatched

    return user


def get_notes_by_user_email(email: str) -> list | None:
    user = get_user_by_email(email)

    if user is None:
        raise UserNotPresented

    cur.execute(f'SELECT id, header, content FROM notes WHERE user_id = {user[0]}')
    notes = cur.fetchall()

    if notes is None:
        raise NotesNotPresented

    return notes


def add_new_notes(header: str, content: str):
    cur.execute(f'INSERT INTO notes VALUES ({header}, {content})')
    con.commit()


def add_new_user(email: str, username: str, password: str):
    user = get_user_by_email(email)

    if user is not None:
        raise UserWithThisEmailAlreadyPresented

    cur.execute(f"""INSERT INTO users VALUES ('{username}', '{email}', '{password}')""")
    con.commit()
