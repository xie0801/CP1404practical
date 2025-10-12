"""
CP1404/CP5632 Practical
Debugging exercise: fixed version of a CSV scores file program.
This code reads the scores per subject and prints the max, min, and average for each subject.
"""

def main():
    """Read and display student scores from scores file."""
    with open("scores.csv") as scores_file:
        scores_data = scores_file.readlines()

    subjects = scores_data[0].strip().split(",")
    scores_by_subject = [[] for _ in subjects]

    # Process each student's scores and assign them to the corresponding subject
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        for i, score in enumerate(score_strings):
            scores_by_subject[i].append(int(score))

    # Print the results for each subject
    for i, subject in enumerate(subjects):
        print(f"{subject} Scores:")
        print(f"Scores: {scores_by_subject[i]}")
        print(f"Max: {max(scores_by_subject[i])}")
        print(f"Min: {min(scores_by_subject[i])}")
        print(f"Average: {sum(scores_by_subject[i]) / len(scores_by_subject[i]):.2f}")
        print()


main()
