import csv
with open('eggs.csv', 'w+') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    spamwriter.writerow(['Spam', 'test'])
    spamwriter.writerows([['Spam'], ['test']])
