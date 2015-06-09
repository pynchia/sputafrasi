import sys

PREFIX = ' '

def main(filename):
    fout = open('newentries.sql', 'w')
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line[0] == PREFIX:
                if line[1] == PREFIX:
                    if line[2] == PREFIX: # Time
                        table = 'time'
                        line = line[3:]
                    else: # # Place
                        table = 'place'
                        line = line[2:]
                else: # Pubfig
                    table = 'pubfig'
                    line = line[1:]
            else: # Thing
                table = 'thing'
            line = line.replace("'","''")
            outs = "INSERT INTO %s (name) VALUES ('%s');\n" % (table, line)
            #print outs
            fout.write(outs)
        fout.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print "Usage: gensql.py filename"