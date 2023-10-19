import textwrap


def wrap(text, width):
    resulting = textwrap.wrap(text, width=width)
    resulting = "\n".join(resulting)
    return resulting

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for part in result:
        print(part)
