def ChangeLengths(List_of_Strings):
    greatest_length = 0
    for string in List_of_Strings:
        if len(str(string)) > greatest_length:
            greatest_length = len(str(string))

    x=0
    for string in List_of_Strings:
        length = len(string)
        needed_length = (greatest_length - length) / 2
        if length < greatest_length:
            if (needed_length % 1) != 0:
                parts = [" " * int(needed_length - 0.5), string, " " * int(needed_length + 0.5)]
            else:
                parts = [" " * int(needed_length), string, " " * int(needed_length)]
        else:
            parts = [string]
        holder = ''.join(parts)
        List_of_Strings[x] = str(holder)
        x+=1
    return List_of_Strings