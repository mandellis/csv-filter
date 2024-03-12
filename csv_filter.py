# Copyright (c) 2023-2024 - Lince srl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "Simone Mandelli"
__maintainer__ = __author__


import pandas as pd

# Definitions
readFileName  = ('mid_clip.csv',
               'rear_clip.csv',
               'front_clip.csv')

# Fluid properties
rho=1.225 #Density (air at 25°)
v = 111.112 #Velocity (400km/h) at 350 -> 97.223

def fx(x):
    return x*0.5*rho*pow(v,2)*1e-6

# Read data and create 
drs_01 = pd.read_csv(readFileName[0])
drs_01.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_02 = pd.read_csv(readFileName[1])
drs_02.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_03 = pd.read_csv(readFileName[2])
drs_03.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

drs_04 = pd.read_csv(readFileName[3])
drs_04.rename(columns={'Points:0':'X','Points:1':'Y','Points:2':'Z','pressure-coefficient':'cp'},inplace=True)

#DRS 1 bounding box close
a=1518
b=1835
c=-765
d=-445
e=30
f=125
"""""
#DRS 1 bounding box open
a=1516
b=1836
c=-765
d=-445
e=65
f=85
"""""
#filter data based on object bounding box
inner01 = drs_01.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner01.loc[inner01.index,"cp"] = fx(inner01["cp"].values)

print(inner01.head())

inner01.to_csv('drs1.csv',index=False)

#DRS 2 bounding box close
a=2648
b=3235
c=-670
d=-340
e=320
f=485
"""""
#DRS 2 bounding box open
a=2648
b=3235
c=-670
d=-340
e=170
f=360
"""""
#filter data based on object bounding box
inner02 = drs_02.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner02.loc[inner02.index,"cp"] = fx(inner02["cp"].values)

print(inner02.head())

inner02.to_csv('drs2.csv',index=False)

#DRS 3 bounding box close
a=4400
b=4650
c=-1085
d=1085
e=760
f=925
"""""
#DRS 3 bounding box open
a=4400
b=4650
c=-1085
d=1085
e=810
f=925
"""""
#filter data based on object bounding box
inner03 = drs_03.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner03.loc[inner03.index,"cp"] = fx(inner03["cp"].values)

print(inner03.head())

inner03.to_csv('drs3.csv',index=False)

#DRS 4 bounding box close
a=-875
b=-635
c=-702
d=702
e=75
f=140

"""""
#DRS 4 bounding box open
a=-875
b=-635
c=-702
d=702
e=35
f=125
"""
#filter data based on object bounding box
inner04 = drs_04.query(f"{a} < X < {b} and {c} < Y < {d} and {e} < Z < {f}") 

#change value 
inner04.loc[inner04.index,"cp"] = fx(inner04["cp"].values)

print(inner03.head())

inner04.to_csv('drs4.csv',index=False)

inner_finale = pd.concat([inner01,inner02,inner03,inner04])

inner_finale.to_csv('drs.csv',index=False)