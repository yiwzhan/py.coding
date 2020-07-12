def moon_weight(hmgey):
    weight=input("how much do you weigh: ")
    for year in range(1,16):
        weight = weight + hmgey
        cw=int(weight)*0.165
        print("Year %s =%s weight" % (year,cw))
moon_weight(8)