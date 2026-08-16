# IX-Fusion Conceptual System BOM

## Authority boundary

This is a **category-level requirements BOM**, not a procurement list or physical build
specification. It intentionally omits quantities, dimensions, voltages, currents, field
strengths, radiation design values, fuel inventories, fabrication drawings, operating
procedures, and component part numbers.

Its purpose is to prevent computational optimization from pretending that the surrounding
engineering system is free.

| System category | Research function | Release-0.1 status |
|---|---|---|
| 3-D magnetic confinement geometry | create target stellarator field | reduced seed only |
| superconducting magnet/shaping system | realize optimized field | conceptual / external solver gate |
| magnet supports | maintain geometry under load | normalized structural proxy only |
| structural/position sensing | detect geometry drift | architecture only |
| plasma diagnostics | estimate plasma/magnetic state | architecture only |
| distributed RF/EM actuation | heating/current drive/active control | spatial phase model only |
| vacuum boundary | contain plasma environment | requirement only |
| plasma-facing components | survive/route surface heat | normalized heat proxy only |
| divertor/edge exhaust | impurity and power exhaust | not modeled |
| blanket/shield | absorb/protect/manage neutron environment | space/penetration proxy only |
| fuel-cycle system | provide/manage fusion fuel | not modeled |
| tritium breeding system | future D-T self-sufficiency | not modeled |
| cryogenic plant | support superconducting magnets | normalized burden proxy only |
| magnet protection/safe dump | manage stored-energy faults | architecture only |
| instrumentation power | deterministic measurement support | architecture only |
| plant thermal conversion | convert recovered heat to electricity | not modeled |
| control and safety systems | interlocks, logging, fault response | software architecture only |
| remote handling/maintenance | service activated/complex hardware | requirement only |

No category in this table is evidence that a corresponding physical subsystem has been
designed or validated.
