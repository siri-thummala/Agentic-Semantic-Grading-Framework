from fastapi import FastAPI
from pydantic import BaseModel

from backend.evaluator.main_pipeline import evaluate_answer

app = FastAPI(title="Answer Evaluation System")


class EvaluationRequest(BaseModel):
    question: str
    model_answer: str = ""
    student_answer: str


@app.get("/")
def home():
    return {"message": "FastAPI backend is running"}


@app.post("/evaluate")
def evaluate(req: EvaluationRequest):
    result = evaluate_answer(
        req.question,
        req.model_answer,
        req.student_answer
    )
    return result

