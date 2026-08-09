from dataclasses import dataclass, field

@dataclass
class StudyRecord:
    topic : str
    minutes : int
    notes : list[str] = field(default_factory=list)
