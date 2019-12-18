import csv
import numpy as np

questions = [
    5,
    6,
    7,
    8,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
]

def make_dic(csv_lists):
    dic = {}
    for i, sbj in enumerate(csv_lists):
        if i == 0:
            continue

        dic[sbj[2]] = sbj

    return dic

def select_questions(q_list):
    out_list = []
    for q in questions:
        out_list.append(float(q_list[q]))

    return np.array(out_list)

def main():
    evalu = None
    with open('Evaluation2018.csv') as f:
        evalu = [row for row in csv.reader(f)]

    raw_subjects = make_dic(evalu)
    subjects = {}
    for k, v in raw_subjects.items():
        subjects[k] = select_questions(v)

    print(subjects)

    title_value = {}
    for k, v in subjects.items():
        title_value[k] = np.sum(v)

    title_value = sorted(title_value.items(), key=lambda x:x[1])

    for i, sbj in enumerate(title_value[:10]):
        print("{0}位: <u>{1}</u>\n　　回答者数: {2},\t値: {3}".format(i+1, sbj[0], raw_subjects[sbj[0]][4], sbj[1]))

if __name__ == "__main__":
    main()