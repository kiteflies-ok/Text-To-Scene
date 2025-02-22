import os
import time
import logging
from pathlib import Path
import shutil

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FileCleaner:
    def __init__(self):
        self.cleanup_dirs = [
            Path("uploads"),
            Path("media/animations"),
            Path("media/voiceovers"),
            Path("temp")
        ]
        self.max_file_age = 24 * 3600  # 24 hours in seconds

    def clean_old_files(self):
        """Delete files older than max_file_age from cleanup directories"""
        try:
            for cleanup_dir in self.cleanup_dirs:
                if not cleanup_dir.exists():
                    continue

                logger.info(f"Cleaning directory: {cleanup_dir}")
                self._clean_directory(cleanup_dir)

        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")

    def _clean_directory(self, directory: Path):
        """Recursively clean files in a directory"""
        for item in directory.iterdir():
            try:
                if item.is_file():
                    self._check_and_remove_file(item)
                elif item.is_dir():
                    self._clean_directory(item)  # Recursive call
                    if not any(item.iterdir()):  # Remove empty directories
                        item.rmdir()
                        logger.info(f"Removed empty directory: {item}")
            except Exception as e:
                logger.error(f"Failed to process {item}: {str(e)}")

    def _check_and_remove_file(self, file_path: Path):
        """Check file age and remove if older than threshold"""
        file_age = time.time() - file_path.stat().st_mtime
        if file_age > self.max_file_age:
            try:
                if file_path.suffix == '.mp4' or file_path.suffix == '.wav':
                    file_path.unlink()  # Delete file
                    logger.info(f"Deleted old file: {file_path}")
                else:
                    logger.warning(f"Skipping non-media file: {file_path}")
            except Exception as e:
                logger.error(f"Failed to delete {file_path}: {str(e)}")

def setup_file_cleaner(interval_hours: int = 1):
    """Setup periodic cleanup (to be called from main application)"""
    import schedule
    import time
    from threading import Event
    
    cleaner = FileCleaner()
    
    def cleanup_job():
        logger.info("Starting scheduled file cleanup")
        cleaner.clean_old_files()
        logger.info("Completed file cleanup")

    # Schedule the cleanup job
    schedule.every(interval_hours).hours.do(cleanup_job)
    
    # Run the scheduler in a separate thread
    stop_event = Event()
    
    def run_scheduler():
        while not stop_event.is_set():
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    
    import threading
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
    return stop_event

if __name__ == "__main__":
    # For testing purposes
    cleaner = FileCleaner()
    cleaner.clean_old_files()