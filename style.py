THEMES = {
    "Light": """
        QWidget { background-color: #ffffff; color: #333333; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #111111; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #222222; }
        QLabel#MetaData { color: #888888; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #dddddd; border-radius: 5px; padding: 5px; background-color: #ffffff; }
        QPushButton:hover { background-color: #f0f0f0; }
        QPushButton#SidebarToggle { 
            border: 1px solid #cccccc; 
            background-color: #e8e8e8; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #007acc; }
        QFrame#Sidebar { background-color: #f8f9fa; border-right: 1px solid #e0e0e0; }
        QLabel#SidebarTitle { color: #111111; font-weight: bold; background-color: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #222222; background-color: #ffffff; color: #111111; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #111111; color: #ffffff; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; background: transparent; }
        QToolButton:hover { background-color: #e0e0e0; border-radius: 4px; }
    """,
    "Dark": """
        QWidget { background-color: #1e1e1e; color: #cccccc; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #ffffff; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #cccccc; }
        QLabel#MetaData { color: #888888; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #444444; border-radius: 5px; padding: 5px; background-color: #2d2d2d; color: #cccccc; }
        QPushButton:hover { background-color: #3d3d3d; }
        QPushButton#SidebarToggle { 
            border: 1px solid #444444; 
            background-color: #333333; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #007acc; }
        QFrame#Sidebar { background-color: #252526; border-right: 1px solid #333333; }
        QLabel#SidebarTitle { color: #ffffff; font-weight: bold; background-color: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #cccccc; background-color: #2d2d2d; color: #ffffff; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #ffffff; color: #111111; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #cccccc; background: transparent; }
        QToolButton:hover { background-color: #3e3e42; border-radius: 4px; }
    """,
    "Sepia": """
        QWidget { background-color: #f4ecd8; color: #433422; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #433422; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #433422; }
        QLabel#MetaData { color: #8c7b65; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #dcd3c1; border-radius: 5px; padding: 5px; background-color: #ebe3d0; color: #433422; }
        QPushButton:hover { background-color: #e0d7c3; }
        QPushButton#SidebarToggle { 
            border: 1px solid #dcd3c1; 
            background-color: #dcd3c1; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #8c7b65; }
        QFrame#Sidebar { background-color: #ebe3d0; border-right: 1px solid #dcd3c1; }
        QLabel#SidebarTitle { color: #433422; font-weight: bold; background: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #433422; background-color: #ebe3d0; color: #433422; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #433422; color: #f4ecd8; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #433422; background: transparent; }
    """,
    "Midnight Blue": """
        QWidget { background-color: #0f172a; color: #cbd5e1; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #f8fafc; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #cbd5e1; }
        QLabel#MetaData { color: #64748b; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #334155; border-radius: 5px; padding: 5px; background-color: #1e293b; color: #cbd5e1; }
        QPushButton:hover { background-color: #334155; }
        QPushButton#SidebarToggle { 
            border: 1px solid #334155; 
            background-color: #334155; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #38bdf8; }
        QFrame#Sidebar { background-color: #1e293b; border-right: 1px solid #334155; }
        QLabel#SidebarTitle { color: #f8fafc; font-weight: bold; background-color: transparent;}
        QPushButton#NewNoteBtn { border: 2px solid #cbd5e1; background-color: #1e293b; color: #f8fafc; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #cbd5e1; color: #0f172a; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #cbd5e1; background: transparent; }
    """,
    "Hacker": """
        QWidget { background-color: #000000; color: #00ff00; font-family: 'Courier New', monospace; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #00ff00; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #00ff00; }
        QLabel#MetaData { color: #008800; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #005500; border-radius: 0px; padding: 5px; background-color: #001100; color: #00ff00; }
        QPushButton:hover { background-color: #003300; }
        QPushButton#SidebarToggle { 
            border: 1px solid #005500; 
            background-color: #002200; 
            width: 14px; 
            border-top-right-radius: 0px; 
            border-bottom-right-radius: 0px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #00ff00; }
        QFrame#Sidebar { background-color: #000a00; border-right: 1px solid #005500; }
        QLabel#SidebarTitle { color: #00ff00; font-weight: bold; background-color: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #00ff00; background-color: #000000; color: #00ff00; border-radius: 0px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #00ff00; color: #000000; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #00ff00; background: transparent; }
    """,
    "Rosé Pine": """
        QWidget { background-color: #191724; color: #e0def4; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #eb6f92; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #e0def4; }
        QLabel#MetaData { color: #908caa; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #26233a; border-radius: 5px; padding: 5px; background-color: #26233a; color: #e0def4; }
        QPushButton:hover { background-color: #31748f; }
        QPushButton#SidebarToggle { 
            border: 1px solid #26233a; 
            background-color: #26233a; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #ebbcba; }
        QFrame#Sidebar { background-color: #1f1d2e; border-right: 1px solid #26233a; }
        QLabel#SidebarTitle { color: #eb6f92; font-weight: bold; background-color: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #ebbcba; background-color: #1f1d2e; color: #ebbcba; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #ebbcba; color: #191724; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #e0def4; background: transparent; }
        QToolButton:hover { background-color: #26233a; border-radius: 4px; }
    """,
    "Gruvbox": """
        QWidget { background-color: #282828; color: #ebdbb2; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #fabd2f; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #ebdbb2; }
        QLabel#MetaData { color: #928374; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #3c3836; border-radius: 5px; padding: 5px; background-color: #3c3836; color: #ebdbb2; }
        QPushButton:hover { background-color: #504945; }
        QPushButton#SidebarToggle { 
            border: 1px solid #3c3836; 
            background-color: #3c3836; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #fe8019; }
        QFrame#Sidebar { background-color: #1d2021; border-right: 1px solid #3c3836; }
        QLabel#SidebarTitle { color: #fabd2f; font-weight: bold; background-color: transparent;}
        QPushButton#NewNoteBtn { border: 2px solid #fabd2f; background-color: #1d2021; color: #fabd2f; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #fabd2f; color: #282828; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #ebdbb2; background: transparent; }
        QToolButton:hover { background-color: #3c3836; border-radius: 4px; }
    """,
    "Evergreen": """
        QWidget { background-color: #0d1b1e; color: #d0e1d4; font-family: 'Segoe UI', Arial, sans-serif; }
        QLineEdit { border: none; background: transparent; padding: 2px; color: #80ed99; }
        QTextEdit { border: none; font-size: 15px; background: transparent; padding: 5px; color: #d0e1d4; }
        QLabel#MetaData { color: #52796f; font-size: 13px; font-weight: 500; }
        QPushButton { border: 1px solid #284b50; border-radius: 5px; padding: 5px; background-color: #1d3539; color: #d0e1d4; }
        QPushButton:hover { background-color: #284b50; }
        QPushButton#SidebarToggle { 
            border: 1px solid #284b50; 
            background-color: #1d3539; 
            width: 14px; 
            border-top-right-radius: 6px; 
            border-bottom-right-radius: 6px; 
        }
        QPushButton#SidebarToggle:hover { background-color: #57cc99; }
        QFrame#Sidebar { background-color: #15282b; border-right: 1px solid #284b50; }
        QLabel#SidebarTitle { color: #80ed99; font-weight: bold; background-color: transparent; }
        QPushButton#NewNoteBtn { border: 2px solid #80ed99; background-color: #15282b; color: #80ed99; border-radius: 6px; font-weight: bold; }
        QPushButton#NewNoteBtn:hover { background-color: #80ed99; color: #0d1b1e; }
        QToolButton { border: none; font-weight: bold; font-size: 20px; color: #d0e1d4; background: transparent; }
        QToolButton:hover { background-color: #1d3539; border-radius: 4px; }
    """
}
