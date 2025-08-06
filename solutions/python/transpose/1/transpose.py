def transpose(input_text):
    transposed_lines = []
    lines = input_text.split("\n")
    line_lengths = []

    for i in range(len(lines)):
        current_length = len(lines[i])
        line_lengths.append(current_length)
        for j in range(i):
            if current_length > len(lines[j]):
                lines[j] += ' ' * (current_length - len(lines[j]))

    for i in range(max(line_lengths)):
        transposed_lines.append("")

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            transposed_lines[j] += lines[i][j]

    return "\n".join(transposed_lines)
