# 📝 Graphite Notepad App

Graphite is a fast, lightweight, and completely local desktop note-taking application built with Python and PyQt6. Featuring a **minimalistic UI** and **sleek visual themes**, Graphite stores all your notes locally in a MySQL database with a dynamic sidebar that automatically organizes notes by recent updates.

---

## ✨ Features
* **Minimalistic UI:** A clean, distraction-free interface designed for effortless note-taking.
* **Themes & Styling:** Styled with modern aesthetic layouts for comfortable day and night reading.
* **Full CRUD Operations:** Create, edit, view, and delete notes seamlessly.
* **Dynamic Sidebar:** Instantly displays and sorts your notes by the most recently updated.
* **Auto-Database Setup:** Automatically generates the required database (`notepad`) and tables on its first launch.
* **No Python Required:** Packaged as a standalone Windows executable (`GRAPHITE.exe`).
* **100% Local Data:** Your notes stay secure on your own machine.

---

## 📦 Download & Quick Setup

### 1. Download
Go to the **Releases** section on the right side of this repository page and download `installer.zip`.

### 2. Extract
Unzip the folder anywhere on your computer. Make sure all of the following files remain together in the extracted folder:
* `GRAPHITE.exe` — Application executable
* `logo.png` — App icon asset
* `password.txt` — Database connection file
* `INSTRUCTIONS.txt` — Offline setup guide

### 3. Database Password Configuration
Graphite connects to your local MySQL server.
1. Open **`password.txt`**.
2. Replace `ENTER YOUR PASSWORD ONLY HERE` with your personal MySQL `root` password.
3. Save and close the file.

### 4. Run
* **Windows:** Double-click **`GRAPHITE.exe`** to launch!
* **Linux (via Wine):** Open a terminal in the folder and run `wine GRAPHITE.exe`.

---

## 🛠️ Running from Source (Developers)

If you want to view, run, or edit the Python source code directly:

1. Clone the repository:
   ```bash
   git clone [https://github.com/nihal-sam911/Graphite.git](https://github.com/nihal-sam911/Graphite.git)
