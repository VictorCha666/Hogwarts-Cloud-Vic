#!/usr/bin/env python3
import subprocess
import os

os.chdir(r"E:\2DAM\Acceso a datos\Hogwarts-Cloud-Vic\Hogwards-Segundo")

# Verificar si gradlew está en Git
try:
    result = subprocess.run(["git", "cat-file", "-e", "HEAD:gradlew"], capture_output=True)
    if result.returncode == 0:
        print("✓ gradlew already in repository")
    else:
        print("✗ gradlew NOT in repository, adding it...")
        subprocess.run(["git", "add", "-f", "gradlew", "gradlew.bat"], check=True)
        subprocess.run(["git", "commit", "-m", "chore: add gradle wrapper scripts"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✓ Successfully pushed gradlew to repository")
except Exception as e:
    print(f"Error: {e}")

