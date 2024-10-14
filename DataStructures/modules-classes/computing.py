
def is_multiple(n:int, m:int) ->bool:
    """The multiple function, that checks wheather n is multiple by m"""
    return n%m == 0

if __name__ == "__main__":
    print(is_multiple(5, 3))