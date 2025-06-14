"""
Module: validator
Date: [Auto-generated]

A *cheap* static validator that runs before the expensive Manim render step.
At the moment it only does two things:
1.  "python -m py_compile" on the script – catches syntax errors fast.
2.  Optionally (toggle via env) run Manim in still-image mode ("-s")
    to detect runtime API mismatches.  The latter can add ~1 s per scene,
    so it is disabled by default but can be enabled by setting
    ENV ``DRISHTI_VALIDATE_FRAME=1``.

Return ``True`` if validation passes, else ``False``.
"""

from __future__ import annotations

import os
import subprocess
import sys
import logging
from pathlib import Path

from project_drishti import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


PYTHON_BIN = sys.executable  # use the same interpreter the pipeline is running under


def validate_script(script_path: str, scene_class_name: str | None = None) -> bool:
    """Return True if script passes fast validation checks."""
    script_path = os.path.abspath(script_path)
    if not os.path.exists(script_path):
        logger.error(f"Validator – script not found: {script_path}")
        return False

    # ------------------------------------------------------------------
    # 1) Syntax check ---------------------------------------------------
    # ------------------------------------------------------------------
    compile_cmd = [PYTHON_BIN, "-m", "py_compile", script_path]
    proc = subprocess.run(compile_cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        logger.error(f"Validator – syntax error in {script_path} :\n{proc.stderr}")
        return False
    logger.debug("Validator – syntax OK")

    # ------------------------------------------------------------------
    # 2) Optional quick Manim frame render ------------------------------
    # ------------------------------------------------------------------
    if os.environ.get("DRISHTI_VALIDATE_FRAME") == "1" and scene_class_name:
        cmd = [
            "manim",
            "-s",  # still image
            "-ql",  # low quality
            script_path,
            scene_class_name,
            "--media_dir",
            os.path.join(config.GENERATED_CONTENT_DIR, "validation_tmp"),
            "--disable_caching",
        ]
        logger.debug(f"Validator – running Manim still-frame check: {' '.join(cmd)}")
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0:
            logger.error(f"Validator – Manim still-frame render failed:\n{proc.stderr}")
            return False
    return True


if __name__ == "__main__":
    # very quick smoke test when invoked directly
    dummy = Path(__file__).resolve()
    print(validate_script(str(dummy))) 