# HW00 Writeup — Song Analysis

Run `uv run python analysis.py` to generate the results, then answer the five questions
below. Replace each `[your answer here]` with your response.

- Questions 1–3 are factual. One or two sentences is enough.
- Question 4 asks you to reflect on something that surprised you.
- Question 5 asks you to connect what you implemented in Part 1 to the two new tools from Part 2.

---

## Question 1 (2 pts)

**Which genre averaged the most weeks on the Billboard chart, and how many
songs is that average computed from?**

Afrobeats spent the most weeks, 30, on the chart, and it was all from one song. 

---

## Question 2 (2 pts)

**Who was the most-streamed artist in the dataset (by total streams across all their songs)?**

Taylor Swift (6560M total streams)

---

## Question 3 (2 pts)

**Which year had the most top-10 hits (songs that peaked at position 10 or better)?**

 2024: 26 hit(s)

---

## Question 4 (4 pts)

**What surprised you about the data?**

Pick one finding from your analysis that was unexpected — something that contradicts what
you assumed going in, or that is more interesting than you expected. Explain:
- What you expected to see, and why.
- What the data actually showed.
- What might explain the difference.

I expected that the genre with 'Average Weeks on Chart by Genre' would be a genre with many songs, like pop or hip-hop. However, the data showed that the genre with the highest only had one song in the data set. (Calm Down,Rema,Afrobeats,2023,30,3,950.) This difference can be explained by how the average is calculated. Because the total weeks for a genre is divide by the number of songs in a genre, a genre with only one song has an advantage. If there was one more Afrobeats song with a low week on chart, it would not have been at the top.





---

## Question 5 (5 pts)

In Part 1 you implemented `count_occurrences` from scratch using only a plain Python
dict. `collections.Counter`, which you used in Part 2, does the same thing but with
extra conveniences built in.

Answer both parts:

**a)** Walk through, step by step, how you accumulated a running total per genre/artist
in `avg_weeks_by_genre` and `most_streamed_artist`, and how you determined the maximum
in `most_streamed_artist`. Would `collections.Counter` have made any part of this
easier, and if so, which part (drawing on how you'd extend your own `count_occurrences`
to do the same thing)?

In count_occurrences I used two for loops. In the first loop I looped through items to create a list of unique keys. I converted the list of keys into a dict using dict.fromkeys(keys) and looped though the dict using dictionary.items().I determined and assigned the key value from the count of keys using items.count().

In most_streamed_artist, I only needed one loop to solve a similar problem. I created a blank counter, then looped through the song list. For each song, I added the artist as a key to the counter, if it wasn't there. Then I incremented the value by adding the value of streams_millions to the exsiting value. 

In `avg_weeks_by_genre` the process was the same. I looped through the songs list to increment the number of weeks on the chart for each genre. 

Counter made the agregation easier and probably faster. I'd have to look into the code behind counter to be sure. If I were to extend count_occurance, I would use counter, although I might just use counter insead of count_occurances.


**b)** `StreamsRanker` and `LongevityRanker` both subclass `SongRanker` and share its
`rank` method, overriding only `score`. If they did **not** share a common base class —
if you had written two separate, unrelated classes instead — what code would you have
had to duplicate? What does inheritance buy you here?

[your answer here]
We would have had to duplicate the sorting code for rank: 

return sorted(songs, key=lambda song: self.score(song), reverse=True)[:n]

Inheritance allows us not to have the duplicate code, which also means that if we change the one sorting method, it changes for all inherited classes. It also would allow us to extend the class further, either with more inherited clases or adding more shred methods.
