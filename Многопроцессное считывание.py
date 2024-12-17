import time
from multiprocessing import Pool

def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']


start_time = time.time()
for file_name in file_names:
    data = read_info(file_name)
end_time = time.time()

print(f'Время работы линейного вызова: {end_time - start_time} секунд')

start_time = time.time()
with Pool() as pool:
    results = pool.map(read_info, file_names)
end_time = time.time()
print(f'Время выполнения параллельного подхода: {end_time - start_time} секунд')