# CAMP Universal Connector Standard v1.0

## Connector Types

**CAMP-BAYONET-60** (Power only)
- XT60-HC inside M16 bayonet housing
- Orange color
- 11.1V / GND

**CAMP-BAYONET-USB-C** (Power + Data)
- USB-C inside M16 bayonet housing
- Blue color
- 11.1V + UART (TX/RX)
- 2× captive M3 screws (quarter-turn to secure)

## Assembly

Power: Insert → Push → Twist 90° CW → Click Data: Screw M3 (×2) → Insert → Twist 90° CW → Click

Release: Unscrew M3 (×2) → Twist 90° CCW → Pull

Code

## Specs

| Part | Spec |
|------|------|
| Housing | 3D-printed PETG, M16 thread insert |
| Bayonet | 3 slots, 120° apart, keyed |
| Power | XT60-HC, 60A rated |
| Data | USB-C, UART 9600 baud (JSON) |
| Cable | 3.5m, silicone, color-coded |
| Cost | ~7€ per connector |

## Locations (Torso rear panel)

Data Connector (Blue): 50mm from top-right Power Connector (Orange): 120mm from top-right

Code

## Protocol (UART)

```json
{"src":"TORSO","cmd":"SERVO","id":2,"angle":45}
{"ack":"SERVO","id":2,"actual":44,"status":"OK"}
