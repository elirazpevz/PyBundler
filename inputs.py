def format_options(options: list) -> str:
    return '\n\t'.join(f"{i + 1}) {item}" for i, item in enumerate(options))


def get_option(options: list) -> list[str]:
    formatted_ops = format_options(options)
    selected = input(
        f"""Please provide the indexes as a list of numbers or ranges (-) seperated by ',': \nOptions: \n\t{formatted_ops}\n""")

    indexes = []
    for i in selected.split(','):
        dashed = i.split("-")
        if len(dashed) == 1:
            indexes.append(int(i) - 1)
        elif len(dashed) == 2:
            for j in range(int(dashed[0]) - 1, int(dashed[1])):
                indexes.append(j)

    return [options[i] for i in indexes]


def get_single_option(options: list):
    formatted_ops = format_options(options)
    selected = input(
        f"""Please provide the index of your choice: \nOptions: \n\t{formatted_ops}\n""")

    return options[int(selected) - 1]
