# AI Workflow Note

## Overview
AI tools were used throughout development to accelerate implementation while maintaining full control over design decisions, validation, and final output quality.

---

## Tools Used
- ChatGPT for architecture planning, code scaffolding, and debugging
- AI-assisted coding for both backend (FastAPI) and frontend (Next.js + TipTap)

---

## Where AI Helped Most

- Generated initial FastAPI structure (routes, models, schemas)
- Assisted in integrating TipTap editor into Next.js
- Helped scaffold React components and state management
- Accelerated debugging of API calls and UI issues
- Suggested implementation approaches for file upload and sharing

---

## What Was Modified

AI-generated code was not used blindly. Key modifications included:

- Adjusted API routes to correctly handle document ownership and sharing
- Fixed frontend state issues (document loading, saving, and refresh)
- Simplified overly complex AI suggestions to match MVP scope
- Improved UI structure for clarity and usability

---

## What Was Rejected

Several AI suggestions were intentionally not implemented:

- Real-time collaboration (WebSockets / CRDTs) — too complex for the time constraint
- Full authentication system — unnecessary for demonstrating core functionality
- Advanced file parsing pipelines — out of scope for MVP

---

## Validation Approach

To ensure correctness and reliability:

- Manually tested all core flows:
  - create → edit → save → reload
  - upload → open → edit
  - share → switch user → access
- Verified persistence by refreshing the application
- Confirmed sharing logic by switching between seeded users
- Added an automated backend test for document lifecycle

---

## Summary

AI significantly improved development speed and iteration quality.
However, all architectural decisions, tradeoffs, and validations were made manually to ensure a practical, reliable, and well-scoped solution.