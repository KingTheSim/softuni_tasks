import os

def save_extensions(dir_name, exts):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            ext = filename.split(".")[-1]

            if ext not in exts:
                exts[ext] = []

            exts[ext].append(filename)

        elif os.path.isdir(file):
            save_extensions(file, exts)


directory = input("Enter directory: ")
extensions = {}

try:
    save_extensions(directory, extensions)
except FileNotFoundError:
    print("Not a valid directory")

result = []

for extension, files in sorted(extensions.items()):
    result.append(f".{extension}")
    result.extend(f"- - - {file}" for file in sorted(files))

with open("file_folder/report.txt", "w") as report_file:
    report_file.write("\n".join(result))
