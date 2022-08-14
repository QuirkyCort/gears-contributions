# Randomization

Worlds created in the World Builder can be randomized by manually editing the json file.
Any of the values can be replaced with a string containing the following pre-processing directives...

## randrange(start, end)

This is replaced with a random float within the specified range.

### Example:

```
"position": ["randrange(-5,5)", 0, 0]
```

The x position of this object will be set to a random value between the range of -5 to 5.

## randchoice(choice1, choice2, choice3, ...)

This is replaced with one of the randomly selected choice.

## Example:

```
"position": ["randchoice(0, 2, 4)", 0, 0]
```

The x position of this object will be set to either 0, 2, or 4.

## randchoice(array1, array2, array3, ...)

randchoice can also work with arrays...

```
"position": "randchoice([0,0,0], [10,10,10], [20,20,20])"
```

The position of this object will be set to either [0,0,0], [10,10,10], or [20,20,20].

## randchoice[X](choice1, choice2, choice3)

...where [X] may be "A", "B", "C", "D", or "E" (ie. randchoiceA, randchoiceB, randchoiceC, ...).

This works the same as randchoice, but uses the same random number for every occurence of randchoiceX.

## Example:

```
"position": ["randchoiceA(0, 1)", "randchoiceA(2, 4)", 0]
```

This will randomly choose 0 or 1 for the x position.
If 0 was choosen (...the first option), then for the y position, it will also choose the first option (ie. 2).

This is useful to swap position of two blocks, while ensuring that they don't overlap.

```
// Box 1
"position": "randchoiceA([0,0,0], [10,0,0])"
.
.
.
// Box 2
"position": "randchoiceA([10,0,0], [0,0,0])"
```

This places box 1 at either [0,0,0] or [10,0,0], and ensures that box 2 will always appear at the other position.
If a normal randchoice was used, there is a risk that both boxes may appear at the same spot.

## Nesting

The directives can be nested...

```
"position": ["randchoice(randrange(-10,-5), randrange(5, 10))", 0, 0]
```

The x position of this object will be either between -10 to -5, or 5 to 10. It will not appear between -5 to 5.