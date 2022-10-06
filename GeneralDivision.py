import random  # import random module for random value generation


class credentials:  # USER CREDENTIALS ARE GENERATED USING THE CLASS "credentials"
    def print_user_credentials(name, topic):  # Method to print user credentials
        print("CREDENTIALS\nName : %s\nTopic : %s" % (name, topic))


class quiz_requirements:  # QUIZ REQUIREMENTS ARE OBTAINED FROM THE USER USING THE CLASS "quiz_requirements"
    # Get difficulty level from user input
    difficulty = int(input("Enter the difficulty level from 1 to 5: "))
    # Get number of questions from user input
    ques = int(input("Enter the number of questions to be generated: "))
    print("\n")


class random_division_problem():  # GENERATING QUESION PARAMETERS BASED ON THE DIFFICULTY LEVEL
    # Method to initialise divisor and dividend
    def generate_problem_parameters(self, diff):
        if(diff == 1):  # difficulty level - 1
            dividend = random.randrange(10, 50)
            divisor = random.randrange(1, 10)
        elif(diff == 2):  # difficulty level - 2
            dividend = random.randrange(100, 200)
            divisor = random.randrange(5, 15)
        elif(diff == 3):  # difficulty level - 3
            dividend = random.randrange(350, 400)
            divisor = random.randrange(15, 20)
        elif(diff == 4):  # difficulty level - 4
            dividend = random.randrange(400, 750)
            divisor = random.randrange(25, 30)
        elif(diff == 5):  # difficulty level - 5
            dividend = random.randrange(750, 1000)
            divisor = random.randrange(30, 40)

        # Calling "generate_question method" in the class "question"
        question.generate_question(dividend, divisor)


class question():
    def generate_question(dividend, divisor):
        answer = (dividend//divisor)  # compute and store the quotient
        remainder = dividend % divisor  # compute and store the remainder
        print("\nWhat is the quotient of ", dividend, " divided by ", divisor)
        # Generate choices from the classs "choices"
        choices.generate_choices(answer, remainder)

        try:
            if(number_of_questions == 0):
                # Promt to finish the quiz
                input("Press enter to finish the quiz\n\n\n")
            else:
                # Block to prompt for next question
                input("Press enter to move to next question...")
        except SyntaxError:
            pass


class choices():  # CLASS TO GENERATE THE CHOICES
    def generate_choices(ans, remain):
        global crt_answers
        answers = [ans, ans+1, ans+2, ans+3]  # list storing possible choices
        # list storing possible remainders
        remainders = [remain, remain+1, remain+2, remain+3]
        random.shuffle(answers)  # shuffle quotients list
        random.shuffle(remainders)  # shuffle remainders list

        print("The options are\n")
        j = 1
        for i in answers:  # block to print the choices
            if(i == ans):
                correct_option = j
                print(j, ") Quotient is ", i, " and remainder ", remain, "\n")
            else:
                print(j, ") Quotient is ", i, " and remainder ",
                      random.choice(remainders), "\n")
            j += 1

        # get user response to the generated question
        choice = int(input("Enter the correct option: "))
        if(choice == correct_option):
            print("\nAwesome it is the correct option!!!\n")
            crt_answers = crt_answers + 1  # increment the value of correctly answered questions

        else:
            print("\nNooo!!!, the option", correct_option, " is correct",
                  "with quotient ", ans, " and remainder ", remain)


class quiz_report():  # CLASS TO GENERATED THE QUIZ REPORT
    def generate_report(total, crt):
        print("Total number of questions - ", total,
              "\nNumber of questions answered correctly - ", crt, "\n")


requirements = quiz_requirements()  # call the quiz requirements class

number_of_questions = requirements.ques
total = number_of_questions
crt_answers = 0
difficulty = requirements.difficulty
quiz = random_division_problem()

while(number_of_questions > 0):
    number_of_questions -= 1
    # generate the problem statements
    quiz.generate_problem_parameters(difficulty)

quiz_report.generate_report(total, crt_answers)  # generate quiz report details
# print the credentials of the quiz owner
credentials.print_user_credentials("Jagadeesh", "General division problems")
