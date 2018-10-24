def myAPI(filename):
    f = open('%s.txt'%filename)
    censusAPIkey = f.read()
    return censusAPIkey