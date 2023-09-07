#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    module_names = dir(hidden_4)
    filtered_strings = [name for name in module_names
                        if isinstance(name, str) and '_' in name
                        and not name.startswith('__')]
    for string in filtered_strings:
        print("{}".format(string))
