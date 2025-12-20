from fastapi import FastAPI
from pydantic import BaseModel



from evaluator.main_pipeline import evaluate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Answer Evaluation System")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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

