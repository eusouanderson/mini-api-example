import subprocess
import os

def build_executable():
    main_file = "aplicacaoTkin.py"
    
    command = [
        "pyinstaller",
        "--onefile",
        "--noconsole",  
        main_file
    ]
    
    try:
        print(f"Building executable for {main_file}...")
        subprocess.run(command, check=True)
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
    finally:
        cleanup()

def cleanup():
    build_folders = ["build", "__pycache__"]
    spec_file = "aplicacaoTkin.spec"
    
    for folder in build_folders:
        if os.path.exists(folder):
            print(f"Removing folder: {folder}")
            os.system(f"rmdir /s /q {folder}" if os.name == "nt" else f"rm -rf {folder}")
    
    if os.path.exists(spec_file):
        print(f"Removing spec file: {spec_file}")
        os.remove(spec_file)
    
    print("Cleanup completed.")

if __name__ == "__main__":
    build_executable()
