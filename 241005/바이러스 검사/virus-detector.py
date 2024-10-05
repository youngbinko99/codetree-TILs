restaurant_number = int(input())
customer_numbers = list(map(int, input().split()))
leader, crew = map(int, input().split())

count_number = 0
leader_count = 0
crew_count = 0

for i in range(0,restaurant_number):
    if leader < customer_numbers[i]:
        leader_count = 1
        crew_count = (customer_numbers[i] - leader) // crew
        if customer_numbers[i]%crew == 0:
            crew_count = crew_count
        else:
            crew_count += 1
    else:
        leader_count = 0
        crew_count = customer_numbers[i] // crew
        if customer_numbers[i]%crew == 0:
            crew_count = crew_count
        else:
            crew_count += 1

    count_number = count_number + leader_count + crew_count

print(count_number)