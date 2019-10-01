from easycli import Root


__version__ = '0.1.0'


class RootGit(Root):
    __completion__ = True
    __arguments__ = [
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        super().__call__(args)


def main():
    RootGit().main()

