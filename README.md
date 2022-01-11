# Wordle Helper

A Python binary to help with Wordle. 

## Instructions

Requires Python3, no libraries used.

```shell
python3 main.py
```

Where input is required, use: 

- upper case for green letters (correct position)
- lower case for orange letters (incorrect position)

For example: 

```shell
What is your input?

pRE__

There 5 possible word(s)

['creep', 'crepe', 'crept', 'greps', 'treap']

<--Count of Letters in Possible Words-->

[('c', 3), ('e', 2), ('t', 2), ('g', 1), ('s', 1), ('a', 1), ('r', 0), ('p', 0)]

<--Weighted Score of Possible Words-->

[('crept', 7), ('creep', 5), ('crepe', 5), ('treap', 5), ('greps', 4)]
```