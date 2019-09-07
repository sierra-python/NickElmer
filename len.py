
years = input("Enter a number of years and I'll tell you how many minutes that is") #prompts the user to enter a variable and it stores it
years = int(years)
days = years * 365
hours = days * 24
minutes = hours * 60
print(years, "years is", minutes, "minutes")
