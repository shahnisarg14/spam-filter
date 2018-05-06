import os
import string


def get_count(path):
    s_count = 0
    total_count = 0
    with open(path, "r") as file:
        for line in file:
            line = pre_process(line)
            label = line.rsplit(" ", 1)[1]
            content = line.rsplit(' ', 1)[0]
            process(content)
            total_count += 1
            if label == "spam":
                s_count += 1
    return s_count, total_count-s_count


def pre_process(line):
    for c in string.punctuation:
        line = line.replace(c, " ")
        line = ''.join([i if ord(i) < 123 else '' for i in line])
    line = line.replace("\n", "")
    print line
    return line


def process(content):
    print content # Process the content here

path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "english_big.txt"
spam_count, ham_count = get_count(path)
p_spam = spam_count/float(spam_count + ham_count)
p_ham = ham_count/float(spam_count + ham_count)

print p_spam, p_ham
