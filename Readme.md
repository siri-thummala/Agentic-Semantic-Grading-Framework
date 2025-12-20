# Intelligent Answer Evaluation System

## Problem Statement
Manual evaluation of descriptive answers is time-consuming and subjective.  
This project proposes an explainable system that evaluates student answers
using semantic similarity and concept coverage analysis.

## Scope (Version 1)
- Text-based answers only
- Semantic similarity evaluation
- Keyword / concept coverage analysis
- Not creativity-based grading

## Evaluation Pipeline
1. Input collection
2. Reference answer selection
3. Text preprocessing
4. Semantic similarity computation
5. Concept / keyword coverage analysis
6. Score calculation
7. Feedback generation

## Mark Distribution
- Semantic similarity: 4 marks
- Keyword coverage: 4 marks
- Structure & grammar: 2 marks

## 🛠 Technologies and Components Used
## 🔹 Backend
- FastAPI – REST API framework for handling evaluation requests
- Python 3 – Core backend programming language
- Pydantic – Request validation and data modeling
- Uvicorn – ASGI server for running the FastAPI application
- CORS Middleware – Enables secure communication between frontend and backend
- Swagger UI – API testing and documentation interface
## 🔹 Frontend
- React.js – Frontend library for building user interfaces
- JavaScript (ES6) – Client-side logic
- HTML5 & CSS – Page structure and styling
- Fetch API – Used to send evaluation requests to backend API
- Node.js & npm – Package management and development server

## Design Philosophy
LLMs are probabilistic and non-deterministic.  
For academic evaluation, explainability and consistency are critical.
Hence, rule-based scoring and ML similarity are used, while LLMs act
only as a support layer.

## Future Enhancements
- Handwritten answer evaluation using OCR
- Multilingual support
- Instructor-defined rubrics
