# from dataclasses import dataclass
from dataclasses import dataclass, field

@dataclass
class StudyRecord:
    topic: str
    minutes: int
    # tags: field(default_factory=list)
    tags: list = field(default_factory=list)

