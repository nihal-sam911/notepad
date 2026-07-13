#--------connector------

import mysql.connector as m


class database :
    
    def connection(self):
        
        try:
            
            con = m.connect (
                host="127.0.0.1",
                user="root",
                password="password",
                database="notepad")

            
            if con.is_connected() : 
                print("successfully conencted")
                return con

        except m.Error as e:
                print(f"connection failed: {e}")
                return None
          

    def create_table(self):
       
       con = self.connection()
       if con is None:
           return False
           
       cur = con.cursor()
       query = """CREATE TABLE IF NOT EXISTS notepad( 
                id int auto_increment primary key,
                Title varchar(300) not null,
                content text,
                UPDATED_AT timestamp default current_timestamp on update current_timestamp);"""   

       cur.execute(query)
       con.commit()
       cur.close()
       con.close()




#---------creation-------
    def create_note(self, title, content):

       con = self.connection()
       if con is None: return None

       cur = con.cursor()
       query = "INSERT INTO notepad (title, content) VALUES (%s, %s)"
       cur.execute(query, (title, content))
       con.commit()
       new_id = cur.lastrowid
       cur.close()
       con.close()
       return new_id

#----------Delete---------
    def delete_note(self, note_id):

       con = self.connection()
       if con is None: return None
       cur = con.cursor()
       query = "DELETE FROM notepad WHERE id = %s"
       cur.execute(query, (note_id,))
       con.commit()
       cur.close()
       con.close()
       return True

#----------EDIT---------
    def EDIT_note(self, note_id,title,content):

       con = self.connection()
       if con is None: return None
       cur = con.cursor()
       query = "UPDATE notepad SET title = %s, content = %s WHERE id = %s"
       cur.execute(query, (title,content,note_id))
       con.commit()
       cur.close()
       con.close()
       return True

#----------VIEW---------
    def view_note(self, note_id):

       con = self.connection()
       if con is None: return None
       cur = con.cursor()
       query = "SELECT title, content FROM notepad WHERE id = %s"
       cur.execute(query, (note_id,))
       note = cur.fetchone()

       cur.close()
       con.close()
       return note

#----------for__slide_bar__list---------
    def slidebar_note(self):

       con = self.connection()
       if con is None: return None
       cur = con.cursor()
       query = "SELECT id, title FROM notepad ORDER BY updated_at DESC"
       cur.execute(query)
       r = cur.fetchall()
       cur.close()
       con.close()
       return r

