
"""
build_video.py
==============

Combine per‑slide PNG images and per‑slide narration WAV files into
`security_awareness.mp4` (≈30‑minute training video).

Directory layout expected:

project_root/
├── slides/
│   ├── slide01.png
│   ├── slide02.png
│   └── ... (22 slides)
├── audio/
│   ├── slide01.wav
│   ├── slide02.wav
│   └── ... (22 WAVs)
└── build_video.py   ← (this script)

Each WAV file should contain the narration that matches its slide.
Durations need not be equal; the script will read the exact length of
each WAV and keep the corresponding image on screen for that time.

Dependencies
------------
pip install moviepy==1.0.3

Usage
-----
python build_video.py

You’ll find `security_awareness.mp4` in the same folder.

Tip: If you prefer a single 30‑minute WAV instead of per‑slide files,
see the notes at the bottom of this script for a one‑liner tweak.

Author: ChatGPT (2025‑07‑11)
"""
import os
from pathlib import Path
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

# ---------- Configuration ----------
SLIDES_DIR = Path("slides")
AUDIO_DIR = Path("audio")
OUTPUT_FILE = "security_awareness.mp4"
FPS = 1  # 1 fps is fine for static slides; increase if you add animations
# -----------------------------------

def zero_pad(num: int, width: int = 2) -> str:
    return str(num).zfill(width)

def gather_assets():
    """Return sorted lists of slide paths and audio paths."""
    slides = sorted(SLIDES_DIR.glob("slide*.png"))
    audio = sorted(AUDIO_DIR.glob("slide*.wav"))
    assert len(slides) == len(audio) > 0, "Slides and audio counts do not match or are empty."
    return slides, audio

def build_video(slides, audio):
    clips = []
    for s_path, a_path in zip(slides, audio):
        # Load audio first to get its duration
        a_clip = AudioFileClip(str(a_path))
        img_clip = (
            ImageClip(str(s_path))
            .set_duration(a_clip.duration)
            .set_audio(a_clip)
            .resize(height=1080)  # ensures 1080p, width adjusted proportionally
        )
        clips.append(img_clip)

    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(OUTPUT_FILE, codec="libx264", audio_codec="aac", fps=FPS)

def main():
    slides, audio = gather_assets()
    print(f"Building video with {len(slides)} slides...")
    build_video(slides, audio)
    print(f"Done. Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()


"""  -------------------------
Single‑audio variation
-------------------------
If you have *one* long narration WAV called `narration.wav`:

1. Replace gather_assets() with:

    slides = sorted(SLIDES_DIR.glob("slide*.png"))
    audio_clip = AudioFileClip("narration.wav")
    # manually define timings in seconds e.g. [25.0, 40.3, 32.1, ...]
    durations = [...]
    assert len(durations) == len(slides)

2. Build each ImageClip with:
    start = sum(durations[:idx])
    img_clip = ImageClip(...).set_start(start).set_duration(durations[idx])

3. After loop: final = CompositeVideoClip(slide_clips, size=(1920,1080)).set_audio(audio_clip)

That’s it!
"""
