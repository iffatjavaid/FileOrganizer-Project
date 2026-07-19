# 📂 File Organizer

## 📌 Description

File Organizer is a Python automation project that automatically sorts files into separate folders based on their file extensions. It helps keep directories clean and organized without manually moving files.

This project was developed as part of my Python learning journey to practice file automation using Python.

---

## ✨ Features

- Automatically organizes files by type
- Creates folders automatically if they do not exist
- Supports Images, PDFs, Documents, Videos, Music, Excel Files, Python Files, and Archives
- Moves unknown file types to an **Others** folder
- Displays every file movement
- Shows the total number of organized files

---

## 🛠 Technologies Used

- Python 3
- os Module
- shutil Module

---

## 📚 Concepts Used

- Functions
- Dictionaries
- Loops
- Conditional Statements
- File Paths
- File Extensions
- os.listdir()
- os.makedirs()
- os.path.splitext()
- shutil.move()

---

## 📂 Project Structure

```
CodeAlpha_File_Organizer/
│
├── FileOrganizer.py
├── README.md
└── Test_Folder/
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone <repository-link>
```

2. Place your files inside the **Test_Folder**.

3. Run:

```bash
python FileOrganizer.py
```

4. The program automatically creates folders and organizes the files.

---

## 📸 Sample Output

```
=============================================
            FILE ORGANIZER
=============================================

Moved: photo.jpg ---> Images
Moved: report.pdf ---> PDFs
Moved: python.py ---> Python Files
Moved: notes.docx ---> Documents
Moved: music.mp3 ---> Music

--------------------------------
Total files organized: 5
Organization Completed Successfully!
--------------------------------
```

---

## 🎯 Learning Outcomes

This project helped me learn:

- File automation using Python
- Working with folders and file paths
- Organizing files based on extensions
- Using the `os` and `shutil` modules
- Building practical automation scripts


## 👨‍💻 Author

**Iffat Javaid**

BS Computer Science Student

Python Learning Journey
