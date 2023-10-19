pages_in_book = int(input())
pages_per_hour = int(input())
days = int(input())
hours_per_book = pages_in_book // pages_per_hour
needed_days = hours_per_book // days
print(needed_days)