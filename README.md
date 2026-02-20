# Smart_File_Organiser

A modular Python CLI application that automatically organises files by type, detects duplicates using content hashing, and helps users review uncertain or low value files.

This project demonstrates structured application design, file system manipulation, hashing, logging, and unit testing in Python.

**Features**

• Classifies files by extension

• Detects duplicates using SHA256 hashing

• Moves junk and low value files into review folders

• Interactive CLI review for unknown files

• Logs all actions for traceability

• Fully testable with pytest

**Project Structure**

smart-file-organiser/
│
├── app/
│   ├── main.py
│   ├── scanner.py
│   ├── classifier.py
│   ├── duplicate_detector.py
│   ├── mover.py
│   ├── interactive.py
│   ├── logger.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├── test_classifier.py
│   ├── test_duplicates.py
│
├── requirements.txt
└── README.md

**Installation**
1. Clone the repository
git clone https://github.com/yourusername/smart-file-organiser.git
cd smart-file-organiser
2. Create a virtual environment (recommended)
Windows:
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
**How to Use the Application**

Run the organiser from the root directory:

python app/main.py /path/to/your/folder

Example:

python app/main.py C:\Users\YourName\Downloads

or

python app/main.py ~/Downloads

**What Happens When You Run It
**
The program scans all files in the given directory.

Duplicates are detected using SHA256 hashing.

Files are classified by type.

Junk files and duplicates are moved into:
organized_output/review/

Unknown or low value files trigger an interactive prompt:
Keep
Delete
Skip

All actions are logged in:
organiser.log

Your organized files will appear inside:

organized_output/

Grouped by category.

**Running Tests**

To run unit tests:

pytest

This validates:

File classification logic

Duplicate detection via hashing
.
