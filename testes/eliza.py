import re

patterns = [
    (r"\b(to|estou|eu estou)\b", "EU ESTOU"),
    (r"\b(sou|eu sou)\b", "EU SOU"),
    (r"\b(olha so,?) ", ""),
    (r".*EU ESTOU (deprimido|triste|cansado).*", r"LAMENTO OUVIR QUE VOCE ESTA \1"),
    (r".*EU SOU (infeliz).*", r"POR QUE VOCE ESTA \1?"),
    (r".* todos .*", "DE QUE FORMA?"),
    (r".* sempre .*", "VOCE PODE PENSAR EM UM EXEMPLO ESPECIFICO?"),
    (r".*tudo bem.*", "ESTOU BEM E VOCÊ ?")
    ]

while True:
    comment = input()
    response = comment.lower()
    for pat, sub in patterns:
        response = re.sub(pat, sub, response)
    print (response.upper())
