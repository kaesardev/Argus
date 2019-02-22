'''
    FILES FLOW LIBRARY
'''
import gc

def mountData(data):
    ''' Assembles a dictionary from the string '''
    data += '\n'
    structure = {}
    obj = []
    attr = str()
    flag = True
    key = ''
    for char in data:
        if char == '\n':
            obj.append(attr)
            attr = str()
            if len(obj) > 1:
                structure[key] = tuple(obj)
                flag = True
                obj = []
        elif char == '\t':
            if flag:
                key = attr
                flag = False
            obj.append(attr)
            attr = str()
        else:
            attr += char
    gc.collect()
    return structure

def mountDataArray2D(data):
    ''' Assembles a list from the string '''
    data += '\n'
    structure = []
    obj = []
    attr = str()
    for char in data:
        if char == '\n':
            if attr != '':
                obj.append(attr)
                attr = str()
            if len(obj) > 1:
                structure.append(tuple(obj))
                obj = []
        elif char == '\t':
            obj.append(attr)
            attr = str()
        else:
            attr += char
    gc.collect()
    return structure

def mountDataArray1D(data):
    ''' Assembles a list from the string '''
    data += '\n'
    structure = []
    attr = str()
    for char in data:
        if char == '\n':
            if attr != '':
                structure.append(attr)
                attr = str()
        else:
            attr += char
    gc.collect()
    return structure

def unmountDataArray(structure):
    ''' Unmount a array to string '''
    structure_size = len(structure)
    if structure_size > 0:
        obj_size = len(structure[0])
    data = str()
    i = 0
    while i < structure_size:
        j = 0
        while j < obj_size:
            data += str(structure[i][j]) + ('\t' if j < (obj_size - 1) else '')
            j += 1
        data += '\n'
        i += 1
    gc.collect()
    return data

def unmountData(structure):
    ''' Unmount a dictionary to string '''
    if len(structure) > 0:
        obj_size = len(structure[list(structure.keys())[0]])
    data = str()
    for key in structure.keys():
        i = 0
        for attr in structure[key]:
            data += str(attr) + ('\t' if i < (obj_size - 1) else '')
            i += 1
        data += '\n'
    gc.collect()
    return data

def importData(filepath):
    '''' Import string from a file '''
    data = str()
    try:
        file = open(filepath, 'r', encoding="utf-8")
        data = file.read()
        file.close()
        #print('Success: import file', filepath)
    except:
        print('Error: Could not import file data. Filepath:', filepath)
    return data

def exportData(filepath, data):
    ''' Export string from a file '''
    try:
        file = open(filepath, 'w', encoding="utf-8")
        file.write(data)
        file.close()
        #print('Success: export file', filepath)
    except:
        print('Error: could not export data to file. Filepath:', filepath)
