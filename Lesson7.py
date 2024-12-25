# 1) Short Long Short
def solution(a, b):
    if len(a) > len(b):
        return f"{b}{a}{b}"
    else:
        return f"{a}{b}{a}"

# print(solution('1', '22'))



# 2) You only need one - Beginner
def check(seq, elem):
    if elem in seq:
        return True
    return False

# print(check([66, 101], 66))
# print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))



# 3) Correct the mistakes of the character recognition software
def correct(s):
    a = {'5': 'S', '0': '0', '1': 'I'}
    r = ''
    for i in s:
        if i in a:
            r += a[i]
        else:
            r += i
    return r

# print(correct("L0ND0N"))
# print(correct("DUBL1N"))
# print(correct("51NGAP0RE"))


# 4) Fake Binary
def fake_bin(x):
    r = ''
    for i in x:
        if int(i) >= 5:
            r += '1'
        else:
            r += '0'
    return r

# print(fake_bin("45385593107843568"))
# print(fake_bin("509321967506747"))
# print(fake_bin("366058562030849490134388085"))



# 5) Abbreviate a Two Word Name
def abbrev_name(name):
    n = name.split()
    return f"{n[0][0].upper()}.{n[1][0].upper()}"

# print(abbrev_name("Sam Harris"))
# print(abbrev_name("patrick feenan"))
# print(abbrev_name("Evan C"))
# print(abbrev_name("P Favuzzi"))



# 6) Convert a string to an array
def string_to_array(s):
    if s != '':
        return s.split()
    return ['']

# print(string_to_array("Robin Singh"))
# print(string_to_array("CodeWars"))
# print(string_to_array("I love arrays they are my favorite"))



# 7) Grasshopper - Personalized Message
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    return 'Hello guest'

# print(greet('Daniel', 'Daniel'))
# print(greet('Greg', 'Daniel'))


# 8) DNA to RNA Conversion
def dna_to_rna(dna):
    r = ''
    for i in dna:
        if i == 'T':
            r += 'U'
        else:
            r += i
    return r

# print(dna_to_rna("TTTT"))
# print(dna_to_rna("GCAT"))
# print(dna_to_rna("GACCGCCGCC"))


# 9) Sentence Smash
def smash(words):
    return " ".join(words)

# print(smash(['hello', 'world', 'this', 'is', 'great']))



# 10) The Feast of Many Beasts
def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False

# print(feast("great blue heron", "garlic naan"))
# print(feast("brown bear", "bear claw"))


# 11) MakeUpperCase
def make_upper_case(s):
    return s.upper()

# print(make_upper_case('hello'))


# 12) Total amount of points
def points(games):
    r = 0
    for i in games:
        if int(i[0]) > int(i[-1]):
            r += 3
        elif int(i[0]) == int(i[-1]):
            r += 1
        else:
            r += 0
    return r

# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
# print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))



# 13) Double Char
def double_char(s):
    r = ''
    for i in s:
        r += i + i
    return r

# print(double_char("String"))
# print(double_char("Hello World"))
# print(double_char("1234!_ "))



# 14) Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"

# print(bonus_time(10000, True))
# print(bonus_time(2, True))
# print(bonus_time(78, False))



# 15 Remove exclamation marks
def remove_exclamation_marks(s):
    r = ''
    for i in s:
        if i != '!':
            r += i
    return r

# print(remove_exclamation_marks("Hello World!"))
# print(remove_exclamation_marks("Hello World!!!"))
# print(remove_exclamation_marks("Hi! Hello!"))
# print(remove_exclamation_marks(''))