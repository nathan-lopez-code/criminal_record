import dlib
import PIL.Image
import numpy as np
import os
from django.conf import settings


class FaceRecognition:

    """ classe reponsable de la reconnaissance faciale  """

    def __init__(self, tolerance=0.6):

        self.tolerance = tolerance
        self.pose_predictor_68_point = dlib.shape_predictor(os.path.join(settings.BASE_DIR,
                                                                         "learn_model/shape_predictor_68_face_landmarks.dat"))
        self.pose_predictor_5_point = dlib.shape_predictor(os.path.join(settings.BASE_DIR,
                                                                        "learn_model/shape_predictor_5_face_landmarks.dat"))
        self.face_encoder = dlib.face_recognition_model_v1(os.path.join(settings.BASE_DIR,
                                                                        "learn_model/dlib_face_recognition_resnet_model_v1.dat"))
        self.face_detector = dlib.get_frontal_face_detector()

    def face_detection(self, databaseimg, testimg):
        """ reconnaissance faciale """

        # encodage de l'image
        imaged_encodage = self.encoding(np.array(PIL.Image.open(databaseimg)))
        imaget_encodage = self.encoding(np.array((PIL.Image.open(testimg))))

        result = np.linalg.norm(imaged_encodage - imaget_encodage)
        if result <= self.tolerance:
            return True
        else:
            return False


    def encoding(self, img):
        face_locations = self.face_detector(img, 1)
        shaped = self.pose_predictor_68_point(img, face_locations[0])
        encoding_img = np.array(self.face_encoder.compute_face_descriptor(img, shaped, num_jitters=1))

        return encoding_img
