---
id: 226d10e788
question: Why does Kestra use IANA timezone identifiers instead of offsets?
sort_order: 17
---

IANA timezone identifiers account for daylight saving transitions and historical changes. Fixed offsets or abbreviations can produce incorrect schedules during DST changes, which is why Kestra enforces IANA-based timezones.