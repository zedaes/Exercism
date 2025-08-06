def value(colors_list):
    colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    return colors.index(colors_list[0]) * 10 + colors.index(colors_list[1])
