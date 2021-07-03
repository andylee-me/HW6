que = input("請輸入要判斷的詞:")
que = list(que)
w = len(que)
z = -1
x = 0
while w//2 != x: 
    if que[x] == que[z]:
        x += 1
        z -= 1
    elif que[x] != que[z]:
        print("不是回文")
        break
if w//2 == x:
    print("是回文")
    
         
    








