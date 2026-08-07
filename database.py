import mysql.connector as m
import os

def get_password():
    try:
        with open("password.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print('NO password.txt FOUND')

    
class Database:
    def connection(self):
        try:
            con = m.connect(
                host="localhost",
                user="root",
                password=get_password(),
                database="notepad"
            )
            if con.is_connected():
                return con
        except m.Error as e:
            print(f"Connection Error: {e}")
            return None

    def create_table(self):
        try:
            temp_con = m.connect(
                host="localhost",
                user="root",
                password=get_password() 
            )
            if temp_con.is_connected():
                temp_cur = temp_con.cursor()
                temp_cur.execute("CREATE DATABASE IF NOT EXISTS notepad")
                temp_con.commit()
                temp_cur.close()
                temp_con.close()
        except m.Error as e:
            print(f"Failed to create database (1): {e}")
            return False

        
        try:
            con = self.connection()
            if con is None: 
                return False
            cur = con.cursor()
            query = """CREATE TABLE IF NOT EXISTS notepad( 
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(300) NOT NULL,
                    content TEXT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"""   
            cur.execute(query)
            con.commit()
            cur.close()
            con.close()
            return True 
        except m.Error as e:
            print(f"Failed to create table (2): {e}")
            return False
        else:
            print("Table created successfully.")
            return True
        

    def create_note(self, title, content):
        try:
            con = self.connection()
            if con is None: 
                return None
            cur = con.cursor()
            query = "INSERT INTO notepad (title, content) VALUES (%s, %s)"
            cur.execute(query, (title, content))
            con.commit()
            new_id = cur.lastrowid
            cur.close()
            con.close()
            return new_id
        except m.Error as e:
            print(f"Error saving note: {e}")
            return None

    def delete_note(self, note_id):
        try:
            con = self.connection()
            if con is None: 
                return False
            cur = con.cursor()
            query = "DELETE FROM notepad WHERE id = %s"
            cur.execute(query, (note_id,))
            con.commit()
            cur.close()
            con.close()
            return True
        except m.Error as e:
            print(f"Error deleting note: {e}")
            return False

    def EDIT_note(self, note_id, title, content):
        try:
            con = self.connection()
            if con is None: 
                return False
            cur = con.cursor()
            query = "UPDATE notepad SET title = %s, content = %s WHERE id = %s"
            cur.execute(query, (title, content, note_id))
            con.commit()
            cur.close()
            con.close()
            return True
        except m.Error as e:
            print(f"Error editing note: {e}")
            return False

    def view_note(self, note_id):
        try:
            con = self.connection()
            if con is None: 
                return None
            cur = con.cursor()
            query = "SELECT title, content, updated_at FROM notepad WHERE id = %s"
            cur.execute(query, (note_id,))
            note = cur.fetchone()
            cur.close()
            con.close()
            return note
        except m.Error as e:
            print(f"Error viewing note: {e}")
            return None

    def slidebar_note(self):
        try:
            con = self.connection()
            if con is None: 
                return []
            cur = con.cursor()
            query = "SELECT id, title FROM notepad ORDER BY updated_at DESC"
            cur.execute(query)
            r = cur.fetchall()
            cur.close()
            con.close()
            return r
        except m.Error as e:
            print(f"Error loading sidebar: {e}")
            return []
