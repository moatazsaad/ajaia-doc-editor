from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import User, Document, DocumentShare
from app.schemas import DocumentCreate, DocumentUpdate, DocumentOut, ShareRequest

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ajaia Docs API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def seed_users(db: Session):
    users = [
        {"id": 1, "email": "owner@ajaia.test", "name": "Owner User"},
        {"id": 2, "email": "reviewer@ajaia.test", "name": "Reviewer User"},
    ]

    for user in users:
        existing = db.query(User).filter(User.id == user["id"]).first()
        if not existing:
            db.add(User(**user))

    db.commit()


@app.on_event("startup")
def startup():
    db = next(get_db())
    seed_users(db)


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.post("/documents", response_model=DocumentOut)
def create_document(payload: DocumentCreate, db: Session = Depends(get_db)):
    doc = Document(
        title=payload.title,
        content="",
        owner_id=payload.owner_id,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


@app.get("/documents/owned/{user_id}")
def get_owned_documents(user_id: int, db: Session = Depends(get_db)):
    return db.query(Document).filter(Document.owner_id == user_id).all()


@app.get("/documents/shared/{user_id}")
def get_shared_documents(user_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Document)
        .join(DocumentShare, Document.id == DocumentShare.document_id)
        .filter(DocumentShare.user_id == user_id)
        .all()
    )


@app.get("/documents/{document_id}", response_model=DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return doc


@app.put("/documents/{document_id}", response_model=DocumentOut)
def update_document(
    document_id: int,
    payload: DocumentUpdate,
    db: Session = Depends(get_db),
):
    doc = db.query(Document).filter(Document.id == document_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if payload.title is not None:
        doc.title = payload.title

    if payload.content is not None:
        doc.content = payload.content

    db.commit()
    db.refresh(doc)
    return doc


@app.post("/documents/{document_id}/share")
def share_document(
    document_id: int,
    payload: ShareRequest,
    db: Session = Depends(get_db),
):
    doc = db.query(Document).filter(Document.id == document_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    user = db.query(User).filter(User.email == payload.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    existing_share = (
        db.query(DocumentShare)
        .filter(
            DocumentShare.document_id == document_id,
            DocumentShare.user_id == user.id,
        )
        .first()
    )

    if existing_share:
        return {"message": "Document already shared with this user"}

    share = DocumentShare(document_id=document_id, user_id=user.id)
    db.add(share)
    db.commit()

    return {"message": f"Document shared with {user.email}"}


@app.post("/documents/upload")
async def upload_document(
    owner_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    allowed_types = [".txt", ".md"]

    if not any(file.filename.endswith(ext) for ext in allowed_types):
        raise HTTPException(
            status_code=400,
            detail="Only .txt and .md files are supported",
        )

    content = (await file.read()).decode("utf-8")

    doc = Document(
        title=file.filename,
        content=content,
        owner_id=owner_id,
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return doc