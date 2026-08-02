from __future__ import annotations

from models import Alert, FlightState


def evaluate_rules(state: FlightState) -> list[Alert]:
    alerts: list[Alert] = []

    if state.overspeed_warning:
        alerts.append(
            Alert(
                code="OVERSPEED",
                severity="critical",
                message="Reduce velocidad inmediatamente.",
                metadata={"ias_kt": state.indicated_airspeed_kt},
            )
        )

    if state.stall_warning:
        alerts.append(
            Alert(
                code="STALL",
                severity="critical",
                message="Advertencia de pérdida: reduzca ángulo de ataque y aplique potencia.",
            )
        )

    if 0 < state.fuel_total_gal < 5:
        alerts.append(
            Alert(
                code="LOW_FUEL",
                severity="warning",
                message="Combustible total bajo.",
                metadata={"fuel_total_gal": state.fuel_total_gal},
            )
        )

    if state.altitude_ft < 1_000 and abs(state.bank_deg) > 30:
        alerts.append(
            Alert(
                code="EXCESSIVE_BANK_LOW_ALTITUDE",
                severity="warning",
                message="Inclinación excesiva a baja altitud.",
                metadata={"bank_deg": state.bank_deg, "altitude_ft": state.altitude_ft},
            )
        )

    return alerts
