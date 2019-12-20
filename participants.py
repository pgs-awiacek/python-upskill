import csv
#import json
import random

with open('data/participants1.csv') as csvfile:
    readCsv = csv.reader(csvfile, delimiter=',')
    for row in readCsv:
        print(row[1], row[2])


participants = open('data/participants1.csv', 'r').readlines()
winners = random.sample(participants, 3)
print('The winners are:', winners)




#def draw_the_winners():

#    draw = random.choice(open('data/participants1.csv', 'r').readlines())
#    print(draw)

#with open('data/participants1.json') as jsonfile:
#    readJson = json.load(jsonfile)
#    print(readJson)
