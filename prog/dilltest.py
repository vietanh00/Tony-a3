import dill
filename = ".\prog\macros_exec.pickle"
finding = ""
all_macros = []
f =  open(filename, 'rb')
while True:
    try:
        macro_obj = dill.load(f)
        all_macros.append(macro_obj)
        print(macro_obj[0])
    except EOFError:
        break
f.close()