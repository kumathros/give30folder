# Gunicorn configuration file for production deployment

# Server socket
bind = "0.0.0.0:8000"
backlog = 2048

# Worker processes
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests, to prevent memory leaks
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = 'myproject'

# Server mechanics
daemon = False
pidfile = '/tmp/gunicorn.pid'
user = None
group = None
tmp_upload_dir = None

# SSL (if you're terminating SSL at gunicorn level)
# keyfile = "/path/to/keyfile"
# certfile = "/path/to/certfile"

# Environment
raw_env = [
    'DJANGO_SETTINGS_MODULE=myproject.settings',
]
