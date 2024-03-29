# 이거를 그래서 어떻게 하는거야..?
from PIL import Image
import json
import os

# JSON 파일에서 메타데이터를 읽는 함수
def read_metadata(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        # 예시로, 'creationTime' 키에서 날짜와 시간을 가져옵니다.
        # 실제 키는 JSON 파일에 따라 다를 수 있습니다.
        return data['creationTime']['timestamp']

# 사진의 EXIF 정보를 수정하는 함수
def update_photo_exif(photo_path, date_time):
    with Image.open(photo_path) as img:
        exif_data = img.getexif()
        # EXIF 태그는 정수로 표현됩니다. 'DateTimeOriginal' 태그는 보통 36867입니다.
        # 날짜와 시간 형식은 "YYYY:MM:DD HH:MM:SS"여야 합니다.
        exif_data[36867] = date_time
        img.save(photo_path, exif=exif_data)

# 메인 로직
def main():
    # 예시 경로입니다. 실제 경로로 변경해야 합니다.
    json_file_path = 'path/to/your/json_file.json'
    photo_path = 'path/to/your/photo.jpg'

    # JSON 파일에서 메타데이터 읽기
    metadata = read_metadata(json_file_path)

    # 사진 파일의 EXIF 정보 업데이트
    update_photo_exif(photo_path, metadata)

    # iCloud에 업로드하는 코드는 생략됩니다.
    # 'pyicloud' 라이브러리를 참고하세요.

if __name__ == "__main__":
    main()
