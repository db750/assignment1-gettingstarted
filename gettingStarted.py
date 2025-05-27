
if question == "Are encoding and encryption the same? - Yes/No":
 answer = "No"
elif question == "Is it possible to decrypt a message without a key? - Yes/No":
 answer = "No"
 else: 
### you should understand why this else case should be included
### what happens if there is a typo in one of the questions?
### maybe put something here to flag an issue and catch errors
answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
return(answer)
# Complete all the questions.


if __name__ == "__main__":
#use this space to debug and verify that the program works
debug_question = "Are encoding and encryption the same? - Yes/No"
answer = 'No'
print(welcome_assignment_answers(debug_question))

def welcome_assignment_answers(question):
#Questions:
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

return (question, answer)
