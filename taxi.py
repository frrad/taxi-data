filename   = '../trip_data_1.csv'
filelength = 14776616


percentcounter = 0
filecounter    = 0
def count():
    global filecounter
    global percentcounter
    filecounter += 1
    if int(100* filecounter/filelength) > percentcounter:
        percentcounter = int(100*filecounter/filelength)
        print percentcounter, '%'
    
    


f = open(filename, 'r')

source = f.next()

print source

for line in f:
    count()

