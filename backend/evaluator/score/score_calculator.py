def calculate_score(similarity_score, concept_result):
    """
    Calculates marks based on similarity and concept coverage.
    """

    # Semantic similarity marks (out of 4)
    similarity_marks = round(similarity_score * 4, 2)

    # Concept coverage marks (out of 4)
    coverage_ratio = concept_result["coverage_ratio"]
    coverage_marks = round(coverage_ratio * 4, 2)

    # Structure / grammar (simple heuristic for now)
    # Full marks if answer length is reasonable
    structure_marks = 2 if coverage_ratio > 0.5 else 1

    total_marks = round(similarity_marks + coverage_marks + structure_marks, 2)

    return {
        "similarity_marks": similarity_marks,
        "coverage_marks": coverage_marks,
        "structure_marks": structure_marks,
        "total": total_marks
    }
