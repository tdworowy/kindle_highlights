import os.path
from os import walk

from thefuzz import fuzz


def clean_up_file_name(name: str):
    illegal_filename_characters = [
        "/",
        "\\",
        "?",
        "%",
        "*",
        ":",
        "|",
        '"',
        "<",
        ">",
        ".",
        ",",
    ]
    for ch in illegal_filename_characters:
        name = name.replace(ch, "")
    name = name.strip()
    name = name.replace(" ", "_")

    return name


def remove_similar(lines: list[str]) -> list[str]:
    results = []
    for string in lines:
        is_unique = True
        for unique_string in results:
            ratio = fuzz.token_set_ratio(string, unique_string)
            if ratio >= 80:
                if len(string) > len(unique_string):
                    results.remove(unique_string)
                else:
                    is_unique = False
                    break
        if is_unique:
            results.append(string)
    return results

def remove_duplicates():
    file_names = next(walk("md"), (None, None, []))[2]
    for file_name in file_names:
        with open(f"md{file_name}", "a") as f:
            deduplicated =(set(f.readlines()))
            f.write(deduplicated)


def generate_md():
    # my_clippings_path = "E:\\documents\\My Clippings.txt"
    my_clippings_path = "My Clippings.txt"
    with open(my_clippings_path, "r", encoding="utf8") as f:
        lines = f.read().split("==========")
        lines = map(lambda line: line.split("\n"), lines)
        lines = [list(filter(lambda ele: ele != "", line)) for line in lines]
        lines = filter(lambda line: len(line) == 3, lines)
        lines = [
            list(map(lambda ele: ele.replace("\ufeff", ""), line)) for line in lines
        ]

        results = {}

        for line in list(lines):
            if line[0] in results.keys():
                results[line[0]].append(line[2])
            else:
                results[line[0]] = [line[2]]
        # print(results)

        for key in results.keys():
            file_name = clean_up_file_name(key)
            file_path = f"md/{file_name}.md"
            file_content = []
            if os.path.isfile(file_path):
                append_or_write = "a"
                f = open(file_path, "r", encoding="utf8")
                file_content = f.readlines()
            else:
                append_or_write = "w"
            with open(file_path, append_or_write, encoding="utf8") as f:
                if append_or_write == "w":
                    f.write(f"#### {key}\n")
                cleared = remove_similar(results[key])
                print(file_content[-2])
                for quote in cleared:
                    if quote not in file_content: #TODO never true
                        f.write(f"      {quote}\n\n")
                f.flush()


if __name__ == "__main__":
    #generate_md()
    remove_duplicates()
#TODO, remove duplicated quotes