# debug_builtins_check.py
import builtins, inspect
import sys
from io import StringIO

# sample to test; change to [], ["a","b"], "abc", 5 etc.
sample = [1, 2, 3]

# skip some builtins that cause heavy side-effects or need special env
SKIP = {
    "open", "print", "input", "exec", "eval", "compile", "breakpoint", "help",
    "__import__", "exit", "quit"
}

# 1) get all callable names in builtins
builtin_names = [name for name in dir(builtins) if callable(getattr(builtins, name))]
print("Total callable names in builtins:", len(builtin_names))

# 2) prepare containers
working_names = []
working_sigs = []
errors = []   # store (name, error_type, error_message)

# 3) try each builtin
for name in builtin_names:
    if name in SKIP:
        print("skipping", name)
        continue

    func = getattr(builtins, name)

    # Try calling safely: capture stdout so print() won't spam if missed
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        # Some callables are classes (e.g., list, int) — those are ok to call with sample
        # Others will raise TypeError or ValueError; we capture that.
        func(sample)
    except Exception as e:
        # record the exception for debugging
        errors.append((name, type(e).__name__, str(e)))
        # restore stdout and continue
        sys.stdout = old_stdout
        continue
    else:
        # restore stdout (no side-effect output will be shown)
        sys.stdout = old_stdout

        # try to get signature (some builtins may not expose inspectable sigs)
        try:
            sig = str(inspect.signature(func))
        except Exception as e:
            errors.append((name, "SignatureError", str(e)))
            sig = "<no-signature>"

        working_names.append(name)
        working_sigs.append(sig)

# 4) Quick summary
print("\nSuccessful builtins that accepted the sample:", len(working_names))
print("Failed/errored builtins checked:", len(errors))

# 5) Print the successful ones in a table
if working_names:
    print("\nFunction Name         | Signature")
    print("-" * 60)
    for n, s in zip(working_names, working_sigs):
        print(f"{n:<22} | {s}")
else:
    print("\nNo builtins accepted the sample (working_names is empty).")

# 6) Print first 10 errors to inspect why things failed
if errors:
    print("\nFirst 12 errors (name, error type, message):")
    for rec in errors[:12]:
        print(rec)
