BASE_STYLE = """
    QWidget#CentralWidget {{
        background-color: {bg_main};
        color: {fg_main};
        font-family: 'Segoe UI', Arial, sans-serif;
    }}
    
    /* Input Fields */
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
        background: transparent;  /* Fixes the background mismatch box */
        font-size: 28px;
        font-weight: 300;
        letter-spacing: 2px;
        color: {fg_title};
    }}
    
    QLabel#MetaData {{
        background: transparent;
        color: {fg_muted};
        font-size: 12px;
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
        border-radius: 5px;
        padding: 8px;
        font-size: 14px;
        margin: 10px;
        background-color: {bg_btn};
        color: {fg_title};
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
        background: transparent;
    }}
    QToolButton:hover {{
        background-color: {bg_btn_hover};
        border-radius: 4px;
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
    "Rose-Pine": {
        "bg_main": "#191724",
        "bg_sidebar": "#1f1d2e",
        "bg_btn": "#26233a",
        "bg_btn_hover": "#31748f",
        "bg_btn_active": "#ebbcba",
        "fg_main": "#e0def4",
        "fg_title": "#eb6f92",
        "fg_muted": "#908caa",
        "border_color": "#26233a",
        "accent": "#ebbcba",
    },
    "Gruvbox": {
        "bg_main": "#282828",
        "bg_sidebar": "#1d2021",
        "bg_btn": "#3c3836",
        "bg_btn_hover": "#504945",
        "bg_btn_active": "#665c54",
        "fg_main": "#ebdbb2",
        "fg_title": "#fabd2f",
        "fg_muted": "#928374",
        "border_color": "#3c3836",
        "accent": "#fe8019",
    },
    "Evergreen": {
        "bg_main": "#0d1b1e",
        "bg_sidebar": "#15282b",
        "bg_btn": "#1d3539",
        "bg_btn_hover": "#284b50",
        "bg_btn_active": "#355e65",
        "fg_main": "#d0e1d4",
        "fg_title": "#80ed99",
        "fg_muted": "#52796f",
        "border_color": "#284b50",
        "accent": "#57cc99",
    },
}

THEMES = {name: BASE_STYLE.format(**colors) for name, colors in PALETTES.items()}
