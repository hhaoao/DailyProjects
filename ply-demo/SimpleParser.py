import ply.lex as lex
import ply.yacc as yacc
import re


# 封装token，语法表达式
class NumberFile:
    def __init__(self):
        self.lexer = None
    # 注意：token跟语法表达式一起
    tokens = (
        'NUMBER', 'LETTER', 'SEPARATOR',
    )

    t_NUMBER = r'\d+'
    t_LETTER = r'[a-zA-Z]+'
    t_SEPARATOR = r'\|'

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # 构建词法分析器
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # 生成token
    def test(self, raw_data):
        self.lexer.input(raw_data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    # 语法分析
    # precedence处理相同规则时是归约还是步进，这里我先归约（主要消除警告）默认是步进但有警告，
    # Tip:可以注释一下，看parser.out的警告。

    precedence = (
        ('right', 'USEPARATOR'),
    )
    def p_expression_long(self, p):
        """expressions : NUMBER expression"""
        p[0] = p[2] + [Node('long', p[1] + p[2][0].children)]

    def p_expression_shout(self, p):
        """expression : LETTER NUMBER"""
        p[0] = [Node('shout', p[1] + p[2])]

    def p_expression_long_separator_long(self, p):
        """expressions : expressions SEPARATOR expressions %prec USEPARATOR"""
        p[0] = p[1] + p[3]

    def p_error(self, p):
        # 这里暂时找不到较好的处理方式SEPARATOR标识符
        if p.type == 'SEPARATOR':
            yaccer.restart()
        else:
            print('syntax error at "%s"' % p.value)


# 语法树
class Node:
    """leaf:'long' or 'shout
    children:string"""
    def __init__(self, leaf, children=None):
        self.type = leaf
        if children:
            self.children = children
        else:
            self.children = None

    def __repr__(self):
        return "Node(%r, %r)" % (self.type, self.children)


# 字符串预处理
def pretreatment(format_data):
    """由于yacc无回退操作，这里设置一个标志符复制原number代替回退操作，
    return: str"""
    d_data = re_str(format_data)
    while d_data:
        format_data = format_data[:d_data.end()] + '|' + d_data.group() + format_data[d_data.end():]
        d_data = re_str(format_data)
        # print(format_data)

    return format_data


def re_str(data_string):
    """return: 搜索前后都含字母的数字"""
    return re.search(r'(?<=[a-zA-Z])\d+(?=[a-zA-Z])', data_string)


def tests(obj, test_data):
    """打印生成的token
    return: token"""
    obj.test(test_data)


if __name__ == '__main__':
    raw_data = '123asd234fgh345jkl456'
    data = pretreatment(raw_data)
    m = NumberFile()
    m.build()
    tests(m, data)
    yaccer = yacc.yacc(module=m)
    # a = yaccer.parse(data, debug=True)
    a = yaccer.parse(data)
    for i in a:
        print(i)

