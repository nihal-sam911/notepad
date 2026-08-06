# style.py


BASE_STYLE = """
    QWidget#CentralWidget {{
        background-color: {bg_main};
        color: {fg_main};
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
  
    QLineEdit {{
        border: 1px solid transparent;
        border-radius: 4px;
        font-size: 24px;
        font-weight: bold;
        background: transparent;
        padding: 5px;
        color: {fg_title};
    }}
    QLineEdit:focus {{
        border-bottom: 2px solid {accent};
    }}
    
    QTextEdit {{
        border: none;
        font-size: 16px;
        background: transparent;
        padding: 5px;
        color: {fg_main};
    }}
    
    /* Sidebar */
    QFrame#Sidebar {{
        background-color: {bg_sidebar};
        border-right: 1px solid {border_color};
    }}
    QLabel#SidebarTitle {{
        font-size: 28px;
        font-weight: 300;
        letter-spacing: 2px;
        color: {fg_title};
    }}
    
    /* Buttons */
    QPushButton {{
        border: 1px solid {border_color};
        border-radius: 5px;
        padding: 6px 12px;
        background-color: {bg_btn};
        color: {fg_main};
    }}
    QPushButton:hover {{
        background-color: {bg_btn_hover};
    }}
    QPushButton:pressed {{
        background-color: {bg_btn_active};
    }}
    
    QPushButton#SidebarToggle {{
        border: none;
        font-size: 18px;
        color: {fg_muted};
        background: transparent;
    }}
    QPushButton#SidebarToggle:hover {{
        color: {fg_title};
    }}
    
    QPushButton#NewNoteBtn {{
        border: 1px solid {border_color};
        padding: 8px;
        font-size: 14px;
        margin: 10px;
        background-color: {bg_btn};
    }}
    QPushButton#NewNoteBtn:hover {{
        background-color: {bg_btn_hover};
    }}
    
    QToolButton {{
        border: none;
        font-weight: bold;
        font-size: 16px;
        color: {fg_main};
        padding: 4px;
    }}
    QToolButton:hover {{
        background-color: {bg_btn_hover};
        border-radius: 4px;
    }}
    
    /* Labels */
    QLabel#MetaData {{
        color: {fg_muted};
        font-size: 12px;
    }}
"""

PALETTES = {
    "Light": {
        "bg_main": "#ffffff",
        "bg_sidebar": "#f5f5f5",
        "bg_btn": "#f9f9f9",
        "bg_btn_hover": "#eeeeee",
        "bg_btn_active": "#e0e0e0",
        "fg_main": "#333333",
        "fg_title": "#111111",
        "fg_muted": "#888888",
        "border_color": "#dddddd",
        "accent": "#0066cc",
    },
    "Dark": {
        "bg_main": "#1e1e1e",
        "bg_sidebar": "#252526",
        "bg_btn": "#2d2d2d",
        "bg_btn_hover": "#3d3d3d",
        "bg_btn_active": "#4d4d4d",
        "fg_main": "#cccccc",
        "fg_title": "#ffffff",
        "fg_muted": "#666666",
        "border_color": "#333333",
        "accent": "#007acc",
    },
    "Sepia": {
        "bg_main": "#f4ecd8",
        "bg_sidebar": "#ebe3d0",
        "bg_btn": "#ebe3d0",
        "bg_btn_hover": "#e0d7c3",
        "bg_btn_active": "#d5cca8",
        "fg_main": "#433422",
        "fg_title": "#2b2013",
        "fg_muted": "#8c7b65",
        "border_color": "#dcd3c1",
        "accent": "#a26a42",
    },
    "Midnight Blue": {
        "bg_main": "#0f172a",
        "bg_sidebar": "#1e293b",
        "bg_btn": "#1e293b",
        "bg_btn_hover": "#334155",
        "bg_btn_active": "#475569",
        "fg_main": "#cbd5e1",
        "fg_title": "#f8fafc",
        "fg_muted": "#64748b",
        "border_color": "#334155",
        "accent": "#38bdf8",
    },
    "Hacker": {
        "bg_main": "#000000",
        "bg_sidebar": "#000a00",
        "bg_btn": "#001100",
        "bg_btn_hover": "#003300",
        "bg_btn_active": "#005500",
        "fg_main": "#00ff00",
        "fg_title": "#00ff00",
        "fg_muted": "#008800",
        "border_color": "#005500",
        "accent": "#00ff00",
    },
}


THEMES = {name: BASE_STYLE.format(**colors) for name, colors in PALETTES.items()}
