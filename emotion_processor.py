import av
import cv2
import numpy as np
import mediapipe as mp
from keras.models import load_model
from streamlit_webrtc import VideoProcessorBase

# Load model and labels once
try:
    model = load_model("model.h5")
    label = np.load("label.npy")
except Exception as e:
    print(f"Error loading model: {e}")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

class EmotionProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        frm = frame.to_ndarray(format="bgr24")
        frm = cv2.flip(frm, 1)  
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
        
        lst = []
        if res.face_landmarks:
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)
        
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            lst = np.array(lst).reshape(1, -1)
        
            pred = label[np.argmax(model.predict(lst))]
            print(pred)
            cv2.putText(frm, pred, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            # Note: Saving to file from a callback might have concurrency issues but keeping original logic for now
            np.save("emotion.npy", np.array([pred]))
            
        if res.face_landmarks:
             drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
             
        if res.left_hand_landmarks:
            drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS) 

        if res.right_hand_landmarks:
            drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
    
        return av.VideoFrame.from_ndarray(frm, format="bgr24")
