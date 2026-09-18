# INPUT:
# 1-qator: default settings (theme lang debug) -> masalan: dark uz 1
# 2-qator: override settings (theme lang debug) -> '-' bo‘lsa o‘zgarmaydi
# debug: 1 yoki 0
# Vazifa: final settings ni 1 qatorda chiqaring: theme lang debug

# default
th1, lang1, dbg1 = input().split()
# override
th2, lang2, dbg2 = input().split()

s = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}

# TODO
ft = s['override']['theme'] if s['override']['theme'] != '-' else s['theme']
fl = s['override']['lang'] if s['override']['lang'] != '-' else s['lang']
fd = s['override']['debug'] if s['override']['debug'] is not None else s['debug']
print(ft, fl, '1' if fd else '0')