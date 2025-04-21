#MapPlot.py
#Name: Tim Weixelman
#Date: 4/20
#Assignment: Lab 10 

import music
import pandas
import matplotlib.pyplot as plt

music = music.get_music()

familiar = []
hot = []


for name in music:
    familiarity = name["artist"]["familiarity"]
    hotttnesss = name["song"]["hotttnesss"]
    if hotttnesss >0:
        familiar.append(familiarity)
        hot.append(hotttnesss)

df = pandas.DataFrame({"familiarity": familiar,
                        "hotttnesss": hot})

print(df)

#plt.plot(familiarity, hotttnesss, 'ro')
df.plot(kind = 'scatter', x = 'familiarity' , y = 'hotttnesss')
plt.savefig("output")
"""The graph shows that in general, the more familiar the artist, the more hot the song is. For the most part, a non familar artist doesn't make a hot song"""