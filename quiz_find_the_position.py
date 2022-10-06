import random
from json_converter import *


class Tools:

    def print_credentials(self, author, topic):   # PRINTS USER CREDENTIALS
        print("CREDENTIALS\nName  : %s\nTopic : %s" % (author, topic))

    def generate_report(self, total):   # GENERATES QUIZ REPORT
        print("Successfully generated ", total, "questions\n")

    def get_random_number(self):  # RANDOM NUMBER GENERATOR IN RANGE 1 TO 100
        return random.randint(1, 100)

    # ADDS THE QUESTION INTO A DICTIONARY
    def convert_question(self, choices, number_sequence, crt_answer, position):
        index = "Question " + str(question_number)
        format_to_dictionary(index,
                             "cd475300-1e30-4cc0-9c1a-55af79624af3",
                             "Jagadeesh",
                             "Not reviewed yet",
                             "NULL",
                             "The number sequence is " +
                             str(number_sequence) + ". what is the position of " +
                             str(crt_answer)+".",
                             choices,
                             "The first position is always 1",
                             position,
                             4,
                             "Find position int the number sequence")


class Quiz(Tools):
    # GETS NUMBER OF QUESTION TO BE GENERATED FROM THE USER
    def get_total_questions(self):
        self.total_questions = int(
            input("\nEnter the number of questions to be generated : "))

    # GENERATES A RANDOM NUMBER SEQUENCE
    def generate_number_sequence(self):
        self.number_sequence = []
        for i in range(0, 10):
            self.number_sequence.append(self.get_random_number())

    # CREATES A NEW QUESTION
    def create_question(self):
        self.generate_number_sequence()
        self.correct_answer = random.choice(self.number_sequence)
        # CORRECT POSITION OF THE CORRESPONDING NUMBER
        self.position = self.number_sequence.index(self.correct_answer) + 1
        self.choices = []  # ARRAY TO STORE THE CHOICES
        self.choices.append(self.position)  # APPENDING CORRECT POSITION

        for i in range(0, 3):  # BLOCK TO GENERATE ALTERNATE CHOICES
            alternate_answer = random.randrange(1, self.position + 3)
            flag = 0
            while(alternate_answer in self.choices):
                alternate_answer = random.randrange(
                    self.position-2, self.position+2)
                if(alternate_answer not in self.choices):
                    break
            self.choices.append(alternate_answer)
        random.shuffle(self.choices)  # SHUFFLES THE CHOICES
        self.convert_question(
            self.choices, self.number_sequence, self.correct_answer, self.position)


if __name__ == "__main__":  # MAINBLOCK
    quiz = Quiz()

    quiz.get_total_questions()
    quiz.total = quiz.total_questions
    question_number = 0

    while(quiz.total_questions > 0):  # RUNS UNTIL REQUIRED NUMBER OF QUESTIONS GENERATED
        question_number += 1
        quiz.create_question()  # GENERATES A SINGLE QUESTION
        quiz.total_questions -= 1

    file_name = "quiz_find_position.json"
    # CREATES A JSON FILE TO STORE ALL THE GENERATED QUESTION
    create_json(file_name)
    quiz.generate_report(quiz.total)
    # PRINTS THE CREDENTIALS OF THE AUTHOR
    quiz.print_credentials("Jagadeesh", "Find position problem")
    # PRINTS THE GENERATED QUESTIONS FROM THE JSON FILE
    print_json(file_name)
