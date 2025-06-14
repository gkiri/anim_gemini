# from __future__ import annotations  # moved below after module docstring
# NOTE: The __future__ import below must come after the module docstring.
# The duplicate at the correct location is already present; commenting this out.
# from __future__ import annotations

"""Scene Planner Module
Auto-generated.

Purpose
-------
Converts a didactic scene description (title + narration) into a **Scene Definition
Language (SDL)** JSON structure that can later be compiled deterministically into
Manim code by ``ManimCompiler``.

The first iteration purposely *does not* call an LLM – it returns a deterministic
stub so that the rest of the enhanced pipeline can be wired and tested end-to-end.
A real prompt-based implementation can be dropped in later by replacing
``_generate_sdl_stub`` with an async OpenAI / OpenRouter call guarded by
``OPENROUTER_API_KEY``.

Exported API
------------
class ``ScenePlanner`` with two public helpers:
* ``generate_sdl_for_scene`` – synchronous version for quick tests.
* ``async_generate_sdl_for_scene`` – awaitable wrapper for concurrent usage.

Both return the SDL **dict** (already validated against a minimal schema).
"""

from __future__ import annotations
# COMMENTED OUT: future import not needed

import asyncio
import json
import logging
from typing import Any, Dict
import os

from pydantic import BaseModel, Field, ValidationError, validator
from openai import AsyncOpenAI

# Local imports
from project_drishti import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# ---------------------------------------------------------------------------
# Pydantic schema for SDL ----------------------------------------------------
# ---------------------------------------------------------------------------
class SDLElement(BaseModel):
    id: str
    type: str = Field("Text", description="Type of element – Text, Shape, Metaphor, Icon …")
    content: str | None = None
    purpose: str | None = None
    position_tag: str = Field("MIDDLE_CENTER")

    # additional free-form properties like font_size, color, shape_type …
    extra: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        extra = "allow"  # allow arbitrary keys beyond the core ones


class SDLAnimation(BaseModel):
    action: str = Field("FadeIn")
    target: str
    duration: float = 1.0
    delay: float = 0.0

    class Config:
        extra = "allow"


class SDLScene(BaseModel):
    scene_number: int
    title: str
    narration: str
    mood_color_profile: str | None = None
    total_scene_duration_hint: float | None = None
    sdl_elements: list[SDLElement] = Field(default_factory=list)
    sdl_animations: list[SDLAnimation] = Field(default_factory=list)

    # automatic basic validation that every animation target exists
    @validator("sdl_animations", each_item=True)
    def _check_animation_target(cls, anim: SDLAnimation, values):  # type: ignore[override]
        element_ids = {e.id for e in values.get("sdl_elements", [])}
        if anim.target not in element_ids:
            raise ValueError(f"Animation target '{anim.target}' not found amongst elements {element_ids}")
        return anim


# ---------------------------------------------------------------------------
# ScenePlanner ----------------------------------------------------------------
# ---------------------------------------------------------------------------
class ScenePlanner:
    """Produces SDL JSON for each didactic scene."""

    def __init__(self):
        # future LLM client could be prepared here (OpenAI / OpenRouter)
        self.use_llm = bool(config.OPENROUTER_API_KEY)
        if self.use_llm:
            try:
                self.async_client = AsyncOpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=config.OPENROUTER_API_KEY,
                )
            except Exception as e:
                logger.error(f"Failed to initialise AsyncOpenAI client: {e}. Falling back to stub generation.")
                self.async_client = None
                self.use_llm = False

    # ------------------------------------------------------------------
    # Public helpers ----------------------------------------------------
    # ------------------------------------------------------------------
    def generate_sdl_for_scene(self, scene_data: dict) -> dict | None:
        """Synchronous wrapper around the async version."""
        return asyncio.run(self.async_generate_sdl_for_scene(scene_data))

    async def async_generate_sdl_for_scene(self, scene_data: dict) -> dict | None:
        """Asynchronously generate SDL for **one** scene.

        A real implementation would fire an async chat completion request.
        For now we create a deterministic stub that is guaranteed to validate.
        """
        try:
            if self.use_llm:
                generated = await self._generate_sdl_via_llm(scene_data)
                if generated:
                    return generated
                logger.warning("LLM generation failed – falling back to stub.")
            return self._generate_sdl_stub(scene_data)
        except ValidationError as e:
            logger.error(f"ScenePlanner produced invalid SDL – {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error in ScenePlanner: {e}")
            return None

    # ------------------------------------------------------------------
    # Internal utilities ------------------------------------------------
    # ------------------------------------------------------------------
    def _generate_sdl_stub(self, scene_data: dict) -> dict:
        """Return a *very* simple SDL that passes validation and compiles."""
        scene_number = scene_data.get("scene_number", 1)
        title = scene_data.get("title", f"Scene {scene_number}")
        narration = scene_data.get("narration", "")

        element_id = "title_text"
        stub = SDLScene(
            scene_number=scene_number,
            title=title,
            narration=narration,
            mood_color_profile="DEFAULT",
            total_scene_duration_hint=8,
            sdl_elements=[
                SDLElement(
                    id=element_id,
                    type="Text",
                    content=title,
                    purpose="title",
                    position_tag="TOP_CENTER",
                    extra={"font_size": 60, "color": "YELLOW"},
                )
            ],
            sdl_animations=[
                SDLAnimation(action="Write", target=element_id, duration=2, delay=0.0)
            ],
        ).dict()

        logger.debug(f"Generated stub SDL for scene {scene_number}: {json.dumps(stub, indent=2)}")
        return stub

    # ------------------------------------------------------------------
    # LLM generation ----------------------------------------------------
    # ------------------------------------------------------------------
    async def _generate_sdl_via_llm(self, scene_data: dict) -> dict | None:
        if not self.async_client:
            return None

        scene_number = scene_data.get("scene_number", 1)
        title = scene_data.get("title", f"Scene {scene_number}")
        narration = scene_data.get("narration", "")

        # Describe the desired JSON schema succinctly
        schema_desc = (
            "Return JSON with keys: scene_number (int), title (str), narration (str), "
            "mood_color_profile (str), total_scene_duration_hint (float), "
            "sdl_elements (list of element objects), sdl_animations (list of animation objects). "
            "Each element object: id (str), type (Text|Shape|Metaphor|Icon), content/text, purpose, position_tag. "
            "Each animation object: action (e.g., FadeIn, Write, MoveTo, Scale), target (element id), duration (float), delay (float)."
        )

        system_msg = (
            "You are an expert Manim storyboard planner. "
            "For each scene you output a compact SDL JSON that conforms exactly to the described schema. "
            "Do NOT output code blocks, comments, or prose – ONLY valid JSON."
        )

        user_prompt = (
            f"Topic title: {title}\n"
            f"Narration: {narration}\n\n"
            f"{schema_desc}\n"
            "Generate the SDL JSON now."
        )

        try:
            # Attempt to call the LLM **in explicit JSON mode** if the backend supports it (OpenAI-compatible).
            # Many modern models (including those exposed via OpenRouter) honour the `response_format={"type":"json_object"}`
            # parameter and will return a *guaranteed* valid JSON object.  We optimistically try this first and
            # transparently fall back to classic text mode if the provider rejects the parameter.
            llm_kwargs = {
                "model": config.OPENROUTER_MODEL_NAME,
                "messages": [
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": user_prompt},
                ],
                "max_tokens": 800,
                "temperature": config.LLM_DEFAULT_TEMPERATURE,
            }
            # Add the JSON-mode hint – will raise if unsupported
            llm_kwargs["response_format"] = {"type": "json_object"}

            try:
                response = await self.async_client.chat.completions.create(**llm_kwargs)
            except Exception as rf_err:
                # Provider may not understand the parameter → retry *once* without it.
                logger.info("Provider rejected response_format json_object – retrying in text mode: %s", rf_err)
                llm_kwargs.pop("response_format", None)
                response = await self.async_client.chat.completions.create(**llm_kwargs)

            # Some providers return an empty string when `response_format={"type":"json_object"}`
            # even though the JSON is embedded elsewhere, or they only support free-text mode.
            # If we detect an empty/None content, transparently retry once *without* the response_format*.
            raw_content = (response.choices[0].message.content or "").strip()

            if not raw_content:
                logger.info("Empty content returned in JSON mode – retrying without response_format hint.")
                llm_kwargs.pop("response_format", None)
                response = await self.async_client.chat.completions.create(**llm_kwargs)
                raw_content = (response.choices[0].message.content or "").strip()

            # As a last resort, some OpenAI objects expose a `.model_dump_json()`; try that if still blank.
            if not raw_content and hasattr(response.choices[0].message, "model_dump_json"):
                try:
                    raw_content = response.choices[0].message.model_dump_json()
                except Exception:
                    pass

            # --- NEW ROBUST JSON EXTRACTION LOGIC START ---
            # LLMs often wrap JSON inside triple back-ticks and may include a language tag
            # such as ```json.  They may also add explanatory prose before / after.  In
            # all cases we search for the first "{" and the last "}" and keep the slice
            # in-between.
            import re, json as _json

            # Remove leading markdown code-fence line (```json or ```)
            raw_content = re.sub(r"^```[a-zA-Z0-9_]*\s*\n", "", raw_content)
            # Remove trailing code-fence
            raw_content = re.sub(r"\n```$", "", raw_content)

            # Locate substring that looks like JSON (naively the block from first '{' to last '}')
            brace_match = re.search(r"{.*}", raw_content, re.DOTALL)
            if brace_match:
                json_str = brace_match.group(0)
            else:
                json_str = raw_content  # fallback – may already be pure JSON

            # Attempt to parse – log preview on failure for easier debugging
            try:
                sdl_dict = _json.loads(json_str)
            except _json.JSONDecodeError as json_err:
                # ----------------------------------------------------
                # Fallback 1 – quick sanitation of common LLM artefacts
                # ----------------------------------------------------
                cleaned = (
                    json_str
                    .replace("…", "")                      # remove Unicode ellipsis
                    .replace("\u2026", "")                 # escaped ellipsis
                )

                # Remove any trailing commas before closing braces/brackets
                import re as _re
                cleaned = _re.sub(r",\s*([}\]])", r"\1", cleaned)

                try:
                    sdl_dict = _json.loads(cleaned)
                    logger.warning("JSON decoded successfully after basic sanitation of Unicode ellipsis / trailing commas.")
                except _json.JSONDecodeError as json_err2:
                    # ----------------------------------------------------
                    # Fallback 2 – attempt Python literal_eval in case of single quotes
                    # ----------------------------------------------------
                    import ast as _ast
                    try:
                        sdl_dict = _ast.literal_eval(cleaned)
                        logger.warning("SDL parsed via ast.literal_eval after JSON decode failures (likely single quotes).")
                    except Exception as lit_err:
                        # Persist raw LLM payload for easier debugging later
                        try:
                            debug_dir = os.path.join(config.COMMON_OUTPUT_DIR, "scene_planner", "raw_failures")
                            os.makedirs(debug_dir, exist_ok=True)
                            dbg_path = os.path.join(debug_dir, f"scene{scene_number}_raw.txt")
                            with open(dbg_path, "w", encoding="utf-8") as dbg_f:
                                dbg_f.write(raw_content)
                            logger.warning("Raw LLM SDL dumped to %s for manual inspection.", dbg_path)
                        except Exception as dump_err:
                            logger.error("Failed to dump raw SDL for debugging: %s", dump_err)

                        # ----------------------------------------------------
                        # Fallback 4 – attempt YAML parse (superset of JSON)
                        # ----------------------------------------------------
                        try:
                            import yaml  # PyYAML if available
                            sdl_dict = yaml.safe_load(cleaned)
                            logger.warning("SDL parsed via yaml.safe_load after all JSON repairs failed.")
                        except Exception:
                            logger.error(
                                "JSON decoding still failed after sanitation, literal_eval, heuristic repair, and YAML fallback: %s. Returning None. Snippet was:\n%s…",
                                lit_err, cleaned[:500]
                            )
                            return None
            # --- NEW ROBUST JSON EXTRACTION LOGIC END ---

            # ------------------------------------------------------------
            # Validate using Pydantic – catches missing/invalid fields
            # ------------------------------------------------------------
            try:
                validated = SDLScene.parse_obj(sdl_dict)
            except ValidationError as ve:
                # Persist the raw_content and the intermediate dict for debugging
                try:
                    debug_dir = os.path.join(config.COMMON_OUTPUT_DIR, "scene_planner", "raw_failures")
                    os.makedirs(debug_dir, exist_ok=True)
                    dbg_path = os.path.join(debug_dir, f"scene{scene_number}_validation_error.txt")
                    with open(dbg_path, "w", encoding="utf-8") as dbg_f:
                        dbg_f.write("# Raw LLM content\n\n")
                        dbg_f.write(raw_content)
                        dbg_f.write("\n\n# Parsed dict (pretty)\n\n")
                        import json as _json
                        dbg_f.write(_json.dumps(sdl_dict, indent=2))
                        dbg_f.write("\n\n# Pydantic validation error\n\n")
                        dbg_f.write(str(ve))
                    logger.error("SDL validation failed – details dumped to %s", dbg_path)
                except Exception as dump_exc:
                    logger.error("Failed to dump SDL validation failure details: %s", dump_exc)
                return None

            return validated.dict()
        except Exception as e:
            logger.error(f"LLM SDL generation failed: {e}")
            return None

    def _attempt_json_repair(self, text: str):
        """Best-effort conversion of almost-JSON text to a valid JSON dict.

        This helper purposefully *does not* try to be a full JSON5 parser – it merely
        performs quick regex replacements that fix the majority of common LLM
        artefacts:
        • single quotes ➔ double quotes
        • python None/True/False ➔ null/true/false
        • C++/JS style comments stripped
        If parsing still fails the method returns ``None`` so the caller can
        continue with the usual fallback logic.
        """
        import re, json as _json

        # Strip out C-style (// …) and hash (# …) comments
        text = re.sub(r"(?m)^\s*(//|#).*?$", "", text)

        # Replace single quotes with double quotes *outside* of already quoted segments.
        # This naive implementation works well enough for typical short SDL payloads.
        # It deliberately avoids touching escaped single quotes within strings.
        def _replace_single(match):
            return match.group(0).replace("'", '"')

        # Only replace quotes that appear *outside* of double-quoted regions
        text = re.sub(r"'(?:[^'\\]|\\.)*'", _replace_single, text)

        # Replace Python literals with JSON equivalents
        text = re.sub(r"\bNone\b", "null", text)
        text = re.sub(r"\bTrue\b", "true", text)
        text = re.sub(r"\bFalse\b", "false", text)

        try:
            return _json.loads(text)
        except Exception:
            return None


# ---------------------------------------------------------------------------
# CLI test (dev only) --------------------------------------------------------
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    planner = ScenePlanner()
    sample_scene = {"scene_number": 1, "title": "Test", "narration": "Something"}
    result = planner.generate_sdl_for_scene(sample_scene)
    print(json.dumps(result, indent=2)) 