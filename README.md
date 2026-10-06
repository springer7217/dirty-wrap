# Dirty Wrap

A memorial wrap for Lee Springer's 2025 Model Y.

This repo started as a fork of [teslamotors/custom-wraps](https://github.com/teslamotors/custom-wraps). Everything that was not this car has been removed. The only template left is the 2025+ Model Y Premium map, which matches this Juniper Dual Motor (full-width rear light bar, Dual Motor badge, not Performance).

The wrap keeps the kids' finger drawings from a mud bath: the scribble mass, the figures, the smileys, `I AM BOO BOO BAKU!`, `we are cool`, `Boo Jesus`, the heart, star, flower, `HI!`, the stick figure, the big stacked `Boo Boo` clear of the wheel, `Boobackoo`, `wow`, and the two-line `HI HAVE A GOOD DAY!` on the hatch. The factory gunmetal stays on the hood, roof, glass, and upper doors. Mud film sits only on the lower doors. The license plate is not part of the wrap.

## This car

- 2025+ Model Y, Juniper body, Dual Motor
- Template: [`modely-2025-premium/template.png`](modely-2025-premium/template.png)
- Paint Shop name to load: `Mud Splatter`

White on the template is paintable. Transparent pixels are ignored, so the factory color shows through. Door lettering is turned toward the center of the template so it reads upright on the car.

## What is on the wrap

| Panel | What the kids wrote |
| --- | --- |
| Driver front door | Scribble mass, figures, smiley, `I AM / BOO BOO / BAKU!`, `we are cool` and two smileys |
| Driver rear door | `Boo` + cross + `Jesus`, heart, angel, star, flower, footprint, `HI!`, stick figure, stacked `Boo Boo` above the wheel |
| Passenger side | Cross, `Boobackoo`, two figures, small `Jesus`, large `wow`, cross |
| Hatch | Smiley, `HI HAVE A GOOD` / `DAY!`, flower. Left of center, under the light bar |

The signed-off file is the text version. A later brown tire-spray experiment was rejected and is not in this repo.

## Load it

Paint Shop needs software 4.59.0 or later. The file must be a PNG, 1024×1024, under 1 MB. The filename can be letters, numbers, spaces, underscores, and dashes, 30 characters max.

Mobile app: Creations → Wrap → Upload, then Toybox → Paint Shop → Wraps.

USB: format exFAT, FAT32, or Mac OS Extended. Make a folder named `Wraps` at the root. Put the PNG in that folder. Do not put map or firmware files on the same drive. NTFS is not supported.

Paint Shop is the on-screen visualization, not a vinyl wrap order.

## Layout

```
modely-2025-premium/template.png    the only vehicle template
modely-2025-premium/vehicle_image.png
wraps/                              notes for the signed-off wrap
```

Tesla's original templates and example wraps for other vehicles live upstream in [teslamotors/custom-wraps](https://github.com/teslamotors/custom-wraps).
