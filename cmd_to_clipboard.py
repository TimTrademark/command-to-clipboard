import argparse
import json
from src import command
import pyperclip


parser = argparse.ArgumentParser(description='Copies a configurable command to your clipboard.')
parser.add_argument('targets', nargs='*', help='target(s) that will be added to your command')


def main():
    args = parser.parse_args()
    targets = args.targets
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.loads(f.read())
        cmd = command.prepare_command(config, targets)
        pyperclip.copy(cmd)
        print(cmd)
        print("Command copied to clipboard!")


if __name__ == '__main__':
    main()
