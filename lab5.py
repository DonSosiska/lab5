import random
import numpy as np
import copy

count = 0
for i in range(100):

    x1_min = -3
    x1_max = 6
    x2_min = 0
    x2_max = 10
    x3_min = -7
    x3_max  = 10

    x_01 = (x1_max + x1_min)/2
    x_02 = (x2_max + x2_min)/2
    x_03 = (x3_max  + x3_min)/2
    x1_del = x1_max - x_01
    x2_del = x2_max - x_02
    x3_del = x3_max  - x_03
    x_Av_max = (x1_max + x2_max + x3_max )/3
    x_Av_min = (x1_min + x2_min + x3_min)/3
    y_max = int(200+x_Av_max)
    y_min = int(200+x_Av_min)
    print()
    print("<>"*40)
    print()
    print("y = b0 + b1*x1 + b2*x2 + b3*x3 + b12*x1*x2 + b13*x1*x3 + b23*x2*x3 + b123*x1*x2*x3 + b11*x1^2 + b22*x2^2 + b33*x3^2\n")
    print("Кодированые значения X:")
    print("{:7} {:6} {:8} {:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7}".format("№","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10"))
    X11 = [-1, -1, -1, -1, 1, 1, 1, 1, -1.215, 1.215, 0, 0, 0, 0, 0]
    X22 = [-1, -1, 1, 1, -1, -1, 1, 1, 0, 0, -1.215, 1.215, 0, 0, 0]
    X33 = [-1, 1, -1, 1, -1, 1, -1, 1, 0, 0, 0, 0, -1.215, 1.215, 0]

    def sumkf2(x1,x2):
        xn = []
        for i in range(len(x1)):
            xn.append(x1[i]*x2[i])
        return xn
    def sumkf3(x1,x2,x3):
        xn = []
        for i in range(len(x1)):
            xn.append(x1[i]*x2[i]*x3[i])
        return xn
    def kv(x):
        xn = []
        for i in range(len(x)):
            xn.append(x[i]*x[i])
        return xn
    X12 = sumkf2(X11,X22)
    X13 = sumkf2(X11,X33)
    X23 = sumkf2(X22,X33)
    X123 = sumkf3(X11,X22,X33)
    X8 = kv(X11)
    X9 = kv(X22)
    X10 = kv(X33)

    X00 = [1]*15
    Xnorm=[X00,X11,X22,X33,sumkf2(X11,X22),sumkf2(X22,X33),sumkf2(X22,X33),sumkf3(X11,X22,X33)]
    for i in range(15):
        print("{:2} {:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7} {:7}".format(i+1,X11[i],X22[i],X33[i],X12[i],X13[i],X23[i],X123[i],round(X8[i],3),round(X9[i],3),round(X10[i],3)))

    print("\nМатрица для m = 15:")
    print("{:4} {:7} {:7} {:9} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8}".format("№","X0","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10","Y1","Y2","Y3"))

    X1 = [x1_min, x1_min, x1_min, x1_min, x1_max, x1_max, x1_max, x1_max, -1.215*x1_del+x_01, 1.215*x1_del+x_01, x_01, x_01, x_01, x_01, x_01]
    X2 = [x2_min, x2_min, x2_max, x2_max, x2_min, x2_min, x2_max, x2_max, x_02, x_02, -1.215*x2_del+x_02, 1.215*x2_del+x_02, x_02, x_02, x_02]
    X3 = [x3_min, x3_max , x3_min, x3_max , x3_min, x3_max , x3_min, x3_max , x_03, x_03, x_03, x_03, -1.215*x3_del+x_03, 1.215*x3_del+x_03, x_03]

    Y1 = [random.randrange(y_min,y_max, 1) for i in range(15)]
    Y2 = [random.randrange(y_min,y_max, 1) for i in range(15)]
    Y3 = [random.randrange(y_min,y_max, 1) for i in range(15)]

    X12 = sumkf2(X1,X2)
    X13 = sumkf2(X1,X3)
    X23 = sumkf2(X2,X3)
    X123 = sumkf3(X1,X2,X3)
    X8 = kv(X1)
    X9 = kv(X2)
    X10 = kv(X3)
    X0 = [1]*15
    Xall=[X0,X1,X2,X3,X12,X13,X23,X123,X8,X9,X10]

    for i in range(15):
        print("{:1} {:5} {:7} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} {:8} ".format(i+1,X0[i],round(X1[i],3),round(X2[i],3),round(X3[i],3),round(X12[i],3),round(X13[i],3),round(X23[i],3),round(X123[i],3),round(X8[i],3),round(X9[i],3),round(X10[i],3),Y1[i],Y2[i],Y3[i]))

    print("\nCредние значения отклика функции по рядкам: ")

    def yav(i):
        return (Y1[i-1]+Y2[i-1]+Y3[i-1])/3

    y1av1 = yav(1)
    y2av2 = yav(2)
    y3av3 = yav(3)
    y4av4 = yav(4)
    y5av5 = yav(5)
    y6av6 = yav(6)
    y7av7 = yav(7)
    y8av8 = yav(8)
    y9av9 = yav(9)
    y10av10 = yav(10)
    y11av11 = yav(11)
    y12av12 = yav(12)
    y13av13 = yav(13)
    y14av14 = yav(14)
    y15av15 = yav(15)

    mx1 = sum(X1)/15
    mx2 = sum(X2)/15
    mx3 = sum(X3)/15

    Yall=[y1av1, y2av2, y3av3, y4av4, y5av5, y6av6, y7av7, y8av8, y9av9, y10av10, y11av11, y12av12, y13av13, y14av14, y15av15]

    def mni(j):
        s=0
        for i in range(len(Xall[j])):
            s=s+Xall[j][i]
        return s/len(Xall[j])

    def mni2(j,k):
        s=0
        for i in range(len(Xall[j])):
            s=s+Xall[j][i]*Xall[k][i]
        return s/len(Xall[j])

    Yalls=sum(Yall)/15
    def kmn(j):
        s=0
        for i in range(len(Yall)):
            s=s+yav(i)*Xall[j][i]
        return s/len(Yall)

    m=[[0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0]]

    m[0][0] = 1

    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == 0:
                m[i][j] = m[j][i] = mni(j)
            if (i != 0) and (j != 0):
                m[i][j] = mni2(i,j)

    k = [Yalls]
    for i in range(10):
        k.append(kmn(i+1))
    b0m = []
    b = []

    for i in range(11):
        b0m.append(copy.copy(m))
        b0m[i][i] = k
        b.append(np.linalg.det(b0m[i])/np.linalg.det(m))

    for i in range(15):
        print("y"+str(i+1)+"av"+str(i+1)+"="+str(round(b[0] + b[1]*X1[i]+b[2]*X2[i]+b[3]*X3[i]+b[4]*X1[i]*X2[i]+b[5]*X1[i]*X3[i]+b[6]*X2[i]*X3[i]+b[7]*X1[i]*X2[i]*X3[i]+b[8]*X8[i]+b[9]*X9[i]+b[10]*X10[i],2))+"="+ str(round(y1av1,2)))
    print("Значения приблизительно совпадают")

    print("\nДисперсия по рядкам:")
    d=[]
    for i in range(15):
        d.append(((Y1[i] - y1av1)**2 + (Y2[i] - y2av2)**2 + (Y3[i] - y3av3)**2)/3)
        print("d"+str(i+1)+"="+str(round(d[i],2)))

    m = 3
    Gp = max(d)/sum(d)
    f1 = m-1
    f2 = N = 15
    Gt = 0.3346
    if Gp < Gt:
        print("Дисперсия однородная")
    else:
        print("Дисперсия неоднородная")

    print("\nКритерий Стьдента:")
    sb = sum(d)/N
    ssbs = sb/N*m
    sbs = ssbs**0.5

    beta0 = (y1av1*1+y2av2*1+y3av3*1+y4av4*1+y5av5*1+y6av6*1+y7av7*1+y8av8*1+y9av9*(-1.215)+y10av10*1.215+y11av11*0+y12av12*0+y13av13*0+y14av14*0+y15av15*0)/15
    beta1 = (y1av1*(-1)+y2av2*(-1)+y3av3*(-1)+y4av4*(-1)+y5av5*1+y6av6*1+y7av7*1+y8av8*1+y9av9*0+y10av10*0+y11av11*(-1.215)+y12av12*1.215+y13av13*0+y14av14*0+y15av15*0)/15
    beta2 = (y1av1*(-1)+y2av2*(-1)+y3av3*1+y4av4*1+y5av5*(-1)+y6av6*(-1)+y7av7*1+y8av8*1+y9av9*0+y10av10*0+y11av11*0+y12av12*0+y13av13*(-1.215)+y14av14*1.215+y15av15*0)/15
    beta3 = (y1av1*(-1)+y2av2*1+y3av3*(-1)+y4av4*1+y5av5*(-1)+y6av6*1+y7av7*(-1)+y8av8*1)/15
    beta4 = (y1av1*1+y2av2*1+y3av3*(-1)+y4av4*(-1)+y5av5*(-1)+y6av6*(-1)+y7av7*1+y8av8*1)/15
    beta5 = (y1av1*1+y2av2*(-1)+y3av3*1+y4av4*(-1)+y5av5*(-1)+y6av6*1+y7av7*(-1)+y8av8*1)/15
    beta6 = (y1av1*1+y2av2*(-1)+y3av3*(-1)+y4av4*1+y5av5*1+y6av6*(-1)+y7av7*(-1)+y8av8*1)/15
    beta7 = (y1av1*(-1)+y2av2*1+y3av3*1+y4av4*(-1)+y5av5*1+y6av6*(-1)+y7av7*(-1)+y8av8*1)/15
    beta8 = (y1av1*1+y2av2*1+y3av3*1+y4av4*1+y5av5*1+y6av6*1+y7av7*1+y8av8*1+y9av9*1.46723+y10av10*1.46723)/15
    beta9 = (y1av1*1+y2av2*1+y3av3*1+y4av4*1+y5av5*1+y6av6*1+y7av7*1+y8av8*1+y11av11*1.46723+y12av12*1.46723)/15
    beta10 = (y1av1*1+y2av2*1+y3av3*1+y4av4*1+y5av5*1+y6av6*1+y7av7*1+y8av8*1+y13av13*1.46723+y14av14*1.46723)/15

    beta = [beta0,beta1,beta2,beta3,beta4,beta5,beta6,beta7,beta8,beta9,beta10]

    t = []
    for i in range(11):
        t.append(abs(beta[i])/sbs)

    f3 = f1*f2
    ttabl  = 2.042
    print("f3 = f1*f2, с таблицы tтабл = 2.306")
    d=11
    for i in range(11):
        if (t[i]<ttabl):
            print("t"+str(i)+"<ttabl, b"+str(i)+" не значимый")
            b[i]=0
            d=d-1
    yy1 = b[0]+b[1]*x1_min+b[2]*x2_min+b[3]*x3_min+b[4]*x1_min*x2_min+b[5]*x1_min*x3_min+b[6]*x2_min*x3_min+b[7]*x1_min*x2_min*x3_min+b[8]*x1_min*x1_min+b[9]*x2_min*x2_min+b[10]*x3_min*x3_min
    yy2 = b[0]+b[1]*x1_min+b[2]*x2_min+b[3]*x3_max +b[4]*x1_min*x2_min+b[5]*x1_min*x3_max +b[6]*x2_min*x3_max +b[7]*x1_min*x2_min*x3_max +b[8]*x1_min*x1_min+b[9]*x2_min*x2_min+b[10]*x3_max *x3_max
    yy3 = b[0]+b[1]*x1_min+b[2]*x2_max+b[3]*x3_min+b[4]*x1_min*x2_max+b[5]*x1_min*x3_min+b[6]*x2_max*x3_min+b[7]*x1_min*x2_max*x3_min+b[8]*x1_min*x1_min+b[9]*x2_max*x2_max+b[10]*x3_min*x3_min
    yy4 = b[0]+b[1]*x1_min+b[2]*x2_max+b[3]*x3_max +b[4]*x1_min*x2_max+b[5]*x1_min*x3_max +b[6]*x2_max*x3_max +b[7]*x1_min*x2_max*x3_max +b[8]*x1_min*x1_min+b[9]*x2_max*x2_max+b[10]*x3_max *x3_max
    yy5 = b[0]+b[1]*x1_max+b[2]*x2_min+b[3]*x3_min+b[4]*x1_max*x2_min+b[5]*x1_max*x3_min+b[6]*x2_min*x3_min+b[7]*x1_max*x2_min*x3_min+b[8]*x1_max*x1_max+b[9]*x2_min*x2_min+b[10]*x3_min*x3_min
    yy6 = b[0]+b[1]*x1_max+b[2]*x2_min+b[3]*x3_max +b[4]*x1_max*x2_min+b[5]*x1_max*x3_max +b[6]*x2_min*x3_max +b[7]*x1_max*x2_min*x3_max +b[8]*x1_max*x1_max+b[9]*x2_min*x2_min+b[10]*x3_min*x3_max
    yy7 = b[0]+b[1]*x1_max+b[2]*x2_max+b[3]*x3_min+b[4]*x1_max*x2_max+b[5]*x1_max*x3_min+b[6]*x2_max*x3_min+b[7]*x1_max*x2_min*x3_max +b[8]*x1_max*x1_max+b[9]*x2_max*x2_max+b[10]*x3_min*x3_min
    yy8 = b[0]+b[1]*x1_max+b[2]*x2_max+b[3]*x3_max +b[4]*x1_max*x2_max+b[5]*x1_max*x3_max +b[6]*x2_max*x3_max +b[7]*x1_max*x2_max*x3_max +b[8]*x1_max*x1_max+b[9]*x2_max*x2_max+b[10]*x3_min*x3_max
    yy9 = b[0]+b[1]*X1[8]+b[2]*X2[8]+b[3]*X3[8]+b[4]*X12[8]+b[5]*X13[8]+b[6]*X23[8]+b[7]*X123[8]+b[8]*X8[8]+b[9]*X9[8]+b[10]*X10[8]
    yy10 = b[0]+b[1]*X1[9]+b[2]*X2[9]+b[3]*X3[9]+b[4]*X12[9]+b[5]*X13[9]+b[6]*X23[9]+b[7]*X123[9]+b[8]*X8[9]+b[9]*X9[9]+b[10]*X10[9]
    yy11 = b[0]+b[1]*X1[10]+b[2]*X2[10]+b[3]*X3[10]+b[4]*X12[10]+b[5]*X13[10]+b[6]*X23[10]+b[7]*X123[10]+b[8]*X8[10]+b[9]*X9[10]+b[10]*X10[10]
    yy12 = b[0]+b[1]*X1[11]+b[2]*X2[11]+b[3]*X3[11]+b[4]*X12[11]+b[5]*X13[11]+b[6]*X23[11]+b[7]*X123[11]+b[8]*X8[11]+b[9]*X9[11]+b[10]*X10[11]
    yy13 = b[0]+b[1]*X1[12]+b[2]*X2[12]+b[3]*X3[12]+b[4]*X12[12]+b[5]*X13[12]+b[6]*X23[12]+b[7]*X123[12]+b[8]*X8[12]+b[9]*X9[12]+b[10]*X10[12]
    yy14 = b[0]+b[1]*X1[13]+b[2]*X2[13]+b[3]*X3[13]+b[4]*X12[13]+b[5]*X13[13]+b[6]*X23[13]+b[7]*X123[13]+b[8]*X8[13]+b[9]*X9[13]+b[10]*X10[13]
    yy15 = b[0]+b[1]*X1[14]+b[2]*X2[14]+b[3]*X3[14]+b[4]*X12[14]+b[5]*X13[14]+b[6]*X23[14]+b[7]*X123[14]+b[8]*X8[14]+b[9]*X9[14]+b[10]*X10[14]

    print("\nКритерий Фишера")
    print(d," значимых коэф.")
    f4 = N - d
    sad = ((yy1-y1av1)**2+(yy2-y2av2)**2+(yy3-y3av3)**2+(yy4-y4av4)**2+(yy5-y5av5)**2+(yy6-y6av6)**2+(yy7-y7av7)**2+(yy8-y8av8)**2+ (yy9-y9av9)**2+(yy10-y10av10)**2+(yy11-y11av11)**2+(yy12-y12av12)**2+(yy13-y13av13)**2+(yy14-y14av14)**2+(yy15-y15av15)**2)*(m/(N-d))
    Fp = sad/sb
    print("Fp=", round(Fp,3))
    F=[4.2,3.3,2.9,2.7,2.5,2.4,2.1,1.9]
    Fi=[1,2,3,4,5,6,12,24]
    dif=100
    counter=0

    for i in range(len(F)):
        if abs(Fi[i]-(i+1))<dif:
            dif= abs(Fi[i]-i)
            counter=i

    Ft=F[counter]
    print("Ft берём с таблицы (16 рядок, ",f4," столбец) Ft = ",Ft)
    if Fp>Ft:
        print("Fp = ",round(Fp,2),">Ft",Ft,"\nУравнение неадекватно оригиналу")
    else:
        count = count + 1
        print("Fp = ",round(Fp,2),"<Ft",Ft,"\nУравнение адекватно оригиналу")

print("-"*80)
print("Адекватное уравнение попадается в ",count,"%")
