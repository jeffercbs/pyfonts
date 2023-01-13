from pyfonts import parser


def main():
    args = vars(parser.parse_args())
    subcommand = args.pop('subcommand')

    if len(args) < 1:
        parser.print_help()
        exit(0)
    try:
        print(subcommand, args)
    except KeyboardInterrupt:
        print("Error")


if __name__ == "__main__":
    main()
