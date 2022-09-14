
from random import randint
from os import system
import time

class Var:
    word_len  = 0
    space_word = False
    letter_inside = ""
    position_of_letter = 0
    letter = "k"
    word = ""
    num_of_letter = 1

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_into_file(path,x):
    f = open(path, "w")
    f.write(str(x))
    f.close

def count_char(s,c):
    idx = 0
    for i in range(len(s)):
        if s[i] != c:
            idx = idx + 1
    return (idx)

def get_letter(s,c):
    idx = 0
    w = ""
    for i in range(len(s)):
        if s[i] != c:
            w = w + s[i]
    return (w)


def get_pos(word):
    pos_list = []
    letter_list = []
    for i in range(len(word)):
        if word[i] != "#":
            pos_list.append(i)
            letter_list.append(word[i])
    return (pos_list,letter_list)

def check_pos(word1,word2):
    ok = True
    pos , letter = get_pos(word1) 
    for i in range(len(pos)):
        if letter[i] == word2[pos[i]]:
            ok = True
        else:
            ok = False
    return (ok)

def auto_search(v):
    SIZE = 2296
    idx = 0
    l_word = []
    for i in range(SIZE):
        line = random_line("list.txt",i,i).lower()
        l = line.split(" ")
        if v.letter_inside == "":
            if v.space_word == False:
                if len(line) == v.word_len:
                    print(line.replace("\n","") , end = "-")
            else:
                if len(line)  == v.word_len  and len(l) > 1:
                    print(line.replace("\n","") , end = "-")
        else:
            if v.space_word == False and v.letter_inside in line and v.num_of_letter == 1:
                if len(line) == v.word_len:
                    print(line.replace("\n","") , end = "-")
            elif v.num_of_letter == 1:
                if len(line) == v.word_len and len(l) > 1 and v.letter_inside in line:
                    print(line.replace("\n","") , end = "-")
            if v.space_word == False and v.letter_inside in line and v.num_of_letter != 1:
                if len(line) == v.word_len:
                    for j in range(len(v.word)):
                        for k in range(len(line)):
                            if line[k] == v.word[j]:
                                idx = idx + 1
                            if k == len(line) - 1:
                                if check_pos(v.word,line) == True and line.replace("\n","") not in l_word:
                                    l_word.append(line.replace("\n",""))
                                    print(line.replace("\n",""), end = "-")
                                idx = 0
            elif v.space_word == True and v.letter_inside in line and v.num_of_letter != 1:
                if len(line) == v.word_len:
                    for j in range(len(v.word)):
                        for k in range(len(line)):
                            if line[k] == v.word[j]:
                                idx = idx + 1
                            if k == len(line) - 1:
                                if line.replace("\n","") not in l_word and len(l) > 1:
                                    l_word.append(line.replace("\n",""))
                                    print(line.replace("\n",""), end = "-")
                                idx = 0
                            
            elif v.space_word == False and v.letter_inside in line and v.num_of_letter == 1:
                if len(line) == v.word_len and len(l) > 1 and v.letter_inside in line:
                    print(line.replace("\n","") , end = "-")
            

v = Var()   
v.space_word = False
v.word = "###a#######"
v.letter_inside = get_letter(v.word,"#")
v.word_len  = len(v.word)
l,l2 = get_pos(v.word)
v.num_of_letter = set(v.word)
v.num_of_letter = len(v.num_of_letter)

system("clear")
if v.space_word == False:
    v.word_len = v.word_len + 1
    auto_search(v)
else:
    auto_search(v)
print("")