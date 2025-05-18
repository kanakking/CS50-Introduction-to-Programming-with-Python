#aske the user for what kind of file they have?
filen = input("File name: ").strip().lower()
#take all the input and return output according their file name.
if ".jpg" in filen:
    print("image/jpeg")
elif ".jpeg" in filen:
    print("image/jpeg")
elif ".gif" in filen:
    print("image/gif")
elif ".png" in filen:
    print("image/png")
elif ".pdf" in filen:
    print("application/pdf")
elif ".txt" in filen:
   print("text/plain")
elif ".zip" in filen:
    print("application/zip")
else:
    print("application/octet-stream ")