def coding():
    text=input("entr ur text...")
    r1="ager"
    r2="bwzx"
    if len(text)>3:
        print(r1+text[1:]+text[0]+r2)
    else:
        print(text[::-1])  
def decode():
    text1=input("entr ur decode text")
    print(text1[0]+text1[4:-5])          
coding()
decode()