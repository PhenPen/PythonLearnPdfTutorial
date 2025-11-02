import builtins, inspect

#print(dir(list))

for f in dir(list): 
    if f.startswith("_") or f.startswith("__"):
        continue
    print(f)

print()
print()



print()
print()

# for getting all functions
builtins_func = [f for f in dir(builtins) if callable(getattr(builtins,f))]

working_func = []
func_sig = []
sample = [1,2,3]

for f in builtins_func:
    func = getattr(builtins,f)
    try:
        func(sample)
    except Exception:
        continue
    else:
        working_func.append(f)
        
for f in builtins_func:
    func = getattr(builtins)
    try:
        sig = inspect.signature(func)
    except Exception:
            continue
    else:
        func_sig.append(str(sig))
        

print(working_func,func_sig)
        
