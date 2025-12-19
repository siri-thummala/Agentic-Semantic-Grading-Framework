def analyze_concepts(ref_tokens, student_tokens):
    """
    Identifies covered and missing concepts based on reference tokens.
    """

    ref_set = set(ref_tokens)
    student_set = set(student_tokens)

    covered = ref_set.intersection(student_set)
    missing = ref_set.difference(student_set)

    coverage_ratio = len(covered) / len(ref_set) if len(ref_set) > 0 else 0

    return {
        "covered": list(covered),
        "missing": list(missing),
        "coverage_ratio": coverage_ratio
    }
