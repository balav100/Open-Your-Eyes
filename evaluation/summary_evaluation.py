from rouge_score import rouge_scorer
from modules.summarizer import summarize_text


SUMMARY_EVALUATION_DATA = [
    {
        "text": (
            "Artificial intelligence is a branch of computer science "
            "that focuses on creating systems capable of performing "
            "tasks that normally require human intelligence. These tasks "
            "include learning, reasoning, problem solving and understanding "
            "language."
        ),
        "reference": (
            "Artificial intelligence creates computer systems that can "
            "perform tasks requiring human intelligence such as learning, "
            "reasoning, problem solving and language understanding."
        )
    },
    {
        "text": (
            "Machine learning is a subset of artificial intelligence. "
            "It allows computers to learn patterns from data and make "
            "predictions without being explicitly programmed for every task."
        ),
        "reference": (
            "Machine learning is a part of AI that enables computers to "
            "learn patterns from data and make predictions."
        )
    },
    {
        "text": (
            "Accessibility technology helps people with disabilities "
            "interact with digital content. Screen readers, Braille "
            "displays and speech synthesis are examples of assistive "
            "technologies."
        ),
        "reference": (
            "Accessibility technology enables people with disabilities "
            "to use digital content through tools such as screen readers, "
            "Braille displays and speech synthesis."
        )
    }
]


def evaluate_summarizer():

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    rouge1_scores = []
    rouge2_scores = []
    rougeL_scores = []

    results = []

    for item in SUMMARY_EVALUATION_DATA:

        generated_summary = summarize_text(
            item["text"]
        )

        scores = scorer.score(
            item["reference"],
            generated_summary
        )

        rouge1 = scores["rouge1"].fmeasure
        rouge2 = scores["rouge2"].fmeasure
        rougeL = scores["rougeL"].fmeasure

        rouge1_scores.append(rouge1)
        rouge2_scores.append(rouge2)
        rougeL_scores.append(rougeL)

        results.append({
            "generated_summary": generated_summary,
            "rouge1": round(rouge1, 4),
            "rouge2": round(rouge2, 4),
            "rougeL": round(rougeL, 4)
        })

    avg_rouge1 = sum(rouge1_scores) / len(rouge1_scores)
    avg_rouge2 = sum(rouge2_scores) / len(rouge2_scores)
    avg_rougeL = sum(rougeL_scores) / len(rougeL_scores)

    overall_quality = (
        avg_rouge1 +
        avg_rouge2 +
        avg_rougeL
    ) / 3

    return {
        "rouge1": round(avg_rouge1, 4),
        "rouge2": round(avg_rouge2, 4),
        "rougeL": round(avg_rougeL, 4),
        "quality_percentage": round(
            overall_quality * 100,
            2
        ),
        "results": results
    }