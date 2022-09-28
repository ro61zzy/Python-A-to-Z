# logical AND and OR and NOT
# if an applicant has high income and/or good credit he/she is eligible for a loan
# AND = both conditions should be true
# OR = at least one should be true

high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible for a loan")