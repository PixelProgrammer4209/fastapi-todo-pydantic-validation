# Task C: Validation & Error Handling (Pydantic)

## Overview

In this task, you will add data validation and error handling to a Todo API using Pydantic. You can either continue building on top of your own working Todo CRUD API from Task B, or use the starter file provided in the `starter/` folder of this repository — whichever works best for you.

Your job is to layer proper Pydantic validation and error responses on top of the existing CRUD logic.

---

## Submission Guidelines

Follow the steps below to submit your solution.

### 1. Fork the Repository

Click the **Fork** button at the top-right of this repository, or use the link below:

```bash
https://github.com/mulearngectcr/fastapi-todo-validation
```

This will create a copy of the repository under your GitHub account.

### 2. Clone Your Fork

Replace `<your-username>` with your GitHub username:

```bash
git clone https://github.com/<your-username>/fastapi-todo-validation.git
cd fastapi-todo-validation
```

### 3. Create a Folder with Your Name

Inside the repo, create a new folder named after you.

Your folder structure should look like this:

```bash
fastapi-todo-validation/
└── john-doe/
  ├── main.py
  ├── requirements.txt
  └── .gitignore
```

### 4. Get Your Starting Code

You have two options — choose whichever applies to you:

**Option 1 — Use your own Task B submission ✅ (recommended if it's working)**

If your Task B CRUD API is working correctly (GET, POST, PUT, DELETE all functional), copy your `main.py` from that submission and paste it into your named folder here. This is the preferred approach.

**Option 2 — Use the starter file (if Task B isn't complete)**

Open the `starter/main.py` file already present in this repository. Copy its contents and paste them into a new `main.py` file inside your named folder.

> ⚠️ Whichever option you choose, do not submit the file unchanged — your task is to add Pydantic validation and error handling on top of the existing CRUD logic.

### 5. Set Up Your Environment

```bash
python -m venv venv
```

Activate it:

- **Windows:**
```bash
venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

Then install the required packages:

```bash
pip install fastapi uvicorn
pip freeze > requirements.txt
```

### 6. Add a .gitignore

Create a `.gitignore` file inside your named folder with the following content:

```bash
venv/
pycache/
*.pyc
.env
```
### 7. Commit Your Changes

Once you are done, stage and commit your files:

```bash
git add .
git commit -m "Add submission - John Doe"
```

Replace `John Doe` with your actual name.

### 8. Push to Your Fork

```bash
git push origin main
```

### 9. Open a Pull Request

1. Go to your fork on GitHub
2. Click **Contribute → Open Pull Request**
3. Make sure the PR is directed from your fork to `mulearngectcr/fastapi-todo-validation`
4. Set the PR title to: `Submission - John Doe` (replace with your name)
5. Click **Create Pull Request**

Happy Building! 🚀
