marks= {
    "Harry": 100,
    "Ram": 56,
    "Shilpa": 99
}
print(marks["Harry"])
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.get("Harry"))
print(marks.get("Satish"))
print(marks["Satish"])


## There's always a difference between marks.get() and marks[] as if we input a key or that is not present in the dictionary then marks.get() would give back none but marks[] throws an error.