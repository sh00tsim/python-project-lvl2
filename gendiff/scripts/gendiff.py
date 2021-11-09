from gendiff.scripts.cli import run
from gendiff.gendiff import output


def main():
    args = run()
    output(args)


if __name__ == '__main__':
    main()
