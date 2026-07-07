import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QTextEdit, 
    QPushButton, QMessageBox, QInputDialog )
from PyQt6.QtCore import Qt



# connector 

import mysql.connector as m


class database :
    
    def connection(self):
        
        try:
            
            con = m.connect (
                  host="localhost",
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
       con.commit()
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


       
       
       
       
       

#---------DATABASE______MODIFICATIONS---------
  

  #------DATA---CREATION-------
class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CREATE Notepad")
        self.resize(500, 400)
        

# 1. elements
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter Note Title Here...")
        
        self.content_input = QTextEdit()
        self.content_input.setPlaceholderText("Write your note here...")
        
        self.save_button = QPushButton("Save to Database")
        self.save_button.clicked.connect(self.save_data)
        

# 2. Arrangement of (1. elements)
        layout = QVBoxLayout()
        layout.addWidget(self.title_input)
        layout.addWidget(self.content_input)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

   def save_data(self):
       note_title = self.title_input.text()
       note_content = self.content_input.toPlainText()

       #wont save if title is empty
       if not note_title.strip():          
           QMessageBox.warning(self, "Error", "Please enter a title first!")
           return

#3. DATA INSERTION
        query = "INSERT INTO notes VALUES ('{}','{}')".format(note_title, note_content)
        cursor.execute(query)
        con.commit()
        con.close()

#clearing input box and success msg
        self.title_input.clear()
        self.content_input.clear()
        QMessageBox.information(self, "Success", "Note saved successfully!")




#-----------STARTING_____APPLICATION---------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = SimpleNotepad()
    notepad.show()
    sys.exit(app.exec())
         
            
            
           






    

