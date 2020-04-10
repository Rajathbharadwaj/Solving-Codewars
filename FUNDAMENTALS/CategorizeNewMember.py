def openOrSenior(data):
    answer = []
    for v in data:
        if v[0]>=55 and v[1]>7:
            answer.append("Senior")
        else:
            answer.append("Open")
            
    return answer
