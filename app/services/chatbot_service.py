import app.startup as startup

from sklearn.metrics.pairwise import cosine_similarity


def chatbot_response(question: str):
    """
    Returns the most relevant answer from the knowledge base
    using semantic similarity.
    """

    # Convert user question into embedding
    query_embedding = startup.embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    # Calculate similarity with all stored questions
    similarities = cosine_similarity(
        query_embedding,
        startup.chatbot_embeddings
    )[0]

    # Best matching question
    best_index = similarities.argmax()

    best_match = startup.chatbot_knowledge[best_index]

    return {
        "matched_question": best_match["question"],
        "answer": best_match["answer"],
        "similarity_score": round(float(similarities[best_index]), 3)
    }