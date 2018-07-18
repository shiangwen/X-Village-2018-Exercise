

def caesar_cipher(words,number):
    
    words=str(words)
    number=int(number)
    x=[]
    for i in range(len(words)):
        x.append(chr(ord(words[i])+number))
    return''.join(x)

print(caesar_cipher('xvillage',3))
'''

    str_change = str_raw.lower()

    abc_all=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index_number=



caesar_cipher("xvillage", 3)




def caesar_cipher(words, bias):
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    caesar = op.itemgetter(*[(alphabets.index(i)+ 3)% len(alphabets) for i in words])
    
    return "".join(list(caesar(alphabets)))

print(caesar_cipher("xvillage", 3))


'''
'''
def key():
    a=input("請輸入明文：")
    b=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*len(a)
    c=[]
    
    for i in a:
        for j in b:
            if j==i:
                d=int(b.index(j))+3
                c.append(b[d])
                break
    str=''
    print(str.join(c))

key()
'''
