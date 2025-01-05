Length = input("Pleas type Length : \n")
Width = input("Pleas type Width : \n")
Price = input("how mcuh for 1 meter? : \n")
#تحويل البيانات النصية الى ارقام عشرية
str_Length =float(Length)
str_Width = float(Width)
str_Price = float(Price)
#اقوم اسوي العمليات الحسابية
Area = str_Length*str_Width 
Pricetootl= Area *str_Price 
#ارجع احول الارقام الى نصوص عشلن اطبعهم
str_area= str(Area)
str_Pricetootl=str(Pricetootl)
#نبدا بالطباعة
print("The total area is :" + str_area )
print("Give the guy :" + str_Pricetootl + "$")
