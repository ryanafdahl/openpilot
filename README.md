# Clarity Pilot

Clarity Pilot is a personal, experimental sunnypilot build for comma 4 with a Jetson Orin Nano Super running JetLink 0.8.5 / protocol v3, or a separately maintained experimental Pixel 11 Pro XL backend.

- [Source repository, device setup, and validation notes](https://github.com/ryanafdahl/Clarity-Pilot)
- [Pixel APK, checksum, and Android installation](https://github.com/ryanafdahl/Clarity-Pilot/tree/main/android)
- [Build log and archive](https://t3st.site)

This is the device deployment repository. Install its `Clarity-Pilot` branch with `installer.comma.ai/ryanafdahl/Clarity-Pilot`. The source of record is `ryanafdahl/Clarity-Pilot`, branch `main`; the installer resolves to `ryanafdahl/openpilot`, branch `Clarity-Pilot`.

Cinque Terre Model V2 is selected on the comma and prepared on the Jetson. The Pixel APK retains its parked-only restrictions; its prior parity and desk results do not qualify it for driving. Upstream sunnypilot changes through `a5f44653d7f43ad57fef2f546f3916ec4cbf3c56` are included, with custom JetLink controls and fallback preserved.

## October 10 reinstall build

This installation branch includes JetLink 0.8.5 and the **Clarity Pilot** home-screen branding. The installed comma build, integration tests, endpoint compatibility check and reboot checks passed. CD210 and Cinque Terre V2 were preserved on the maintained device; a fresh installation still needs normal setup and model selection.

The subsequent [October 10 USB drive review](https://github.com/ryanafdahl/Clarity-Pilot/blob/main/docs/JETLINK_DRIVE_2026-10-10.md) parsed 47 full-rate segments from two sessions: **53,609 large-model outputs**, consecutive within each session, with no fallback after joining. Mean reported execution was **22.55 ms** across those outputs. The report documents startup retries, a shutdown-only controls-mismatch event, GPS backup warnings and missing paired Jetson journals. These sessions provide initial USB evidence; intermittent failure recovery and longer-term reliability remain unqualified.

[Exact pins, validation, device backups and reinstall guidance](https://github.com/ryanafdahl/Clarity-Pilot/blob/main/docs/JETLINK_UPDATE_2026-10-10.md). The source repository and this installation branch are both updated; their Git histories remain separate.

The [nightly assisted-mileage tracker](https://github.com/ryanafdahl/Clarity-Pilot/tree/main/tools/assisted_mileage) is a separate offroad maintenance job under `/data/maintenance/ai-mileage`, outside this driving checkout. Back up its private `ledger.json` and `baseline.json` before wiping `/data`; reinstall its systemd units after an AGNOS image replacement. Its public totals combine the owner's reported comma 4 / comma 3 history with new logged assistance and appear on [t3st.site](https://t3st.site/mileage.html).

## Upstream project

![](https://user-images.githubusercontent.com/47793918/233812617-beab2e71-57b9-479e-8bff-c3931347ca40.png)

## 🌞 What is sunnypilot?
[sunnypilot](https://github.com/sunnyhaibin/sunnypilot) is a fork of comma.ai's openpilot, an open source driver assistance system. sunnypilot offers the user a unique driving experience for over 300+ supported car makes and models with modified behaviors of driving assist engagements. sunnypilot complies with comma.ai's safety rules as accurately as possible.

## 💭 Join our Community Forum
Join the official sunnypilot community forum to stay up to date with all the latest features and be a part of shaping the future of sunnypilot!
* https://community.sunnypilot.ai/

## Documentation
https://docs.sunnypilot.ai/ is your one stop shop for everything from features to installation to FAQ about the sunnypilot

## 🚘 Running on a dedicated device in a car
First, check out this list of items you'll need to [get started](https://community.sunnypilot.ai/t/getting-started-using-sunnypilot-in-your-supported-car/251).

## Installation
Next, refer to the sunnypilot community forum for [installation instructions](https://community.sunnypilot.ai/t/read-before-installing-sunnypilot/254), as well as a complete list of [Recommended Branch Installations](https://community.sunnypilot.ai/t/recommended-branch-installations/235).

## 🎆 Pull Requests
We welcome both pull requests and issues on GitHub. Bug fixes are encouraged.

Pull requests should be against the most current `master` branch.

## 📊 User Data

By default, sunnypilot uploads the driving data to comma servers. You can also access your data through [comma connect](https://connect.comma.ai/).

sunnypilot is open source software. The user is free to disable data collection if they wish to do so.

sunnypilot logs the road-facing camera, CAN, GPS, IMU, magnetometer, thermal sensors, crashes, and operating system logs.
The driver-facing camera and microphone are only logged if you explicitly opt-in in settings.

By using this software, you understand that use of this software or its related services will generate certain types of user data, which may be logged and stored at the sole discretion of comma. By accepting this agreement, you grant an irrevocable, perpetual, worldwide right to comma for the use of this data.

## Licensing

sunnypilot is released under the [MIT License](LICENSE). This repository includes original work as well as significant portions of code derived from [openpilot by comma.ai](https://github.com/commaai/openpilot), which is also released under the MIT license with additional disclaimers.

The original openpilot license notice, including comma.ai’s indemnification and alpha software disclaimer, is reproduced below as required:

> openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.
>
> Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.
>
> **THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
> YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
> NO WARRANTY EXPRESSED OR IMPLIED.**

For full license terms, please see the [`LICENSE`](LICENSE) file.

## 💰 Support sunnypilot
If you find any of the features useful, consider becoming a [sponsor on GitHub](https://github.com/sponsors/sunnyhaibin) to support future feature development and improvements.


By becoming a sponsor, you will gain access to exclusive content, early access to new features, and the opportunity to directly influence the project's development.


<h3>GitHub Sponsor</h3>

<a href="https://github.com/sponsors/sunnyhaibin">
  <img src="https://user-images.githubusercontent.com/47793918/244135584-9800acbd-69fd-4b2b-bec9-e5fa2d85c817.png" alt="Become a Sponsor" width="300" style="max-width: 100%; height: auto;">
</a>
<br>

<h3>PayPal</h3>

<a href="https://paypal.me/sunnyhaibin0850" target="_blank">
<img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="PayPal this" title="PayPal - The safer, easier way to pay online!" border="0" />
</a>
<br></br>

Your continuous love and support are greatly appreciated! Enjoy 🥰

<span>-</span> Jason, Founder of sunnypilot
