import pandas as pd

drs_01 = pd.read_csv("Lince/mid_clip.csv")
drs_01.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_02 = pd.read_csv("Lince/mid_clip.csv")
drs_02.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_03 = pd.read_csv("Lince/rear_clip.csv")
drs_03.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_04 = pd.read_csv("Lince/front_clip.csv")
drs_04.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

rho=1.225
V_id01 = 111.112
V_id03 = 97.223
V_id04 = 111.112
V_id08 = 83.334

def fx(x):
    return x*0.5*rho*pow(V_id01,2)*1e-6

#DRS 1 bounding box
a=1518
b=1835
c=-765
d=-445
e=30
f=125

#filter data based on object bounding box
inner01 = drs_01.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner01.loc[inner01.index,"cp"] = fx(inner01["cp"].values)

print(inner01.head())

inner01.to_csv('drs1.csv',index=False)

#DRS 2 bounding box
a=2648
b=3235
c=-670
d=-340
e=320
f=485

#filter data based on object bounding box
inner02 = drs_02.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner02.loc[inner02.index,"cp"] = fx(inner02["cp"].values)

print(inner02.head())

inner02.to_csv('drs2.csv',index=False)

#DRS 3 bounding box
a=4400
b=4650
c=-1085
d=0
e=760
f=900

#filter data based on object bounding box
inner03 = drs_03.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner03.loc[inner03.index,"cp"] = fx(inner03["cp"].values)

print(inner03.head())

inner03.to_csv('drs3.csv',index=False)

#DRS 4 bounding box
a=-875
b=-635
c=-702
d=0
e=75
f=140

#filter data based on object bounding box
inner04 = drs_04.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner04.loc[inner04.index,"cp"] = fx(inner04["cp"].values)

print(inner03.head())

inner04.to_csv('drs4.csv',index=False)

