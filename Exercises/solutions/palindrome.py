def palindrome(word):

    if len(word)<2:
        return True

    for i in range(len(word)//2):
        if word[i]!=word[len(word)-1-i]:
            return False
    return True