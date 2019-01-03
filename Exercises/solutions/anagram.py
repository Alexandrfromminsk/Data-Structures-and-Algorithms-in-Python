def anagram(word1, word2):

    def count_chars(word):
        d={}
        for letter in word:
            if letter.isalpha():
                if letter in d.keys():
                    d[letter]+=1
                else:
                    d[letter]=1
        return d

    counter1=count_chars(word1.lower())
    counter2=count_chars(word2.lower())

    if len(counter1)!=len(counter2):
        return False
    for letter in counter1.keys():
        if counter1[letter]!=counter2[letter]:
            return False

    return True