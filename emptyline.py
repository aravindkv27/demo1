def find_empty(text):
    #f = open("test.txt", "r")
    lines=text.split('\n')
    empty_list=[]
    count=0
    for line in lines:
        count+=1
        if len(line)==0:
            empty_list.append(count)
    return empty_list



