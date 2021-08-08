from gstore_code import get_answer_1, get_answer_2, get_answer_3
from utils import print_answer


def main():
    ## task1
    print('task1')
    company1 = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/深圳市楚源投资发展有限公司>'
    company2 = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/招商基金管理有限公司>'
    # company2 = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/深圳市集盛投资发展有限公司>'
    answer_1 = get_answer_1(company1, company2)
    print_answer(answer_1, short=True)
    ## task2
    print('task2')
    company = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/深圳市楚源投资发展有限公司>'
    answer_2 = get_answer_2(company, level=3)
    all_level = set([j for i in answer_2 for j in i if j != company[1:-1]])
    print('所有公司有'+str(len(all_level))+'个')
    print_answer([[i] for i in all_level], short=True)
    print('持股关系如下')
    print_answer(answer_2, short=True)
    ## task3
    print('task3')
    company1 = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/A>'
    company2 = '<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/C>'
    answer_3 = get_answer_3(company1, company2)
    if answer_3 != []:
        print('存在环形持股')
        print_answer(answer_3, short=True)
    else:
        print('不存在环形持股')


if __name__ == '__main__':
    main()