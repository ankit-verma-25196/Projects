if __name__ == '__main__':
    li1 = []
    li2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li1.append(name)
        li2.append(score)
        
    li3 = sorted(li2)
    #print(li1)
    #print(li2)
    #print(li3)
    
    final_names = []
    for i in range(len(li2)):
        if li3[1] == li2[i]:
            final_names.append(li1[i])
            
    final_names.sort()
    
    for i in range(len(final_names)):
        print(final_names[i])

