def fre(text):
    xdict = {}
    for i in text:
        if i in xdict:
            xdict[i] += 1
        else:
            xdict[i] = 1
    return xdict
def buil_tree(frequency):
    trees=[[weight,[char,""]] for char, weight in frequency.items()]
    print(trees)
    while len(trees)>1:
        trees.sort()
        print("sorted is:")
        print(trees)
        left=trees.pop(0) #first two smallest weights
        right=trees.pop(0)
        for pair in left[1:]:
            print("inside left")
            print(pair)
            pair[1]='0'+pair[1]
            print("pair in left")
            print(pair)
        print("out of frst left")
        for pair in right[1:]:
            print("inside right")
            print(pair)
            pair[1] = '1' + pair[1]
            print("pair in right")
            print(pair)
        trees.append([left[0]+right[0]]+left[1:]+right[1:])
        print("after merge")
        print(trees)
    return trees[0] if trees else []
def generate_codes(tree):
    return dict((char,code) for char, code in tree[1:])
def encode(text,codes):
    return ' '.join(codes[char] for char in text)
def huffman_coding(text):
    frequency=fre(text)
    huffman_tree=buil_tree(frequency)
    codes=generate_codes(huffman_tree)
    encode_text=encode(text,codes)
    return codes,encode_text
text="AAB"
codes,encode_text=huffman_coding(text)
print("frequency:",fre(text))
print("huffman codes:",codes)
print("encoded text after huffman encoding:",encode_text)

