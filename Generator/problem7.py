# Q7. Generator that reads a large file line by line.

def read_file_lines(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_file_lines('data.txt'):
    print(line)


#  Logic:

# File ko ek baar me nahi, line by line read karta hai.
# Memory efficient hai.
#  Real-Life Example:
# Big log files (e.g. 5GB server logs) ko analyze karne me useful.