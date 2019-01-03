#divide list on chunks of given size
# [1,2,3,4,5] size=2 -> [[1,2], [3,4], [5]]

def chunks(array, size):

    if size<=0:
        return array
    chunked=[]
    i=0
    while i<(len(array)):
        chunk=[]
        j=0
        while j<size and i<(len(array)) :
            chunk.append(array[i])
            i+=1
            j+=1
        chunked.append(chunk)

    return chunked

