# Agent

###### breaf
Given a folder, the agent will start to search the ComponentList.yalm.
After found it, the agent will perform the interpretation of the data.
Then it will does the Generation of the code.

###### flow

### Searcher
Given the path, it will perform a greedy search recursively in all the
folder. It will return *result* True if it will find the ComponentList.

### Interpret
The Interpret receive the ComponentList file path from the *Searcher* and it will
interpret in a dictionary it's contents.

Available files type: [ yalm ]

### Generator
The Generator receiving the interpreted dictionary will generate the Components code.
