"""בונה משני קובצי המקור שני עותקים: עותק עבודה (הנתונים בקוד) ועותק להפצה (בלי נתונים).
שימוש: python3 בנייה.py <חותמת זמן בתבנית HH.MM_DDMMYYYY>
"""
import json
import pathlib
import shutil
import sys

here = pathlib.Path(__file__).resolve().parent
out = here.parent
stamp = sys.argv[1]

template = (here / "תבנית.html").read_text(encoding="utf-8")
data = json.loads((here / "נתונים.json").read_text(encoding="utf-8"))
marker = "/*__DATA__*/null"
assert template.count(marker) == 1

embedded = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
work = template.replace(marker, embedded)
dist = template.replace(marker, "null")

(out / f"מערכת_הרשאות_עבודה_{stamp}.html").write_text(work, encoding="utf-8")
(out / f"מערכת_הרשאות_להפצה_{stamp}.html").write_text(dist, encoding="utf-8")
shutil.copyfile(here / "נתונים.json", out / f"נתוני_מערכת_הרשאות_{stamp}.json")
print("נבנו שלושה קבצים בתיקייה", out.name)
