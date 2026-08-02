from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


class FlightState(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    altitude_ft: float = 0.0
    indicated_airspeed_kt: float = 0.0
    heading_deg: float = 0.0
    pitch_deg: float = 0.0
    bank_deg: float = 0.0
    latitude_deg: float = 0.0
    longitude_deg: float = 0.0
    fuel_total_gal: float = 0.0
    gear_down: bool = False
    stall_warning: bool = False
    overspeed_warning: bool = False


class Alert(BaseModel):
    code: str
    severity: str
    message: str
    metadata: dict[str, Any] = Field(default_factory=dict)
