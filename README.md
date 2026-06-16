# IDP Backend

## Intelligent Document Processing (IDP) Platform

AI-powered document processing backend built with FastAPI, EasyOCR, Groq LLM, ChromaDB, and PostgreSQL-ready architecture.

---

## Features

### Document Upload

* Upload images (.jpg, .jpeg, .png)
* Upload PDF documents

### OCR Extraction

* EasyOCR based text extraction
* PDF support via pdf2image + Poppler
* Image text recognition

### AI Processing

* Document Classification
* Entity Extraction
* Document Summarization
* Structured JSON Output

### Current Supported Types

* Aadhaar Card
* Resume
* Invoice
* Financial Statement
* Generic Documents

---

## Tech Stack

Backend:

* FastAPI
* Python

OCR:

* EasyOCR
* pdf2image
* Poppler

LLM:

* Groq
* LangChain
* LangChain-Groq

Vector Database:

* ChromaDB

Database:

* PostgreSQL (Ready for Integration)

---

## Project Structure

backend/
│
├── app.py
│
├── routes/
│   ├── upload.py
│   ├── extract.py
│   └── summary.py
│
├── services/
│   ├── ocr_service.py
│   └── llm_service.py
│
├── uploads/
│
├── chroma_db/
│
├── database/
│
├── .env
├── requirements.txt
└── README.md

---

## API Endpoints

### Upload File

POST /upload

Request:
multipart/form-data

Field:
file

Response:

{
"path": "uploads/file.jpg"
}

---

### Extract Document

POST /extract

Request:
multipart/form-data

Field:
file

Response:

{
"filename": "sample.jpg",
"document_type": "Aadhaar",
"ocr_text": "...",
"structured_data": {},
"summary": "..."
}

---

### Health Check

GET /

Response:

{
"message": "IDP Platform Running"
}

---

### Summary

GET /summary

Response:

{
"status": "ready"
}

---

## Environment Variables

Create .env file:

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile

---

## Installation

Create Virtual Environment

python -m venv .venv

Activate

.venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

---

## Run Server

python -m uvicorn app:app --reload

Server:

http://127.0.0.1:8000

Swagger Docs:

http://127.0.0.1:8000/docs

---

## Current Status

Completed:

* FastAPI Backend
* OCR Pipeline
* PDF Processing
* Groq Integration
* Document Classification
* Entity Extraction
* Document Summary
* Swagger Documentation

Pending:

* PostgreSQL Integration
* ChromaDB Persistence
* Frontend Integration
* Authentication
* Deployment

---

## Author

Ayush Pandey

MCA, NIT Jamshedpur
