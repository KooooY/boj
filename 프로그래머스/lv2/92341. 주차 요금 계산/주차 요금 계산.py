def solution(fees, records):
    answer = []
    car_dict = {}
    car_list = set()
    time_dict = {}

    for record in records:
        if record[6:10] not in car_dict:
            car_dict[record[6:10]] = record[:5]
            car_list.add(record[6:10])
        else:
            time = (int(record[:2])-int(car_dict[record[6:10]][:2]))*60 + (int(record[3:5])-int(car_dict[record[6:10]][3:5]))
            if record[6:10] in time_dict:
                time_dict[record[6:10]] += time
            else:
                time_dict[record[6:10]] = time

            car_dict.pop(record[6:10])

    for car in car_dict:
        time = (23 - int(car_dict[car][:2]))*60 + (59 - int(car_dict[car][3:5]))
        if car in time_dict:
            time_dict[car] += time
        else:
            time_dict[car] = time

    car_list = list(car_list)
    car_list.sort()
    for car_number in car_list:
        temp_fee = fees[1]
        if time_dict[car_number] > fees[0]:
            if (time_dict[car_number] - fees[0]) % fees[2]:
                temp_fee += ((time_dict[car_number] - fees[0]) // fees[2] + 1) * fees[3]
            else:
                temp_fee += ((time_dict[car_number] - fees[0]) // fees[2]) * fees[3]
        answer.append(temp_fee)

    return answer