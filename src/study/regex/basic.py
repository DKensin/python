import re

# get raw data from raw log file
file = open("raw_log.log", 'r')
raw_data = file.read()
file.close()

regex = r".*(Testing the PFE.+bytes)"
test_cases = re.findall(regex, raw_data)

regex = r".+\s+(\d+)\s(\wbits/sec).+(sender|receiver)$"
sender_receiver = re.findall(regex, raw_data)

regex = r"Average.+all.+\s+(\d+.\d+)"
all_cores = re.findall(regex, raw_data)

regex = r"Average:\s+(\d).+\s+(\d+.\d+)"
seperate_cores = re.findall(regex, raw_data)