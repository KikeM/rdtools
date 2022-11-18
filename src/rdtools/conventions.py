import re


def create_conventions(keys, name_class="Dimensions", show=False):
    """Create conventions Python class.

    Parameters
    ----------
    keys : list of str
        _description_
    name_class : str, optional
        _description_, by default "Dimensions"
    show : bool, optional
        If True, prints the class definition, by default False

    Returns
    -------
    lines : list of str
    """
    keys = list(keys)

    pattern = "[a-zA-Z][^A-Z]*"
    template = '\t{variable} = "{column}"\n'
    lines = []
    for column in keys:
        split = re.findall(pattern, column)
        variable = "_".join(split)
        variable = variable.upper()
        line = template.format(variable=variable, column=column)
        lines.append(line)

    if show:
        print(f"class {name_class}:\n")
        print("".join(lines))

    return lines
