# Practical 06
# CP1404 Practical 06 – Classes

**Student:** Xuanyi Xie
**Date:** 2 Nov 2025 (Asia/Singapore)

---

## 1) What did I do this week?

* Set up a fresh branch (`prac_06_feedback`) from an up‑to‑date `master`, opened a PR, and requested a peer review.
* Studied the provided `Car` class and extended it (fuel ops, `drive`, `__str__`, added `name`).
* Modified `used_cars.py` to construct and interact with named cars (including a “limo” with fuel manipulations).
* Implemented `ProgrammingLanguage` with `is_dynamic()` and a readable `__str__`; built `languages.py` and filtered for dynamically‑typed languages.
* Built a `Guitar` class with `get_age()` and `is_vintage()`, plus a small test driver `guitar_test.py`.
* Wrote `guitars.py` to collect user guitars and print a neatly formatted summary (using `enumerate`, width formatting, and the vintage tag).
* Completed this REFLECTION.

---

## 2) Time estimates vs actuals (by task)

> Recorded in module docstrings as well; summarised here.

| Task                                                       | Estimate | Actual | Notes                                                  |
| ---------------------------------------------------------- | -------: | -----: | ------------------------------------------------------ |
| Git flow: sync `master`, new branch, PR + reviewer mention |   10 min |  8 min | Getting faster with the repeatable flow.               |
| `used_cars.py` changes (limo, add fuel, drive, print)      |   15 min | 12 min | Straightforward once `Car` was understood.             |
| Add `__str__` + `name` to `Car`                            |   10 min |  8 min | f-strings made this clean.                             |
| `ProgrammingLanguage` + `languages.py`                     |   25 min | 20 min | Kept constructor param order consistent.               |
| Filter dynamic languages (paper → code)                    |   10 min |  9 min | `is_dynamic()` kept client code tidy.                  |
| `Guitar` class (`get_age`, `is_vintage`)                   |   30 min | 28 min | Reused `get_age()` inside `is_vintage()`.              |
| `guitar_test.py` (manual tests)                            |   20 min | 18 min | Printed *Expected vs Got*; caught an off‑by‑one early. |
| `guitars.py` (client program)                              |   35 min | 32 min | Used `enumerate(..., 1)` and formatted columns.        |
| REFLECTION.md                                              |   10 min | 12 min | Summarised learning succinctly.                        |

**Total**: **165 min** estimated vs **147 min** actual.

---

## 3) What did I learn / reinforce?

* **Encapsulation matters:** putting logic like “is dynamic typing?” inside the class keeps the client code simple and expressive.
* **`__str__` is user‑friendly output:** printing objects becomes a debugging and UX tool.
* **Reusability:** `is_vintage()` leveraging `get_age()` avoids duplicating logic.
* **Test mindset:** even manual *Expected / Got* lines are valuable; they made an off‑by‑one bug obvious.
* **Git habits:** branch‑per‑prac + PR + reviewer mention scales well and keeps changes focused.

---

## 4) What was challenging? How did I handle it?

* **Constructor parameter order** in `ProgrammingLanguage` can be error‑prone. I mitigated it with explicit naming in the call sites and consistent ordering in the class docstring.
* **Formatting alignment** in `guitars.py` (name width & currency). I tested with a few different name lengths and used format specifiers (`{guitar.name:>20}`, `{guitar.cost:10,.2f}`).
* **Edge cases** in `Car.drive()` (e.g., trying to drive further than fuel allows). I verified the branch where the car “runs out of fuel” prints the right text and updates odometer correctly.

---

## 5) Code review – giving and receiving

* **This prac PR:** *link pasted in Learn submission form.*
  *Reviewer mentioned:* @<peer‑username‑this‑week>
* **Review I gave (for last week’s prac):** *link pasted in Learn submission form.*

**What I looked for when reviewing:**

* Clear `__str__` outputs for quick object inspection.
* Single‑responsibility methods and no duplicate logic (e.g., using helper methods like `get_age()`).
* Input validation for negative values in menu flows (drive/refuel).
* Consistent naming, docstrings, and type‑like behaviour (e.g., `is_` prefix for Booleans).

**What I changed based on feedback (if any):**

* Normalised f‑string formatting and improved docstrings (“Args/Returns”) for clarity.

---

## 6) How will I improve next week?

* Add **doctests or `pytest`** to move beyond manual print testing.
* Prefer **keyword arguments** for constructors with many parameters to reduce ordering mistakes.
* Keep each commit small and message in **imperative mood** (e.g., “Add `is_vintage` check”).
* Start with a short **paper sketch** for loops/filters before coding—this reduced syntax retries.

---

## 7) Notes to marker

* Required files completed: `car.py` (with `name` and `__str__`), `used_cars.py` (named cars), `programming_language.py`, `languages.py`, `guitar.py`, `guitar_test.py`, `guitars.py`, and this `REFLECTION.md`.
* Two PR URLs supplied in the submission form as requested. If a review is not received in time, PR is still merged and available for later review (per instructions).

---

## 8) Concise summary (per my learning goals)

**Main points (1–2 sentences):** I applied OOP fundamentals (encapsulation, `__str__`, small cohesive methods) to build simple class models and client programs. The PR‑based workflow and manual tests helped catch issues early.

**Key details (≤100 words):** I extended the `Car` class, built `ProgrammingLanguage` and `Guitar` with clear constructors and behaviour (`is_dynamic`, `get_age`, `is_vintage`), and wrote small clients (`languages.py`, `guitars.py`) to exercise them. Formatting and input validation improved output readability. Manual *Expected vs Got* tests surfaced an age edge case early. Using a branch‑per‑prac with a reviewer mention kept changes focused and traceable.

**Outlook (2–3 sentences):** Next, I’ll introduce doctests/pytest for repeatable testing and prefer keyword args for multi‑param constructors. I’ll continue refining formatting and validation patterns so later pracs can reuse them. The same Git flow will be used to streamline collaboration and reviews.
