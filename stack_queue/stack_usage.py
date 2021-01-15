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


if __name__ == '__main__':
    reverse_file("stack.py")
