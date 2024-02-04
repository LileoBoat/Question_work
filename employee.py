from Question import Question

question_prompt = [
    "What is the best overall phone?\n(a) S24 ultra\n(b) iphone 15 pro max\n(c) google pixel 8 pro\n\n: ",
    "What is the best camera phone phone?\n(a) iphone 15 pro max\n(b) google pixel 8 pro\n(c) S24 ultra\n\n: ",
    "What is the best designed phone?\n(a) google pixel 8 pro\n(b) S24 ultra\n(c) iphone 15 pro max\n\n: ",
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You had {score} / {len(questions)} correctly")

run_test(questions)