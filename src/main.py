from __future__ import annotations

import json
import time
from pathlib import Path

from rules import evaluate_rules
from telemetry import SimConnectTelemetry


LOG_PATH = Path("logs/flight.jsonl")


def main() -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    telemetry = SimConnectTelemetry()

    print("Black Mamba AI Copilot online. Waiting for telemetry...")

    while True:
        try:
            state = telemetry.read()
            alerts = evaluate_rules(state)

            with LOG_PATH.open("a", encoding="utf-8") as log_file:
                log_file.write(state.model_dump_json() + "\n")

            print(
                json.dumps(
                    {
                        "altitude_ft": round(state.altitude_ft, 1),
                        "ias_kt": round(state.indicated_airspeed_kt, 1),
                        "heading_deg": round(state.heading_deg, 1),
                        "alerts": [alert.model_dump() for alert in alerts],
                    },
                    ensure_ascii=False,
                )
            )

            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Copilot stopped.")
            break
        except Exception as exc:
            print(f"Telemetry error: {exc}")
            time.sleep(2)


if __name__ == "__main__":
    main()
