import os

## write data on an external file
def writeData():
    data = '\nHello world!' ## data you want to put in the file.
    with open('test.txt','a') as f: ## while the file test.txt is open: call the file 'f'. The 'a' means append.
        f.write(data) ##write the data onto the file 'f'
        f.close() ## close the file


## Open an external file and print its contents
def openFile(): 
    with open('test.txt','r') as f: ## while the file test.txt is open: call the file 'f'. The 'r' means read only.
        data = f.read() ## read the file 'f' and store the content as the vasriable 'data'
        print(data)
        f.close() ## close the file



if __name__ == '__main__':
    writeData()
    openFile()
