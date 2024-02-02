"""Exercise: Hash Table: New York City Weather Analysis """

"""(1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the average temperature in first week of Jan

  (b) What was the maximum temperature in first 10 days of Jan

  Figure out data structure that is best for this problem"""



#(a) What was the average temperature in first week of Jan

data = []
file_path = r'Datastructures\HashMaps\hashmap_exercises\Weather Exercise\nyc_weather.csv'
with open(file_path  , 'r') as file:
    next(file)
    for line_number,line in enumerate(file, start=1):
        index=line.strip().split(',')
        if len(index) >= 2:

           try:
            temp = int(index[1])
            data.append(temp)
           except ValueError:
            print(f'Invalid Temperature on line {line_number}: {index[1]}')

average=sum(data)/ len(data)
#(b)What was the maximum temperature in first 10 days of Jan
max_temps= max(data)
print("Question 1" "\n")
print(f" This is how the List looks like:{data}" "\n") 
print(f" (a) The average temperature of the first week was: {average}" "\n")
print(f" (b) The maximum temperature in the first 10 days of Jan was:{max_temps}" "\n")

"""2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the temperature on Jan 9?

  (b) What was the temperature on Jan 4?

  Figure out data structure that is best for this problem""" 

print("Question 2" "\n")
weather_dict = {}

with open(file_path, 'r') as data:
    next(data)
    for line in data:
        index = line.strip().split(',')

        if len(index) >= 2:
            key=index[0]
            temp=int(index[1])

            if key not in weather_dict:
                weather_dict[key] = []
                   
                
            weather_dict[key].append(temp)
     

print(f" This is how the dictionary looks like : {weather_dict}" "\n")
print(f" (a) What was the temperature on Jan 9 : {weather_dict['Jan 9']}" "\n")
print(f" (b) What was the temperature on Jan 4 : {weather_dict['Jan 4']}" "\n")

