print("\n ---Mini Quiz---")


def run_quiz():
    questions = {
        'What is the name of england captain? ': 'kane',
        'What is the name of nigeria captain? ' : 'ndidi',
        'What is the name of chelsea captain? ' : 'james',
        'What is the name of tottenham captain? ' : 'romero'
    }
    all_questions = len(questions)
    scores = 0

    for question, ans in questions.items():
        user_answer = input(question).lower()
        if user_answer == ans:
            scores += 1
        else:
            print(f"wrong answer, the answer is {ans}")
    print(f"\n Quiz Completed!!")
    print(f"\n Your total score is {scores}")

    percentage = (scores/all_questions) * 100

    if percentage == 100:
        print("\nExcellent you are a genius!!")
    elif percentage >= 70:
        print("\nGreat job!!")
    elif percentage >= 50:
        print("\nPassed")
    elif percentage < 49:
        print("\nFailed...")

run_quiz()