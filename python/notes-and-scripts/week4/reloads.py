import importlib
import filechanges

def changes():
    try:
        # Trying out the reload() command
        # to experience the dynamic changes in code
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    # Adding input to have some control over the script
    input("Hit enter to reload...")