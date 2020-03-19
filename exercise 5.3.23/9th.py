song = "The rain in Spain..."
print(song)

print(song.split()) #*.split splits the words in the assigned variable.

print(" ".join(song.split())) #*.join appends different lists.

#in the end, they're same, but if we change sth before the .join, then it will produce different as such:
print(";".join(song.split()))