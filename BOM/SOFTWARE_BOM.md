# IX-Fusion Software BOM

Release: 0.1.0

## Required runtime

| Component | Supported range | Purpose |
|---|---|---|
| Python | >=3.11 | runtime and validation tooling |
| NumPy | >=2.0,<3 | deterministic numerical arrays and integration support |
| Matplotlib | >=3.8,<4 | reproducible review figures |

The package does not require a database, network service, GPU, cloud account, or external
API for its internal release-0.1 proof of concept.

## Optional high-authority tools

These are **not dependencies of the internal POC** and are not bundled:

| Tool family | Intended use |
|---|---|
| DESC | 3-D MHD equilibrium and optimization |
| SIMSOPT | stellarator coil/field optimization and engineering constraints |
| VMEC-class solver | independent 3-D ideal-MHD equilibrium cross-check |
| guiding-center / orbit solver | particle confinement |
| MHD stability tool | finite-pressure stability |
| gyrokinetic / transport tool | turbulent transport |
| RF full-wave/deposition tool | heating/current-drive/control validation |
| neutronics tool | blanket, shielding and breeding analysis |

A future release must record exact versions/hashes of external tools in each evidence bundle.

## License note

IX-Fusion itself is under `LicenseRef-IX-Fusion-Eval-Only-1.0`. Third-party software keeps
its own license. This BOM is descriptive and is not a license grant for third-party tools.
