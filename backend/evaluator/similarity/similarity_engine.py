from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(ref_tokens, student_tokens):
    # Convert tokens back to text
    ref_text = " ".join(ref_tokens)
    student_text = " ".join(student_tokens)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([ref_text, student_text])

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return float(similarity_score[0][0])
