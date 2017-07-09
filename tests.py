import os

for filename in os.listdir("dev/tests/"):
    if filename.startswith("test_"):
        print("Test: {}".format(filename))
        os.system("python -m dev.tests.{}".format(filename.replace(".py", "")))
        os.system("pause")
