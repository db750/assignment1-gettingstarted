### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    if question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    if question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    if question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    if question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code":
        answer = "52a9b9b03b3e6113a89ae37772d20eee00d5fef678adbb1161dfd7a78c089684"
    if question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "34e51e4d5455479ed3a3414e78ced364ea8d4448d37690d2b8c8f7bc71cbe74a"
    if question == "Is MD5 a secured hashing algorithm? - Yes/No": 
        answer = "No"
    if question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "5"
    if question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "3"

    return answer

if __name__ == "__main__":
    questions = [
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
        "Are encoding and encryption the same? - Yes/No",
        "Is it possible to decrypt a message without a key? - Yes/No",
        "Is it possible to decode a message without a key? - Yes/No",
        "Is a hashed message supposed to be un-hashed? - Yes/No",
        "What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
        "Is MD5 a secured hashing algorithm? - Yes/No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    ]
#use this space to debug and verify that the program works
for debug_question in questions:
    print(debug_question)
    print(welcome_assignment_answers(debug_question))