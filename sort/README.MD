# אלגוריתמי מיון - פרויקט השוואה וניתוח ביצועים

פרויקט זה מממש ומשווה ארבעה אלגוריתמי מיון קלאסיים: מיון הכנסה, מיון מיזוג, מיון מהיר ומיון ערימה. הפרויקט כולל מדידת ביצועים, השוואות והתחלות עבור כל אלגוריתם במגוון תרחישי קלט.

## מבנה הפרויקט

```
sorting_algorithms/
├── algorithms/
│   ├── __init__.py
│   ├── insertion_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── heap_sort.py
├── tests/
│   ├── __init__.py
│   └── test_sorting_algorithms.py
├── requirements.txt
└── README.md
```

## האלגוריתמים

### מיון הכנסה (Insertion Sort)
- מיון ברירה פשוט ויעיל למערכים קטנים
- סיבוכיות זמן: O(n²)
- יעיל במיוחד כאשר המערך כמעט ממוין
- נמצא ב-`insertion_sort.py`

### מיון מיזוג (Merge Sort)
- אלגוריתם מיון יציב מבוסס "הפרד ומשול"
- סיבוכיות זמן: O(n log n)
- מבטיח ביצועים טובים בכל המקרים
- נמצא ב-`merge_sort.py`

### מיון מהיר (Quick Sort)
- אלגוריתם מיון יעיל מבוסס "הפרד ומשול"
- סיבוכיות זמן ממוצעת: O(n log n)
- במקרה הגרוע: O(n²)
- נמצא ב-`quick_sort.py`

### מיון ערימה (Heap Sort)
- אלגוריתם מיון מבוסס מבנה נתונים ערימה
- סיבוכיות זמן: O(n log n)
- יעיל במיוחד כשנדרש מיון במקום
- נמצא ב-`heap_sort.py`

## תרחישי בדיקה

הפרויקט בודק את האלגוריתמים במספר תרחישים:
1. מערך ממוין
2. מערך הפוך
3. מערך עם הרבה כפילויות
4. מערך עם מספרים חיוביים ושליליים
5. מערך עם טיפוסי נתונים מעורבים

## מדדי ביצועים

כל אלגוריתם נמדד על פי:
- מספר השוואות
- מספר השמות/התחלות
- סך כל הפעולות

## שימוש בקוד

```python
from algorithms.insertion_sort import insertion_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.heap_sort import heap_sort

# דוגמה לשימוש
arr = [64, 34, 25, 12, 22, 11, 90]
comparisons, assignments = insertion_sort(arr)
print(f"Sorted array: {arr}")
print(f"Comparisons: {comparisons}")
print(f"Assignments: {assignments}")
```

## הרצת בדיקות

```bash
python -m tests.test_sorting_algorithms
```

## תלויות (Dependencies)

- Python 3.x
- matplotlib
- pytest (לבדיקות)

להתקנת התלויות:
```bash
pip install -r requirements.txt
```

## תוצאות והשוואות

הפרויקט מייצר גרפים המשווים את ביצועי האלגוריתמים השונים:
- גרף לוגריתמי של זמני ריצה
- השוואת מספר פעולות
- ניתוח לפי גודל קלט
- השוואה בין תרחישי בדיקה שונים