def prime_num(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prost_500():
    data = []
    num = 2
    while len(data) != 500:
        if prime_num(num):
            data.append(str(num))
        num += 1
    return data


def max_dict(dictionary):
    max_value = max(dictionary.values())
    for k, v in dictionary.items():
        if v == max_value:
            max_key = k
            break
    return max_key, max_value


def naivn(string):
    dictionary = dict()
    for i in range(10, 100):
        c = 0
        a, b = str(i)[0], str(i)[1]
        for j in range(1, len(string)):
            if a == string[j - 1] and b == string[j]:
                c += 1
        dictionary[i] = c

    return max_dict(dictionary)


def rabin_carp(string):
    dictionary = dict()
    len_alphabet = 10
    for i in range(10, 100):
        curr_str = str(i)
        c = 0
        hash_str = int(curr_str[0]) * (len_alphabet ** 1) + int(curr_str[1]) * (len_alphabet ** 0)

        for j in range(1, len(string)):
            hash_curr = int(string[j - 1]) * (len_alphabet ** 1) + int(string[j]) * (len_alphabet ** 0)
            if hash_curr == hash_str:
                if curr_str[0] == string[j - 1] and curr_str[1] == string[j]:
                    c += 1
        dictionary[int(curr_str)] = c

    return max_dict(dictionary)


def boer_mur(string):
    dictionary = dict()
    for i in range(10, 100):
        a, b = str(i)[0], str(i)[1]
        c = 0
        for j in range(1, len(string)):
            a1, b1 = string[j - 1], string[j]
            if b == b1:
                if a == a1:
                    c += 1
                else:
                    if a1 in str(i):
                        continue
                    else:
                        j += 1
            else:
                if b1 in str(i):
                    continue
                else:
                    j += 2
        dictionary[i] = c

    return max_dict(dictionary)


def knut_morris_prat(string):
    dictionary = dict()
    for q in range(10, 100):
        curr_str = str(q)
        c = 0
        if curr_str[0] == curr_str[1]:
            pref_blank = [0, 1, 0]
        else:
            pref_blank = [0, 0, 0]
        i = 0
        while i < len(s):
            j = i
            while j - i < 2 and j < len(string) and curr_str[j - i] == string[j]:
                j += 1
            if j - i == 2 or j == len(string):
                c += 1
                i += 1
            else:
                step = j - i - 1 - pref_blank[j - i] + 1
                if step > 0:
                    i += j - i - 1 - pref_blank[j - i] + 1
                else:
                    i += 1
        dictionary[q] = c

    return max_dict(dictionary)


s = ''.join(prost_500())
print('Наивный алгоритм:', naivn(s))
print('Алгоритм Рабина-Карпа:', rabin_carp(s))
print('Алгоритм Бойера-Мура:', boer_mur(s))
print('Алгоритм Кнута-Морриса-Пратта:', knut_morris_prat(s))


