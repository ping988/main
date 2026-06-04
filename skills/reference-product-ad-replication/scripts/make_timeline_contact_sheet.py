#!/usr/bin/env python3
"""Create a labeled timeline contact sheet for frame-level video review."""

from __future__ import annotations

import argparse
import math
import shutil
import tempfile
from pathlib import Path

import cv2
from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--start", type=float, default=0.0)
    parser.add_argument("--end", type=float)
    parser.add_argument("--step", type=float, default=0.5)
    parser.add_argument("--cols", type=int, default=8)
    parser.add_argument("--thumb-width", type=int, default=160)
    return parser.parse_args()


def open_capture(path: Path) -> tuple[cv2.VideoCapture, Path | None]:
    capture = cv2.VideoCapture(str(path))
    if capture.isOpened():
        return capture, None

    # Some OpenCV Windows builds fail on non-ASCII paths.
    temp_dir = Path(tempfile.mkdtemp(prefix="video-contact-sheet-"))
    temp_path = temp_dir / f"input{path.suffix}"
    shutil.copy2(path, temp_path)
    capture = cv2.VideoCapture(str(temp_path))
    if not capture.isOpened():
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise RuntimeError(f"Could not open video: {path}")
    return capture, temp_dir


def main() -> None:
    args = parse_args()
    if args.step <= 0 or args.cols <= 0 or args.thumb_width <= 0:
        raise ValueError("step, cols, and thumb-width must be positive")

    capture, temp_dir = open_capture(args.video)
    try:
        fps = capture.get(cv2.CAP_PROP_FPS) or 24.0
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
        duration = frame_count / fps if frame_count else 0.0
        end = duration if args.end is None else min(args.end, duration)
        if args.start < 0 or end <= args.start:
            raise ValueError("Invalid start/end range")

        times = []
        current = args.start
        while current <= end + 1e-9:
            times.append(current)
            current += args.step

        cards: list[Image.Image] = []
        thumb_height = round(args.thumb_width * 16 / 9)
        label_height = 28
        for timestamp in times:
            capture.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)
            ok, frame = capture.read()
            if not ok:
                continue
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image.thumbnail((args.thumb_width, thumb_height))
            card = Image.new("RGB", (args.thumb_width, thumb_height + label_height), "white")
            card.paste(image, ((args.thumb_width - image.width) // 2, 0))
            ImageDraw.Draw(card).text((5, thumb_height + 5), f"{timestamp:.2f}s", fill=(15, 15, 15))
            cards.append(card)

        if not cards:
            raise RuntimeError("No frames were extracted")

        rows = math.ceil(len(cards) / args.cols)
        sheet = Image.new(
            "RGB",
            (args.cols * args.thumb_width, rows * (thumb_height + label_height)),
            (238, 234, 228),
        )
        for index, card in enumerate(cards):
            sheet.paste(
                card,
                ((index % args.cols) * args.thumb_width, (index // args.cols) * (thumb_height + label_height)),
            )

        args.output.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(args.output, quality=94)
        print(args.output)
    finally:
        capture.release()
        if temp_dir is not None:
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
