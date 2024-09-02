# Fake Word Generator
Generates fake, but believable, english sounding words

## How It Works
Words are made up individual syllables, each of which have a distinct, english sounding sound. If we randomly combine syllables, we form a word. However, not all syllables make sense
at different parts of a word. For example "ing" and "tion" make much more sense at the end of a word rather than the beginning, making the fake word "tionad" not very believable,
while "adtion" is much more believable. To fix this, we need to know what syllables are likely to follow another. We store this information by making a weighted directed graph, 
where nodes represent syllables and syllables are connected by an edge if one follows another. The weight of the edge represents the frequency that the second syllable follows the first
in our list of 10,000 words. We can then take steps through the graph by following a weighted random decision to create new english sounding words.

## Letter Version
Alternatively, our graph can connnect letters rather than syllables. On average, this version seems to produce worse words, but the best words from this version seem better than
the best words from syllable version

## Issues
Neither a graph of syllables nor letters seems optimal. For example, "node", "lode", and "tode" are all considered unique syllables. For the sake of word generation, it would be better
if nodes "n", "l", and "t" all pointed to the "ode" sound. This highlights how even syllables can be split further down while still be larger than individual letters. I think a graph
of phonetic sounds would be better, and it might be something I come back to for this project
