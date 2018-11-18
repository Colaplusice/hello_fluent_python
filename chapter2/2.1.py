symbols='#$%^&'

codes=[ord(symol) for symol in symbols]

print(codes)
s= list(filter(lambda c:c>175,map(ord,symbols)))

print(s)