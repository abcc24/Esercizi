s: str="La meccanica quantistica è la teoria fisica che descrive"

"""def counter(s:str):
    l: list=[]
    el1=len(s)
    el2=len(s.split())

print(counter(s))"""


"""def word_count(fr: str):
    fr: str="ciao come stai, tutto bene, ciao io sto bene"
    fr=fr.replace('.','').replace(',','').replace(',','').replace(',','')
    words=fr.split()
    d: dict[str, int]=dict()
    for i in words:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    d_filtrated:dict[str,int]=dict()
    for key, val in d:
        if d[key]>1:
            d_filtrated[key]=val
    return d_filtrated"""

v:str = "Amo Roma"
def is_palindromo(v: str):
    v: str=v.lower(), v.replace(' ','')
    l: list=list(v)
    for i in v:
        if i[0]==i[-1]:
            return True
        else:
            return False
print(is_palindromo(v))