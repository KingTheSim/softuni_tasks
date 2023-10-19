deposit = float(input())
months = int(input())
yearly_percentage = float(input())
acc_interest = deposit * (yearly_percentage / 100)
monthly_interest = acc_interest / 12
total_sum = deposit + (months * monthly_interest)
print(total_sum)