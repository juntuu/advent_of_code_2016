import functools
import importlib
import os
import sys
import time


def timed(f):

    @functools.wraps(f)
    def wrap(*args):
        t0 = time.perf_counter()
        res = f(*args)
        t1 = time.perf_counter()
        t = t1 - t0
        m = int(t / 60)
        t -= 60 * m
        print(f"{m}:{t:.04} | {f.__qualname__}({', '.join(args)})", file=sys.stderr)
        return res

    return wrap


@timed
def run_day(day):
    try:
        mod = importlib.import_module(day.strip("/") + ".solution")
    except ModuleNotFoundError:
        raise NotImplementedError from None
    try:
        with open(os.path.join(day, "input.txt")) as f:
            mod.main(f)
            return
    except FileNotFoundError:
        pass
    mod.main()


def main(days):
    for day in days:
        try:
            print("*" *  40, file=sys.stderr)
            run_day(day)
        except (Exception, KeyboardInterrupt) as e:
            print("\n" + day, repr(e), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])

