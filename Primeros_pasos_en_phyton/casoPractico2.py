#Invertir palabras de una cadena dada:

def rev_sentence(sentence):

    words = sentence.split(' ')

    reverse_sentence = ' '.join(reversed(words))

    return reverse_sentence

if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print (rev_sentence(input))
