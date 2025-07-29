


```python
!git clone https://github.com/Mouneshgouda/chest_xrays.git

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE=64   
BATCH_SIZE=32

train_path="/content/chest_xrays/chest_xray/train"
test_path="/content/chest_xrays/chest_xray/test"

train_path=ImageDataGenerator(rescale=1./255).flow_from_directory(
    train_path,
    target_size=(IMG_SIZE,IMG_SIZE), 
    batch_size=BATCH_SIZE,   
    class_mode='binary',
)
test_path=ImageDataGenerator(rescale=1./255).flow_from_directory(
    test_path,
    target_size=(IMG_SIZE,IMG_SIZE), 
    batch_size=BATCH_SIZE,   
    class_mode='binary',
)
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_path, epochs=5, validation_data=test_path)
model.save('pneumonia_model.h5')

```
