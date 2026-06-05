## Custom Hex Protocol (CHP)

Files that use the `.chp` file extension follow the Custom Hex Protocol. Information about `.chp` files can be found here.

## Format Specification

The `.chp` format is a image file extension, supporting a 16x16 resolution with 256 colors.

| Line(s) | Data Component | Content Example / Format | Purpose |
| :--- | :--- | :--- | :--- |
| **Line 1** | Name Header | `NAME: Colors` | Defines the title of the artwork. |
| **Line 2** | Author Header | `AUTHOR: ghite0` | Credits the creator/artist. |
| **Line 3** | Date Header | `DATE: 2026-06-04` | Logs the date of creation (YYYY-MM-DD). |
| **Lines 4–19** | Pixel Grid Matrix | `016 016 057 ... 016` | A 16x16 grid of numbers separated by spaces. |
| **Data Values** | Color Protocol | `000` to `255` | 3-digit integers that map directly to ANSI 256 color IDs. |

## Viewing CHP

Attached in this repo is `chp-viewer.py`, which can display any valid `.chp` file in your terminal. Simply do the command `python chp-viewer.py` or `python3 chp-viewer.py` if you are on Linux.
