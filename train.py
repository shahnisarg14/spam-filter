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
            process(content, label)
            total_count += 1
            if label == "spam":
                s_count += 1
    return s_count, total_count-s_count


def pre_process(line):
    for c in string.punctuation:
        line = line.replace(c, " ")
        line = ''.join([i if ord(i) < 123 else '' for i in line])
    line = line.replace("\n", "")
    return line


def process(content, label):
    global positive_total, negative_total
    for word in content:
        if label == "spam":
            train_positive[word] = train_positive.get(word, 0) + 1
            positive_total += 1
        else:
            train_negative[word] = train_negative.get(word, 0) + 1
            negative_total += 1

train_positive = {}
train_negative = {}
positive_total = 0
negative_total = 0
path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "english_big.txt"
spam_count, ham_count = get_count(path)
p_spam = spam_count/float(spam_count + ham_count)
p_ham = ham_count/float(spam_count + ham_count)
