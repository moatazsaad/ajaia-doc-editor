# Ajaia Collaborative Document Editor

## Overview

This is a lightweight collaborative document editor inspired by Google Docs.

It allows users to create, edit, save, upload, and share documents. The project was built as a focused MVP to demonstrate product judgment, full-stack execution, persistence, file handling, sharing logic, and practical AI-assisted development.

---

## Live Demo

Frontend:
https://ajaia-doc-editor-gules.vercel.app

Backend API:
https://ajaia-backend-iccl.onrender.com

Walkthrough Video:
https://youtu.be/dXLzKOLLSH8

---

## Features

### Document Editing

- Create new documents
- Rename documents
- Edit document content in the browser
- Save and reopen documents
- Rich-text formatting:
  - Bold
  - Italic
  - Underline
  - Headings
  - Bulleted lists
  - Numbered lists

### File Upload

- Upload `.txt` or `.md` files
- Uploaded files are converted into editable documents

### Sharing

- Seeded users are used to simulate ownership and sharing
- Documents have an owner
- Owners can share documents with another user by email
- Shared documents appear under **Shared With Me**

### Persistence

- Documents are stored in SQLite
- Saved content remains available after refresh
- Sharing data is persisted

---

## Tech Stack

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- TipTap editor

### Backend

- FastAPI
- SQLAlchemy
- SQLite

### Testing

- pytest
- FastAPI TestClient

---

## Project Structure

```text
ajaia-doc-editor/
  backend/
    app/
      main.py
      database.py
      models.py
      schemas.py
    tests/
      test_documents.py
    requirements.txt

  frontend/
    app/
      page.tsx
      doc/[id]/page.tsx
    package.json

  README.md
  ARCHITECTURE.md
  AI_WORKFLOW.md
  SUBMISSION.md
````

---

## Local Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:3000
```

---

## Test Users

The app uses seeded users instead of full authentication.

```text
Owner User
Email: owner@ajaia.test
userId: 1
```

```text
Reviewer User
Email: reviewer@ajaia.test
userId: 2
```

---

## How to Test Sharing

1. Open the app as Owner User.
2. Create a document.
3. Open the document.
4. Share it with:

```text
reviewer@ajaia.test
```

5. Switch to Reviewer User.
6. The document appears under **Shared With Me**.

---

## Run Tests

From the backend folder:

```bash
pytest
```

The included test validates the basic document lifecycle:

```text
create → update → read
```

---

## Intentional Scope Decisions

This project intentionally does not include:

* Full authentication
* Real-time collaboration
* Advanced permissions
* Complex file parsing
* Version history

These were deprioritized to keep the MVP stable, focused, and deliverable within the timebox.

---

## Future Improvements

With more time, I would add:

* User authentication
* Real-time collaboration
* Role-based permissions
* Version history
* Comments and suggestions
* Export to PDF or Markdown

---

## AI Workflow

AI tools were used to accelerate planning, scaffolding, debugging, and integration. Final architecture, scope decisions, validation, and tradeoffs were manually reviewed and controlled.

See:

```text
AI_WORKFLOW.md
```


