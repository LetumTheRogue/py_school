def calculate_overpay(sum_of_loan, percent):

    return sum_of_loan * percent / 100


def monthly_payment(sum_of_loan, percent, payment_period):
    full_loan = sum_of_loan + calculate_overpay(sum_of_loan, percent)
    monthly_payment = full_loan / payment_period

    return monthly_payment


request_sum = input("Enter your loan: ")
request_sum = float(request_sum)

bank_percent = input("Enter bank percent: ")
bank_percent = float(bank_percent)

period = input("Enter your payment period: ")
period = int(period)

result = monthly_payment(request_sum, bank_percent, period)  # calculate_overpay or monthly_payment

print(result)
