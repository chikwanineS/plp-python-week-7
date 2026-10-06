# Week 7 Assignment: Shopping List Manager

- `list_warmup.py` – practises list creation, index access, append, remove and len.
- `shopping_list.py` – an interactive menu to add, remove and show shopping items.
- `list_report.py` – loops through a list to number items, count long names and find the longest.

## Why check `in` before `.remove()`?

Calling `.remove()` on an item that isn't in the list raises a `ValueError` and crashes the program. Checking with `in` first lets the program print a friendly message and keep running instead. It makes the manager safe even when the user mistypes or removes the same item twice.