# Ajaia Collaborative Document Editor

## Overview
This is a lightweight collaborative document editor inspired by Google Docs.
It supports document creation, rich-text editing, file upload, sharing, and persistence.

The goal was to deliver a strong, usable MVP within a constrained timebox.

---

## Features

### Core
- Create, rename, edit documents
- Rich-text editor (bold, italic, underline, headings, lists)
- Save and reopen documents
- File upload (.txt, .md → converted to document)
- Share documents between users
- Separate "My Documents" and "Shared With Me"

### Technical
- Full stack (Next.js + FastAPI)
- SQLite persistence
- REST API
- Basic automated test

---

## Tech Stack

- Frontend: Next.js + Tailwind + TipTap
- Backend: FastAPI
- Database: SQLite
- Testing: pytest

---

## Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend runs at:
http://127.0.0.1:8000

Frontend
cd frontend
npm install
npm run dev

Frontend runs at:
http://localhost:3000

Test Users
owner@ajaia.test
 (userId = 1)
reviewer@ajaia.test
 (userId = 2)
How to Test Sharing
Create document as userId = 1
Share with reviewer@ajaia.test
Change userId = 2 in frontend
Refresh → document appears in "Shared With Me"
File Upload

Supported:

.txt
.md

Uploaded files are converted into editable documents.

Notes
Authentication is simplified using seeded users
Real-time collaboration is intentionally not implemented due to time constraints