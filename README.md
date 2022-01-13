# Wordle Helper

A Python binary to help with Wordle. 

## Instructions

Requires Python3.

```shell
python3 main.py
```

Where input is required, use: 

- upper case for green letters (correct position)
- lower case for orange letters (incorrect position)

For example: 

```shell
What was your guess?

print

What was the result?

P_i_t

There 7 possible word(s):

['patio', 'pieta', 'piety', 'pitas', 'pitch', 'piths', 'pithy']

<--Count of Letters in Possible Words-->

[('a', 3), ('h', 3), ('e', 2), ('y', 2), ('s', 2), ('o', 1), ('c', 1), ('p', 0), ('t', 0), ('i', 0)]

<--Weighted Score of Possible Words-->

[('pieta', 5), ('pitas', 5), ('piths', 5), ('pithy', 5), ('patio', 4), ('piety', 4), ('pitch', 4)]
```