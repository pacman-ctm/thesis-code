import json
import os
import pandas as pd
import pickle
from vncorenlp import VnCoreNLP
rdrsegmenter = VnCoreNLP('../vncorenlp/VnCoreNLP-1.1.1.jar', annotators="wseg", max_heap_size='-Xmx500m')


data = dict()

annotations = []
images = []


caption_id = 0
for image_name in os.listdir("./train-images"):
    image_id = int(image_name.split(".")[0])
    if not os.path.exists(f"./annotations/{image_id}.txt"):
        continue
    captions = [line.strip() for line in open(f"./annotations/{image_id}.txt", "r", encoding="utf-8")]
    images.append({
        "id": image_id, 
        "filename": image_name,
    })

    for caption in captions:
        sent_tokenizer = rdrsegmenter.tokenize(caption)
        # print(sent_tokenizer)
        segment_caption = " ".join(s for s in sent_tokenizer[0])
        annotations.append({
        "id": caption_id,
        "image_id": image_id,
        "caption": caption,
        "segment_caption": segment_caption
        })
        caption_id += 1



data['images'] = images
data['annotations'] = annotations

with open("train_data.json", "w+", encoding="utf-8") as file:
    json.dump(data, fp = file, ensure_ascii=False, indent=1)

print("Done")
