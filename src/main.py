from preprocess import preprocess
from get_train import get_train

def main():
    outcome = preprocess(get_train())

    print(outcome)

if __name__ == '__main__':
    main()