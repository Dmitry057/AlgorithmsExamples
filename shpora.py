
"""
    id посылки - 70645307	


        -- ПРИНЦИП РАБОТЫ –-
    1. Для каждого слова создаем префиксное дерево. 
        (terminal - длина слова в ноде)
    2. Создаем dp, в которой будем проверять, можно ли создать строку с данным индексом или нет
        
        Проходимся по префиксному дереву и когда встречаем терминальный узел и при этом,
        ответ положительный и для строки без текущего рассматриваемого слова,
        тогда записываем в массив True, иначе False

        T.E - в строке 'shpora' и двух словах 'shp' 'ora' буллевые значения dp будут указывать на окончание (если оно есть)
        этих слов - 
        
                 s      h     p      o      r      a
        [True, False, False, True, False, False, True],

        Соотв. поиск слов будет происходить только со значений True, что существенно увеличивает скорость работы алгоритма
        (поиск следующего слова происходит с 0 элемента либо с конца найденного слова)

        -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ –-
    
    https://habr.com/ru/post/113266/

        -- ВРЕМЕННАЯ СЛОЖНОСТЬ –-

    Создание префиксного дерева - O(n), n - суммарная длина всех слов
    Поиск слов с помощью префиксного дерева - O(m**2), m - длина строки

        -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Преф. дерево - O(n), n - суммарная длина всех слов
    Dp - O(m), m - длина строки
"""

from collections import defaultdict
class Node:
    def __init__(self, next=None):
        self.next = defaultdict(Node) if not next else next 
        self.terminal = False

def create_tree(words):
    root = Node()
    for word in words:
        node = root
        for char in word:
            node = node.next[char]
        node.terminal = len(word)
    return root
def is_split_words(s, words):
    root = create_tree(words)
    dp = [True] + [False]*len(s)
    for i in range(len(s)):
        node = root
        if(dp[i]):
            for j in range(i, len(s)+1):
                if(node.terminal):
                    dp[j] = True
                if(j == len(s) or not s[j] in node.next):
                    break
                node = node.next[s[j]]
    return dp[-1]
s = input()
words = [input() for _ in range(int(input()))]
if(is_split_words(s, words)):
    print('YES')
else:
    print('NO')

