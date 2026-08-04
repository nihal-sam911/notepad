
QSS = """
QMainWindow {
    background-color: #1E1E2E;
}

QWidget#sidebar {
    background-color: #181825;
    border-right: 1px solid #313244;
}

QListWidget {
    background-color: #313244;
    color: #CDD6F4;
    border: none;
    border-radius: 6px;
    padding: 5px;
    font-size: 14px;
}

QListWidget::item {
    padding: 8px;
    border-radius: 4px;
}

QListWidget::item:selected {
    background-color: #89B4FA;
    color: #11111B;
    font-weight: bold;
}

QLineEdit {
    background-color: #313244;
    color: #CDD6F4;
    border: none;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 15px;
    font-weight: bold;
}

QTextEdit {
    background-color: #313244;
    color: #CDD6F4;
    border: none;
    border-radius: 6px;
    padding: 10px;
    font-size: 14px;
}

QPushButton#btn_new, QPushButton#btn_save {
    background-color: #89B4FA;
    color: #11111B;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 13px;
}

QPushButton#btn_new:hover, QPushButton#btn_save:hover {
    background-color: #B4BEFE;
}

QPushButton#btn_delete {
    background-color: #F38BA8;
    color: #11111B;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 13px;
}

QPushButton#btn_delete:hover {
    background-color: #EBA0AC;
}
"""
