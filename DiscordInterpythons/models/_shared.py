from __future__ import annotations

from typing import Any

from pydantic import BaseModel as PyDanticBaseModel


class _BaseModel(PyDanticBaseModel):
    _omit: set[str] = {}

    @property
    def _omitted_fields(self) -> set[str]:
        return {
            name
            for name in self._omit
            if getattr(self, name, None) is None
        }

    def dict(
        self,
        **kwargs,
    ) -> dict[str, Any]:
        return super().dict(exclude=self._omitted_fields)

    def json(
        self,
        **kwargs,
    ) -> str:
        return super().json(exclude=self._omitted_fields)
