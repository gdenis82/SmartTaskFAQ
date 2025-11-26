# gunicorn.conf.py

import multiprocessing
import os

def _get_int_env(var_name, default):
    val = os.getenv(var_name, default)
    try:
        return int(val)
    except (TypeError, ValueError):
        return int(default)

def _get_float_env(var_name, default):
    val = os.getenv(var_name, default)
    try:
        return float(val)
    except (TypeError, ValueError):
        return float(default)

# --- Bind ---
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "8000")
bind = os.getenv("BIND", f"{host}:{port}")

# --- Workers ---
workers = _get_int_env("WEB_CONCURRENCY", "1")
worker_class = "uvicorn.workers.UvicornWorker"

# --- Timeouts ---
timeout = _get_int_env("TIMEOUT", "60")
keepalive = _get_int_env("KEEP_ALIVE", "5")

# --- Logging ---
loglevel = os.getenv("LOG_LEVEL", "info")
errorlog = "-"
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# --- Max requests (anti memory leaks) ---
max_requests = _get_int_env("MAX_REQUESTS", "1000")
max_requests_jitter = _get_int_env("MAX_REQUESTS_JITTER", "100")

# --- Security / Misc ---
preload_app = False
forwarded_allow_ips = "*"

# --- Startup hook ---
def when_ready(server):
    server.log.info("Server is ready. Spawning workers")
    server.log.info(f"Workers: {workers}, Bind: {bind}, Worker class: {worker_class}")