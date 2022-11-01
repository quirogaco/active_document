import dateparser

datetime_str = "1-6-2000"
datetime_object = dateparser.parse(datetime_str)
datetime_format = datetime_object.strftime('%m/%d/%Y')

print(datetime_str, datetime_object, datetime_format)