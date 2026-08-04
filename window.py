# window.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QLineEdit, QTextEdit, QPushButton, QMessageBox, QListWidgetItem)

from PyQt6.QtCore import Qt
from database import Database
import style


class NotepadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CBSE Class 12 Notepad (PyQt6)")
        self.resize(900, 600)

        # Database Connection
        self.db = Database()
        self.db.create_table()

      
        self.current_note_id = None
        self.notes_data = []

        self.init_ui()
        self.setStyleSheet(style.QSS)
        self.load_sidebar_notes()

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Main Layout
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # ----------------- LEFT SIDEBAR -----------------
        sidebar_widget = QWidget()
        sidebar_widget.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout(sidebar_widget)

        # New Note Button
        self.btn_new = QPushButton("+ New Note")
        self.btn_new.setObjectName("btn_new")
        self.btn_new.clicked.connect(self.clear_editor)
        sidebar_layout.addWidget(self.btn_new)

        # Sidebar Notes List
        self.note_list = QListWidget()
        self.note_list.itemClicked.connect(self.on_note_select)
        sidebar_layout.addWidget(self.note_list)

        main_layout.addWidget(sidebar_widget, stretch=1)

        # ----------------- RIGHT EDITOR -----------------
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)

        # Top Bar
        top_bar = QHBoxLayout()

        self.title_entry = QLineEdit()
        self.title_entry.setPlaceholderText("Enter Note Title...")
        top_bar.addWidget(self.title_entry, stretch=1)

        self.btn_save = QPushButton("Save")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.clicked.connect(self.save_note)
        top_bar.addWidget(self.btn_save)

        self.btn_delete = QPushButton("Delete")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.delete_note)
        top_bar.addWidget(self.btn_delete)

        editor_layout.addLayout(top_bar)

        # Note Content Area
        self.content_text = QTextEdit()
        self.content_text.setPlaceholderText("Write your note content here...")
        editor_layout.addWidget(self.content_text)

        main_layout.addWidget(editor_widget, stretch=3)

    # ----------------- APP LOGIC & DATABASE ---------------------------

    def load_sidebar_notes(self):
        """Fetches notes from DB and populates the sidebar QListWidget."""
        self.note_list.clear()
        self.notes_data = self.db.slidebar_note() or []  

        for note_id, title in self.notes_data:
            item = QListWidgetItem(title)
            item.setData(Qt.ItemDataRole.UserRole, note_id)
            self.note_list.addItem(item)

    def clear_editor(self):
        """Clears text fields to create a brand new note."""
        self.current_note_id = None
        self.title_entry.clear()
        self.content_text.clear()
        self.note_list.clearSelection()

    def save_note(self):
        """Handles creating a new note or updating an existing one."""
        title = self.title_entry.text().strip()
        content = self.content_text.toPlainText().strip()

        if not title and not content:
            QMessageBox.warning(self, "Warning", "Cannot save an empty note!")
            return

        if not title:
            title = "Untitled Note"

        if self.current_note_id is not None:
          
            success = self.db.EDIT_note(self.current_note_id, title, content)[cite: 1]
            if success:
                QMessageBox.information(self, "Success", "Note updated successfully!")
        else:
            
            new_id = self.db.create_note(title, content)[cite: 1]
            if new_id:
                self.current_note_id = new_id
                QMessageBox.information(self, "Success", "Note saved successfully!")

        self.load_sidebar_notes()

    def on_note_select(self, item):
        """Loads selected note content into the editor."""
        note_id = item.data(Qt.ItemDataRole.UserRole)
        self.current_note_id = note_id

        note = self.db.view_note(note_id)[cite: 1]
        if note:
            self.title_entry.setText(note[0])  # Set title[cite: 1]
            self.content_text.setPlainText(note[1] if note[1] else "")  # Set content[cite: 1]

    def delete_note(self):
        """Deletes selected note from database."""
        if self.current_note_id is None:
            QMessageBox.warning(self, "Warning", "Please select a note to delete.")
            return

        confirm = QMessageBox.question(
            self, 
            "Confirm Delete", 
            "Are you sure you want to delete this note?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            success = self.db.delete_note(self.current_note_id)[cite: 1]
            if success:
                QMessageBox.information(self, "Success", "Note deleted.")
                self.clear_editor()
                self.load_sidebar_notes()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadWindow()
    window.show()
    sys.exit(app.exec())
    
