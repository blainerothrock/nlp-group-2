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
- [x] Write a Query that results in ~5 million tokens

### Task 2
- [x] Strip HTML
- [x] Added `<s>` & `</s>` boundries
- [x] Tokenized using `nltk`
    - [x] Remove punctuation
    - [x] Remove "[citation needed]" - could just adjust current regex code in prepare-corpus branch
- [x] Generated train, test & validation text files
- [x] Remove tokens with frequency < 3
- [x] Add punctuation back in!

### Task 3
- [x] Construct a vocabulary from the training set
- [x] Replace out-of-vocabularly words in test and validation with `<unk>`
- [x] Remove all one-character tokens that are not 'a' (see group2.test.txt for examples)
- [x] Save Python list of vocabulary
- [x] Save dictionary `{ [WORD] : [IDX] }`
- [x] Construct integer representation of training, validation and test corpora, save as lists
- [x] Don't forget to write integer representations to pickle files

### Task 4
- [x] Insert tags for years
- [x] Insert tags for real numbers
- [x] Keep other numbers in as tokens (don't tag or remove them)
- [x] Insert tags for `c` <-- decide what tag to remove
- [x] Insert tags for `d` <-- decide what tag to remove
- [x] Add these tags to the `vocab` list before making integer representation
- [x] Construct integer representation of training, validation and test corpora, save as lists

### Task 5
- [x] Prepare statistical summary of corpus
    - number of tokens
    - vocabulary size
        - untagged
        - tagged corpus
        - each 4 word classes

### Task 6
- [x] [Summary](https://docs.google.com/document/d/1dFqweNHXq2So4Abm2NIHZwCo0SC6XjwCwIdu5MjohlQ/edit) describing each task, including ambiguity and decisions we made 
    
## List of Questions for David
