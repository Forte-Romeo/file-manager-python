# 📁 Simple File Manager Script

A beginner-friendly command-line File Manager built with Python.

This project allows users to create, read, edit, delete, rename, and manage files directly from the terminal. It demonstrates core Python concepts such as Object-Oriented Programming (OOP), file handling, loops, functions, and working with the operating system through the `os` module.

---

## 🚀 Features

### File Operations

* Create files
* Read file contents
* Edit existing files
* Delete files
* Rename files

### File Management

* View all files in the storage folder
* Search for files
* Display file information
* Count words inside a file

### Additional Features

* Automatic creation of storage folder
* Input validation
* User-friendly menu system
* Error handling for missing files
* Continuous CLI interaction until exit

---

## 🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* OS Module

---

## 📂 Project Structure

```text
file-manager-python/
│
├── main.py
│
└── files/
    ├── notes.txt
    ├── tasks.txt
    └── ...
```

The `files` directory is automatically created when the application runs for the first time.

---

## 📋 Menu Options

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
10. Exit
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Forte-Romeo/file-manager-python.git
```

### 2. Navigate to the Project Folder

```bash
cd file-manager-python
```

### 3. Run the Application

```bash
python file-manager.py
```

Or:

```bash
python3 file-manager.py
```

---

## 🔍 Feature Breakdown

### 1. Create File

Creates a new file inside the storage folder.

Example:

```text
Filename: notes.txt
Content: My first file
```

Result:

```text
notes.txt created successfully.
```

---

### 2. Read File

Displays the contents of an existing file.

Example:

```text
Milk
Bread
Eggs
```

---

### 3. Edit File

Overwrites the contents of an existing file with new content.

---

### 4. Delete File

Removes a file permanently after user confirmation.

Example:

```text
Are you sure? (y/n)
```

---

### 5. Rename File

Changes a file's name while preserving its contents.

Example:

```text
old_name.txt
→
new_name.txt
```

---

### 6. View All Files

Displays every file stored in the application folder.

Example:

```text
1. notes.txt
2. tasks.txt
3. shopping.txt
```

---

### 7. Search File

Checks whether a file exists.

Example:

```text
File exists.
```

or

```text
File not found.
```

---

### 8. File Information

Displays information about a selected file.

Example:

```text
Filename: notes.txt
Size: 1024 bytes
```

---

## 9. Word Count

Counts the total number of words in a file.

Example:

```text
Total words: 156
```

---

## 🎯 Python Concepts Demonstrated

This project applies several fundamental Python concepts:

| Concept       | Usage                                    |
| ------------- | ---------------------------------------- |
| Variables     | Store user input and file data           |
| Functions     | Organize file operations                 |
| Loops         | Keep application running                 |
| Conditionals  | Menu navigation and validation           |
| Lists         | Display file collections                 |
| File Handling | Create, read, update, and delete files   |
| OOP           | Encapsulate functionality inside a class |
| OS Module     | Manage files and directories             |

---

## 📚 Learning Outcomes

By building this project, you will gain experience with:

* Designing command-line applications
* Structuring code using classes
* Managing files and directories
* Working with user input
* Error handling
* Building CRUD-based applications
* Organizing Python projects

---

## 🔮 Future Improvements

Possible enhancements include:

* Multi-line text editor
* File copy functionality
* Move files between folders
* File extension filtering
* Sort files alphabetically
* Sort files by size
* Recently modified files view
* Colored terminal output
* Advanced CLI menus using Questionary
* Activity logs
* Password-protected files
* SQLite database integration
* GUI version using Tkinter or CustomTkinter

---

## 👨‍💻 Author

Built by Ferguson Romeo (Forte Romeo)  
Software + AI Engineer | IT Student | Builder in Progress 🚀

---

## ⭐ Support

If you like this project:
- Star the repository
- Fork the project
- Feel free to improve it
- Build your own version

Happy Coding 🚀
