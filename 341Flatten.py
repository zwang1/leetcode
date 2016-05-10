__author__ = 'zhengyiwang'

def flat(array, result):
    if type(array) != list:
        result.append(array)
    else:
        for subarray in array:
            flat(subarray, result)




def flat1(array):

    indexstack = [[0,array]]
    result = []
    while len(indexstack) > 0 and array:
        index, currentarray = indexstack.pop()

        if index + 1 < len(currentarray):

            indexstack.append([index + 1, currentarray])

        if type(currentarray[index]) == int:
            result.append(currentarray[index])
        else:
            #is a list, update the current array and push index in stack
            if currentarray[index]:
                indexstack.append([0,currentarray[index]])

    return result

result = flat1([0])
print result

