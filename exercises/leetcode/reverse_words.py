def reverse_word(input):
    output = ''
    for i in input:
        output = i + output
    return output

def reverse_sentence(input):
    output = ''
    word = ''
    for i,char in enumerate(input):

        if char == ' ':
            output = output + word + ' '
            print('output : #{}#'.format(output))
            print('word : #{}#'.format(word))
            word = ''
        elif i == len(input)-1:
            output = output + word
            word = ''
        else:
            word = char + word
    return(output)



# def reverse_sentence(input):
#     return " ".join(input.split()[::-1])

print(reverse_sentence('Hello world! NETSETOS'))