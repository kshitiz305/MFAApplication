# Development Team Project: Coding Output

# Prerequisite

The following should be installed already before setup.
- Python3

Requirements:
```
pip install -r requirements.txt
```
# Program

Running in Linux from the downloaded directory:
```
export FLASK_APP=__init__.py
flask run
```

Running in Windows from the downloaded directory:
Change to downloaded directory
```
set FLASK_APP=__init__.py
flask run
```
User management page (Admin role required)

Change to admin directory
```
flask run --port=8888
```
Admin user: admin@test.com
Default user password: P@ssw0rd

# Database

DB details:
```
Host: sql5.freesqldatabase.com:3306
Database user: sql5495299
Database name: sql5495299
Database password: hz7bDRYNPh
Web console: https://www.phpmyadmin.co/
```

Database Query:

Code to recreate the 2 x NASA database tables:
```
CREATE TABLE IF NOT EXISTS user(id INT(5) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, email VARCHAR(64) UNIQUE NOT NULL, password VARCHAR(64) NOT NULL, name VARCHAR(30) NOT NULL, role ENUM('ISS', 'Ground Staff', 'Government', 'Admin') NOT NULL, PRIMARY KEY(id));

CREATE TABLE IF NOT EXISTS document_repository(fileID INT(7) UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE, filename VARCHAR(255) NOT NULL UNIQUE, uploaded DATE NOT NULL, classification TINYINT(1) NOT NULL, owner INT(5) UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(fileID), FOREIGN KEY (owner) REFERENCES user(id))
```
***
Removed username field due to redundancy as email address can be used.
