this_dict = {
    "name" : "keshab",
    "grade" : "a",
    "date" : 2026,
    "date" : 2025
}
print(this_dict["name"])
print(this_dict.get("city"))
print(this_dict.pop("date"))
print(this_dict.pop ("city", "not found"))
print(len(this_dict))
this_dict["date"] = 2027
print(this_dict)