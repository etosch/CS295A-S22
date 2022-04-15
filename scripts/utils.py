import pandas


def check_format(src):
    # Make sure we don't have errant |s in the file
    with open(src, "r") as f:
        while True:
            line = f.readline()
            if not line: break
            if line.startswith("|"):
                num_bars = 0
                for c in line: 
                    if c == '|':
                        num_bars +=1
                if num_bars != 5:
                    print(line, num_bars)
                    exit()


def read_markdown_table(src):
    check_format(src)
    with open(src, "r") as f:
        while True:
            line = f.readline()
            if line.startswith("|"):
                names = line.split("|")
                table = pandas.read_table(f, sep="|")
                break

    # pandas doesn't understand how to read markdown.
    names = [s.strip() for s in names if s.strip()]
    # drop the two extra columns and apply the names
    table = table.iloc[:, 1:len(names)+1].set_axis(names, axis=1)
    # strip the extra space from each column
    # (do this later)
    return table
