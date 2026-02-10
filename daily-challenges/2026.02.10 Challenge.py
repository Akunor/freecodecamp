# start of main.py

def _to_seconds(hms: str) -> int:
    parts = [int(p) for p in hms.split(":")]
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h, m, s = 0, parts[0], parts[1]
    else:
        raise ValueError(f"Invalid time format: {hms!r}")
    return h * 3600 + m * 60 + s


def _format_delta(seconds: int) -> str:
    if seconds < 0:
        raise ValueError("Negative deltas are not supported")

    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)

    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def get_relative_results(results):
    winner = _to_seconds(results[0])
    return [
        "0" if (t := _to_seconds(r)) == winner else f"+{_format_delta(t - winner)}"
        for r in results
    ]

# end of main.py

