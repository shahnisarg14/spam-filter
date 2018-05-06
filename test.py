import os
import string
from train import p_spam, p_ham, train_positive, train_negative, positive_total, negative_total


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
    is_spam = p_spam * conditional_message(content, label)
    is_ham = p_ham * conditional_message(content, label)
    if is_spam > is_ham:
        return True
    else:
        return False


def conditional_message(content, label):
    result = 1.0
    tokens = content.split(" ")
    for word in tokens:
        result *= conditional(word, label)
    return result


def conditional(word, label):
    if label == "spam":
        return (train_positive.get(word, 1))/float(positive_total + len(train_positive) + len(train_negative))
    else:
        return (train_negative.get(word, 1))/float(negative_total + len(train_positive) + len(train_negative))

path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "english.txt"
predict(path)
