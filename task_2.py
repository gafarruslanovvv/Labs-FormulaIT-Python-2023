def find_common_participants(participants1, participants2, x = ","):
    set1 = set(participants1.split(x))
    set2 = set(participants2.split(x))
    common_participants = list(set1.intersection(set2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники: ", participants)