#import pdb

# sandwich s2 between s1 and encluse in double quotes
def combine(s1,s2):
    s3 = s1 + s2 + s1
    s3 = """ + s3 + """
    return s3

def main():
    a = "aaa"
    #pdb.set_trace()
    b = "bbb"
    c = "ccc"
    final = combine(a,b)
    print final

if __name__ == "__main__":
    main()
