def generate_feedback(score_breakdown, missing_concepts):
    """
    Generates human-readable feedback based on marks and missing concepts.
    """

    feedback_parts = []

    # Overall performance comment
    total = score_breakdown["total"]

    if total >= 8:
        feedback_parts.append("Very good answer with strong conceptual understanding.")
    elif total >= 6:
        feedback_parts.append("Good answer, but there are some missing points.")
    elif total >= 4:
        feedback_parts.append("The answer shows partial understanding of the topic.")
    else:
        feedback_parts.append("The answer lacks key concepts and clarity.")

    # Concept-based feedback
    if missing_concepts:
        missing_str = ", ".join(missing_concepts)
        feedback_parts.append(
            f"You did not adequately cover the following key concepts: {missing_str}."
        )

    # Structure / clarity feedback
    if score_breakdown["structure_marks"] < 2:
        feedback_parts.append(
            "The answer structure and clarity can be improved."
        )

    return " ".join(feedback_parts)
