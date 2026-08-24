from modules.braille_converter import text_to_braille


REFERENCE_DATA = [

    # ==========================================================
    # 1. LOWERCASE WORDS - 20 TESTS
    # ==========================================================

    {"text": "hello", "expected": "⠓⠑⠇⠇⠕"},
    {"text": "world", "expected": "⠺⠕⠗⠇⠙"},
    {"text": "computer", "expected": "⠉⠕⠍⠏⠥⠞⠑⠗"},
    {"text": "education", "expected": "⠑⠙⠥⠉⠁⠞⠊⠕⠝"},
    {"text": "student", "expected": "⠎⠞⠥⠙⠑⠝⠞"},
    {"text": "teacher", "expected": "⠞⠑⠁⠉⠓⠑⠗"},
    {"text": "learning", "expected": "⠇⠑⠁⠗⠝⠊⠝⠛"},
    {"text": "technology", "expected": "⠞⠑⠉⠓⠝⠕⠇⠕⠛⠽"},
    {"text": "accessibility", "expected": "⠁⠉⠉⠑⠎⠎⠊⠃⠊⠇⠊⠞⠽"},
    {"text": "platform", "expected": "⠏⠇⠁⠞⠋⠕⠗⠍"},
    {"text": "artificial", "expected": "⠁⠗⠞⠊⠋⠊⠉⠊⠁⠇"},
    {"text": "intelligence", "expected": "⠊⠝⠞⠑⠇⠇⠊⠛⠑⠝⠉⠑"},
    {"text": "braille", "expected": "⠃⠗⠁⠊⠇⠇⠑"},
    {"text": "student", "expected": "⠎⠞⠥⠙⠑⠝⠞"},
    {"text": "knowledge", "expected": "⠅⠝⠕⠺⠇⠑⠙⠛⠑"},
    {"text": "information", "expected": "⠊⠝⠋⠕⠗⠍⠁⠞⠊⠕⠝"},
    {"text": "language", "expected": "⠇⠁⠝⠛⠥⠁⠛⠑"},
    {"text": "reading", "expected": "⠗⠑⠁⠙⠊⠝⠛"},
    {"text": "writing", "expected": "⠺⠗⠊⠞⠊⠝⠛"},
    {"text": "development", "expected": "⠙⠑⠧⠑⠇⠕⠏⠍⠑⠝⠞"},


    # ==========================================================
    # 2. UPPERCASE / MIXED CASE - 20 TESTS
    # ==========================================================

    {"text": "Hello", "expected": "⠠⠓⠑⠇⠇⠕"},
    {"text": "World", "expected": "⠠⠺⠕⠗⠇⠙"},
    {"text": "Braille", "expected": "⠠⠃⠗⠁⠊⠇⠇⠑"},
    {"text": "Education", "expected": "⠠⠑⠙⠥⠉⠁⠞⠊⠕⠝"},
    {"text": "Accessibility", "expected": "⠠⠁⠉⠉⠑⠎⠎⠊⠃⠊⠇⠊⠞⠽"},
    {"text": "Computer", "expected": "⠠⠉⠕⠍⠏⠥⠞⠑⠗"},
    {"text": "Learning", "expected": "⠠⠇⠑⠁⠗⠝⠊⠝⠛"},
    {"text": "Technology", "expected": "⠠⠞⠑⠉⠓⠝⠕⠇⠕⠛⠽"},
    {"text": "Artificial", "expected": "⠠⠁⠗⠞⠊⠋⠊⠉⠊⠁⠇"},
    {"text": "Intelligence", "expected": "⠠⠊⠝⠞⠑⠇⠇⠊⠛⠑⠝⠉⠑"},
    {"text": "AI", "expected": "⠠⠁⠠⠊"},
    {"text": "PDF", "expected": "⠠⠏⠠⠙⠠⠋"},
    {"text": "AI Tutor", "expected": "⠠⠁⠠⠊ ⠠⠞⠥⠞⠕⠗"},
    {"text": "Open Your Eyes", "expected": "⠠⠕⠏⠑⠝ ⠠⠽⠕⠥⠗ ⠠⠑⠽⠑⠎"},
    {"text": "Smart Learning", "expected": "⠠⠎⠍⠁⠗⠞ ⠠⠇⠑⠁⠗⠝⠊⠝⠛"},
    {"text": "Digital Education", "expected": "⠠⠙⠊⠛⠊⠞⠁⠇ ⠠⠑⠙⠥⠉⠁⠞⠊⠕⠝"},
    {"text": "Visual Learning", "expected": "⠠⠧⠊⠎⠥⠁⠇ ⠠⠇⠑⠁⠗⠝⠊⠝⠛"},
    {"text": "AI Education", "expected": "⠠⠁⠠⠊ ⠠⠑⠙⠥⠉⠁⠞⠊⠕⠝"},
    {"text": "OpenAI", "expected": "⠠⠕⠏⠑⠝⠠⠁⠠⠊"},
    {"text": "D-AI", "expected": "⠠⠙⠤⠠⠁⠠⠊"},


    # ==========================================================
    # 3. NUMBERS - 15 TESTS
    # ==========================================================

    {"text": "1", "expected": "⠼⠁"},
    {"text": "2", "expected": "⠼⠃"},
    {"text": "3", "expected": "⠼⠉"},
    {"text": "4", "expected": "⠼⠙"},
    {"text": "5", "expected": "⠼⠑"},
    {"text": "6", "expected": "⠼⠋"},
    {"text": "7", "expected": "⠼⠛"},
    {"text": "8", "expected": "⠼⠓"},
    {"text": "9", "expected": "⠼⠊"},
    {"text": "0", "expected": "⠼⠚"},
    {"text": "12345", "expected": "⠼⠁⠼⠃⠼⠉⠼⠙⠼⠑"},
    {"text": "2026", "expected": "⠼⠃⠚⠼⠃⠋"},
    {"text": "1234567890", "expected": "⠼⠁⠼⠃⠼⠉⠼⠙⠑⠼⠋⠼⠛⠼⠓⠼⠊⠼⠚"},
    {"text": "10 students", "expected": "⠼⠁⠼⠚ ⠎⠞⠥⠙⠑⠝⠞⠎"},
    {"text": "2026 education", "expected": "⠼⠃⠚⠼⠃⠋ ⠑⠙⠥⠉⠁⠞⠊⠕⠝"},


    # ==========================================================
    # 4. PUNCTUATION - 15 TESTS
    # ==========================================================

    {"text": "Hello.", "expected": "⠠⠓⠑⠇⠇⠕⠲"},
    {"text": "Hello!", "expected": "⠠⠓⠑⠇⠇⠕⠖"},
    {"text": "Hello?", "expected": "⠠⠓⠑⠇⠇⠕⠦"},
    {"text": "Hello, world!", "expected": "⠠⠓⠑⠇⠇⠕⠂ ⠺⠕⠗⠇⠙⠖"},
    {"text": "What?", "expected": "⠠⠺⠓⠁⠞⠦"},
    {"text": "Yes; no", "expected": "⠠⠽⠑⠎⠆ ⠝⠕"},
    {"text": "Time: 10", "expected": "⠠⠞⠊⠍⠑⠒ ⠼⠁⠚"},
    {"text": "Hello - world", "expected": "⠠⠓⠑⠇⠇⠕ ⠤ ⠺⠕⠗⠇⠙"},
    {"text": "(Hello)", "expected": "⠷⠠⠓⠑⠇⠇⠕⠾"},
    {"text": "\"Hello\"", "expected": "⠶⠠⠓⠑⠇⠇⠕⠶"},
    {"text": "It's", "expected": "⠠⠊⠞⠄⠎"},
    {"text": "AI/ML", "expected": "⠠⠁⠠⠊⠌⠠⠍⠠⠇"},
    {"text": "Hello, AI!", "expected": "⠠⠓⠑⠇⠇⠕⠂ ⠠⠁⠠⠊⠖"},
    {"text": "Why?", "expected": "⠠⠺⠓⠽⠦"},
    {"text": "Yes!", "expected": "⠠⠽⠑⠎⠖"},


    # ==========================================================
    # 5. MIXED TEXT - 15 TESTS
    # ==========================================================

    {
        "text": "Hello 123",
        "expected": "⠠⠓⠑⠇⠇⠕ ⠼⠁⠼⠃⠼⠉"
    },
    {
        "text": "AI 2026",
        "expected": "⠠⠁⠠⠊ ⠼⠃⠚⠼⠃⠋"
    },
    {
        "text": "Braille 101",
        "expected": "⠠⠃⠗⠁⠊⠇⠇⠑ ⠼⠁⠚⠼⠁"
    },
    {
        "text": "Student 25",
        "expected": "⠠⠎⠞⠥⠙⠑⠝⠞ ⠼⠃⠑"
    },
    {
        "text": "Chapter 1",
        "expected": "⠠⠉⠓⠁⠏⠞⠑⠗ ⠼⠁"
    },
    {
        "text": "Chapter 10",
        "expected": "⠠⠉⠓⠁⠏⠞⠑⠗ ⠼⠁⠚"
    },
    {
        "text": "AI Tutor 2",
        "expected": "⠠⠁⠠⠊ ⠠⠞⠥⠞⠕⠗ ⠼⠃"
    },
    {
        "text": "Page 25.",
        "expected": "⠠⠏⠁⠛⠑ ⠼⠃⠑⠲"
    },
    {
        "text": "Score: 95!",
        "expected": "⠠⠎⠉⠕⠗⠑⠒ ⠼⠊⠑⠑⠖"
    },
    {
        "text": "Lesson 3?",
        "expected": "⠠⠇⠑⠎⠎⠕⠝ ⠼⠉⠦"
    },
    {
        "text": "Unit 4 - AI",
        "expected": "⠠⠥⠝⠊⠞ ⠼⠙ ⠤ ⠠⠁⠠⠊"
    },
    {
        "text": "Level 5",
        "expected": "⠠⠇⠑⠧⠑⠇ ⠼⠑"
    },
    {
        "text": "AI: 2026",
        "expected": "⠠⠁⠠⠊⠒ ⠼⠃⠚⠼⠃⠋"
    },
    {
        "text": "Test 100!",
        "expected": "⠠⠞⠑⠎⠞ ⠼⠁⠚⠚⠖"
    },
    {
        "text": "Open Your Eyes 2026",
        "expected": "⠠⠕⠏⠑⠝ ⠠⠽⠕⠥⠗ ⠠⠑⠽⠑⠎ ⠼⠃⠚⠼⠃⠋"
    },


    # ==========================================================
    # 6. EDUCATIONAL / REALISTIC TEXT - 15 TESTS
    # ==========================================================

    {
        "text": "Learning is important.",
        "expected": "⠠⠇⠑⠁⠗⠝⠊⠝⠛ ⠊⠎ ⠊⠍⠏⠕⠗⠞⠁⠝⠞⠲"
    },
    {
        "text": "Education helps students.",
        "expected": "⠠⠑⠙⠥⠉⠁⠞⠊⠕⠝ ⠓⠑⠇⠏⠎ ⠎⠞⠥⠙⠑⠝⠞⠎⠲"
    },
    {
        "text": "Technology improves learning.",
        "expected": "⠠⠞⠑⠉⠓⠝⠕⠇⠕⠛⠽ ⠊⠍⠏⠗⠕⠧⠑⠎ ⠇⠑⠁⠗⠝⠊⠝⠛⠲"
    },
    {
        "text": "Braille supports accessibility.",
        "expected": "⠠⠃⠗⠁⠊⠇⠇⠑ ⠎⠥⠏⠏⠕⠗⠞⠎ ⠁⠉⠉⠑⠎⠎⠊⠃⠊⠇⠊⠞⠽⠲"
    },
    {
        "text": "AI can help students learn.",
        "expected": "⠠⠁⠠⠊ ⠉⠁⠝ ⠓⠑⠇⠏ ⠎⠞⠥⠙⠑⠝⠞⠎ ⠇⠑⠁⠗⠝⠲"
    },
    {
        "text": "Students can read books.",
        "expected": "⠠⠎⠞⠥⠙⠑⠝⠞⠎ ⠉⠁⠝ ⠗⠑⠁⠙ ⠃⠕⠕⠅⠎⠲"
    },
    {
        "text": "Accessible content matters.",
        "expected": "⠠⠁⠉⠉⠑⠎⠎⠊⠃⠇⠑ ⠉⠕⠝⠞⠑⠝⠞ ⠍⠁⠞⠞⠑⠗⠎⠲"
    },
    {
        "text": "Digital tools improve education.",
        "expected": "⠠⠙⠊⠛⠊⠞⠁⠇ ⠞⠕⠕⠇⠎ ⠊⠍⠏⠗⠕⠧⠑ ⠑⠙⠥⠉⠁⠞⠊⠕⠝⠲"
    },
    {
        "text": "Reading builds knowledge.",
        "expected": "⠠⠗⠑⠁⠙⠊⠝⠛ ⠃⠥⠊⠇⠙⠎ ⠅⠝⠕⠺⠇⠑⠙⠛⠑⠲"
    },
    {
        "text": "Every student deserves access.",
        "expected": "⠠⠑⠧⠑⠗⠽ ⠎⠞⠥⠙⠑⠝⠞ ⠙⠑⠎⠑⠗⠧⠑⠎ ⠁⠉⠉⠑⠎⠎⠲"
    },
    {
        "text": "Learning should be accessible.",
        "expected": "⠠⠇⠑⠁⠗⠝⠊⠝⠛ ⠎⠓⠕⠥⠇⠙ ⠃⠑ ⠁⠉⠉⠑⠎⠎⠊⠃⠇⠑⠲"
    },
    {
        "text": "AI improves digital learning.",
        "expected": "⠠⠁⠠⠊ ⠊⠍⠏⠗⠕⠧⠑⠎ ⠙⠊⠛⠊⠞⠁⠇ ⠇⠑⠁⠗⠝⠊⠝⠛⠲"
    },
    {
        "text": "Braille enables independent reading.",
        "expected": "⠠⠃⠗⠁⠊⠇⠇⠑ ⠑⠝⠁⠃⠇⠑⠎ ⠊⠝⠙⠑⠏⠑⠝⠙⠑⠝⠞ ⠗⠑⠁⠙⠊⠝⠛⠲"
    },
    {
        "text": "Technology creates new opportunities.",
        "expected": "⠠⠞⠑⠉⠓⠝⠕⠇⠕⠛⠽ ⠉⠗⠑⠁⠞⠑⠎ ⠝⠑⠺ ⠕⠏⠏⠕⠗⠞⠥⠝⠊⠞⠊⠑⠎⠲"
    },
    {
        "text": "Open Your Eyes supports inclusive learning.",
        "expected": "⠠⠕⠏⠑⠝ ⠠⠽⠕⠥⠗ ⠠⠑⠽⠑⠎ ⠎⠥⠏⠏⠕⠗⠞⠎ ⠊⠝⠉⠇⠥⠎⠊⠧⠑ ⠇⠑⠁⠗⠝⠊⠝⠛⠲"
    }
]


def evaluate_braille():

    total_characters = 0
    correct_characters = 0

    total_tests = len(REFERENCE_DATA)
    passed_tests = 0

    results = []

    for item in REFERENCE_DATA:

        original_text = item["text"]
        expected = item["expected"]

        generated = text_to_braille(
            original_text
        )

        max_length = max(
            len(expected),
            len(generated)
        )

        correct = 0

        for i in range(max_length):

            expected_char = (
                expected[i]
                if i < len(expected)
                else ""
            )

            generated_char = (
                generated[i]
                if i < len(generated)
                else ""
            )

            if expected_char == generated_char:
                correct += 1

        accuracy = (
            correct / max_length * 100
            if max_length > 0
            else 100
        )

        passed = generated == expected

        if passed:
            passed_tests += 1

        total_characters += max_length
        correct_characters += correct

        results.append({
            "text": original_text,
            "expected": expected,
            "generated": generated,
            "accuracy": round(
                accuracy,
                2
            ),
            "passed": passed
        })

    overall_accuracy = (
        correct_characters /
        total_characters *
        100
        if total_characters > 0
        else 0
    )

    test_success_rate = (
        passed_tests /
        total_tests *
        100
        if total_tests > 0
        else 0
    )

    return {
        "accuracy": round(
            overall_accuracy,
            2
        ),
        "test_success_rate": round(
            test_success_rate,
            2
        ),
        "total_tests": total_tests,
        "passed_tests": passed_tests,
        "total_characters": total_characters,
        "correct_characters": correct_characters,
        "results": results
    }