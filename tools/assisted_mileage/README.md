# Maintenance collectors

## Retired from the comma on October 17, 2026

At the owner's request, the installed mileage updater, systemd service/timer and
device-side website deploy key were removed. Private historical JSON ledgers were
retained under `/data/maintenance/20261017/mileage-retired-data`.

The website now displays only the combined comma 3 and comma 4 totals fetched
from comma connect by the website repository's hourly GitHub Actions workflow.
Do not reinstall this local updater as part of a normal comma recovery. The code
and descriptions below remain as a historical reference; model/engagement log
mileage is no longer published by the comma or shown on the homepage.

These are the collector fixes tested before the updater was retired.
The publisher previously ran outside the driving checkout
at `/data/maintenance/ai-mileage`; that installation has now been removed.

For the historical attribution method and dependencies, see
[the source repository's mileage tools](https://github.com/ryanafdahl/Clarity-Pilot/tree/main/tools/assisted_mileage).
Never replace a private ledger with a fresh empty copy during an update or reinstall.
The maintenance report documents the backup, tests and one-time publication check.
