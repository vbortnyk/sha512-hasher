import hashlib
import argparse


def hash_wordlist(input_file, output_file):
    with open(input_file, "r", encoding="latin-1") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            password = line.rstrip("\r\n")

            if not password:
                continue

            hash_value = hashlib.sha512(
                password.encode("utf-8")
            ).hexdigest()

            outfile.write(f"{hash_value}:{password}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Create a Hashcat potfile from a wordlist using SHA-512."
    )

    parser.add_argument("input", help="Input wordlist")
    parser.add_argument("output", help="Output .potfile")

    args = parser.parse_args()

    hash_wordlist(args.input, args.output)


if __name__ == "__main__":
    main()