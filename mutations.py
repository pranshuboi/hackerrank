def mutate_string(string, position, character):
    L=list(string)
    L[position]=character
    string=''.join(L)
    return string

