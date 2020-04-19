import argparse

def main(n):
    for i in range(1,n):
        print(str(" " * (n-i)) + ("#" * i))
    print("#"*n)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=6, help="Enter an integer (default: 6)")
    args = ap.parse_args()
    main(args.n)