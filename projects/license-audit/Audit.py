o365 = open("licenses.csv")
header = next(o365)

license_counts = {}
dept_counts = {}
inactive = []

for line in o365:
    clean = line.rstrip()
    fields = clean.split(",")
    user = fields[0]
    dept = fields[1]
    license_type = fields[2]
    days = int(fields[3])

    license_counts[license_type] = license_counts.get(license_type, 0) + 1
    dept_counts[dept] = dept_counts.get(dept, 0) + 1

    if days > 90:
        inactive.append((user, days))

o365.close()

inactive.sort(key=lambda row: row[1], reverse=True)

print("License Audit")

print("Licenses in use:")
for license_type, count in license_counts.items():
    print(f"  {license_type}: {count}")

print("Users by department:")
for dept, count in dept_counts.items():
    print(f"  {dept}: {count}")

print("Inactive over 90 days:")
for user, days in inactive:
    print(f"  {user:<20}{days:>3} days")

print(f"Reclaimable licenses: {len(inactive)}")