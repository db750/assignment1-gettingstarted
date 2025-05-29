def welcome_assignment_answers(question):
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code":
        answer = "52a9b9b03b3e6113a89ae37772d20eee00d5fef678adbb1161dfd7a78c089684"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        answer = "34e51e4d5455479ed3a3414e78ced364ea8d4448d37690d2b8c8f7bc71cbe74a"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = "5"
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = "2"
    else:
        answer = "Error: Question not recognized. Check for typos."
    return answer