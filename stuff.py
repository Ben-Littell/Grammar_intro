# Look to the slideshow in google classroom for notes
import csv

# prompt = input('Enter a query: ')


########################################################################################################################

########################################################################################################################

def open_file():
    company_db_list = []
    with open('company_db.csv') as db:
        company_db = list(csv.reader(db))
        keys = company_db[0]
        for i in company_db[1:]:
            empty_dict = {}
            for j in range(len(keys)):
                empty_dict[keys[j]] = i[j]
            company_db_list.append(empty_dict)
    return company_db_list


def check_tokens(tokens, csv_dict):
    work = True
    key_list = ['first', 'last', 'sex', 'age', 'date', 'salary', 'position']
    lo_op_list = ['<', '>', '==', '!=', '<=', '>=']
    tokens_s = tokens.split()
    if len(tokens_s) != 3 and len(tokens_s) != 7:
        work = False
    if len(tokens_s) == 3:
        if tokens_s[0] not in key_list:
            work = False
        elif tokens_s[1] not in lo_op_list:
            work = False
        elif tokens_s[2] not in csv_dict.get(tokens_s[0]):
            work = False
        if tokens_s[0] == 'age':
            if type(eval(tokens_s[2])) is int:
                work = True
    if len(tokens_s) == 7:
        if tokens_s[4] not in key_list:
            work = False
        elif tokens_s[5] not in lo_op_list:
            work = False
        elif tokens_s[6] not in csv_dict.get(tokens_s[4]):
            work = False
        if tokens_s[4] == 'age':
            if type(eval(tokens_s[6])) is int:
                work = True
    if work:
        print('Valid')
        return tokens_s
    else:
        print('Not Valid')



file = open_file()
print(file)

# tokens_g = check_tokens(prompt, file)

# def evaluations(tokens):



