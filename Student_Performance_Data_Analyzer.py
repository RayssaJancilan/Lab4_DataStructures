from collections import Counter, defaultdict
from statistics import mean, median

LAST_NAME = "Jancilan"
SEED_NUM = 8
FAVORITE_ARTIST = "Rico Blanco"

SUBJECTS = [
    "Programming",
    "Mathematics",
    "Electronics",
    "Physics",
    "English"
]

STUDENTS = [
    f"{LAST_NAME}_Student_{i}"
    for i in range(1, 6)
]


def get_category(score):
    if score is None:
        return "Incomplete"
    elif score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Needs Improvement"
    else:
        return "Poor"


def generate_score(student, subject):
    # Character positions are counted from 1.
    artist_value = sum(
        (i + 1) * ord(char)
        for i, char in enumerate(FAVORITE_ARTIST)
    )

    student_number = int(student.split("_")[-1])
    subject_number = SUBJECTS.index(subject) + 1

    subject_value = sum(
        (i + 1) * ord(char)
        for i, char in enumerate(subject)
    )

    score = (
        artist_value
        + SEED_NUM * student_number
        + subject_value
        + student_number * subject_number
    ) % 41 + 60

    return score


records = []

for student in STUDENTS:
    for subject in SUBJECTS:
        score = generate_score(student, subject)

        records.append({
            "student": student,
            "subject": subject,
            "score": score,
            "category": get_category(score)
        })


records.append(records[0].copy())


records.append({
    "student": STUDENTS[0],
    "subject": "English",
    "score": None,
    "category": "Incomplete"
})


seen = set()
duplicates = []
unique_records = []

for record in records:
    key = (record["student"], record["subject"])

    if key in seen:
        duplicates.append(record)
    else:
        seen.add(key)
        unique_records.append(record)

incomplete_records = [
    record for record in unique_records
    if record["score"] is None
]

valid_records = [
    record for record in unique_records
    if record["score"] is not None
]


student_data = defaultdict(list)
subject_data = defaultdict(list)

for record in valid_records:
    student_data[record["student"]].append(record)
    subject_data[record["subject"]].append(record)


def numerical_summary(scores):
    if not scores:
        return None

    return {
        "count": len(scores),
        "average": mean(scores),
        "median": median(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }


print("=" * 72)
print("       STUDENT PERFORMANCE DATA ORGANIZER")
print("=" * 72)
print(f"Last Name       : {LAST_NAME}")
print(f"Seed Number     : {SEED_NUM}")
print(f"Favorite Artist : {FAVORITE_ARTIST}")
print(f"Number of Students: {len(STUDENTS)}")
print(f"Number of Subjects: {len(SUBJECTS)}")

print("\nSTUDENT LABELS")
for student in STUDENTS:
    print("-", student)

print("\nALL GENERATED RECORDS")
print("-" * 72)
print(f"{'STUDENT':<25} {'SUBJECT':<16} {'SCORE':<8} CATEGORY")
print("-" * 72)

for record in records:
    score_text = (
        str(record["score"])
        if record["score"] is not None
        else "N/A"
    )

    print(
        f"{record['student']:<25} "
        f"{record['subject']:<16} "
        f"{score_text:<8} "
        f"{record['category']}"
    )


print("\nDUPLICATE RECORDS")
if duplicates:
    for record in duplicates:
        print(
            f"Repeated: {record['student']} - "
            f"{record['subject']} - Score: {record['score']}"
        )
else:
    print("No duplicates found.")

print("\nINCOMPLETE RECORDS")
if incomplete_records:
    for record in incomplete_records:
        print(
            f"{record['student']} - {record['subject']}: "
            "Missing score"
        )
else:
    print("No incomplete records found.")


print("\n" + "=" * 72)
print("NUMERICAL SUMMARY BY STUDENT")
print("=" * 72)

for student in STUDENTS:
    scores = [
        record["score"]
        for record in student_data[student]
    ]

    summary = numerical_summary(scores)

    if summary:
        print(f"\n{student}")
        print(f"  Number of scores: {summary['count']}")
        print(f"  Average: {summary['average']:.2f}")
        print(f"  Median: {summary['median']:.2f}")
        print(f"  Highest score: {summary['highest']}")
        print(f"  Lowest score: {summary['lowest']}")


print("\n" + "=" * 72)
print("NUMERICAL SUMMARY BY SUBJECT")
print("=" * 72)

for subject in SUBJECTS:
    scores = [
        record["score"]
        for record in subject_data[subject]
    ]

    summary = numerical_summary(scores)

    if summary:
        print(f"\n{subject}")
        print(f"  Number of scores: {summary['count']}")
        print(f"  Average: {summary['average']:.2f}")
        print(f"  Median: {summary['median']:.2f}")
        print(f"  Highest score: {summary['highest']}")
        print(f"  Lowest score: {summary['lowest']}")


print("\n" + "=" * 72)
print("CATEGORICAL PERFORMANCE SUMMARY")
print("=" * 72)

category_counts = Counter(
    record["category"] for record in unique_records
)

category_order = [
    "Excellent",
    "Very Good",
    "Good",
    "Needs Improvement",
    "Poor",
    "Incomplete"
]

for category in category_order:
    print(f"{category:<22}: {category_counts[category]}")


print("\n" + "=" * 72)
print("CONSOLIDATED STUDENT PERFORMANCE REPORT")
print("=" * 72)

overall_scores = [
    record["score"] for record in valid_records
]

overall = numerical_summary(overall_scores)

print(f"Student labels generated : {len(STUDENTS)}")
print(f"Subjects included        : {len(SUBJECTS)}")
print(f"Total records generated  : {len(records)}")
print(f"Unique records           : {len(unique_records)}")
print(f"Repeated records         : {len(duplicates)}")
print(f"Incomplete records       : {len(incomplete_records)}")
print(f"Valid scores analyzed    : {len(valid_records)}")

print(f"\nOverall average score    : {overall['average']:.2f}")
print(f"Overall median score     : {overall['median']:.2f}")
print(f"Overall highest score    : {overall['highest']}")
print(f"Overall lowest score     : {overall['lowest']}")

student_averages = {
    student: mean([
        record["score"]
        for record in student_data[student]
    ])
    for student in STUDENTS
    if student_data[student]
}

if student_averages:
    top_student = max(student_averages, key=student_averages.get)
    print(
        f"Highest average student : {top_student} "
        f"({student_averages[top_student]:.2f})"
    )

print("\nREPORT COMPLETE")
print("=" * 72)
