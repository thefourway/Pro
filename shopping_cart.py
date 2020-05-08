goods = ([1,'粉蒸肉',3.00],[2,'贡糕',5.00],[3,'茶叶',4.00])

print('------xx特色小吃店-------')
print('编号    商品    单价')
for i in range(len(goods)):
       print('{:<5}'.format(goods[i][0]),'{:^7s}'.format(goods[i][1]),'{:>7.2f}'.format(goods[i][2]))

changeGoodList=[]

flag=True

while flag:
    changeGoodNumber = int(input("请选择你要购买的商品序号:"))
    changeGoodQuantity = int(input("请选择购买的商品数量:"))
    if changeGoodNumber==0 and changeGoodQuantity==0:
       break
    newlist = [(goods[changeGoodNumber-1][1]),changeGoodQuantity,(changeGoodQuantity*goods[changeGoodNumber-1][2])]
    changeGoodList.append(newlist)
   
    
print('------购物清单-------')
print('商品    数量    金额')
print('{:<5s}'.format(changeGoodList[0][0]),'{:^4d}'.format(changeGoodList[0][1]),'{:>7.2f}'.format(changeGoodList[0][2]))
for i in range(len(changeGoodList)-1):
    print('{:<5s}'.format(changeGoodList[i+1][0]),'{:^4d}'.format(changeGoodList[i+1][1]),'{:>7.2f}'.format(changeGoodList[i+1][2]))

totalprice = 0
for i in range(len(changeGoodList)):
    totalprice = totalprice + changeGoodList[i][2]
    
print('商品总价为：','{:.2f}'.format(totalprice))
print('今日折扣九折，折扣后价格为：''{:.2f}'.format(totalprice*0.9))

