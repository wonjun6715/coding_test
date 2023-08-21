def solution(id_pw, db):
    count = 0   
    for idd, pww in db:
        if idd == id_pw[0] and pww == id_pw[1]:
            return "login"
        elif idd == id_pw[0]:
            count += 1
    if count != 0:
        return "wrong pw"
    return "fail"
        
   