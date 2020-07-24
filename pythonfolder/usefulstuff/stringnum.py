string="abbcccddddeeeeeffffffggggggg"
lens=len(string)
dictinary={}
for i in string:
    lod=string.count(i)
    dictinary.update({i:lod}) 
print(dictinary)

