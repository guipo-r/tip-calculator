print(f"Welcome to the tip calculator!\nAnswer these questions and we'll tell you how much each person will pay.\n")

bill = float(input('What was the total bill? $'))

pct = input("What percentage tip would you like to give? 10, 12, or 15? ")

pct = int(pct)
#if pct!=10 or pct!=12 or pct!=15:
#  print('Please try choosing between 10%, 12% or 15%')
#  pct = input("What percentage tip would you like to #give?") 

ppl = int(input('How many people to split the bill? '))

if pct == 10:
  total_payment = bill * 1.10
if pct == 12:
  total_payment = bill * 1.12
if pct == 15:
  total_payment = bill * 1.15

pay_per_person = round((total_payment / ppl), 2)

print(f'Each person should pay: ${pay_per_person: .2f}')
                