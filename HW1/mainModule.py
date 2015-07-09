# -*- coding:utf-8 -*-
__author__ = 'Sogo'
import csv

A1Ratings = open('A1Ratings.csv', 'r') # 21x21 Matrix
reader = csv.reader(A1Ratings)

# for row in reader:
#     print(row)

ratings = []
for i in range(21):
    ratings.append('')

for row in reader:
    # print(row[1])
    for j in range(21):
        ratings[j] += (row[j] + '|')

for cate in range(21):
    if cate is not 0:
        item = ratings[cate].split('|')
        starWars = ratings[1].split('|')
        # print(item)
        sum = 0
        count = 0
        hcount = 0
        scount = 0
        for i in range(21):
            if i is not 0:
                if item[i] is not '':
                    sum += int(item[i])
                    count = count + 1
                    if int(item[i]) >= 4:
                        hcount = hcount + 1
                if starWars[i] is not '':
                    if item[i] is not '':
                        scount = scount + 1
        # PROBLEM 1
        print(sum/count)
        # PROBLEM 2
        print(count)
        # PROBLEM 3
        print(hcount/count)
        # PROBLEM 4
        print(scount)