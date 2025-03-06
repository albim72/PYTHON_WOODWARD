class FileManager:
    def __init__(self,filename,mode,encode):
        self.encode = encode
        self.mode = mode
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write("to jest ważna informacja\n")

print(f.closed)

with open("drugi.txt","a",encoding="utf-8") as h:
    h.write("drugi plik txt!\n")

print(h.closed)

h = open("drugi.txt","a",encoding="utf-8")
h.write("kolejna linia...\n")
h.close()

print(h.closed)

with FileManager("drugi.txt","r","utf-8") as f:
    print(f.read())

print(f.closed)
