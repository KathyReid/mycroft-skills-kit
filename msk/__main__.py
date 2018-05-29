import sys

from argparse import ArgumentParser

from msk.actions.create import CreateAction
from msk.actions.upgrade import UpgradeAction
from msk.actions.upload import UploadAction
from msk.exceptions import MskException

console_actions = {
    'upgrade': UpgradeAction,
    'upload': UploadAction,
    'create': CreateAction
}


def main():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')
    subparsers.required = True
    for action, cls in console_actions.items():
        cls.register(subparsers.add_parser(action))
    args = parser.parse_args(sys.argv[1:])

    try:
        return console_actions[args.action](args).perform()
    except MskException as e:
        print('{}: {}'.format(e.__class__.__name__, str(e)))
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == '__main__':
    main()