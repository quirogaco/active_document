from pyzipcode import ZipCodeDatabase
zcdb = ZipCodeDatabase()

print(zcdb["39095"])
print(dir(zcdb[39095]))