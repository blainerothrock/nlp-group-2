# nlp-group-2

## To Install
* Install required dependencies
    - `pip install -r requirements.txt`
* Execute main
    - `python main.py`

## Configurations
Configurations/parameters can be found in `constants.py`

## Project Structure To Do:
- [ ] Configure main method take parameters based on task to be ran
    * **For example**: `python main.py build_corpus`
    
## Assignment 1 Checklist
### Task 1
- [x] Generated raw Wikipedia Text
- [ ] Write a Query that results in ~5 million tokens

### Task 2
- [x] Strip HTML
- [x] Added `<s>` & `</s>` boundries
- [ ] Tokenized using `nltk`
    - [ ] Remove punctuation
    - [ ] Remove "[citation needed]" - could just adjust current regex code in prepare-corpus branch
- [x] Generated train, test & validation text files
- [ ] Remove tokens with frequency token of < 3

### Task 3
- [ ] Construct a vocabulary from the training set
- [ ] Replace out-of-vocabularly words in test and validation with `<unk>`
- [ ] Remove all one-character tokens that are not 'a' (see group2.test.txt for examples)
- [ ] Save Python list of vocabulary
- [ ] Save dictionary `{ [WORD] : [IDX] }`
- [ ] Construct integer representation of training, validation and test corpra, save as lists

### Task 4
- [ ] Insert tags for years
- [ ] Insert tags for real numbers
- [ ] Insert tags for `c` <-- decide what tag to remove
- [ ] Insert tags for `d` <-- decide what tag to remove
- [ ] create new integer represetnations of training, validation and test corpra, save as lists

### Task 5
- [ ] Prepare statistical summary of corpus
    - number of tokens
    - vocabulary size
        - untagged
        - tagged corpus
        - each 4 word classes

### Task 6
- [ ] [Summary](https://docs.google.com/document/d/1dFqweNHXq2So4Abm2NIHZwCo0SC6XjwCwIdu5MjohlQ/edit) describing each task, including ambiguity and decisions we made 
    
## List of Questions for David
- [ ] Q1
- [ ] etc.
