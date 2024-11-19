from typing import List, Dict, Set


def fill_in_interval(interval: List[int]) -> Set[int]:
    result = set()
    for start, end in zip(interval[::2], interval[1::2]):
        result.update(range(start, end))
    return result


def appearance(intervals: Dict[str, List[int]]) -> int:
    lesson = fill_in_interval(intervals["lesson"])
    pupil = fill_in_interval(intervals["pupil"])
    tutor = fill_in_interval(intervals["tutor"])

    together = lesson & pupil & tutor

    return len(together)
