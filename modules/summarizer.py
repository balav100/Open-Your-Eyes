from transformers import pipeline


summarizer_pipeline = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text):

    text = text.strip()

    if not text:
        return ""

    text = text[:4000]

    input_words = len(text.split())

    if input_words < 30:

        max_length = max(
            10,
            min(50, input_words)
        )

        min_length = max(
            5,
            min(15, input_words // 2)
        )

    else:

        max_length = min(
            150,
            max(30, input_words // 2)
        )

        min_length = min(
            50,
            max(10, input_words // 4)
        )

    if min_length >= max_length:
        min_length = max(
            5,
            max_length - 5
        )

    summary = summarizer_pipeline(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]
