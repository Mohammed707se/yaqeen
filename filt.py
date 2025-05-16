import json

# 1) ضبط حدود الـ bbox لمنطقة الرياض (قابل للتعديل حسب الدقة اللي تحتاجها)
MIN_LAT, MAX_LAT = 24.45, 25.00
MIN_LON, MAX_LON = 46.35, 47.00

# 2) قراية الملف الأصلي
with open('facilities.json', 'r', encoding='utf-8') as f:
    facilities = json.load(f)

# 3) فلترة المراكز ضمن الـ bbox فقط
filtered = []
for item in facilities:
    lat = float(item.get('facilityLatitude', 0))
    lon = float(item.get('facilityLongitude', 0))
    if MIN_LAT <= lat <= MAX_LAT and MIN_LON <= lon <= MAX_LON:
        filtered.append(item)

# 4) حفظ النتيجة في ملف جديد
with open('facilities_riyadh.json', 'w', encoding='utf-8') as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f'تم الاحتفاظ بـ {len(filtered)} مركز داخل حدود الرياض.')
