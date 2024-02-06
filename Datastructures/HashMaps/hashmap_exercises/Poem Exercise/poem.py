
#QUESTION

"""poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure 
out why you selected that specific data structure. """


file_path=r"Datastructures\HashMaps\hashmap_exercises\Poem Exercise\poem.txt"

word_count={}
with open(file_path, "r") as f:
    poem= f.read()
words = poem.split()
for word in words:
    word=word.strip(",.!?:;-").lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

for word,count in word_count.items():
    print(f"{word}: {count}")


