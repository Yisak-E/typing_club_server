# 🧰 Development Setup & Troubleshooting Guide

**TypingClub Backend (Flask + Git + MySQL + Ubuntu)**

This document summarizes **all terminal commands used**, their **purpose**, and **practical benefits**, based on real issues encountered during setup and development.

---

## 1️⃣ Python Virtual Environment (Ubuntu / PEP 668 Fix)

### Create virtual environment

```bash
python3 -m venv .venv
```

**What it does**

* Creates an isolated Python environment for the project.

**Why it matters**

* Ubuntu blocks system-wide `pip install` (PEP 668).
* Prevents breaking OS Python.

**Where**

* Run inside the project root.

---

### Activate virtual environment

```bash
source .venv/bin/activate
```

**What it does**

* Switches Python & pip to the project environment.

**How to verify**

```bash
which python
which pip
```

Expected:

```text
.../typing_club_server/.venv/bin/python
```

---

## 2️⃣ Installing Flask & Backend Dependencies

### Install core Flask stack

```bash
pip install flask flask-cors flask-sqlalchemy flask-migrate python-dotenv pymysql
```

**What it does**

* Installs Flask framework and common backend extensions.

**Why it matters**

* Missing packages break Flask CLI (`flask db`, `flask run`).

---

### Save dependencies

```bash
pip freeze > requirements.txt
```

**Benefit**

* Allows reproducible installs:

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Flask CLI & Database Migrations (Flask-Migrate)

### Set Flask app (Linux)

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

**What it does**

* Tells Flask where the application entry point is.

---

### Initialize migrations (run once)

```bash
flask db init
```

**What it does**

* Creates `migrations/` directory.

**Important**

* Does NOT require MySQL to be installed.

---

### Generate migration

```bash
flask db migrate -m "Initial migration"
```

**What it does**

* Detects model changes and creates migration files.

---

### Apply migration

```bash
flask db upgrade
```

**What it does**

* Applies schema changes to the database.

---

## 4️⃣ MySQL Installation (Ubuntu)

### Install MySQL server

```bash
sudo apt update
sudo apt install mysql-server -y
```

---

### Start & enable MySQL

```bash
sudo systemctl start mysql
sudo systemctl enable mysql
```

---

### Create database & user

```bash
sudo mysql
```

```sql
CREATE DATABASE typing_club;
CREATE USER 'typing_user'@'localhost' IDENTIFIED BY 'StrongPassword123!';
GRANT ALL PRIVILEGES ON typing_club.* TO 'typing_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Why it matters**

* Required before running `flask db upgrade`.

---

## 5️⃣ Testing Flask APIs (curl)

### Test GET endpoint

```bash
curl "http://127.0.0.1:5000/get_text?level=1"
```

**What it does**

* Confirms API route works.
* Useful for backend testing without frontend.

---

### Pretty-print JSON (optional)

```bash
curl -s "http://127.0.0.1:5000/get_text?level=1" | jq
```

---

## 6️⃣ Git Authentication Problem (Repeated Username/Password)

### Check current remote

```bash
git remote -v
```

**Why it matters**

* HTTPS remotes cause repeated auth prompts.

---

### Test SSH authentication

```bash
ssh -T git@github.com
```

**Expected**

```text
Hi Yisak-E! You've successfully authenticated.
```

---

### Switch repo from HTTPS → SSH

```bash
git remote set-url origin git@github.com:Yisak-E/typing_club_server.git
```

**Benefit**

* Eliminates username/password prompts permanently.

---

### Verify SSH remote

```bash
git remote -v
```

Expected:

```text
origin git@github.com:Yisak-E/typing_club_server.git (fetch)
origin git@github.com:Yisak-E/typing_club_server.git (push)
```

---

### Final confirmation

```bash
git pull
git push
```

**Expected behavior**

* No authentication prompts.

---

## 7️⃣ SSH Key Management (Persistence)

### Check loaded SSH keys

```bash
ssh-add -l
```

---

### Load SSH key (if missing)

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

### Permanent fix (optional)

Add to `~/.bashrc`:

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
  eval "$(ssh-agent -s)" >/dev/null
  ssh-add ~/.ssh/id_ed25519 2>/dev/null
fi
```

---

## 8️⃣ Common Errors & Lessons Learned

### ❌ `externally-managed-environment`

**Cause**

* Installing packages without a virtual environment.

**Fix**

* Always use `.venv`.

---

### ❌ `No such command 'db'`

**Cause**

* Flask app failed to import (missing dependency).

**Fix**

* Install missing packages before running Flask CLI.

---

## ✅ Final Benefits of This Setup

* 🔐 Secure Git authentication (SSH)
* 🧪 Reliable Flask CLI & migrations
* 🐍 Safe Python package management
* 🗄️ Proper MySQL integration
* 🚀 Professional backend workflow

---

**Status:** ✅ Fully configured & verified
**Target audience:** Flask backend developers on Ubuntu
**Project:** TypingClub Server

---