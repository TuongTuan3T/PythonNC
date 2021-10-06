def skip_header(reader):
    '''Skip the header in reader r, and return the first
    real piece of data.'''
    
    # Read the description line and then the comment lines.
    line = reader.readline()    
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline() 
    # Now line contains the first real piece of data.
    return line

def process_file(reader):
    '''(file open for reading) -> NoneType
    Read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with '#', 
    then a sequence of data.
    '''

    # Find the first piece of data.
    line = skip_header(reader).strip()
    print(line)
    # Read the rest of the data.
    for line in reader:
        line = line.strip()
        print(line)

input_file = open('d:/python nc/PythonNC/Lab03/Chuong10/alkaline_metals.txt', 'r')
process_file(input_file)
input_file.close()