import re
def how_strong(pw):
    cont=0
    if re.search(r'\d', pw):
        cont=cont+10
    if re.search(r'[a-z]', pw):
        cont=cont+26
    if re.search(r'[A-Z]', pw):
        cont=cont+26
    if re.search(r'[^a-zA-Z0-9]', pw):
        cont=cont+30
    return len(pw)*cont

def  in_englsh(x):
    y=int(x)
    if y < 100:
        return "Too Weak"
    elif 100 < y < 300:
        return "Weak"
    elif 300<y<500:
        return "strong"
    elif 500 < y :
        return "Too stong"
