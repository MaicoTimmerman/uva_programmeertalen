def judicium(mark):
    if float(mark)<5.5:
    	suffix="(Failed)"
    elif float(mark)>=8.5:
   		suffix="(Cum Laude)"
    elif float(mark)>= 7.5 and float(mark)<8.5:
    	suffix="(With Honors)"
    else:
    	suffix=""
    print "Uitslag: {} {}".format(mark,suffix)

judicium(10.0)
judicium(8.5)
judicium(8.4)
judicium(7.5)
judicium(7.4)
judicium(5)

