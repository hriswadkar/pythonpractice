import datetime

Name = "Harshad"
Date = datetime.date.today()

letter = '''
    Dear {},
    You are selected!
    {}
    '''.format(Name, Date)

print(letter)