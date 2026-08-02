from __future__ import annotations

from SimConnect import AircraftRequests, SimConnect

from models import FlightState


class SimConnectTelemetry:
    def __init__(self) -> None:
        self._sim = SimConnect()
        self._requests = AircraftRequests(self._sim, _time=500)

    def read(self) -> FlightState:
        return FlightState(
            altitude_ft=float(self._requests.get("PLANE_ALTITUDE") or 0.0),
            indicated_airspeed_kt=float(self._requests.get("AIRSPEED_INDICATED") or 0.0),
            heading_deg=float(self._requests.get("PLANE_HEADING_DEGREES_TRUE") or 0.0),
            pitch_deg=float(self._requests.get("PLANE_PITCH_DEGREES") or 0.0),
            bank_deg=float(self._requests.get("PLANE_BANK_DEGREES") or 0.0),
            latitude_deg=float(self._requests.get("PLANE_LATITUDE") or 0.0),
            longitude_deg=float(self._requests.get("PLANE_LONGITUDE") or 0.0),
            fuel_total_gal=float(self._requests.get("FUEL_TOTAL_QUANTITY") or 0.0),
            gear_down=bool(self._requests.get("GEAR_HANDLE_POSITION") or 0),
            stall_warning=bool(self._requests.get("STALL_WARNING") or 0),
            overspeed_warning=bool(self._requests.get("OVERSPEED_WARNING") or 0),
        )
