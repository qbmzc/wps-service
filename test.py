import time
import timeout_decorator


@timeout_decorator.timeout(4)
def test():
    time.sleep(5)
    return 5


if __name__ == '__main__':
    try:
        a = test()
        print(a)
    except Exception as e:
        print(e)
    finally:
        print("finally")
