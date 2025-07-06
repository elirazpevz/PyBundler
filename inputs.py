def get_option(options: list) -> list[str]:
    formatted_ops = '\n\t'.join(f"{i + 1}) {item}" for i, item in enumerate(options))
    selected = input(f"""Please provide the indexes as a list of numbers or ranges (-) seperated by ',': \nOptions:
    {formatted_ops}\n""")

    indexes = []
    for i in selected.split(','):
        dashed = i.split("-")
        if len(dashed) == 1:
            indexes.append(int(i) - 1)
        elif len(dashed) == 2:
            for j in range(int(dashed[0]) - 1, int(dashed[1])):
                indexes.append(j)

    return [options[i] for i in indexes]
