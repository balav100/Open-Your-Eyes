def calculate_overall_score(
    braille_accuracy,
    document_success,
    summary_quality,
    tutor_quality,
    audio_success
):

    overall_score = (
        braille_accuracy * 0.40
        + document_success * 0.20
        + summary_quality * 0.15
        + tutor_quality * 0.15
        + audio_success * 0.10
    )

    return round(
        overall_score,
        2
    )


def generate_evaluation_report(
    braille_accuracy,
    document_success,
    summary_quality,
    tutor_quality,
    audio_success
):

    overall_score = calculate_overall_score(
        braille_accuracy,
        document_success,
        summary_quality,
        tutor_quality,
        audio_success
    )

    return {
        "Braille Accuracy": round(
            braille_accuracy,
            2
        ),
        "Document Processing": round(
            document_success,
            2
        ),
        "Summary Quality": round(
            summary_quality,
            2
        ),
        "AI Tutor Quality": round(
            tutor_quality,
            2
        ),
        "Audio Generation": round(
            audio_success,
            2
        ),
        "Overall System Score": overall_score
    }