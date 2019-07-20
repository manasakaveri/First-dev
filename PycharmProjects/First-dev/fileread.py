def file_read(fname):
    with open(fname) as f:
        content_list=f.readline()
        print("content_list")

file_read(\'test.txt\")



fo =open("file.txt",r)
for line in fo.readlines():
    print line