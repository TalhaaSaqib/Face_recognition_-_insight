import face_recognition
import cv2
import time
def check(first,second):
    r = cv2.imread(first)
    p = cv2.imread(second)
    
    biden_encoding = face_recognition.face_encodings(r)[0]
    unknown_encoding = face_recognition.face_encodings(p)[0]
    

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    return results
    
# try:
count = 0
import os 

fols = "forTest"

fol_list = os.listdir(fols)
# fol_list.sort()
for folder in fol_list:
    
    if folder.endswith(".txt"):
        continue
    else:
        sub_dir = os.listdir(f'{fols}/{folder}')
        
        t = len(sub_dir)    
        if t > 1:
            # t = time(hour, minute, second, microsecond)
            _one = f'{fols}/{folder}/{sub_dir[0]}'
            _two = f'{fols}/{folder}/{sub_dir[1]}'
            count = count + 1 
                    
            print(f' count : {count} of {len(fol_list)} , {_one} , {_two} , no.of pics : {t}')
            try:
                start = time.time()
                ubc = check(_one,_two)
                end = time.time()
                totalTime = end-start
                with open('errors.txt', 'a') as file_object:
                   file_object.write(f'Folder name : {folder} , image_one : {_one} , image_two : {_two} , Boolean : {ubc} , time : {totalTime} \n')
            except Exception as e:
                # print("failed")
                with open('errors.txt', 'a') as file_object:
                    file_object.write(f"Folder name : {folder} ,image_one : {_one} , image_two : {_two} , Failed : {e} , time : {totalTime}  \n")
                continue
        