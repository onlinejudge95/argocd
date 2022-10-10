import dataclasses
import functools
import os


@dataclasses.dataclass
class Config:
    server_url: str = dataclasses.field(
        default_factory=functools.partial(os.environ.get, "ARGOCD_API_BASE_URL")
    )
