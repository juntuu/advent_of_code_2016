if __name__ == "__main__":
    import fileinput
    import sys
    from pathlib import Path
    try:
        try:
            from .solution import main
        except ImportError:
            from solution import main  # type: ignore
    except ModuleNotFoundError:
        day = Path(__file__).parts[-2]
        print("Not implemented:", day, file=sys.stderr)
        exit(1)
    try:
        main(fileinput.input())
    except Exception as e:
        print(repr(e), file=sys.stderr)
        exit(1)
