import mysql.connector as m


class Database:
    
    def connection(self):
        try:
            con = m.connect(
                host="localhost",
                user="root",
                password="YourNewPassword123!",
                database="notepad")
            
            if con.is_connected():
                return con
        except m.Error as e:
            print(f"Connection failed: {e}")
            return None

    def create_table(self):
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

    def create_note(self, title, content):
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

    def delete_note(self, note_id):
        con = self.connection()
        if con is None: 
            return None
        cur = con.cursor()
        query = "DELETE FROM notepad WHERE id = %s"
        cur.execute(query, (note_id,))
        con.commit()
        cur.close()
        con.close()
        return True

    def EDIT_note(self, note_id, title, content):
        con = self.connection()
        if con is None: 
            return None
        cur = con.cursor()
        query = "UPDATE notepad SET title = %s, content = %s WHERE id = %s"
        cur.execute(query, (title, content, note_id))
        con.commit()
        cur.close()
        con.close()
        return True

    def view_note(self, note_id):
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

    def slidebar_note(self):
        con = self.connection()
        if con is None: 
            return None
        cur = con.cursor()
        query = "SELECT id, title FROM notepad ORDER BY updated_at DESC"
        cur.execute(query)
        r = cur.fetchall()
        cur.close()
        con.close()
        return r

