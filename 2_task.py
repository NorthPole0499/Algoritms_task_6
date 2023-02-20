import timeit
import wikipediaapi
from docx import Document

s = ['\n', '–', '.', '...', ':', '\"', '\"', '!', '@', '#', '№', '$', ';', '%', '^', '?', '&', '*', '(', ')', '[', ']',
     '{', '}', '<', '>', '/', '|', '-', '—', '\t', ' ']


def get_text_from_doc(filename):
    doc = Document(filename)
    text = []
    for p in doc.paragraphs:
        for i in p.text.split():
            word = i
            if word:
                for j in s:
                    word = word.strip(j)
                if word:
                    text.append(word)
    return text


def get_text_from_wiki(page_name):
    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    p_wiki = wiki_wiki.page(page_name)
    text = []
    for i in p_wiki.text.split():
        word = i
        if word:
            for j in s:
                word = word.strip(j)
            if word:
                text.append(word)
    return text


plag, res = 0, 0
report, wiki = get_text_from_doc('Научный метод.docx'), get_text_from_wiki('Научный метод')
for word in report:
    res += len(word)
start = timeit.default_timer()
for i in range(len(report) - 2):
    ex_report = ''.join(report[i:i + 3])
    for j in range(len(wiki) - 3):
        ex_wiki = ''.join(wiki[j:j + 3])
        if ex_wiki == ex_report:
            plag += len(ex_report)
print(f'Наивный алгоритм: {timeit.default_timer() - start}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

alphabet = list(set(wiki))
plag = 0
ex_wiki_hashes = []
start = timeit.default_timer()
for j in range(len(wiki) - 3):
    ex_wiki = wiki[j:j + 3]
    ex_wiki_hashes.append(sum([alphabet.index(ex_wiki[i]) * len(alphabet) ** (2 - i) for i in range(3)]))
for i in range(len(report) - 2):
    ex_report = report[i:i + 3]
    hash_ex_report = sum(
        [alphabet.index(ex_report[i]) * len(alphabet) ** (2 - i) for i in range(3) if ex_report[i] in alphabet])
    if hash_ex_report in ex_wiki_hashes:
        for j in range(len(ex_wiki_hashes)):
            hash_ex_wiki = ex_wiki_hashes[j]
            if hash_ex_report == hash_ex_wiki:
                if ''.join(ex_report) == ''.join(wiki[j:j + 3]):
                    plag += len(''.join(ex_report))

print(f'Алгоритм Рабина-Карпа: {timeit.default_timer() - start}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

plag = 0
start = timeit.default_timer()
for i in range(len(report) - 3):
    ra, rb, rc = report[i:i + 3]
    for j in range(len(wiki) - 3):
        wa, wb, wc = wiki[j:j + 3]
        if wc == rc:
            if wb == rb:
                if wa == ra:
                    plag += len(''.join([ra, rb, rc]))
                else:
                    continue
            elif wb == ra:
                continue
            else:
                j += 1
        elif wc == rb:
            continue
        elif wc == ra:
            j += 1
        else:
            j += 2
print(f'Алгоритм Бойера-Мура: {timeit.default_timer() - start}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')

plag = 0
start = timeit.default_timer()
for i in range(len(report) - 3):
    ex_report = report[i:i + 3]
    prefix = [0, 0, 0]
    if ex_report[0] == ex_report[1]:
        prefix[1] += 1
        prefix[-1] += 1
    if ex_report[0] == ex_report[-1]:
        prefix[-1] += 1
    for j in range(len(wiki) - 3):
        ex_wiki = wiki[j:j + 3]
        if ''.join(ex_wiki) == ''.join(ex_report):
            plag += len(''.join(ex_report))
        elif ex_wiki[0] == ex_report[0]:
            if ex_wiki[1] == ex_report[1]:
                j += 2 - prefix[-1]
            else:
                j += 1 - prefix[1]
        else:
            continue
print(f'Алгоритм Кнута-Морриса-Пратта: {timeit.default_timer() - start}с')
print(f'Процент плагиата – {round(plag / res * 100, 2)}%')