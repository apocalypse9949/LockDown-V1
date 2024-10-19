import os
import signal
import psutil

def all_processes():
  for proc in psutil.process.iter(['pid','name']):
    try:
      if proc.info
