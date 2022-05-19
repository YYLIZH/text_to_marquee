from text_to_marquee.marquee import text_to_marquee
import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="text-to-marquee")
    parser.add_argument("text", type=str, help="the marquee text")
    parser.add_argument("--config", type=str, help="config path")
    return parser.parse_args()


def main():
    arg = parse_arguments()
    text_to_marquee(text=arg.text, config_path=arg.config)


if __name__ == "__main__":
    main()
