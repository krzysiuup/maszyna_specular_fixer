import os
for file_ in os.listdir():
    if file_.endswith(".ui"):
        os.system("pyuic5 {} -o {}".format(file_, file_.replace(".ui", ".py")))
        print("{} file was successfully compiled to {} file.".format(file_, file_.replace(".ui", ".py")))
print("All UI's was successfully compiled.")
input()
