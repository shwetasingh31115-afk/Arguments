def shutdown():
    """This is a Program to shutdown your PC
    --------CONDITIONS--------
    1.It will close all the apps and programs.
    2.It will turn off the computer.
    3.You will lose all the unsaved work."""
print(shutdown.__doc__)
chose=input("Do you agree with the Conditions and want to shutdown your PC type yes/no:")
if chose=="yes"or chose=="Yes":
    print("---------Shutting down the Computer See you again---------")
elif chose=="no"or chose=="No":
    print("---------Abort shutdown---------")
else:
    print("SORRY")
shutdown