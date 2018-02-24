def mshd2s(minutter, sekunder, hundredeler):
    return (minutter*60+sekunder+0.01*hundredeler)

def rundeTid(startTid,sluttTid):
    startSek = mshd2s(startTid[0],startTid[1],startTid[2])
    sluttSek = mshd2s(sluttTid[0],sluttTid[1],sluttTid[2])
    return sluttSek-startSek

def alleRundeTider(passeringsTider):
    rundetider = []
    for i in range(len(passeringsTider)-1):
        rundetider.append(rundeTid(passeringsTider[i],passeringsTider[i+1]))
    return rundetider

print(alleRundeTider([[0,20,0],[0,50,10],[1,21,21],[1,53,33]]))
