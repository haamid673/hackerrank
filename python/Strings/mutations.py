def mutate_string(string, position, character):
    s1=list(string)
    s1[position]=character
    string=''.join(s1)
    return string