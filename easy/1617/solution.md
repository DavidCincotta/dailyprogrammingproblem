There are three solutions that I can think of, the second was never implemented but lead me to the third

The trivial method is to modify one character at a time until no modifications are done. This takes $O(n^2)$ time as you have at most $n$ modifications, and you have to loop through the whole string each pass. This still resolves to $O(n^2)$ even if you truncate the edges)

Slightly more complicated is doing multiple characters in a single pass. This is also $O(n^2)$ for the same reasons. Just a single string "R..." would take $O(n^2)$. Even checking for the first or last occurrance of a viable character takes $O(n)$ time. So we need a more clever method to make this faster.

This next method could be a recursive method that attempts to fill the string concurrently, by breaknig the string down into subproblems, such as the begining, end, middle.

This method would have the relation $T(n) = \sum_{0}^m(T(n-c)) + O(n)$ where n is the length of the string, and m is the number of modifications, and c is the size of that modification. You may only be updating 1 char, or n chars, if the string is "R...". 

After thinging about this method for longer, the runtime would have to be $O(n)$ as there can only be at most $n$ modifications. There would also be at most $O(n)$ modifications thad require recursion, 



after walking through how to even identify the recursive points, I'm pretty sure we can just do this in O(n) with a two pointer method. If there must at most be $n$ modifications, can't we just detect what modification we are doing at the moment, and do that accoringly in linear time.


|Step|CurString|ci|l|r|Notes|
|-|---|-|-|-|---|
|0|"...L..R..L..R..."|0|0|0|Input String|
|1|"...L..R..L..R..."|3|3|0|Loop forward to L|
|2|"LLLL..R..L..R..."|0|3|0|backtrack to last char|
|3|"LLLL..R..L..R..."|3|3|0|jump to l|
|4|"LLLL..R..L..R..."|4|3|0|jump to l+1|
