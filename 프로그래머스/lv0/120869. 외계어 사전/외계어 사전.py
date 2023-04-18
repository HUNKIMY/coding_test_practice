def solution(spell, dic):
    for word in dic:
        if len(word) == len(spell):
            valid = True
        else:
            vald = False
        for i in spell:
            if word.count(i) == 1:
                pass
            else:
                valid = False
        if valid:
            return 1
    return 2
            
        
    