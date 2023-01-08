# create a function for replacing char in string
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    print(string)


mutate_string('abracadabra', 5, 'k')
