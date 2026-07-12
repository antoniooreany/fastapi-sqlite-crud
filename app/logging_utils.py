import logging
import json
import datetime
import os
from logging.handlers import RotatingFileHandler
from app.config import settings

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "process": record.process,
            "thread_name": record.threadName,
            "app_version": settings.app_version,
            "environment": settings.environment,
            "salt_used": settings.salt_used,
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        
        # Add extra fields if they exist in the record
        if hasattr(record, "request_id"):
            log_record["request_id"] = record.request_id
            
        return json.dumps(log_record)

def setup_logging():
    log_level = logging.DEBUG if settings.environment == "development" else logging.INFO
    
    # Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(JSONFormatter())
    
    # Rotating File Handler
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, "app.log"),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(JSONFormatter())
    
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Clear existing handlers to avoid duplicates
    if root_logger.hasHandlers():
        root_logger.handlers.clear()
        
    root_logger.addHandler(stream_handler)
    root_logger.addHandler(file_handler)
    
    # Specifically set level for app logger if needed
    logging.getLogger("app").setLevel(log_level)
