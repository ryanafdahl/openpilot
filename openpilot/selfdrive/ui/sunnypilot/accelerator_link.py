"""
Copyright (c) 2026-, Zeph Leggett.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.

The user's say over the accelerator link, shared by the mici and tici models panels.
On is the only enable; the backend reads the param, the panels only write it.
"""
from openpilot.selfdrive.ui.ui_state import ui_state
from openpilot.sunnypilot import accelerators

LINK_PARAM = "JetlinkEnabled"


def link_enabled() -> bool:
  """never raises: a params library older than the key would take the settings panel down"""
  try:
    return bool(ui_state.params.get(LINK_PARAM))
  except Exception:
    return False


def set_link_enabled(enabled: bool) -> None:
  try:
    ui_state.params.put_bool(LINK_PARAM, enabled, block=True)
    # manager caches which modeld it runs; the link decides that
    ui_state.params.remove('ModelRunnerTypeCache')
  except Exception:
    pass  # same unknown-key case as the read


def link_toggle_meaningful() -> bool:
  """Always expose the opt-in control, including before first detection.

  USB gadget setup only runs after JetlinkEnabled is set. Hiding this control
  until the accelerator is present therefore makes a fresh installation
  impossible to enable from the UI.
  """
  return True


def selected_accelerator_model() -> str:
  """The picked accelerator model's name, '' when the link has no registry."""
  return next((m['name'] for m in accelerators.model_choices() if m['selected']), '')
