가로 병합 코드 문서화 

##개요
이 코드는 두 개의 폴더에서 동일한 이름을 가진 이미지를 찾아 가로로 병합한 후, 새로운 폴더에 저장 기능을 수행합니다. 

## 필요 라이브러리
- `os` : 파일 및 폴더 경로를 처리하는 모듈
- `PIL` (Python Imaging Library, `Pillow` 패키지) : 이미지 열기, 병합, 저장을 위한 라이브러리

## 코드 설명

```python
import os
from PIL import Image  # 이미지 처리를 위한 PIL 모듈
```
- `os` 모듈을 사용하여 폴더 및 파일을 관리합니다.
- `PIL` 라이브러리의 `Image` 모듈을 사용하여 이미지를 불러오고 조작합니다.

```python
# 이미지가 저장된 폴더 경로
folder1 =[]   # 첫 번째 이미지 폴더
folder2 = []  # 두 번째 이미지 폴더
output_folder =[]   # 결과를 저장할 폴더
```
- 병합할 이미지가 저장된 두 개의 폴더 경로를 지정합니다.
- 병합된 이미지를 저장할 폴더를 지정합니다.

```python
# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
```
- `os.path.exists()`를 사용하여 출력 폴더가 존재하는지 확인합니다.
- 존재하지 않으면 `os.makedirs()`를 사용하여 폴더를 생성합니다.

```python
# 첫 번째 폴더의 이미지 파일 리스트 가져오기
folder1_images = os.listdir(folder1)
folder2_images = os.listdir(folder2)
```
- `os.listdir()`를 사용하여 각 폴더 내의 파일 목록을 가져옵니다.

```python
# 동일한 이름의 이미지 병합
for file_name in folder1_images:
    if file_name in folder2_images:  # 동일한 이름의 파일이 두 폴더에 있을 경우
```
- 첫 번째 폴더의 파일 목록을 순회하면서 동일한 이름의 파일이 두 번째 폴더에도 존재하는지 확인합니다.

```python
        # 이미지 파일 경로
        path1 = os.path.join(folder1, file_name)
        path2 = os.path.join(folder2, file_name)
```
- `os.path.join()`을 사용하여 각 이미지 파일의 전체 경로를 생성합니다.

```python
        # 이미지 열기
        image1 = Image.open(path1)
        image2 = Image.open(path2)
```
- `Image.open()`을 사용하여 두 이미지를 메모리로 로드합니다.

```python
        # 두 이미지 크기 확인 (2560x1261인지 확인)
        width1, height1 = image1.size
        width2, height2 = image2.size
```
- `.size` 속성을 사용하여 이미지의 너비와 높이를 가져옵니다.

```python
        if width1 == 2560 and height1 == 1261 and width2 == 2560 and height2 == 1261:
```
- 두 이미지의 크기가 `(2560, 1261)`인지 확인하여 일치하는 경우에만 병합을 수행합니다.

```python
            # 새 캔버스 생성 (가로 병합)
            new_width = width1 + width2
            new_height = height1
            new_image = Image.new("RGB", (new_width, new_height), (255, 255, 255))  # 배경 흰색 캔버스
```
- `Image.new()`를 사용하여 새로운 빈 캔버스를 생성합니다.
- 가로 크기는 두 이미지를 합친 크기로 설정하고, 배경색은 흰색(`(255, 255, 255)`)으로 지정합니다.

```python
            # 이미지 붙이기
            new_image.paste(image1, (0, 0))  # 첫 번째 이미지를 왼쪽에 붙이기
            new_image.paste(image2, (width1, 0))  # 두 번째 이미지를 오른쪽에 붙이기
```
- `paste()` 메서드를 사용하여 첫 번째 이미지는 왼쪽, 두 번째 이미지는 오른쪽에 배치합니다.

```python
            # 결과 저장
            output_path = os.path.join(output_folder, file_name)  # 동일한 이름으로 저장
            new_image.save(output_path)
            print(f"병합된 이미지 저장: {output_path}")
```
- 병합된 이미지를 `output_folder`에 저장합니다.
- 저장된 이미지의 경로를 출력하여 확인할 수 있도록 합니다.

```python
        else:
            print(f"이미지 크기가 일치하지 않습니다: {file_name}")
```
- 이미지 크기가 다를 경우, 해당 파일명을 출력하여 경고 메시지를 표시합니다.

```python
    else:
        print(f"두 번째 폴더에 없는 파일: {file_name}")
```
- 두 번째 폴더에 해당 이미지가 존재하지 않는 경우 경고 메시지를 출력합니다.

```python
print("모든 병합이 완료되었습니다.")
```
- 모든 파일에 대한 병합이 완료되었음을 알리는 메시지를 출력합니다.

## 결론
이 코드는 두 개의 폴더에서 동일한 이름을 가진 이미지를 찾아 가로로 병합한 후, 새로운 폴더에 저장하는 기능을 수행합니다. 이미지 크기가 `(2560, 1261)`일 때만 병합을 수행하도록 설정되어 있으며, 크기가 맞지 않거나 파일이 존재하지 않을 경우 경고 메시지를 출력합니다.
