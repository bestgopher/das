from stack_queue.stack import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    s = ArrayStack()
    original = open(filename)
    for line in original:
        s.push(line.rstrip("\n"))
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename + '_test.txt', "w")
    while not s.is_empty():
        output.write(s.pop() + '\n')
    output.close()


def is_matched(expr):
    """Return True if all delimiters are properly matched; False otherwise."""
    lefty = "({["
    rightly = ")}]"
    s = ArrayStack()

    for i in expr:
        if i in lefty:
            s.push(i)
        else:
            if s.is_empty() or lefty.index(s.pop()) != rightly.index(i):
                return False

    return s.is_empty()


def is_matched_html(html: str):
    """Return True if all HTML tags are properly match; False otherwise."""
    s = ArrayStack()
    j = html.find("<")
    while j != -1:
        k = html.find(">", j + 1)
        if k == -1:
            return False
        tag = html[j + 1: k]
        if not tag.startswith("/"):
            s.push(tag)
        else:
            if s.is_empty() or tag[1:] != s.pop():
                return False
        j = html.find("<", k + 1)

    return s.is_empty()


if __name__ == '__main__':
    reverse_file("stack.py")
    print(is_matched("([]){([])}[]"))
