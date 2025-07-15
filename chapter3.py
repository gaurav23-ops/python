name = "gaurav"
print(name[-4:]) # negative
print(name[2:5]) # posstive
print(name[2:4]) # posstive

# SLICING WITH SKIP VALUE
name = "guraavkonadne"
print (name[1:9:4])

# len
name = "gaurav"
print(len(name))
print (name.endswith("rav"))#it tell as end of word
print (name.startswith("gau"))#it tell as start of word

# replace

a = "gaurav"
a=a.replace("gaurav","kondane")
print(a)

# splict
b = "gaurav kondane"
n= b.maketrans("gau","GAU")
print(b.translate(n))


# escape str character 
a = "gaurav is good boy also not bad boy so  i can hired you"
print(a)



