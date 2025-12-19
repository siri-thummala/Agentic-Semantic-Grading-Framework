from backend.evaluator.reference.llm_client import call_llm
def generate_reference_answer(question):
    """
    Uses LLM to generate a reference answer ONLY when model answer is absent.
    """

    prompt = f"""
    Generate a concise, factual reference answer (5-7 lines)
    suitable for academic evaluation.

    Question:
    {question}
    """

    # pseudo-code (API abstracted)
    response = call_llm(prompt)

    return response.strip()
