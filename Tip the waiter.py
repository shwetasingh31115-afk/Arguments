def Totalcalculation(Bill_amount,Tip_per):
    total=Bill_amount*(1+0.01*Tip_per)
    total=round(total,2)
    print(total)
Totalcalculation(140,7)