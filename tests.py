import os

for filename in os.listdir("dev/tests/"):
    if filename.startswith("test_"):
        os.system("python -m dev.tests.{}".format(filename.replace(".py", "")))
        os.system("pause")
