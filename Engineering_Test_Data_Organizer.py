from collections import defaultdict, Counter
from statistics import mean, median


LAST_NAME = "Jancilan"
SEED_NUM = 8
FAVORITE_ARTIST = "Rico Blanco"

TEST_SOURCES = [
    f"{LAST_NAME}_T1",
    f"{LAST_NAME}_T2",
    f"{LAST_NAME}_T3",
    f"{LAST_NAME}_T4",
    f"{LAST_NAME}_T5"
]

CATEGORIES = [
    "TEMPERATURE",
    "VOLTAGE",
    "CURRENT",
    "PRESSURE",
    "SPEED"
]


def generate_value(source_index, category_index, measurement_index):
    """
    Generate numerical values using SEED_NUM,
    the character positions in FAVORITE_ARTIST,
    and the source/category/measurement indices.
    """

    artist_score = sum(
        position * ord(character)
        for position, character in enumerate(FAVORITE_ARTIST, start=1)
    )

    value = (
        artist_score
        + SEED_NUM * 10
        + source_index * 17
        + category_index * 13
        + measurement_index * 7
    ) % 1000

    return round(value / 10.0, 2)


records = []

for source_index, source in enumerate(TEST_SOURCES, start=1):
    for category_index, category in enumerate(CATEGORIES, start=1):

        measurement_count = (
            2 if category in ["TEMPERATURE", "VOLTAGE"] else 1
        )

        for measurement_index in range(1, measurement_count + 1):
            record = {
                "source": source,
                "category": category,
                "value": generate_value(
                    source_index,
                    category_index,
                    measurement_index
                ),
                "measurement_no": measurement_index
            }

            records.append(record)


records.append(records[0].copy())


organized_data = defaultdict(lambda: defaultdict(list))

for record in records:
    organized_data[record["source"]][record["category"]].append(
        record["value"]
    )


record_counts = Counter(
    (r["source"], r["category"], r["value"], r["measurement_no"])
    for r in records
)

repeated_records = {
    key: count
    for key, count in record_counts.items()
    if count > 1
}

distinct_records = set(record_counts.keys())


category_values = defaultdict(list)
source_values = defaultdict(list)

for record in records:
    category_values[record["category"]].append(record["value"])
    source_values[record["source"]].append(record["value"])


def calculate_summary(values):
    return {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "mean": round(mean(values), 2),
        "median": round(median(values), 2)
    }


category_summaries = {
    category: calculate_summary(values)
    for category, values in sorted(category_values.items())
}

source_summaries = {
    source: calculate_summary(values)
    for source, values in sorted(source_values.items())
}


source_counts = Counter(r["source"] for r in records)
category_counts = Counter(r["category"] for r in records)

ordered_records = sorted(
    records,
    key=lambda r: (
        r["source"],
        r["category"],
        r["measurement_no"],
        r["value"]
    )
)


print("=" * 65)
print("       ENGINEERING TEST DATA ORGANIZER")
print("=" * 65)

print("\nSTUDENT-SPECIFIC INPUTS")
print("Last Name       :", LAST_NAME)
print("Seed Number     :", SEED_NUM)
print("Favorite Artist :", FAVORITE_ARTIST)

# A. Generated test data
print("\n" + "=" * 65)
print("A. GENERATED TEST DATA")
print("=" * 65)

for record in records:
    print(
        f"Source: {record['source']:<15} | "
        f"Category: {record['category']:<12} | "
        f"Measurement: {record['measurement_no']} | "
        f"Value: {record['value']}"
    )

print("\n" + "=" * 65)
print("B. ORGANIZED TEST DATA BY SOURCE AND CATEGORY")
print("=" * 65)

for source in sorted(organized_data):
    print(f"\n{source}")

    for category in sorted(organized_data[source]):
        values = organized_data[source][category]
        print(f"  {category:<12}: {values}")

print("\n" + "=" * 65)
print("C. REPEATED AND DISTINCT RECORDS")
print("=" * 65)

print("Total records          :", len(records))
print("Distinct record types  :", len(distinct_records))
print("Repeated record types  :", len(repeated_records))
print("Extra duplicate entries:", sum(
    count - 1 for count in repeated_records.values()
))

for key, count in sorted(repeated_records.items()):
    source, category, value, measurement_no = key
    print(
        f"Repeated: {source}, {category}, "
        f"Measurement {measurement_no}, Value {value} "
        f"(appears {count} times)"
    )

print("\n" + "=" * 65)
print("D. NUMERICAL SUMMARIES BY CATEGORY")
print("=" * 65)

for category, summary in category_summaries.items():
    print(f"\n{category}")
    for label, value in summary.items():
        print(f"  {label.capitalize():<10}: {value}")

print("\n" + "=" * 65)
print("E. NUMERICAL SUMMARIES BY TEST SOURCE")
print("=" * 65)

for source, summary in source_summaries.items():
    print(f"\n{source}")
    for label, value in summary.items():
        print(f"  {label.capitalize():<10}: {value}")

print("\n" + "=" * 65)
print("F. CATEGORICAL SUMMARIES")
print("=" * 65)

print("\nRecords per source:")
for source, count in sorted(source_counts.items()):
    print(f"  {source:<15}: {count}")

print("\nRecords per category:")
for category, count in sorted(category_counts.items()):
    print(f"  {category:<15}: {count}")

print("\n" + "=" * 65)
print("G. ORDERED TEST RECORDS")
print("=" * 65)

for record in ordered_records:
    print(
        f"{record['source']:<15} "
        f"{record['category']:<12} "
        f"Measurement {record['measurement_no']} "
        f"Value = {record['value']}"
    )


all_values = [record["value"] for record in records]

print("\n" + "=" * 65)
print("H. CONSOLIDATED FINAL SUMMARY")
print("=" * 65)

print("Student                  :", LAST_NAME)
print("Seed Number              :", SEED_NUM)
print("Favorite Artist          :", FAVORITE_ARTIST)
print("Number of test sources   :", len(TEST_SOURCES))
print("Number of categories     :", len(CATEGORIES))
print("Total measurement records:", len(records))
print("Distinct record types    :", len(distinct_records))
print("Repeated record types    :", len(repeated_records))
print("Overall minimum          :", min(all_values))
print("Overall maximum          :", max(all_values))
print("Overall average          :", round(mean(all_values), 2))
print("Overall median           :", round(median(all_values), 2))

print("\nFINAL REPORT")
print(
    "The generated dataset contains five test sources and five "
    "measurement categories. Records are organized by source and "
    "category, and repeated entries are identified. Numerical "
    "summaries include count, minimum, maximum, mean, and median. "
    "Categorical summaries show the record counts for each source "
    "and category. The records are sorted and presented in a "
    "consolidated report."
)

print("\n" + "=" * 65)
print("END OF REPORT")
print("=" * 65)
