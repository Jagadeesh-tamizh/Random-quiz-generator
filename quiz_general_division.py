import random
from json_converter import format_to_dictionary, create_json, print_json


class Tools:
    def print_credentials(self, name, topic):  # PRINTS AUTHOR CREDENTIALS
        print("CREDENTIALS\nName : %s\nTopic : %s" % (name, topic))

    def generate_report(self, total):  # GENERATES REPORT OF THE QUIZ
        print("\nTotal number of questions generated - ", total, "\n")


class Quiz(Tools):
    def get_requirements(self):  # GET THE REQUIREMENTS FROM THE USER
        self.difficulty = int(
            input("Enter the difficulty level from 1 to 5: "))
        self.ques = int(
            input("Enter the number of questions to be generated: "))


class Question(Quiz):
    # GENERATES PROBLEM PARAMETERS
    def generate_problem_parameters(self, difficulty):
        if(difficulty == 1):  # difficulty level - 1
            dividend = random.randrange(10, 50)
            divisor = random.randrange(1, 10)
        elif(difficulty == 2):  # difficulty level - 2
            dividend = random.randrange(100, 200)
            divisor = random.randrange(5, 15)
        elif(difficulty == 3):  # difficulty level - 3
            dividend = random.randrange(350, 400)
            divisor = random.randrange(15, 20)
        elif(difficulty == 4):  # difficulty level - 4
            dividend = random.randrange(400, 750)
            divisor = random.randrange(25, 30)
        elif(difficulty == 5):  # difficulty level - 5
            dividend = random.randrange(750, 1000)
            divisor = random.randrange(30, 40)
        # GENERATES QUIZ QUESTION BASED ON DIFFICULTY LEVEL
        self.generate_question(dividend, divisor)

    # GENERATES THE ANSWER FOR THE GENERATED PARAMETERS
    def generate_question(self, dividend, divisor):
        answer = (dividend // divisor)  # CORRECT QUOTIENT
        remainder = dividend % divisor  # REMAINDER
        self.generate_alternate_answers(
            answer, remainder, dividend, divisor)  # GENERATES CHOICES

    # GENERATES ALTERNATE ANSWERS
    def generate_alternate_answers(self, correct_answer, remain, dividend, divisor):
        # CHOICES ARE STORED IN A LIST
        alternate_answers = [correct_answer, correct_answer +
                             1, correct_answer+2, correct_answer+3]
        # REMAINDERS ARE STORED IN A LIST
        remainders = [remain, remain+1, remain+2, remain+3]
        random.shuffle(remainders)  # REMAINDERS ARE SHUFFLED
        for i in range(0, 4):
            if(alternate_answers[i] == correct_answer):
                alternate_answers[i] = correct_answer
            else:
                alternate_answers[i] = alternate_answers[i]
        random.shuffle(alternate_answers)  # CHOICES ARE SHUFFLED
        format_to_dictionary("Question "+str(question_number),  # QUESTION NUMBER
                             "cd475300-1e30-4cc0-9c1a-55af79624af3",  # AUTHOR GUID
                             "Jagadeesh",  # AUTHOR'S NAME
                             "Not reviewed yet",  # REVIEWER'S GUID
                             "karthick",  # REVIEWER NAME
                             # QUESTION
                             "What is the quotient of " + \
                             str(dividend) + " divided by "+str(divisor),
                             alternate_answers,  # ARRAY OF OPTIONS
                             "A dividend is divided by divisor",  # HINT TO THE QUESTION
                             correct_answer,  # CORRECT ANSWER
                             4,  # OPTION COUNT
                             "Find the quotient")  # QUIZ TOPIC


if __name__ == "__main__":
    quiz = Question()
    question_number = 0
    quiz.get_requirements()
    number_of_questions = quiz.ques
    total = number_of_questions
    question_number = 0  # VARIABLE TO STORE THE CURRENT QUESTION NUMBER
    while(number_of_questions > 0):  # BLOCK WHICH RUNS UNTIL REQUIRED NUMBER OF QUESTIONS GENERATED
        question_number += 1
        number_of_questions -= 1
        # GENERATES A SINGLE QUESTION WITH THE LEVEL OF DIFFICULTY PROVIDED BY THE USER
        quiz.generate_problem_parameters(quiz.difficulty)
    file_name = "quiz_general_division.json"
    create_json(file_name)
    quiz.generate_report(total)  # GENERATES THE QUIZ REPORT
    quiz.print_credentials(
        "Jagadeesh", "General division problems")  # PRINTS AUTHOR CREDENTIALS
    print_json(file_name)  # PRINTS THE GENERATED QUESTIONS FROM THE JSON FILE
