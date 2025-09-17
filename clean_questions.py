#!/usr/bin/env python3
"""
Clean Questions Directory Script
Removes all files in the _questions directory before FAQ extraction to prevent
leftover or malformed files from interfering with the static site generator.
"""

import shutil
from pathlib import Path
import sys

def clean_questions_directory():
    """Remove all files and subdirectories in _questions directory"""
    questions_dir = Path('_questions')
    
    if not questions_dir.exists():
        print("No _questions directory found. Nothing to clean.")
        return True
    
    try:
        print(f"Cleaning _questions directory...")
        
        # Count files before deletion
        file_count = 0
        for item in questions_dir.rglob('*'):
            if item.is_file():
                file_count += 1
        
        # Remove all contents but keep the directory
        for item in questions_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
                print(f"Removed directory: {item}")
            else:
                item.unlink()
                print(f"Removed file: {item}")
        
        print(f"✅ Successfully cleaned _questions directory (removed {file_count} files)")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning _questions directory: {e}")
        return False

def main():
    """Main execution function"""
    print("DataTalks.Club FAQ Questions Directory Cleaner")
    print("=" * 50)
    
    success = clean_questions_directory()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()