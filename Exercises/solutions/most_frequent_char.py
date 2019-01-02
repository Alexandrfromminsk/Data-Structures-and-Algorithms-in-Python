#if the same amount return higher sorted char: aabb ->b

def most_frequent_char(word):
    if not word:
        return ""
    counter={}
    for char in word:
        if char in counter:
            counter[char]+=1
        else:
            counter[char]=1

    m=0
    ans=""
    for letter in counter.keys():
        print (letter, counter[letter])
        if counter[letter]>m:
            m=counter[letter]
            ans= letter
        elif counter[letter]==m:
            ans=max(ans,letter)

    print ("\n")
    return ans