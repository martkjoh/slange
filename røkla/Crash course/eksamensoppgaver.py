def mshd2s(m, s, h):
    return m*60 + s + h/100


def rundetid(strt, sltt):
    return mshd2s(*sltt) - mshd2s(*strt)


def aRT(pT):
    T = []
    for t in pT:
        T.append(rundetid(*t))
    return T

def high_score(lst, name,new_score):
    for place, score in lst.items():
        if new_score >= score[1]:
            #lst[place] = [name, new_score]
            return place
    return False

high_score_list = {
    1: ["Martin", 99956],
    2: ["<artv", 99546],
    3: ["AAA", 10034],
    4: ["nitram", 2003]
}

high_score(high_score_list, "lasdjkf", 99999)

for a, b in high_score_list.items():
    print(str(a).ljust(10) + "  " + str(b[0]).ljust(0) + str(b[1]).rjust(20))


