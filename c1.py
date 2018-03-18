import requests
from bs4 import BeautifulSoup
import re


def qiushibaike():
    content = requests.get('https://www.qiushibaike.com/').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())


def demo_string():
    stra = "hello world"
    print(stra.capitalize())
    print(stra.replace('world', 'nowcoder'))
    strb = '    \n\rhello nowcoder  \r\n   '
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    strc = 'hello w'
    print(3, strc.startswith('hel'))
    print(4, strc.endswith('s'))
    print(5, stra + strb)
    print(6, len(stra))
    print(7, '-'.join(['a', 'b', 'c']))
    print(8, strc.split(' '))
    print(9, stra.find('hello'))


def demo_operation():
    print(1, 1 + 3, 5 / 2, 5 * 2, 5 - 2)
    print(2, True, not True)
    print(3, 1 < 2, 5 > 2)
    print(4, 2 << 3)
    print(5, 5 | 3, 5 & 3, 5 ^ 3)


def demo_buildfunction():
    print(1, max(2, 1), min(5, 3))
    print(2, len('xxx'), len([1, 2, 3, 4]))
    print(3, abs(-1))
    print(4, list(range(1, 10, 2)))
    print(5, dir(list))
    x = 2
    print(6, eval('x+3'))
    print(7, chr(97), ord('a'))
    print(8, divmod(10, 4))


def demo_re():
    str = '1@qq.com;22a@163.com;sk@gmail.com,;dsad@xsd@163.com;asd@16334.com;ds@qqqq.com;ds@163|qq.com'
    p1 = re.compile('[\w]+@[163|qq]\.com')
    print(1, p1.findall(str))


if __name__ == '__main__':
    # print("hello nowcoder")
    # comment
    # demo_string()
    # demo_operation()
    demo_re()
