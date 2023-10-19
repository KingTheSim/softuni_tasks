symbols = ["-", ",", ".", "!", "?"]

with open("file_folder/text.txt", "r") as cur_file:
    sentences = cur_file.readlines()

    for line in range(0, len(sentences), 2):

        for symbol in symbols:
            sentences[line] = sentences[line].replace(symbol, "@")

        print(*sentences[line].split()[::-1], sep=' ')
