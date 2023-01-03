"""
    id посылки - 70646058


        -- ПРИНЦИП РАБОТЫ –-

    Для каждой распакованной строки ищем общий префикс - 
        пока префикс не будет равен началу строки - убираем у префикса один символ с конца
    
        -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ –-
    
    https://habr.com/ru/post/113266/

        -- ВРЕМЕННАЯ СЛОЖНОСТЬ –-

    Распаковка строки - O(n), n - число символов в строке
    Поиск префикса - O(m*n), m - число строк, n - число символов в самой большой строке

        -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    O(m), m - число символов в самой большой строке
"""
def unpack(s):
    pref = []
    res = []
    multi = []

    for ch in s:
        if(ch.isnumeric()):
          multi.append(int(ch))
          continue
        if(ch == '['):
            pref.append([])
            continue
        if(ch == ']'):
            if(len(pref) == 1):
                res.append(''.join(pref.pop()) * multi.pop())
                continue
            prev = ''.join(pref.pop())
            pref[-1].append(prev*multi.pop())
            continue
        if(len(pref) == 0):
            res.append(ch)
            continue
        pref[-1].append(ch)
    return ''.join(res)

def find_prefixes():
    n = int(input())
    pref = unpack(input())
    
    for _ in range(1, n):
        s = unpack(input())
        for i in range(len(pref)):
            if(s[i] != pref[i]):
                pref = pref[:i]
                break
    return pref
print(find_prefixes())
    
