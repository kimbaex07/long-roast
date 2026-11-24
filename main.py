import os
import sys

LINE = (
    "My agent reads 200 skills, spawns three subagents, and writes a report "
    "\u2014 all to avoid the one tool call that would actually finish the job."
)


def main():
    if not (1 <= len(LINE) <= 200):
        sys.stderr.write("entry line must be 1-200 characters\n")
        return 1
    if not LINE.strip():
        sys.stderr.write("entry line must not be only whitespace\n")
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.umask(0o022)
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        path = os.path.join(fallback, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
