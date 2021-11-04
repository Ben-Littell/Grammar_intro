# Look to the slideshow in google classroom for notes
import csv

prompt = input('Enter a query: ')


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
    # print(company_db_list[0])
    return company_db_list


def open_file2():
    company_db_dict = {}
    list1 = []
    list2 = []
    file_row_numb = 0
    with open('company_db.csv') as db:
        company_db = csv.reader(db)
        line1 = db.readline()
        lines = db.readlines()[1:]
        keys = []
        line1_len = len(line1.split(','))
        for i in line1.split(','):
            company_db_dict[i.strip()] = []
            keys.append(i.strip())
        # print(keys)
        for row in lines:
            for j in range(line1_len):
                # print(j)
                company_db_dict[keys[j]].append(row.split(',')[j].strip())
    return company_db_dict


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
            print(f'{tokens_s[0]} is an invalid key')
        elif tokens_s[1] not in lo_op_list:
            work = False
        elif tokens_s[2].capitalize() not in csv_dict.get(tokens_s[0]):
            work = False
        if tokens_s[0] == 'age' or tokens_s[0] == 'salary':
            if type(eval(tokens_s[2])) is int:
                work = True
    if len(tokens_s) == 7:
        if tokens_s[4] not in key_list:
            work = False
        elif tokens_s[5] not in lo_op_list:
            work = False
        elif tokens_s[6] not in csv_dict.get(tokens_s[4]):
            work = False
        if tokens_s[4] == 'age' or tokens_s[4] == 'salary':
            if type(eval(tokens_s[6])) is int:
                work = True
        else:
            work = False
    if work:
        print('Valid')
        return tokens_s


def evaluations(tokens, file):
    for item in file:
        # print(item.get(tokens[0]))
        if len(tokens) == 3:
            if tokens[0] == 'age' or tokens[0] == 'salary':
                token_str1 = f'{item[tokens[0]]} {tokens[1]} {tokens[2]}'
                # print(token_str)
                if eval(token_str1):
                    print(item)
            else:
                token_str2 = f'{item[tokens[0]]} {tokens[1]} {tokens[2]}'
                if eval(token_str2):
                    print(item)


file1 = open_file()
# print(file)

file2 = open_file2()
# print(file2)

tokens_g = check_tokens(prompt, file2)

evaluations(tokens_g, file1)
