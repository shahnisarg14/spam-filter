import os
import string
from train import p_spam, p_ham


def predict(path):
    with open(path, "r") as file:
        for line in file:
            line = pre_process(line)
            label = line.rsplit(" ", 1)[1]
            content = line.rsplit(' ', 1)[0]
            classify(content, label)


def pre_process(line):
    for c in string.punctuation:
        line = line.replace(c, " ")
        line = ''.join([i if ord(i) < 123 else '' for i in line])
    line = line.replace("\n", "")
    return line


def classify(content, label):
    is_spam = p_spam * conditional_message(content, True)
    is_ham = p_ham * conditional_message(content, False)
    if is_spam > is_ham:
        return True
    else:
        return False


def conditional_message(content, label):
    return 1

path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "english.txt"
predict(path)
