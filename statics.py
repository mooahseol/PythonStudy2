# statics.py

def getMode(numList) :
    num_set = set(numList)
    num_dict = dict()
    for n in num_set :    
        num_dict[n] = numList.count(n)
    # print(num_dict)

    max_num = max(num_dict.values())
    mdoes = []
    for k,v in num_dict.items() :
        if v == max_num :
            print('최빈값', k, v)
            #mode = k
            mdoes.append(k)
            #break 
    return mdoes

def getAvg(numList) :
    return sum(numList) / len(numList)



