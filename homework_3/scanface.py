import os
import cv2
import numpy as np
import face_recognition
import matplotlib.pyplot as plt
from tqdm import tqdm

analysing_img = 'sanich_and_nigga.png'

class Face:
    def __init__(self, bounding_box, cropped_face, name, feature_vector):
        self.bounding_box = bounding_box
        self.cropped_face = cropped_face
        self.name = name
        self.feature_vector = feature_vector

def load_image(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def show_image(image):
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def draw_bounding_box(image_test, loc_test):
    top, right, bottom, left = loc_test
    line_color = (0, 255, 0)
    line_thickness = 2
    cv2.rectangle(image_test, (left, top), (right, bottom), line_color, line_thickness)
    return image_test

def draw_name(image_test, loc_test, pred_name):
    top, right, bottom, left = loc_test
    font_style = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5
    font_color = (0, 0, 255)
    font_thickness = 3
    text_size, _ = cv2.getTextSize(pred_name, font_style, font_scale, font_thickness)
    bg_top_left = (left, top - text_size[1])
    bg_bottom_right = (left + text_size[0], top)
    line_color = (0, 255, 0)
    line_thickness = -1
    cv2.rectangle(image_test, bg_top_left, bg_bottom_right, line_color, line_thickness)
    cv2.putText(image_test, pred_name, (left, top), font_style, font_scale, font_color, font_thickness)
    return image_test

def detect_faces(image_test, faces, threshold=0.6):
    locs_test = face_recognition.face_locations(image_test, model='hog')
    vecs_test = face_recognition.face_encodings(image_test, locs_test, num_jitters=1)
    for loc_test, vec_test in zip(locs_test, vecs_test):
        distances = []
        for face in faces:
            distance = face_recognition.face_distance([vec_test], face.feature_vector)
            distances.append(distance)
        if np.min(distances) > threshold:
            pred_name = 'unknown'
        else:
            pred_index = np.argmin(distances)
            pred_name = faces[pred_index].name
        image_test = draw_bounding_box(image_test, loc_test)
        image_test = draw_name(image_test, loc_test, pred_name)
    return image_test

def create_database() -> list[object]:
    def get_filenames() -> list[str]:
        filenames = os.listdir('templates')
        filenames = [filename for filename in filenames if not filename.startswith('!')]
        return filenames
    
    def load_image(path):
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
    
    faces = []
    filenames = get_filenames()
    for filename in tqdm(filenames, total=len(filenames)):
        image = load_image(os.path.join('templates', filename))
        locs = face_recognition.face_locations(image, model='hog')
        if len(locs) == 0:
            print(f"{filename} is not detected on photo")
            continue
        
        loc = locs[0]
        vec = face_recognition.face_encodings(image, [loc], num_jitters=20)[0]
        top, right, bottom, left = loc
        cropped_face = image[top:bottom, left:right]
        face = Face(bounding_box=loc, cropped_face=cropped_face, name=filename.split('.')[0], feature_vector=vec)
        faces.append(face)
    return faces

def detect_faces_in_image(image_path, faces):
    image_test = load_image(image_path)
    result_image = detect_faces(image_test, faces)
    show_image(result_image)

faces = create_database()
detect_faces_in_image(f"photos/{analysing_img}", faces)