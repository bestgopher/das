import time


def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time.time()
    for k in range(n):
        data.append(None)
    end = time.time()
    return (end - start) / n


if __name__ == '__main__':
    print(f"100 --- {compute_average(100)}")
    print(f"1000 --- {compute_average(1000)}")
    print(f"10000 --- {compute_average(10000)}")
    print(f"100000 --- {compute_average(100000)}")
    print(f"1000000 --- {compute_average(1000000)}")
    print(f"10000000 --- {compute_average(10000000)}")
