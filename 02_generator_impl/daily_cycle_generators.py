from __future__ import annotations

import math
import random
from typing import Dict, List

from resource_loader import FileMetadata, FileRecord

###############################################
#  ProblemContainer
###############################################

class ProblemContainer:
    def __init__(self, metadata: FileMetadata, source_code: str) -> None:
        self.metadata = metadata
        self.source_code = source_code
        self.age = 0  # Number of cycles since last selection

    def get_priority(self) -> int:
        return self.metadata.weight + self.age

    def category(self) -> str:
        return self.metadata.category


###############################################
#  CategoryContainer
###############################################

class CategoryContainer:
    def __init__(
        self,
        name: str,
        problems: List[ProblemContainer],
        category_weights: Dict[str, int]
    ) -> None:
        self.name = name
        self.problems = problems
        self.age = 0
        self.weight = category_weights.get(name, 0)
        self.size = len(problems)

    def get_priority(self) -> float:
        size_factor = math.log(self.size + 1)
        return (self.weight * size_factor) + self.age

    def select_problem(self, used_names: set[str] | None = None) -> ProblemContainer:
        """Select highest-priority problem, avoiding names already used in the cycle."""
        used_names = used_names or set()
        candidates = [p for p in self.problems if p.metadata.name not in used_names]
        if not candidates:
            candidates = self.problems

        selected = max(candidates, key=lambda p: p.get_priority())

        for p in self.problems:
            if p is selected:
                p.age = 0
            else:
                # Progressive age increment to avoid starvation
                p.age += 1 + (p.age // 3)

        return selected


###############################################
#  CycleGenerator (shared engine)
###############################################

class CycleGenerator:
    def __init__(
        self,
        problem_list: List[FileRecord],
        category_weights: Dict[str, int]
    ) -> None:

        self.categories: Dict[str, CategoryContainer] = {}

        for record in problem_list:
            problem = ProblemContainer(record.metadata, record.content)
            category_name = record.metadata.category

            if category_name not in self.categories:
                self.categories[category_name] = CategoryContainer(
                    category_name, [], category_weights
                )

            self.categories[category_name].problems.append(problem)

    def select_next_category(self) -> CategoryContainer:
        selected = max(self.categories.values(), key=lambda c: c.get_priority())

        # update ages
        for c in self.categories.values():
            if c is selected:
                c.age = 0
            else:
                c.age += 1 + (c.age // 3)

        return selected

    def generate_cycle(
        self,
        num_problems_per_category: int,
        num_categories: int
    ) -> List[ProblemContainer]:

        cycle: List[ProblemContainer] = []
        used_names: set[str] = set()

        for _ in range(num_categories):
            category = self.select_next_category()
            for _ in range(num_problems_per_category):
                problem = category.select_problem(used_names)
                used_names.add(problem.metadata.name)
                cycle.append(problem)

        return cycle

    def generate_cycles(
        self,
        num_cycles: int,
        num_problems_per_category: int,
        num_categories: int
    ) -> List[List[ProblemContainer]]:
        all_cycles: List[List[ProblemContainer]] = []
        for _ in range(num_cycles):
            cycle = self.generate_cycle(
                num_problems_per_category,
                num_categories
            )
            all_cycles.append(cycle)
        return all_cycles


###############################################
#  LeetCode Difficulty-Based Cycle Generator
###############################################

class LeetCodeCycleGenerator:
    """
    Difficulty-aware LC generator with:
      - priority selection
      - no duplicate problems within a cycle
    """

    def __init__(self, problem_list: List[FileRecord], category_weights: Dict[str, int]) -> None:

        self.buckets: Dict[str, Dict[str, CategoryContainer]] = {
            "easy": {},
            "medium": {},
            "hard": {},
        }

        for record in problem_list:
            difficulty = record.metadata.difficulty.lower()
            category = record.metadata.category
            problem = ProblemContainer(record.metadata, record.content)

            if category not in self.buckets[difficulty]:
                self.buckets[difficulty][category] = CategoryContainer(
                    category, [], category_weights
                )

            self.buckets[difficulty][category].problems.append(problem)

    def _select_problem_unique(
        self, bucket: Dict[str, CategoryContainer], used: set
    ) -> ProblemContainer:

        # Build a flat list of candidate problems
        all_problems: List[ProblemContainer] = []
        for category in bucket.values():
            all_problems.extend(category.problems)

        # Filter out used problems
        candidates = [p for p in all_problems if p.metadata.name not in used]
        if not candidates:
            # fallback: allow repeating only if absolutely no other candidate exists
            candidates = all_problems

        # Select highest-priority
        selected = max(candidates, key=lambda p: p.get_priority())

        # Increase ages
        for category in bucket.values():
            for p in category.problems:
                if p is selected:
                    p.age = 0
                else:
                    p.age += 1 + (p.age // 3)

        return selected

    def generate_cycle(self, difficulties: List[str]) -> List[ProblemContainer]:
        """
        difficulties is an ordered list like ["easy","easy","medium"].
        Ensures no duplicates in a single cycle.
        """

        used = set()
        result: List[ProblemContainer] = []

        for diff in difficulties:
            bucket = self.buckets[diff.lower()]
            p = self._select_problem_unique(bucket, used)
            used.add(p.metadata.name)
            result.append(p)

        return result
    
    def generate_cycles(
        self,
        num_cycles: int,
        rotation: List[str],
        modes: Dict[str, List[str]],
    ) -> List[List[ProblemContainer]]:
        """
        Generate multiple cycles based on the specified mode.
        """
        all_cycles: List[List[ProblemContainer]] = []
        for i in range(num_cycles):
            mode_name = rotation[i % len(rotation)]
            difficulties = modes[mode_name]
            cycle = self.generate_cycle(difficulties)
            all_cycles.append(cycle)
        return all_cycles
