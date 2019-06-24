from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from template.core.template import Template


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("-m", "--method",  required=True,
                        choices=['template'],
                        help='The processing method:token, pdf2text, cutbio, word2vec, ner-train, '
                             'ner-predict, predict-company, other')
    parser.add_argument("-input", "--input", default=None, help="The input file")
    parser.add_argument("-output", "--output", default=None, help="The output file")
    args = parser.parse_args()
    return args


def main(args):
    if args.method == 'template':
        temp = Template(args.input, args.ourput)
        return temp.run()


if __name__ == "__main__":
    main(parse_args())