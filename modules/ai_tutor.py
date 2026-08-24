from transformers import pipeline
from modules.braille_converter import text_to_braille


tutor_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def ask_ai_tutor(question):

    prompt = f"""
Explain clearly for a visually impaired student:

{question}
"""

    response = tutor_pipeline(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )

    return response[0]["generated_text"]


def explain_chapter(text, question):

    prompt = f"""
Based on the following text:

{text}

Answer the question clearly and accurately for a visually impaired student.

Question:
{question}
"""

    response = tutor_pipeline(
        prompt,
        max_new_tokens=150,
        do_sample=False
    )

    explanation = response[0]["generated_text"]

    braille_explanation = text_to_braille(
        explanation
    )

    return explanation, braille_explanation
