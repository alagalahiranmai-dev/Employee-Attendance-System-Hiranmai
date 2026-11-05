
from werkzeug.security import generate_password_hash
from database import get_connection
import getpass

username = input("Enter manager username: ")
password = getpass.getpass("Enter new manager password: ")

password_hash = generate_password_hash(password)

connection = get_connection()
cursor = connection.cursor()

try:
    cursor.execute(
        """
        UPDATE employees
        SET username = %s,
            password_hash = %s,
            role = 'manager'
        WHERE employee_code = 'MGR001'
        """,
        (username, password_hash)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Manager login updated successfully!")
        print("Username:", username)
    else:
        print("Manager MGR001 was not found.")

except Exception as e:
    connection.rollback()
    print("Error:", e)

finally:
    cursor.close()
    connection.close()
