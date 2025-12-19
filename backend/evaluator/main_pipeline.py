from backend.evaluator.preprocessing.text_cleaner import clean_text
from backend.evaluator.similarity.similarity_engine import compute_similarity
from backend.evaluator.concept.concept_analyzer import analyze_concepts
from backend.evaluator.score.score_calculator import calculate_score
from backend.evaluator.feedback.feedback_generator import generate_feedback
from backend.evaluator.feedback.feedback_enhancer import enhance_feedback



def evaluate_answer(question, model_answer, student_answer):
    """
    Runs the complete answer evaluation pipeline.
    """

    # 1. Reference answer selection
    if model_answer and model_answer.strip():
        reference_answer = model_answer
    else:
        reference_answer = generate_reference_answer(question)

    # 2. Text preprocessing
    ref_tokens = clean_text(reference_answer)
    student_tokens = clean_text(student_answer)

    # 3. Semantic similarity
    similarity_score = compute_similarity(ref_tokens, student_tokens)

    # 4. Concept / keyword coverage
    concept_result = analyze_concepts(ref_tokens, student_tokens)

    # 5. Score calculation
    score_breakdown = calculate_score(similarity_score, concept_result)

    # 6. Feedback generation
    raw_feedback = generate_feedback(score_breakdown, concept_result["missing"])

    final_feedback = enhance_feedback(raw_feedback)


    return {
        "question": question,
        "reference_answer": reference_answer,
        "student_answer": student_answer,
        "similarity_score": round(similarity_score, 2),
        "concept_coverage": concept_result,
        "score_breakdown": score_breakdown,
        "feedback": final_feedback
    }

