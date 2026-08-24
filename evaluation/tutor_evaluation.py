from sentence_transformers import SentenceTransformer
from modules.ai_tutor import explain_chapter


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


TUTOR_EVALUATION_DATA = [
    {
        "context": (
            "Machine learning is a subset of artificial intelligence "
            "that enables computers to learn patterns from data."
        ),
        "question": "What is machine learning?",
        "reference": (
            "Machine learning is a part of artificial intelligence "
            "that allows computers to learn patterns from data."
        )
    },
    {
        "context": (
            "Braille is a tactile writing system used by people who "
            "are blind or visually impaired. It represents letters "
            "and symbols using raised dots."
        ),
        "question": "What is Braille?",
        "reference": (
            "Braille is a tactile writing system that uses raised "
            "dots to represent letters and symbols for people who "
            "are blind or visually impaired."
        )
    },
    {
        "context": (
            "Artificial intelligence enables computer systems to "
            "perform tasks that normally require human intelligence."
        ),
        "question": "What is artificial intelligence?",
        "reference": (
            "Artificial intelligence allows computers to perform "
            "tasks that normally require human intelligence."
        )
    }
]


def calculate_similarity(
    generated_answer,
    reference_answer
):

    embeddings = embedding_model.encode(
        [
            generated_answer,
            reference_answer
        ]
    )

    similarity = (
        embeddings[0] @ embeddings[1]
    ) / (
        (embeddings[0] @ embeddings[0]) ** 0.5
        *
        (embeddings[1] @ embeddings[1]) ** 0.5
    )

    return float(similarity)


def evaluate_tutor():

    similarity_scores = []

    results = []

    for item in TUTOR_EVALUATION_DATA:

        question = item["question"]

        context = item["context"]

        reference = item["reference"]

        try:

            explanation, _ = explain_chapter(
                context,
                question
            )

            similarity = calculate_similarity(
                explanation,
                reference
            )

            similarity_scores.append(
                similarity
            )

            results.append({
                "question": question,
                "generated_answer": explanation,
                "reference_answer": reference,
                "similarity": round(
                    similarity,
                    4
                )
            })

        except Exception as e:

            results.append({
                "question": question,
                "error": str(e),
                "similarity": 0
            })

            similarity_scores.append(0)

    if similarity_scores:

        average_similarity = (
            sum(similarity_scores)
            / len(similarity_scores)
        )

    else:

        average_similarity = 0

    return {
        "semantic_similarity": round(
            average_similarity,
            4
        ),
        "quality_percentage": round(
            average_similarity * 100,
            2
        ),
        "results": results
    }