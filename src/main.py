from preprocess import preprocess
from get_train import get_train

def main():
    outcome = preprocess(get_train())
    '''
    # testing:
    print(outcome)
    print(type(outcome))
    print(type(outcome[1]))
    print(len(outcome))
    '''
if __name__ == '__main__':
    main()