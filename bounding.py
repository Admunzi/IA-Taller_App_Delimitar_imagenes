from PIL import Image, ImageFilter, ImageDraw
import credentials


def bounding_faces(filename, faces_detected):
    image = Image.open(credentials.PATH_UPLOADS_FILES + filename)

    for face in faces_detected['FaceDetails']:
        bounding_box(face, image)

    image.save(credentials.PATH_UPLOADS_FILES + filename)
    return filename


def bounding_box(face, image):
    box = face['BoundingBox']
    x = image.size[0] * box['Left']
    y = image.size[1] * box['Top']
    w = image.size[0] * box['Width']
    h = image.size[1] * box['Height']

    # create bounding box
    draw = ImageDraw.Draw(image)
    draw.rectangle(((x, y), (x + w, y + h)), outline='red', width=2)
