def score_annotation(relevance, accuracy, safety):
    return round((relevance + accuracy + safety) / 3, 2)


sample_score = score_annotation(0.9, 0.85, 0.95)

print(f"Annotation QA Score: {sample_score}")
