import random
import datetime
import math

LIMIT_LO = 24.95
LIMIT_HI = 25.05

accepted = 0
rejected = 0

consecutive_rejects = 0
alarms = 0
first_alarm_part = None

for part in range(1, 201):

    if part <= 100:
        dia = round(random.uniform(24.85, 25.15), 3)
    else:
        dia = round(random.uniform(24.90, 25.20), 3)

    if LIMIT_LO <= dia <= LIMIT_HI:

        accepted += 1
        consecutive_rejects = 0

        print("Part", part, ":", dia, "ACCEPT ✓")

    else:

        rejected += 1
        consecutive_rejects += 1

        print("Part", part, ":", dia, "REJECT ✗")

    if consecutive_rejects == 3:

        print("⚠ TOOL WEAR SUSPECTED at part", part)

        alarms += 1

        if first_alarm_part is None:
            first_alarm_part = part


# -------------------------------
# STAMPED SHIFT REPORT
# -------------------------------

now = datetime.datetime.now()

print("\n========================================")
print("SHIFT REPORT ·", now.strftime("%d-%m-%Y %H:%M"))
print("========================================")

print("Operators    : Ayushi Srivastava, Partner Name")
print("Parts        :", 200)
print("Accepted     :", accepted)
print("Rejected     :", rejected)

print("Acceptance   :", round(accepted / 200 * 100, 1), "%")

print("Tolerance    :", LIMIT_LO, "mm -", LIMIT_HI, "mm")

print("Alarm count  :", alarms)

if first_alarm_part is not None:
    print("First alarm  : Part", first_alarm_part)
else:
    print("First alarm  : None")

print("Nominal area :", round(math.pi * (25.0 / 2) ** 2, 2), "mm2")

print("========================================")
