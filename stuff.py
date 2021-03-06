# Look to the slideshow in google classroom for notes
import csv

run = True


########################################################################################################################

########################################################################################################################

def open_file():
    company_db_list = []
    with open('company_db.csv') as db:
        company_db = list(csv.reader(db))
        keys = company_db[0]
        for i in company_db[1:]:
            # print(i)
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
    # print(len(tokens_s))
    if len(tokens_s) != 3 and len(tokens_s) != 7 and len(tokens_s) != 1:
        work = False
        print('Invalid, input length needs to be 3 or 7')
    if len(tokens_s) == 1:
        work = False
    elif len(tokens_s) == 3:
        if tokens_s[0] not in key_list:
            work = False
            print(f'{tokens_s[0]} is an invalid key')
        elif tokens_s[2].capitalize() not in csv_dict.get(tokens_s[0]):
            work = False
            if tokens_s[0] != 'age' and tokens_s[0] != 'salary' and tokens_s[0] != 'date':
                print('Value does not match with key')
        if tokens_s[0] == 'age' or tokens_s[0] == 'salary':
            if type(eval(tokens_s[2])) is int:
                work = True
        if tokens_s[0] == 'date':
            if len(tokens_s[2]) == 10:
                work = True
        if tokens_s[1] not in lo_op_list:
            work = False
            print('Invalid operator')
    #############################
    elif len(tokens_s) == 7:
        if tokens_s[0] not in key_list:
            work = False
            print(f'{tokens_s[0]} is an invalid key')
        elif tokens_s[2].capitalize() not in csv_dict.get(tokens_s[0]):
            work = False
            if tokens_s[0] != 'age' and tokens_s[0] != 'salary' and tokens_s[0] != 'date':
                print(f'{tokens_s[2]} does not match with {tokens_s[0]}')
        if tokens_s[0] == 'age' or tokens_s[0] == 'salary':
            if type(eval(tokens_s[2])) is int:
                work = True
        if tokens_s[0] == 'date':
            if len(tokens_s[2]) == 10:
                work = True
        if tokens_s[1] not in lo_op_list:
            work = False
            print(f'{tokens_s[1]} is an invalid operator')
        if tokens_s[4] not in key_list:
            work = False
            print(f'{tokens_s[4]} is an invalid key')
        elif tokens_s[5] not in lo_op_list:
            work = False
            print(f'{tokens_s[5]} is an invalid operator')
        elif tokens_s[6] not in csv_dict.get(tokens_s[4]):
            work = False
            if tokens_s[4] != 'age' and tokens_s[4] != 'salary' and tokens_s[4] != 'date':
                print(f'{tokens_s[6]} does not match with {tokens_s[4]}')
        if tokens_s[4] == 'age' or tokens_s[4] == 'salary':
            if type(eval(tokens_s[6])) is int:
                work = True
        if tokens_s[4] == 'date':
            if len(tokens_s[6]) == 10:
                work = True
            else:
                print('Date not formatted right, MM/DD/YYYY')
        if tokens_s[3] != 'and' and tokens_s[3] != 'or':
            work = False
            print(f'{tokens_s[3]} needs to be \'and\' or \'or\'')
    # elif len(tokens_s) == 1:
    #     if tokens_s[0].lower() == 'exit':
    #         run = False
    else:
        work = False
    if work:
        print('Valid')
        return tokens_s, work
    else:
        return tokens_s, work


def evaluations(tokens, file):
    # print(tokens)
    work_list1 = []
    work_list2 = []
    for item in file:
        # print(item.get(tokens[0]))
        if len(tokens) == 1:
            if tokens[0].lower() == 'exit':
                return False
            else:
                return True
        if len(tokens) == 3:
            if tokens[0] == 'age' or tokens[0] == 'salary':
                token_str1 = f'{item[tokens[0]]} {tokens[1]} {tokens[2]}'
                # print(token_str)
                if eval(token_str1):
                    print(item)
            elif tokens[0] == 'date':
                date_split = tokens[2].split('/')
                new_date = date_split[2] + date_split[0] + date_split[1]
                date_csv_s = item[tokens[0]].split('/')
                new_date_csv = date_csv_s[2] + date_csv_s[0] + date_csv_s[1]
                token_str2 = f'{new_date_csv} {tokens[1]} {new_date}'
                if eval(token_str2):
                    print(item)
            else:
                token_str3 = f'{item}[\'{tokens[0]}\'] {tokens[1]} \'{tokens[2].capitalize()}\''
                # print(token_str2)
                if eval(token_str3):
                    print(item)
        elif len(tokens) == 7:
            if tokens[0] == 'age' or tokens[0] == 'salary':
                token_str1 = f'{item[tokens[0]]} {tokens[1]} {tokens[2]}'
                # print(token_str)
                if eval(token_str1):
                    work_list1.append(item)
            elif tokens[0] == 'date':
                date_split = tokens[2].split('/')
                new_date = date_split[2] + date_split[0] + date_split[1]
                date_csv_s = item[tokens[0]].split('/')
                new_date_csv = date_csv_s[2] + date_csv_s[0] + date_csv_s[1]
                token_str2 = f'{new_date_csv} {tokens[1]} {new_date}'
                if eval(token_str2):
                    work_list1.append(item)
            else:
                token_str3 = f'{item}[\'{tokens[0]}\'] {tokens[1]} \'{tokens[2].capitalize()}\''
                # print(token_str2)
                if eval(token_str3):
                    work_list1.append(item)
            if tokens[3] == 'and':
                if tokens[4] == 'age' or tokens[4] == 'salary':
                    token_str4 = f'{item[tokens[4]]} {tokens[5]} {tokens[6]}'
                    if eval(token_str4):
                        if item in work_list1:
                            work_list2.append(item)
                elif tokens[4] == 'date':
                    date_split = tokens[6].split('/')
                    new_date = date_split[2] + date_split[0] + date_split[1]
                    date_csv_s = item[tokens[4]].split('/')
                    new_date_csv = date_csv_s[2] + date_csv_s[0] + date_csv_s[1]
                    token_str2 = f'{new_date_csv} {tokens[5]} {new_date}'
                    if eval(token_str2):
                        if item in work_list1:
                            work_list2.append(item)
                else:
                    token_str3 = f'{item}[\'{tokens[4]}\'] {tokens[5]} \'{tokens[6].capitalize()}\''
                    if eval(token_str3):
                        if item in work_list1:
                            work_list2.append(item)
            elif tokens[3] == 'or':
                if tokens[4] == 'age' or tokens[4] == 'salary':
                    token_str4 = f'{item[tokens[4]]} {tokens[5]} {tokens[6]}'
                    if eval(token_str4):
                        if item not in work_list1:
                            work_list2.append(item)
                elif tokens[4] == 'date':
                    date_split = tokens[6].split('/')
                    new_date = date_split[2] + date_split[0] + date_split[1]
                    date_csv_s = item[tokens[4]].split('/')
                    new_date_csv = date_csv_s[2] + date_csv_s[0] + date_csv_s[1]
                    token_str2 = f'{new_date_csv} {tokens[5]} {new_date}'
                    if eval(token_str2):
                        if item not in work_list1:
                            work_list2.append(item)
                else:
                    token_str3 = f'{item}[\'{tokens[4]}\'] {tokens[5]} \'{tokens[6].capitalize()}\''
                    if eval(token_str3):
                        if item not in work_list1:
                            work_list2.append(item)
                for val in work_list1:
                    if val not in work_list2:
                        work_list2.append(val)

    for val in work_list2:
        print(val)


while run:
    prompt = input('Enter a query: ')

    file1 = open_file()
    # print(file1)

    file2 = open_file2()
    # print(file2)

    tokens_g, eval_y_n = check_tokens(prompt, file2)

    if eval_y_n:
        evals = evaluations(tokens_g, file1)
    elif not evals:
        run = False
    # try:
    #     if not evals:
    #         run = False
    # except NameError:
    #     continue

