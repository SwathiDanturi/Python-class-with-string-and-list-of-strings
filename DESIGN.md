- **Developer**: Swathi Danturi
- **Collaborator(s)**: None
- **File Name**: Design.md
- **Date**: 09/30/2024

## size() method design
To find out how many elements in the `self.notes` list, we use the Python built-in 
function `len()`.
- Call `len()` with argument `self.notes` and return the result. 

## how_often_word() method design
- `sentence` is a parameter to this method and is a string of words separated by white spaces
- Define an empty dictionary `word_occurences`
- for each `word` in `sentence.split()`, iterate through the following:
    - using `word_occurences.get(word, 0)` get the value of `word` and increment it by `1`
    - assign this count to `word_occurences[word]`
- return `word_occurences`