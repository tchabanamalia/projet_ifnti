import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

link_path = "/home/amk/IFNTI/StageL3/projet_ifnti/projet_ifnti/static/pdf/maquette"
target_path = "/home/amk/IFNTI/StageL3/projet_ifnti/media/pdf/maquette"

class SymbolicLinkUpdater(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == target_path:
            os.remove(link_path)
            os.symlink(target_path, link_path)
            print("Symbolic link updated")

if __name__ == "__main__":
    event_handler = SymbolicLinkUpdater()
    observer = Observer()
    observer.schedule(event_handler, path=target_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

