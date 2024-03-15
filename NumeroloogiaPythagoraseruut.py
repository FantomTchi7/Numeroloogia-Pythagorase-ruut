import datetime
import MuMoodul

aasta=int(input("Sisesta aasta: "))
kuu=int(input("Sisesta kuu: "))
paev=int(input("Sisesta päev: "))
kuupaev=datetime.date(aasta,kuu,paev)

aastaEraldatud=MuMoodul.IntToListInt(kuupaev.year)
kuuEraldatud=MuMoodul.IntToListInt(kuupaev.month)
paevEraldatud=MuMoodul.IntToListInt(kuupaev.day)

aastaSumma=sum(aastaEraldatud)
kuuSumma=sum(kuuEraldatud)
paevSumma=sum(paevEraldatud)

# 1) Складываем цифры дня и месяца рождения: 5+1+2=8.
# 2) Складываем цифры года: 1+9+7+9=26.
# 3) Складываем полученные числа: 8+26=34 - это 1 рабочее число.
int1=paevSumma+kuuSumma+aastaSumma
print(int1)
# 4) Складываем цифры первого рабочего числа: 3+4=7 - это 2 рабочее число.
int2=sum(MuMoodul.IntToListInt(int1))
print(int2)
# 5) Из первого рабочего числа вычитаем удвоенную первую цифру дня рождения: 34-2*5=24 - это 3 рабочее число.
int3=int1-(int(paevEraldatud[0])*2)
print(int3)
# 6) Складываем цифры третьего рабочего числа: 2+4=6 - это 4 рабочее число. 
int4=sum(MuMoodul.IntToListInt(int3))
print(int4)

esimeneRida=int(str(kuupaev.day)+str(kuupaev.month)+str(kuupaev.year))
print("Esimene rida:",esimeneRida)
MuMoodul.CountNumber(esimeneRida)
teineRida=int(str(int1)+str(int2)+str(int3)+str(int4))
print("Teine ride",teineRida)
MuMoodul.CountNumber(teineRida)