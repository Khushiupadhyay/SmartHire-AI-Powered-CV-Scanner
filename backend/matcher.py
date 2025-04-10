from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_score(jd_summary, cv_data):
    # Make the comparison richer and case-insensitive
    jd_text = jd_summary.lower()
    cv_text = f"{cv_data['text']} {cv_data['name']} {cv_data['email']}".lower()

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([jd_text, cv_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)
