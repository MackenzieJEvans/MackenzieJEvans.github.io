"""Convert the UNL 'Majors by College' workbook into majors.json for the search app.

Usage: python3 build_data.py "../DR12573 - Majors by College (Fall25-Fall16).xlsx"
Requires openpyxl.
"""
import json, re, sys
from collections import defaultdict
import openpyxl

src = sys.argv[1] if len(sys.argv) > 1 else "../DR12573 - Majors by College (Fall25-Fall16).xlsx"

# College renamed after Fall 2017.
COLLEGE_ALIAS = {"Business Administration": "Business"}
# Obvious program renames so a major's trend line isn't split in two.
MAJOR_ALIAS = {
    "ARCHITECTURAL ENGR (OMAHA)": "ARCHITECTURAL ENGINEERING",
    "ACCOUNTING (RAIKES PROGAM ONLY)": "ACCOUNTING (RAIKES PROGRAM ONLY)",
    "ACTUARIAL SCIENCE (RAIKES PROGAM ONLY)": "ACTUARIAL SCIENCE (RAIKES PROGRAM ONLY)",
}

wb = openpyxl.load_workbook(src, data_only=True)
counts = defaultdict(int)          # (year, major, college, level, degree) -> n
totals = {}
for ws in wb:
    year = int(re.search(r"(20\d\d)", ws.title).group(1))
    tot = 0
    for row in ws.iter_rows(min_row=2, values_only=True):
        college, major, _code, degree, n = (list(row) + [None] * 5)[:5]
        if not major or not str(major).strip():
            continue  # skips blank / grand-total rows
        n = int(n)
        major = MAJOR_ALIAS.get(major.strip(), major.strip())
        college = (college or "").strip()
        level = "Undergraduate"
        if college.startswith("Grad Studies"):
            level = "Graduate"
            college = college.split(" - ", 1)[1] if " - " in college else "Graduate Studies"
        elif college == "Law":
            level = "Graduate"
        college = COLLEGE_ALIAS.get(college, college)
        counts[(year, major, college, level, (degree or "").strip() or "—")] += n
        tot += n
    totals[year] = tot

years = sorted(totals)
# Sanity checks against the grand-total rows found in the workbook.
assert totals[2024] == 24393, totals[2024]
assert totals[2025] == 24375, totals[2025]

# Compact: rows = [yearIndex, majorIndex, collegeIndex, level(0/1), degree, n]
majors = sorted({k[1] for k in counts})
colleges = sorted({k[2] for k in counts})
mi = {m: i for i, m in enumerate(majors)}
ci = {c: i for i, c in enumerate(colleges)}
rows = [[years.index(y), mi[m], ci[c], 1 if l == "Graduate" else 0, d, n]
        for (y, m, c, l, d), n in sorted(counts.items())]

out = {"source": "University of Nebraska-Lincoln, Fall census: Majors by College (DR12573), Fall 2016-Fall 2025",
       "years": years, "totals": [totals[y] for y in years],
       "majors": majors, "colleges": colleges, "rows": rows}
with open("majors.json", "w") as f:
    json.dump(out, f, separators=(",", ":"))
print(len(majors), "majors,", len(rows), "rows; totals", totals)
