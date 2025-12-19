from backend.evaluator.reference.llm_client import call_llm

def enhance_feedback(raw_feedback):
    """
    Uses LLM only to improve language quality.
    Does NOT change content or meaning.
    """

    prompt = f"""
    Rewrite the following academic feedback in a polite,
    clear, examiner-like tone without changing the meaning.

    Feedback:
    {raw_feedback}
    """

    enhanced = call_llm(prompt)

    return enhanced.strip()
