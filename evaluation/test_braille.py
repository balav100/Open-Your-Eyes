import sys
from pathlib import Path

# Ensure project root is in sys.path when running script directly
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from evaluation.braille_evaluation import evaluate_braille


def main():

    result = evaluate_braille()

    print("\n" + "=" * 60)
    print("BRAILLE CONVERSION EVALUATION")
    print("=" * 60)

    print(
        f"\nCharacter Accuracy: "
        f"{result['accuracy']:.2f}%"
    )

    print(
        f"Test Success Rate: "
        f"{result['test_success_rate']:.2f}%"
    )

    print(
        f"Tests Passed: "
        f"{result['passed_tests']}/"
        f"{result['total_tests']}"
    )

    print(
        f"Correct Characters: "
        f"{result['correct_characters']}/"
        f"{result['total_characters']}"
    )

    print("\n" + "-" * 60)
    print("INDIVIDUAL TEST RESULTS")
    print("-" * 60)

    for item in result["results"]:

        status = (
            "PASS"
            if item["passed"]
            else "FAIL"
        )

        print(
            f"\n{status}"
            f" | Text: {item['text']}"
        )

        print(
            f"  Expected : {item['expected']}"
        )

        print(
            f"  Generated: {item['generated']}"
        )

        print(
            f"  Accuracy : "
            f"{item['accuracy']:.2f}%"
        )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()