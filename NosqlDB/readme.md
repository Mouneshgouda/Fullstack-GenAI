## Mongodb

```python

from pymongo import MongoClient
import gridfs

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['hotel_booking']
fs = gridfs.GridFS(db)

# Hotel data
hotels_data = [
    {"name": "Taj Hotel", "location": "Mumbai", "price": 5000, "image": "taj.jpg"},
    {"name": "Oberoi Hotel", "location": "Delhi", "price": 4500, "image": "oberoi.jpg"},
    {"name": "Leela Palace", "location": "Bangalore", "price": 6000, "image": "leela.jpg"}
]

# Insert hotels with images
for hotel in hotels_data:
    with open(f"static/images/{hotel['image']}", "rb") as img_file:
        image_id = fs.put(img_file, filename=hotel['image'])
        db.hotels.insert_one({
            "name": hotel['name'],
            "location": hotel['location'],
            "price": hotel['price'],
            "image_id": image_id
        })

print("Hotels with images inserted successfully!")



```


