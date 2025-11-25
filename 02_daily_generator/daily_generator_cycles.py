from __future__ import annotations

import math
from typing import Dict, List

from resource_loader import FileMetadata, FileRecord, ResourceLoader

###############################
### Cycle Selection Logic ###
###############################

WEIGHT_GROUPS = {
    10: {"arrays","arrays_and_strings","sliding_window","two_pointers","hashing","strings"},
    9:  {"binary_search","dp","trees","graphs"},
    8:  {"intervals","greedy","heap","heaps","backtracking"},
    7:  {"linked_list","stack","stacks","queues","grids"},
    6:  {"bit_manipulation","math"},
    5:  {"union_find","tries"},
    4:  {"design"},
    3:  {"extra_20_must_know"}
}

CATEGORY_WEIGHTS = {c: w for w, cats in WEIGHT_GROUPS.items() for c in cats}


class ProblemContainer:
    def __init__(self, metadata: FileMetadata, source_code: str) -> None:
        self.metadata = metadata
        self.source_code = source_code
        self.age = 0 # Number of cycles since last selection
        
    def get_priority(self) -> int:
        return self.metadata.weight + self.age

    def category(self) -> str:
        return self.metadata.category

class CategoryContainer:
    def __init__(self, name: str, problems: List[ProblemContainer]) -> None:
        self.name = name
        self.problems: List[ProblemContainer] = problems
        self.age = 0 # Number of cycles since last selection
        self.weight = CATEGORY_WEIGHTS.get(name, 0)
        self.size = len(problems)

    def get_priority(self) -> float:
        size_factor = math.log(self.size + 1)
        return (self.weight * size_factor) + self.age


    def select_problem(self) -> ProblemContainer:
        # Select problem with highest priority
        selected = max(self.problems, key=lambda p: p.get_priority())
        # Reset age of selected problem, increment others
        for problem in self.problems:
            if problem == selected:
                problem.age = 0
            else:
                problem.age += 1
        return selected

class CycleGenerator:
    def __init__(self, problem_list: List[FileRecord]) -> None:
        self.categories: Dict[str, CategoryContainer] = {}
        for record in problem_list:
            problem = ProblemContainer(record.metadata, record.content)
            category_name = record.metadata.category
            if category_name not in self.categories:
                self.categories[category_name] = CategoryContainer(category_name, [])
            self.categories[category_name].problems.append(problem)
    
    def select_next_category(self) -> CategoryContainer:
        # Select category with highest priority
        selected = max(self.categories.values(), key=lambda c: c.get_priority())
        # Reset age of selected category, increment others
        for category in self.categories.values():
            if category == selected:
                category.age = 0
            else:
                category.age += 1
        return selected
    
    def generate_cycle(self, num_problems_per_category: int, num_categories: int) -> List[ProblemContainer]:
        cycle: List[ProblemContainer] = []
        for _ in range(num_categories):
            category = self.select_next_category()
            for _ in range(num_problems_per_category):
                problem = category.select_problem()
                cycle.append(problem)
        return cycle



if __name__ == "__main__":

    resource_loader = ResourceLoader()
    
    fundamentals_cycle_generator = CycleGenerator(resource_loader.fundamentals)
    cycles: List[List[ProblemContainer]] = []
    for i in range(60):
        cycle = fundamentals_cycle_generator.generate_cycle(num_problems_per_category=2, num_categories=2)
        cycles.append(cycle)
    
    # Count duplicates within the cycles
    problem_count: Dict[str, int] = {}
    for cycle in cycles:
        for problem in cycle:
            name = problem.metadata.name
            problem_count[name] = problem_count.get(name, 0) + 1
    duplicates = {name: count for name, count in problem_count.items() if count > 1}
    print("Duplicates in fundamentals cycles:", duplicates)
    print("Total unique problems in fundamentals cycles:", len(problem_count))
    print("Duplicate count:", sum(count - 1 for count in duplicates.values()))
