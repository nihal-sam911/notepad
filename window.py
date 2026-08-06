import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, 
                             QVBoxLayout, QFrame, QLabel, QPushButton, QLineEdit, 
                             QTextEdit, QToolButton, QMenu, QScrollArea, QSizePolicy)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QAction, QFont,QIcon

from database import Database
from style import THEMES


class NoteListItem(QWidget):
    def __init__(self, note_id, title, main_window):
        super().__init__()
        self.note_id = note_id
        self.main_window = main_window
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        
        self.title_btn = QPushButton(f"› {title}")
        self.title_btn.setFont(QFont("Segoe UI", 11))
        self.title_btn.setStyleSheet("border: none; text-align: left; background: transparent;")
        self.title_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.title_btn.clicked.connect(self.load_note)
        
        self.menu_btn = QToolButton()
        self.menu_btn.setText("")
        self.menu_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        
        menu = QMenu(self)
        edit_action = QAction("Edit", self)
        edit_action.triggered.connect(self.edit_note)
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(self.delete_note)
        
        menu.addAction(edit_action)
        menu.addAction(delete_action)
        self.menu_btn.setMenu(menu)
        
        layout.addWidget(self.title_btn)
        layout.addWidget(self.menu_btn)

    def load_note(self):
        self.main_window.open_note(self.note_id)

    def edit_note(self):
        self.main_window.open_note(self.note_id)
        self.main_window.set_edit_mode(True)

    def delete_note(self):
        self.main_window.db.delete_note(self.note_id)
        self.main_window.load_sidebar_notes()
        if self.main_window.current_note_id == self.note_id:
            self.main_window.clear_editor()


class GraphiteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GRAPHITE")
        self.resize(950, 650)
        self.setWindowIcon(QIcon("logo.png"))  
        self.db = Database()
        self.db.create_table()
        
        self.current_note_id = None
        self.is_editing = False
        self.saved_timestamp = ""
        
        self.setup_ui()
        self.apply_theme("Sepia")
        self.load_sidebar_notes()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ================= SIDEBAR =================
        self.sidebar = QFrame()
        self.sidebar.setObjectName("Sidebar")
        self.sidebar.setMinimumWidth(0)
        self.sidebar.setMaximumWidth(280)
        
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(15, 15, 15, 15)
        sidebar_layout.setSpacing(12)

        # Top Bar: Big "NOTES" title on left, 3-dots Settings menu on right
        top_sidebar_layout = QHBoxLayout()
        notes_title = QLabel("NOTES")
        notes_title.setObjectName("SidebarTitle")
        notes_title.setFont(QFont("Segoe UI", 34, QFont.Weight.Bold))
        
        self.theme_btn = QToolButton()
        self.theme_btn.setText("")
        self.theme_btn.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        
        theme_menu = QMenu(self)
        for theme_name in THEMES.keys():
            action = QAction(theme_name, self)
            action.triggered.connect(lambda checked, t=theme_name: self.apply_theme(t))
            theme_menu.addAction(action)
        self.theme_btn.setMenu(theme_menu)

        top_sidebar_layout.addWidget(notes_title)
        top_sidebar_layout.addStretch()
        top_sidebar_layout.addWidget(self.theme_btn)
        sidebar_layout.addLayout(top_sidebar_layout)

        # Large Bold "+ NEW NOTE" Button
        self.new_note_btn = QPushButton("+ NEW NOTE")
        self.new_note_btn.setObjectName("NewNoteBtn")
        self.new_note_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.new_note_btn.setFixedHeight(42)
        self.new_note_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.new_note_btn.clicked.connect(self.prepare_new_note)
        sidebar_layout.addWidget(self.new_note_btn)

        # Scroll Area for Notes List
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_widget = QWidget()
        self.notes_layout = QVBoxLayout(self.scroll_widget)
        self.notes_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)
        sidebar_layout.addWidget(self.scroll_area)

        # ================= MAIN CONTENT AREA =================
        self.content_area = QWidget()
        content_layout = QHBoxLayout(self.content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Sidebar Toggle handle bar (Stays visible on left edge when sidebar collapses)
        self.toggle_btn = QPushButton("")
        self.toggle_btn.setObjectName("SidebarToggle")
        self.toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.toggle_btn.setFixedWidth(14)
        self.toggle_btn.setToolTip("Toggle Sidebar")
        self.toggle_btn.clicked.connect(self.toggle_sidebar)
        
        # Editor Area
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        editor_layout.setContentsMargins(25, 20, 25, 20)

        # Title & Action Buttons
        title_layout = QHBoxLayout()
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")
        self.title_input.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        self.title_input.textChanged.connect(self.trigger_edit_mode)
        
        self.btn_cancel = QPushButton("✖")
        self.btn_save = QPushButton("✔")
        self.btn_save.setFixedSize(32, 32)
        self.btn_cancel.setFixedSize(32, 32)
        self.btn_save.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.btn_cancel.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.btn_save.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_cancel.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_save.clicked.connect(self.save_note)
        self.btn_cancel.clicked.connect(self.cancel_edit)
        
        self.btn_save.hide()
        self.btn_cancel.hide()

        title_layout.addWidget(self.title_input)
        title_layout.addWidget(self.btn_cancel)
        title_layout.addWidget(self.btn_save)

        # Meta Data Label
        self.meta_label = QLabel("")
        self.meta_label.setObjectName("MetaData")

        # Text Area
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("start Typing...")
        self.text_area.setFont(QFont("Segoe UI", 12))
        self.text_area.textChanged.connect(self.update_char_count_only)
        self.text_area.textChanged.connect(self.trigger_edit_mode)

        editor_layout.addLayout(title_layout)
        editor_layout.addWidget(self.meta_label)
        editor_layout.addWidget(self.text_area)

        content_layout.addWidget(self.toggle_btn)
        content_layout.addWidget(editor_widget)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.content_area)

    def apply_theme(self, theme_name):
        self.setStyleSheet(THEMES[theme_name])

    def toggle_sidebar(self):
        current_width = self.sidebar.width()
        target_width = 0 if current_width > 50 else 280
        
        self.anim = QPropertyAnimation(self.sidebar, b"maximumWidth")
        self.anim.setDuration(250)
        self.anim.setStartValue(current_width)
        self.anim.setEndValue(target_width)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.anim.start()

    def load_sidebar_notes(self):
        for i in reversed(range(self.notes_layout.count())): 
            widget = self.notes_layout.itemAt(i).widget()
            if widget: 
                widget.deleteLater()
            
        notes = self.db.slidebar_note()
        if not notes: 
            return
        
        for note_id, title in notes:
            item = NoteListItem(note_id, title, self)
            self.notes_layout.addWidget(item)

    def trigger_edit_mode(self):
        if not self.is_editing:
            self.set_edit_mode(True)

    def set_edit_mode(self, state):
        self.is_editing = state
        self.btn_save.setVisible(state)
        self.btn_cancel.setVisible(state)

    def update_char_count_only(self):
        char_count = len(self.text_area.toPlainText())
        if self.saved_timestamp:
            self.meta_label.setText(f"{self.saved_timestamp} | {char_count} characters")

    def prepare_new_note(self):
        self.current_note_id = None
        self.title_input.clear()
        self.text_area.clear()
        self.saved_timestamp = datetime.now().strftime("%d %B %I:%M %p")
        self.set_edit_mode(True)
        self.update_char_count_only()
        self.title_input.setFocus()

    def open_note(self, note_id):
        note = self.db.view_note(note_id)
        if note:
            self.title_input.blockSignals(True)
            self.text_area.blockSignals(True)
            
            self.current_note_id = note_id
            self.title_input.setText(note[0])
            self.text_area.setPlainText(note[1])
            
            # Use stored database timestamp from MySQL tuple (index 2: updated_at)
            if len(note) >= 3 and note[2]:
                if isinstance(note[2], datetime):
                    self.saved_timestamp = note[2].strftime("%d %B %I:%M %p")
                else:
                    self.saved_timestamp = str(note[2])
            else:
                self.saved_timestamp = datetime.now().strftime("%d %B %I:%M %p")
                
            self.update_char_count_only()
            self.set_edit_mode(False)
            
            self.title_input.blockSignals(False)
            self.text_area.blockSignals(False)

    def save_note(self):
        title = self.title_input.text().strip() or "Untitled"
        content = self.text_area.toPlainText()
        
        # Capture current time only when saving changes
        self.saved_timestamp = datetime.now().strftime("%d %B %I:%M %p")
        
        if self.current_note_id is None:
            self.current_note_id = self.db.create_note(title, content)
        else:
            self.db.EDIT_note(self.current_note_id, title, content)
            
        self.set_edit_mode(False)
        self.load_sidebar_notes()
        self.update_char_count_only()

    def cancel_edit(self):
        self.set_edit_mode(False)
        if self.current_note_id:
            self.open_note(self.current_note_id)
        else:
            self.clear_editor()

    def clear_editor(self):
        self.current_note_id = None
        self.title_input.clear()
        self.text_area.clear()
        self.saved_timestamp = ""
        self.meta_label.setText("Start Typing...")
        self.set_edit_mode(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GraphiteWindow()
    window.show()
    sys.exit(app.exec())
