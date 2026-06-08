# 📁 Advanced Python File Manager

A command-line File Manager built with Python that allows users to create, organize, edit, copy, move, and manage files directly from the terminal.

This project was developed to practice Python fundamentals while simulating real-world file system operations. It combines Object-Oriented Programming (OOP), file handling, loops, functions, and operating system interactions into a single practical application.

---

## 🚀 Features

### File Operations

* Create files
* Read file contents
* Edit existing files
* Delete files
* Rename files

### File Organization

* View all files
* Search for files
* Display file information
* Count words in files

### Advanced Features

* Multi-line text editor
* Copy files
* Move files between folders
* Automatic folder creation
* Input validation
* Error handling
* Persistent file storage

---

## 🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* OS Module
* Shutil Module

---

## 📂 Project Structure

```text
file-manager-python/
│
├── file-manager.py
│
├── files/
│   ├── notes.txt
│   ├── report.txt
│   └── ...
│
├── documents/
│
└── backups/
```

The `files` folder is automatically created when the program runs for the first time.

Additional folders are automatically generated whenever a file is moved to a destination that does not already exist.

---

## 📋 Application Menu

```text
===================================
      SIMPLE FILE MANAGER
===================================

1. Create File
2. Read File
3. Edit File
4. Delete File
5. Rename File
6. View All Files
7. Search File
8. File Information
9. Word Count
10. Copy File
11. Move File
12. Exit
```

---

## ⚙️ Installation

#### Clone the Repository

```bash
git clone https://github.com/Forte-Romeo/file-manager-python.git
```

#### Navigate into the Project Folder

```bash
cd file-manager-python
```

#### Run the Application

```bash
python file-manager.py
```

or

```bash
python3 file-manager.py
```

---

## 🔍 Feature Breakdown

### 1. Create File

Creates a new file in the storage directory.

#### Example

```text
Filename: notes.txt
```

The program then launches the multi-line editor.

```text
Enter text below.
Type 'SAVE' on a new line when finished.

My first note
Learning Python
SAVE
```

Result:

```text
File created successfully.
```

---

### 2. Read File

Displays the contents of an existing file.

#### Example

```text
My first note
Learning Python
```

---

### 3. Edit File

Allows the user to overwrite the contents of an existing file using the multi-line editor.

#### Example

```text
Enter text below.
Type 'SAVE' on a new line when finished.

Updated content
More information
SAVE
```

---

### 4. Delete File

Permanently removes a selected file after confirmation.

#### Example

```text
Are you sure you want to delete 'notes.txt'? (y/n)
```

---

### 5. Rename File

Changes the name of an existing file.

#### Example

```text
Current filename:
notes.txt

New filename:
python_notes.txt
```

---

### 6. View All Files

Lists every file stored inside the application directory.

#### Example

```text
1. notes.txt
2. report.txt
3. tasks.txt
```

---

### 7. Search File

Checks whether a file exists.

#### Example

```text
Enter filename:
notes.txt
```

Output:

```text
File exists.
```

---

### 8. File Information

Displays file metadata.

#### Example

```text
Filename: notes.txt
Size: 2048 bytes
```

---

### 9. Word Count

Calculates the number of words in a file.

#### Example

```text
Total words: 125
```

---

### 10. Copy File

Creates a duplicate of an existing file.

### Example

```text
File to copy:
notes.txt

New file name:
notes_backup.txt
```

Result:

```text
notes.txt
notes_backup.txt
```

Both files contain identical content.

---

### 11. Move File

Moves a file from the main storage folder to another directory.

#### Example

```text
Filename:
report.txt

Destination folder:
documents
```

Result:

```text
documents/report.txt
```

If the destination folder does not exist, it is automatically created.

---

## ✍️ Multi-Line Text Editor

The application includes a built-in text editor for creating and editing files.

Users can enter multiple lines of text and save when finished.

### Example

```text
Enter text below.
Type 'SAVE' on a new line when finished.

This is line one.
This is line two.
This is line three.
SAVE
```

The content is then written to the selected file.

---

## 📚 Python Concepts Demonstrated

| Concept       | Application                              |
| ------------- | ---------------------------------------- |
| Variables     | User input and data storage              |
| Functions     | File operation methods                   |
| Loops         | Menu navigation and editor functionality |
| Conditionals  | Input validation and error handling      |
| Lists         | File listing and text storage            |
| Strings       | Content processing                       |
| Classes       | Application structure                    |
| OOP           | Encapsulation of file operations         |
| File Handling | Create, read, update, delete files       |
| OS Module     | File and directory management            |
| Shutil Module | Copying and moving files                 |

---

## 🎯 Learning Objectives

This project helps developers gain practical experience with:

* Command-Line Application Development
* Object-Oriented Programming
* File System Management
* Error Handling
* Data Processing
* User Interaction Design
* Software Project Structure

---

## 📈 Skills Demonstrated

This project demonstrates understanding of:

### Beginner Level

* Variables
* Input/Output
* Loops
* Functions
* Lists
* Dictionaries

### Intermediate Level

* Classes and Objects
* File Handling
* Directory Management
* Program Organization
* User Experience Design

### Real-World Concepts

* CRUD Operations
* File Management Systems
* Folder Organization
* Backup Management
* Data Persistence

---

## 🔮 Future Enhancements

Potential improvements include:

### File Management

* Sort files alphabetically
* Sort files by size
* Recently modified files
* File extension filtering
* File compression

### User Experience

* Colored terminal interface
* Progress indicators
* Better menu navigation

### Advanced Features

* Activity logs
* Recycle bin system
* Password-protected files
* File encryption
* SQLite database integration

### GUI Version

* Tkinter Interface
* CustomTkinter Interface
* PyQt Desktop Application

---

## 👨‍💻 Author

Built by Ferguson Romeo (Forte Romeo)  
Software + AI Engineer | IT Student | Builder in Progress 🚀

Developed as a Python learning project to strengthen skills in:

* Python Fundamentals
* File Handling
* Object-Oriented Programming
* Command-Line Interfaces
* Operating System Interactions

---

## 📄 License

This project is open-source and available for educational and personal use.

---

## ⭐ Support

If you like this project:
- Star the repository
- Fork the project
- Feel free to improve it
- Build your own version

Happy Coding 🚀
