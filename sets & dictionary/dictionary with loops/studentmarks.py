marks = {
    "Lilly": 85,
    "Ravi": 70,
    "Anu": 90,
    "Priya": 65,
    "Kiran": 80
}

for name, mark in marks.items():
    if mark > 75:
        print(name, ":", mark)