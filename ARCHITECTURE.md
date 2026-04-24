# Architecture Note

## Overview
This application is a lightweight full-stack document editor designed to demonstrate strong product judgment and practical engineering within a limited time.

---

## System Components

### Frontend
- Next.js (App Router)
- TipTap for rich-text editing
- Tailwind CSS for styling

Responsibilities:
- Document UI
- Editor interaction
- API communication

---

### Backend
- FastAPI
- REST API design

Responsibilities:
- Document CRUD operations
- Sharing logic
- File upload handling

---

### Database
- SQLite

Tables:
- users
- documents
- document_shares

---

## Data Flow

1. User interacts with UI (create/edit/share)
2. Frontend sends request to backend API
3. Backend processes logic and updates database
4. Frontend fetches updated data and renders it

---

## Key Design Decisions

### 1. TipTap Editor
Chosen for fast integration and realistic editing experience.

### 2. Simplified Authentication
Used seeded users instead of full auth to reduce scope and focus on core product features.

### 3. File Upload Scope
Limited to `.txt` and `.md` to avoid complex parsing and keep system reliable.

### 4. No Real-time Collaboration
Deferred due to complexity and time constraints.

---

## Tradeoffs

- No authentication system
- No real-time collaboration
- Limited file format support

These were intentional decisions to prioritize a stable, testable MVP.

---

## Scalability Considerations

With more time, the system could be extended with:
- PostgreSQL instead of SQLite
- Authentication and role-based access
- WebSocket-based real-time collaboration
- Version history and document diffing