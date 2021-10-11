d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
d3 = {}
for key in d2.keys():
    if key in d1.keys():
        #print(key," got added")
        d3[key] = d2[key] + d1[key]
    else:
        #print(key," only in d2")
        d3[key] = d2[key]
        
for key in d1.keys():
    if key not in d2.keys():
        #print(key," only in d1")
        d3[key] = d1[key]

print(d3)