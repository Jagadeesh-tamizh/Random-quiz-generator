import random
from app import printPoly
from json_converter import create_json, format_to_dictionary, print_json


class Tools:

    def print_report(self):
        print("CREDENTIALS\nName  : %s\nTopic : %s" %
              ("Jagadeesh", "Polynomial addition"))
        print("\nTotal number of questions generated - ", total, "\n")

    def add(self, A, B, m, n):
        size = max(m, n)
        sum = [0 for i in range(size)]
        # Initialize the product polynomial
        for i in range(0, m, 1):
            sum[i] = A[i]
        # Take ever term of first polynomial
        for i in range(n):
            sum[i] += B[i]
        return sum

    # A utility function to print a polynomial
    def printPoly(self, poly, n):
        string = ""
        for i in range(n):
            string = string+str(poly[i])
            if (i != 0):
                string = string + "x^{"+str(i)+"}"
            if (i != n - 1):
                string = string + " + "
        return string


class Quiz(Tools):
    # Generate choices
    def choices(self, A, B, m, n, sum):
        global alternate_answers
        alternate_answers = []
        # alternate_answers.append(sum)
        alternate_answers.append(str(sum))
        for i in range(0, 3):
            for j in range(0, m):
                A[j] += 1
            for k in range(0, n):
                B[k] += 1
            sum = self.add(A, B, m, n)
            sum = self.printPoly(sum, size)
            alternate_answers.append(sum)
        random.shuffle(alternate_answers)

    def generateQuestion(self):
        order1 = random.randint(2, 6)
        order2 = random.randint(2, 6)
        A = []
        B = []
        for i in range(1, order1+1):
            A.append(random.randint(1, 10))
        for i in range(1, order2+1):
            B.append(random.randint(1, 10))
        m = len(A)
        n = len(B)

        question1 = self.printPoly(A, m)
        question2 = self.printPoly(B, n)
        global size
        size = max(m, n)
        sum = self.add(A, B, m, n)
        sum = self.printPoly(sum, size)
        question = "What is the sum of " + \
            str(question1)+" and "+str(question2)
        crt_answer = sum
        self.choices(A, B, m, n, sum)

        format_to_dictionary("Questions "+str(question_number),
                             "cd475300-1e30-4cc0-9c1a-55af79624af3",
                             "Jagadeesh",
                             "reviewer guid",
                             "Karthick",
                             question,
                             alternate_answers,
                             "Add the base of equivalent power",
                             crt_answer, 4,
                             "Polynomial addition")


if __name__ == '__main__':

    quiz = Quiz()
    quiz.total_questions = int(
        input("Enter the number of questions to be generated : "))
    total = quiz.total_questions
    question_number = 0

    while(quiz.total_questions > 0):
        # RUNS UNTIL REQUIRED NUMBER OF QUESTIONS GENERATED
        question_number += 1
        quiz.generateQuestion()  # GENERATES A SINGLE QUESTION
        quiz.total_questions -= 1

    quiz.print_report()
    # CREATES A JSON FILE TO STORE ALL THE GENERATED QUESTION
    file_name = "quiz_polynomial_addition.json"
    create_json(file_name)
    print_json(file_name)
