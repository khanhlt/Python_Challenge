s = ''.join([line.rstrip() for line in open('bodyguard.txt')])
for i in range(4, len(s) - 4):
    if (s[i-4].islower()):
        if (s[i-3].isupper()):
            if(s[i-2].isupper()):
                if(s[i-1].isupper()):
                    if(s[i].islower()):
                        if(s[i+1].isupper()):
                            if(s[i+2].isupper()):
                                if(s[i+3].isupper()):
                                    if(s[i+4].islower()):
                                        print(s[i])

# need a smart code though