# 简单解析一系列字符串

####需求:

**输入**: 

```
    123asd234fgh345jkl456
```
    
**输出**: 一共6组数
    
```
    {'asd234', 
    '123asd234', 
    'fgh345', 
    '234fgh345',
     'jkl456', 
     '345jkl456'}
```      

#### 解决方案：

预处理：将字母之间的数字复制一份，并用一个标识符分隔。
        
如源码一样用lex生成token。

使用yacc书写无歧义的语法表达式即可。
处理不需要的标识符有两种方案：

```
    一种是在error中处理掉，另一种是为标识符写一个表达式
```


**Note**：

```
    我在期间遇到的最大的问题就是关于p[0]这个值的传递总是不合我心意，
    最后是阅读了《编译原理》（龙书）结合ply自带的例子及文档歪打正着写出了
    满意的语法表达式，成功生成了最简单的语法树。
```

####结果如下：

```
LexToken(NUMBER,'123',1,0)
LexToken(LETTER,'asd',1,3)
LexToken(NUMBER,'234',1,6)
LexToken(SEPARATOR,'|',1,9)
LexToken(NUMBER,'234',1,10)
LexToken(LETTER,'fgh',1,13)
LexToken(NUMBER,'345',1,16)
LexToken(SEPARATOR,'|',1,19)
LexToken(NUMBER,'345',1,20)
LexToken(LETTER,'jkl',1,23)
LexToken(NUMBER,'456',1,26)
Generating LALR tables
Node('shout', 'asd234')
Node('long', '123asd234')
Node('shout', 'fgh345')
Node('long', '234fgh345')
Node('shout', 'jkl456')
Node('long', '345jkl456')
```
