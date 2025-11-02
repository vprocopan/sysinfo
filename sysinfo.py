import shutil
import os

def show_env_vars(limit=5):
    print("\n🌍 Environment Variables:")
    for i, (k, v) in enumerate(os.environ.items()):
        print(f"  {k}={v}")
        if i >= limit:
            print("  ...")
            break

def show_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    print(f"\n💾 Disk usage for {path}:")
    print(f"  Total: {total // (2**30)} GiB")
    print(f"  Used:  {used // (2**30)} GiB")
    print(f"  Free:  {free // (2**30)} GiB")

show_env_vars()
show_disk_usage("/")