from functools import lru_cache
import csv

@lru_cache
def read(path):
    with open(path, encoding= "utf-8") as file:
        reader = csv.DictReader(file, delimiter= "," )
        return list(reader)


read('src/jobs.csv')