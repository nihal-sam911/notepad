import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QLabel, QLineEdit, QTextEdit, 
    QPushButton, QMessageBox, QInputDialog )
from PyQt6.QtCore import Qt



# connector 

import mysql.connector as m

def connection():

    try:
        con = m.connect (
             host="localhost",
             user="root",
             password="password",
             database="notepad"
             )
       
        if con.is_connected() :
            print("successfully conencted")
            return con

    except m.Error as e:
        print(f"connection failed: {e}")
        return None

             


def create():

    con = connection()
    if con is None:
        return false
    cur = con.cusor()

    query = "CREATE IF NOT EXISTS notepad;"

    cur.execute(query)
    cur.close()
    con.close()



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
         
            
            
           






    

