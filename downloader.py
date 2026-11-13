import json, os, time, requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

with open("enter_json_file_name_here", "r", encoding="utf-8", errors="ignore") as f:
    items = json.load(f)

os.makedirs("photos", exist_ok=True)

def download_image(task):
    p, owner, i, u = task
    folder = f"photos/{owner}"
    path = f"{folder}/{p.get('shortCode','_')}_{i}.jpg"

    if os.path.exists(path):
        return True


    for attempt in range(3):
        try:
            r = requests.get(u, timeout=60)
            if r.ok:
                os.makedirs(folder, exist_ok=True)
                with open(path, "wb") as img_file:
                    img_file.write(r.content)
                return True
        except Exception as e:
            if attempt == 2: 
                print(f"\nSkip {u}: {e}")
            else:
                time.sleep(1) 
    return False


tasks = []
for p in items:
    if p.get("type") == "Video":
        continue
    kids = [k for k in p.get("childPosts") or [] if k.get("type") != "Video"]
    urls = [k.get("displayUrl") for k in kids] or [p.get("displayUrl")]
    owner = p.get("ownerUsername", "unknown")
    for i, u in enumerate(filter(None, urls)):
        tasks.append((p, owner, i, u))

print(f"startung parallel download of {len(tasks)} images...")

with ThreadPoolExecutor(max_workers=8) as executor:
    list(tqdm(executor.map(download_image, tasks), total=len(tasks), desc="downloading photos"))
