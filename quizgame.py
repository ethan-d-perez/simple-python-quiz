import questiongloss as q
import random

questions = q.questions
answers = q.answers
correct_answers = q.correct_answers

groups = q.groups

print("---------------------------")
print("Welcome to a Pop Quiz game made with Python!")
print("---------------------------")

def max_questions():
    desired_ans = False
    while desired_ans == False:
        try:
            max_questions = int(input(f"How many questions, from 1 to {len(questions)}, do you want to answer? "))
        except ValueError:
            print(f"Please only type in a whole number from 1 to {len(questions)}.")
            print("---------------------------")
        else:
            if max_questions > len(questions) or max_questions <= 0:
                print(f"There are only {len(questions)} questions to answer. Please pick a number between 1 and {len(questions)}.")
                print("---------------------------")
            else:
                print("---------------------------")
                desired_ans = True
                quiz(max_questions)


def quiz(m_questions):
    question_number = 1
    correct = 0
    incorrect = 0

    quiz_answers = []
    guessed_answers = []

    random.shuffle(groups)
    for group in groups:
        print(f"Question {question_number}:")
        print(questions[group])
        print(answers[group])

        user_answer = input("Enter either A, B, C, or D: ").upper()
        guessed_answers.append(user_answer)
        if user_answer == correct_answers[group]:
            print(f"Correct! The answer is {correct_answers[group]}!")
            correct += 1
        else:
            print(f"Incorrect! The answer was {correct_answers[group]}.")
            incorrect += 1

        print("---------------------------")
        quiz_answers.append(correct_answers[group])
        question_number += 1

        if question_number > m_questions:
            end_quiz(correct, incorrect, quiz_answers, guessed_answers)

def end_quiz(c_answers, i_answers, q_answers, g_answers):

    print(f"You finished the quiz! You got {c_answers} questions correct and {i_answers} questions incorrect!")
    print(f"The correct answers are: {q_answers}")
    print(f"Your guessed answers are: {g_answers}")

    desired_ans = False
    while desired_ans == False:
        playagain = input("Do you want to play again? Type 'yes' to reset the quiz. Type 'no' to end the quiz. ")
        if "yes" in playagain:
            desired_ans = True
            print("---------------------------")
            max_questions()
        elif "no" in playagain:
            desired_ans = True
            print("Goodbye!")
            quit()
        else:
            print("Please respond with either 'yes' or 'no,' nothing else.")

max_questions()