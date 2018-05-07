import string
from train import test_data, p_spam, p_ham, train_positive, train_negative, positive_total, negative_total


def predict(test_data):
    global spam_prediction, ham_prediction
    for line in test_data:
        line = pre_process(line)
        label = line.rsplit(" ", 1)[1]
        content = line.rsplit(' ', 1)[0]
        if classify(content, label):
            spam_prediction += 1
        else:
            ham_prediction += 1


def pre_process(line):
    for c in string.punctuation:
        line = line.replace(c, " ")
        line = ''.join([i if ord(i) < 123 else '' for i in line])
    line = line.replace("\n", "")
    return line


def classify(content, label):
    is_spam = p_spam * conditional_message(content, label)
    is_ham = p_ham * conditional_message(content, label)
    print is_spam, is_ham
    if is_spam > is_ham:
        return True
    else:
        return False


def conditional_message(content, label):
    result = 1.0
    tokens = content.split(" ")
    for word in tokens:
        word = word.lower()
        result *= conditional(word, label)
    return result


def conditional(word, label):
    if label == "spam":
        return (train_positive.get(word, 1))/float(positive_total)
    else:
        return (train_negative.get(word, 1))/float(negative_total)

spam_prediction = 0
ham_prediction = 0
predict(test_data)
print spam_prediction, ham_prediction
