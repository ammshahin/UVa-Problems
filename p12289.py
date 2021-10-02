n = int(input())
words = ['one','two','three']

while n>0:
    word = str(input())
    for id,i in enumerate(words):
        if len(word) == len(i):
            j = 0
            count = 0
            while j< len(word):
                if word[j] != i[j]:
                    count += 1
                j+=1
            if count <2:
                print(id+1)
    n-=1
        
