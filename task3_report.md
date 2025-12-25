# Task 3 Report – High-Level Requirement to Low-Level Technical Specification Tool  
**Name:** Divyanshi  
**Date:** (Today’s Date)  
**Tech Stack:** Python, Streamlit, OpenAI (optional), JSON/Markdown formatting, PDF Export  

---

## 1. Objective  
The objective of this task is to build an AI-based automation tool that converts high-level business requirements into low-level technical specifications.  
The tool generates module breakdown, database schemas, API specifications, and pseudocode from a simple business requirement input.

---

## 2. Tool Overview  
This prototype tool takes a business requirement as input and outputs:

✅ Modules / component breakdown  
✅ Database schema (tables + relationships)  
✅ API contracts (request/response)  
✅ Core workflow pseudocode  
✅ Exported technical specification document (JSON + Markdown + PDF)

---

## 3. Pipeline Workflow  

### Step 1: Input Requirement  
User provides a business requirement through the Streamlit UI.

Example input:  
“Build a job portal with login, job posting, job search, and application tracking.”

---

### Step 2: Requirement Analysis & Module Breakdown  
The tool detects requirement intent (e.g., job portal, food delivery) and breaks the system into modules such as:  
- Authentication  
- Job Posting  
- Search & Filters  
- Applications  
- Admin Panel  

---

### Step 3: Schema Design  
The tool generates database schemas including tables and relationships.

Example tables:  
- users  
- jobs  
- applications  

---

### Step 4: API Specification  
The tool generates REST API endpoints with request/response schemas and status codes.

Example:  
- POST /auth/login  
- POST /jobs  
- GET /jobs  
- POST /applications  

---

### Step 5: Pseudocode Generation  
The tool generates pseudocode to describe low-level logic for core workflows, such as:  
- job search flow  
- apply for job  
- employer review logic  

---

### Step 6: Export Outputs  
Generated specification is saved as:  
- output/spec.json  
- output/spec.md  
- output/spec.pdf  

---

## 4. Prototype Tool (Streamlit App)  
The project includes a Streamlit UI app where users can enter requirements and download JSON/Markdown/PDF outputs.

**Command to run:**  
```bash
streamlit run app.py
