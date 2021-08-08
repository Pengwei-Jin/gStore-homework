from utils import post, get_answer_list_from_res
from config import predicate

def get_answer_1(company1:str, company2:str):
    sql1 = f"""
    select ?x ?y where{{
        {{
            {company1} {predicate} ?x.
            ?x {predicate} {company2}.
        }}
        UNION
        {{
            {company1} ?y {company2}.
        }}
    }}
"""
    res = post(sql1)
    answer_list_1 = get_answer_list_from_res(res, 1, company1, company2)
    sql2 = f"""
    select ?x ?y where{{
        {{
            {company2} {predicate} ?x.
            ?x {predicate} {company1}.
        }}
        UNION
        {{
            {company2} ?y {company1}.
        }}
    }}
"""
    res = post(sql2)
    answer_list_2 = get_answer_list_from_res(res, 1, company2, company1)
    answer = answer_list_1 + answer_list_2
    return answer


def get_answer_2(company:str, level:int):
    variable = list('qwertyuiopasdfghjklzxcvbnm')
    try:
        assert 1 <= level <= 26
    except:
        print('只支持层数大于等于1并且小于等于26')
        exit()
    sql = "select " + ' '.join(['?'+ variable[i] for i in range(level)]) + " where {\n"
    if level == 1:
        sql += f"{company} {predicate} ?{variable[0]}.\n"
        sql += "}"
    else:
        for i in range(level):
            if i == 0:
                sql += f"{{\n{company} {predicate} ?{variable[0]}.\n}}\nUNION\n"
            elif i == level-1:
                sql += "{\n" + '\n'.join([f"{company} {predicate} ?{variable[0]}."] + [f"?{variable[j]} {predicate} ?{variable[j+1]}." for j in range(i)]) + "\n}\n}"
            else:
                sql += "{\n" + '\n'.join([f"{company} {predicate} ?{variable[0]}."] + [f"?{variable[j]} {predicate} ?{variable[j+1]}." for j in range(i)]) + "\n}\nUNION\n"
    res = post(sql)
    answer = get_answer_list_from_res(res, 2, company)
    return answer


def get_answer_3(company1:str, company2:str):
    sql = f"""
    select ?a ?b ?c ?d where{{
        {{
            {company1} {predicate} {company2}.
            {company2} {predicate} ?a.
            ?a {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} {company2}.
            {company2} {predicate} ?a.
            ?a {predicate} ?b.
            ?b {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} {company2}.
            {company2} {predicate} ?a.
            ?a {predicate} ?b.
            ?b {predicate} ?c.
            ?c {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?d.
            ?d {predicate} {company2}.
            {company2} {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?a.
            ?a {predicate} {company2}.
            {company2} {predicate} ?d.
            ?d {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?a.
            ?a {predicate} {company2}.
            {company2} {predicate} ?d.
            ?d {predicate} ?c.
            ?c {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?d.
            ?d {predicate} ?b.
            ?b {predicate} {company2}.
            {company2} {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?a.
            ?a {predicate} ?b.
            ?b {predicate} {company2}.
            {company2} {predicate} ?d.
            ?d {predicate} {company1}.
        }}
        UNION
        {{
            {company1} {predicate} ?d.
            ?d {predicate} ?b.
            ?b {predicate} ?c.
            ?c {predicate} {company2}.
            {company2} {predicate} {company1}.
        }}
    }}
"""
    res = post(sql)
    answer = get_answer_list_from_res(res, 3, company1, company2)
    return answer