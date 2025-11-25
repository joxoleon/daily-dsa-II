from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class FileMetadata:
    name: str
    category: str
    topic: str
    weight: int
    difficulty: Optional[str] = None
    link: Optional[str] = None


@dataclass
class FileRecord:
    path: Path
    content: str
    metadata: FileMetadata


class ResourceLoader:
    """
    Loads all structured solution files, keeping their text and parsed metadata
    in memory for later scheduling/output.
    """

    def __init__(
        self,
        fundamentals_dir: Path | str | None = None,
        leetcode_dir: Path | str | None = None,
    ) -> None:
        self.repo_root = Path(__file__).resolve().parents[1]
        base = self.repo_root / "00_structured"
        self.fundamentals_dir = Path(fundamentals_dir) if fundamentals_dir else base / "fundamentals"
        self.leetcode_dir = Path(leetcode_dir) if leetcode_dir else base / "leetcode"

        self.fundamentals: List[FileRecord] = []
        self.leetcode: List[FileRecord] = []
        self.file_map: Dict[Path, FileRecord] = {}
        self.refresh()

    def refresh(self) -> None:
        """(Re)load all fundamentals and leetcode files into memory."""
        self.fundamentals = self._load_dir(self.fundamentals_dir)
        self.leetcode = self._load_dir(self.leetcode_dir)
        combined = self.fundamentals + self.leetcode
        self.file_map = {record.path: record for record in combined}

    def _load_dir(self, directory: Path) -> List[FileRecord]:
        if not directory.exists():
            raise FileNotFoundError(f"Missing directory: {directory}")

        records: List[FileRecord] = []
        for path in sorted(directory.rglob("*.py")):
            content = path.read_text(encoding="utf-8")
            metadata = self._parse_metadata(content)
            records.append(
                FileRecord(
                    path=path.relative_to(self.repo_root),
                    content=content,
                    metadata=metadata,
                )
            )
        return records

    def _parse_metadata(self, content: str) -> FileMetadata:
        lines = content.splitlines()
        raw_meta: Dict[str, str] = {}

        for line in lines[:3]:
            stripped = line.strip()
            if stripped.startswith("# ["):
                raw_meta.update(self._extract_metadata_pairs(stripped))

        weight = self._safe_int(raw_meta.get("Weight"))
        return FileMetadata(
            name=raw_meta.get("Name", ""),
            category=raw_meta.get("Category", ""),
            topic=raw_meta.get("Topic", ""),
            weight=weight,
            difficulty=raw_meta.get("Difficulty"),
            link=raw_meta.get("Link"),
        )

    @staticmethod
    def _extract_metadata_pairs(line: str) -> Dict[str, str]:
        pairs = re.findall(r"\[\s*([^:\]]+):\s*([^\]]+)\]", line)
        return {key.strip(): value.strip() for key, value in pairs}

    @staticmethod
    def _safe_int(value: Optional[str]) -> int:
        try:
            return int(value) if value is not None else 0
        except ValueError:
            return 0
