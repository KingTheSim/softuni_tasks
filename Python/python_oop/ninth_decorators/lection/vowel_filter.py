def vowel_filter(function):
    def wrapper():
        vowels = ['a', 'e', 'i', 'o', 'u']
        return [c for c in function() if c in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
