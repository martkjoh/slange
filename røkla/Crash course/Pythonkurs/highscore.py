def check_highscore(points,scores):
    for place in scores:
        if points>scores[place][1]:
            return place
    return -1

def print_highscores(scores):
    for x in scores:
        print(str(x).rjust(2)+" "+scores[x][0].ljust(20)+str(scores[x][1]).rjust(5))

def add_highscore(points,name,scores):
    place = check_highscore(points,scores)
    print(place)
    if not place==-1:
        changes = len(scores)-place
        for i in range(changes):
            scores[len(scores)-i] = scores[len(scores)-1-i]
        scores[place] = [name,points]
    return scores


highscores = {}
highscores[1] = ['Vernon',100]
highscores[2] = ['Sirius',90]
highscores[3] = ['Severus',80]
highscores= add_highscore(50,"hei",highscores)
print_highscores(highscores)
