d = {}
def is_mashable(valid_words,word):
    global d
    if len(word) == 0:
        return True
    if word not in valid_words:
        return False
    if word in d:
        return d[word]
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if is_mashable(valid_words,new_word): 
            d[new_word] = True 
            return True
    return False

valid_words = {'ab'}
print(is_mashable(valid_words,'ab'))
