from question_class import Question

question_prompt = [
    "What is the capital of France?\n(a) Berlin\n(b) London\n(c) Paris\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n\n"
    ]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            score += 1
    print(f"You got {score} out of {len(questions)} correct.")

print("Welcome to the Quiz Game!")
run_quiz(questions)
    
       