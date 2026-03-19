#!./venv/bin/python3
import os
import webvtt
import sys

from webvtt.errors import MissingFilenameError

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("--help", "-h"):
        sys.stdout.write("Usage: python srtToVttConverter.py srtFile\nOutput is written into srtFile.vtt\n")
    elif os.path.isfile(sys.argv[1]):
        outPath = f"{sys.argv[1]}.vtt"
        try:
            webvtt.from_srt(sys.argv[1]).save(outPath, "utf-8")
            sys.stdout.write(f"VTT file saved into {outPath}\n")
        except MissingFilenameError:
            sys.stdout.write(f"Invalid filename: {sys.argv[1]}\n")
        except Exception as e:
            sys.stdout.write(f"Unexpected error: {e}\n")
    else:
        sys.stdout.write(f"Error: File {sys.argv[1]} does not exist\n")
        sys.exit(1)
