import datetime
import os
import re
from pathlib import Path

# Career start year (Zibazi, first front-end job per resume)
START_YEAR = 2022

README = Path(__file__).resolve().parents[2] / "README.md"

year = int(os.environ.get("FORCE_YEAR", datetime.date.today().year))
years = max(0, year - START_YEAR)

s = README.read_text(encoding="utf-8")

# 1. Typing SVG banner (URL-encoded): "4%2B+Years+Shipping..."
s = re.sub(r"\d+(?=%2B\+Years)", str(years), s)
# 2. About Me block: "with 4+ years ..."
s = re.sub(r"\d+(?=\+ years)", str(years), s, flags=re.IGNORECASE)

README.write_text(s, encoding="utf-8")
print(f"Experience banner set to {years}+ years (computed for year {year})")
