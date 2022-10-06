import json  # IMPORTS JSON MODULE


dict1 = {}  # DICTIONARY TO HOLD THE QUESTIONS DATA

# METHOD TO FORMAT THE QUESTIONS INTO A DICTIONARY


def format_to_dictionary(question_number,  # QUESTION NUMBER
                         author_GUID,  # AUTHOR GUID
                         author_name,  # AUTHOR'S NAME
                         reviewer_GUID,  # REVIEWER'S GUID
                         reviewer_name,  # REVIEWER NAME
                         question,  # QUESTION
                         options,  # ARRAY OF OPTIONS
                         hint,  # HINT TO THE QUESTION
                         correct_answer,  # CORRECT ANSWER
                         option_count,  # OPTION COUNT
                         topic):  # QUESTION TOPIC
    '''
        This function formatts the data into a dictionary
        List Of Parameters
        Question_number     - String
        author_GUID         - String
        author_name         - String
        reviewer_GUID       - String
        reviewer_name       - String
        question            - LaTex Formatted String
        options             - List
        hint                - String
        correct_answer      - Integer
        option_count        - Integer
        topic               - String
    '''
    dict1["Author of below question"] = author_name
    dict1["topic"] = topic
    data = {
        "content": question,
        "answer": [],
        "hint": hint,
        "credits": {
            "author": {
                "id": author_GUID,
                "name": author_name
            },
            "reviewer": {
                "id": reviewer_GUID,
                "name": reviewer_name
            }
        }
    }

    for i in range(option_count):
        answer_dict = {}
        answer_dict["id"] = i+1
        answer_dict["value"] = (options[i])
        if(options[i] == correct_answer):
            answer_dict["is_key"] = True
        else:
            answer_dict["is_key"] = False
        data["answer"].append(answer_dict)
    dict1[question_number] = data


def create_json(filename):
    out_file = open(filename, "w")  # CREATES OR JSON FILE
    json.dump(dict1, out_file, indent=6)  # DUMPS DICTIONARY INTO THE JSON FILE
    out_file.close()  # CLASES THE JSON FILE


def print_json(file_name):
    # Opening JSON file
    f = open(file_name)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data:
        print(i)
        print(data[i])

    # Closing file
    f.close()
