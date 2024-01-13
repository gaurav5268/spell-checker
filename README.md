# spell-checker

Spell checkers are ubiquitous in everyday applications, seamlessly integrated into word 
processors, browsers, and communication platforms, making them easily accessible to 
users.

Data Requirement

We need a trusted text corpus that we'll use to build the auto-correct system. There are many 
public domain text corpus. Since it's an unsupervised type of problem here what we need is 
just text. You can use any competition data or any other public dataset that has text field 
column. In the current version I have used Shakespeare corpus. Since. it's a very small corpus 
we need to compromise on word probabilities. 

This auto-correct architecture has 4 components -

1.Filtering Misspelling: 

One simple approach could be checking if a word is there in the vocabulary or not. This 
is a basic way to find errors, but there are smarter ways. Instead of just checking if a 
word is exactly on the list, we can use special methods that look at how similar words 
are to each other. It’s like having a friend who can tell if you meant to say “apple” even 
if you accidentally typed “aple” These methods make spell-checking more accurate.

2.Word Suggestion Mechanism:

This mechanism suggests candidate words based on deletion, insertion, switch or 
replace of one/two characters in the original word. A word suggestion mechanism is 
like a helpful tool that tries to guess the correct word when you make a small mistake 
in typing. It does this by suggesting words that are close to what you've written. Here's 
how it works:

1. Deletion: If you accidentally leave out a letter from a word, the mechanism might 
suggest words by adding that missing letter back in. For example, if you wrote 
"elborate" (missing an 'a'), it could suggest "elaborate."

2. Insertion: If you accidentally add an extra letter, the mechanism may suggest words 
by removing that extra letter. If you wrote "elborrate" (with an extra 'r'), it might suggest 
"elaborate."

3. Switch: If you swap two letters by mistake, the mechanism could suggest words 
where those letters are in the correct order. For instance, if you wrote "ealborate" 
(switching 'l' and 'a'), it might suggest "elaborate."

4. Replace:
If you mistakenly use the wrong letter, the mechanism might suggest words by changing 
that incorrect letter to the right one. If you wrote "elaboratw" (replacing 'e' with 't'), it 
could suggest "elaborate."

3.Probability Distribution Mechanism: 

The probability distribution {key(word): value(probability)} is created calculated using 
a large text corpus. Probability of each candidate is found using this distribution and the 
most probable candidate is the final one. when you make a typo or don't spell a word 
quite right, the tool checks all the words that are close to what you typed and picks the 
one with the highest probability. It's like having a smart helper that says, "I see these 
options, but this one is the most common or likely to be what you meant." This helps 
make autocorrect or suggestions more accurate in predicting the words you're trying to 
write.

4.Replace Misspells:

Simple replace the misspelled word with the most probable suggestion.
In simple terms, the tool checks what you wrote, figures out what word is most likely 
based on common usage, and replaces your mistake with the correct word. It's like 
having a clever friend who understands your typos and helps you express yourself more 
accurately.

Algorithms 

1. Probability distribution

2. N gram probability - the N-gram model is looking at groups of words, 
not just single words. These groups can be pairs of words, triplets, or even longer. The 
"N" in N-gram tells us how many words are in each group. 

3. Min Distance probability - These operations can be adding a letter, removing a letter, or changing a letter. The fewer 
operations needed, the closer the words are in terms of their "edit distance." 
For example, turning "cat" into "cot" might require just changing one letter, so the edit 
distance is low. But turning "cat" into "cats" might involve adding a letter, making the 
edit distance a bit higher. 
So, in a nutshell, Edit Distance Algorithms measure how similar two words are by 
counting the minimum number of operations needed to transform one into the other.

4. User Feedback and Learning Algorithm -  it's like having a smart friend who adapts and improves based on the feedback you provide. User feedback helps these algorithms become more accurate and personalized 
in serving your needs.

This project is like a helpful tool that fixes your spelling mistakes as you type. The way 
it's set up now, it's about 52% to 55% accurate in catching and correcting mistakes. To 
make it better, they upgraded the system. Now, it looks not only at the current word but 
also at the word you typed just before it. This little change improved accuracy.
