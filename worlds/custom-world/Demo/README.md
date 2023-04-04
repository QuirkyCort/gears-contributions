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

## randrange[X](start, end)

...where [X] may be "A", "B", "C", "D", or "E" (ie. randrangeA, randrangeB, randrangeC, ...).

This works the same as randrange, but uses the same random number for every occurance of randrangeX.

### Example:

```
"position": ["randrangeA(0, 1)", "randrangeA(0, 8)", 0]
```

The x position of this object will be set to a random value between the range of 0 to 1.
For illustration purposes, let's imagine that x was set to 0.25 (...about a quarter of the range).
When selecting the y position, it will also be set to a quarter of the range, which in this case will be 2.

This is useful when you need to maintain a proportional relationship between two values (eg. when you need an object to be positioned randomly along a diagonal line).

### Note:

The random number used by **randrangeX** is the same as that used by **randchoiceX**.
This means that there will be a proportional relationship between the random values selected by say **randrangeA** and **randchoiceA**.
If this is not desired, use a different **X** (eg. **randrangeA** and **randchoiceB**).

## randchoice(choice1, choice2, choice3, ...)

This is replaced with one of the randomly selected choice.

### Example:

```
"position": ["randchoice(0, 2, 4)", 0, 0]
```

The x position of this object will be set to either 0, 2, or 4.

## randchoice(string1, string2, string3, ...)

This works with strings as well.
Strings do not need to be quoted unless they start with a number.

### Example:

```
"imageURL": "randchoice(textures/box/cardboard.png, textures/maps/custom.png)"
```

The strings starts with a letter, "t", so no quoting required.

### Example 2:

```
"color": "randchoice(#FF0000, #00FF00, '000099')",
```

The first two colors starts with a "#", so no quoting required.
The third color starts with a 0, so single quotes are required to ensure it is interpreted as a string and not a number.

## randchoice(array1, array2, array3, ...)

randchoice can also work with arrays...

```
"position": "randchoice([0,0,0], [10,10,10], [20,20,20])"
```

The position of this object will be set to either [0,0,0], [10,10,10], or [20,20,20].

## randchoice[X](choice1, choice2, choice3, ...)

...where [X] may be "A", "B", "C", "D", or "E" (ie. randchoiceA, randchoiceB, randchoiceC, ...).

This works the same as randchoice, but makes the same random choice for every occurence of randchoiceX.

### Example:

```
"position": ["randchoiceA(0, 1)", "randchoiceA(2, 4)", 0]
```

This will randomly choose 0 or 1 for the x position.
If 0 was choosen (...the first option), then for the y position, it will also choose the first option (ie. 2).
Similarly, if 1 (second option) was choosen for x, then 4 (second option) will also be selected for y.

This is useful when you need two or more blocks to appear in corresponding positions (ie. one on top of the other).

```
// Box 1
"position": "randchoiceA([0,0,0], [10,0,0])"
.
.
.
// Box 2
"position": "randchoiceA([0,0,10], [10,0,10])"
```

This places box 1 at either [0,0,0] or [10,0,0], and ensures that box 2 will always appear on top of box 1.

See randomizationDemo2.json

## shuffle[X](choice1, choice2, choice3, ...)

...where [X] may be "A", "B", "C", "D", or "E" (ie. shuffleA, shuffleB, shuffleC, ...).

This randomly select one of the options, but will not select an option that was already selected in a previous occurance.

### Example:

```
// Box 1
"position": ["shuffleA(0, 1, 2, 3)", 0, 0]
.
.
.
// Box 2
"position": ["shuffleA(0, 1, 2, 3)", 0, 0]
.
.
.
// Box 3
"position": ["shuffleA(0, 1, 2, 3)", 0, 0]
```

This places box 1 at either x = 0, 1, 2, or 3.
For illustration purposes, let's imagine that x = 2 (...third option) was selected.
Now box 2 can only appear at 0, 1, or 3; the third option will not be selected.
Let's imagine that x = 1 was selected for box 2.
Now box 3 can only appear at 0 or 3.

**IMPORTANT** You must ensure that there are enough options for selection.
(eg. If there are 3 occurences of shuffleA, then shuffleA must have at least 3 options).

See randomizationDemo3.json

## shuffle[X][Y](choice1, choice2, choice3, ...)

...where [X] may be "A", "B", "C", "D", or "E" (ie. shuffleA, shuffleB, shuffleC, ...).
...and [Y] may be a number (eg. 0, 1, 2, 3...)

This selects the using the same index from a previous shuffle.
This means that if the first "shuffleA" selected the second index (...index 1), then "shuffleA0" will also select index 1.

"shuffleA0" will use the index from the first "shuffleA", "shuffleA1" will use the index from the second "shuffleA", etc.

Note that the index starts from 0 and not 1.

### Example:

```
// Box 1
"position": ["shuffleA(0, 1, 2)", 0, 0]
"rotation": [0, "shuffleA0(0, 45, 90)", 0]
.
.
.
// Box 2
"position": ["shuffleA(0, 1, 2)", 0, 0]
"rotation": [0, "shuffleA1(0, 45, 90)", 0]
```

This places box 1 at either x = 0, 1, or 2.
For illustration purposes, let's imagine that x = 2 (...third option) was selected.
The "shuffleA0" will also select the third option (ie. 90).

Now box 2 can only appear at 0, or 1; the third option will not be selected.
Let's imagine that x = 1 (second option) was selected for box 2.
The "shuffleA1" will also select the second option (ie. 45).

**IMPORTANT** You must ensure that the referenced shuffle appears before you reference it.

Something like this is not valid...

```
// Box 1
"position": ["shuffleA(0, 1, 2)", 0, 0]
"rotation": [0, "shuffleA1(0, 45, 90)", 0]
.
.
.
// Box 2
"position": ["shuffleA(0, 1, 2)", 0, 0]
"rotation": [0, "shuffleA0(0, 45, 90)", 0]
```

...because the "shuffleA1" is referencing the second shuffle, but the second shuffle hasn't appear yet.

See randomizationDemo4.json

## Nesting

The directives can be nested...

```
"position": ["randchoice(randrange(-10,-5), randrange(5, 10))", 0, 0]
```

The x position of this object will be either between -10 to -5, or 5 to 10. It will not appear between -5 to 5.