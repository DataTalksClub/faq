"""Opik tracing helpers for FAQ automation.

Local Opik (docker compose in ../opik):
  OPIK_URL_OVERRIDE=http://localhost:5173/api
  OPIK_WORKSPACE=default
  OPIK_PROJECT_NAME=faq-automation

Disable tracing:
  OPIK_ENABLED=false

All helpers are no-ops when opik is not installed or disabled,
so CI / Lambda / tests without opik keep working.
"""

from __future__ import annotations

import functools
import os


def is_opik_enabled() -> bool:
    return os.environ.get("OPIK_ENABLED", "true").lower() not in ("0", "false", "no", "off")


def project_name(default: str = "faq-automation") -> str:
    return os.environ.get("OPIK_PROJECT_NAME", default)


def configure_opik() -> None:
    """Point the SDK at local Opik when env vars say so. Safe to call always."""
    if not is_opik_enabled():
        return
    try:
        import opik  # type: ignore
    except ImportError:
        return
    # use_local=True sets URL to http://localhost:5173/api when OPIK_URL_OVERRIDE is unset.
    # When OPIK_URL_OVERRIDE is set explicitly we respect it.
    try:
        if os.environ.get("OPIK_URL_OVERRIDE"):
            opik.configure(
                url_override=os.environ["OPIK_URL_OVERRIDE"],
                workspace=os.environ.get("OPIK_WORKSPACE", "default"),
            )
        else:
            # Only auto-configure local if nothing else configured yet.
            if not os.environ.get("OPIK_URL_OVERRIDE") and not os.path.exists(
                os.path.expanduser("~/.opik.config")
            ):
                opik.configure(use_local=True)
    except Exception:
        pass


def wrap_openai_client(client, project: str | None = None):
    """Wrap an OpenAI client with track_openai. Returns original on failure."""
    if not is_opik_enabled():
        return client
    try:
        from opik.integrations.openai import track_openai  # type: ignore

        configure_opik()
        return track_openai(client, project_name=project or project_name())
    except Exception:
        return client


def track(_fn=None, *, name: str | None = None, project: str | None = None, **kwargs):
    """Drop-in replacement for opik.track that no-ops when disabled/missing."""

    def decorator(fn):
        if not is_opik_enabled():
            return fn
        try:
            from opik import track as opik_track  # type: ignore

            configure_opik()
            tracked = opik_track(
                project_name=project or project_name(),
                **kwargs,
            )(fn)
            # Preserve explicit span name via metadata when provided.
            if name:
                @functools.wraps(fn)
                def wrapper(*args, **kw):
                    return tracked(*args, **kw)

                wrapper.__opik_span_name__ = name  # type: ignore
                return wrapper
            return tracked
        except Exception:
            return fn

    if _fn is None:
        return decorator
    return decorator(_fn)
