from roboflow import Roboflow
rf = Roboflow(api_key="mUl24lsWupBcc7L4t0Pe")
project = rf.workspace("workspace-btbkh").project("oakridge-codefest")
model = project.version(1).model

# infer on a local image
# print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("1-15.jpg", confidence=75).save("prediction.jpg")
# model.predict("1-15.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())