import commands
def getSigKey(fileName):
    (status, output) = commands.getstatusoutput("cat " + fileName)
    return  output
if __name__ == "__main__":
    #sigKey(1, 'maxl', '1255610113')
    # sigKey(1, 'test2', '1255610839')
    print getSigKey("./1255610113_maxl_sig")
