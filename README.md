[![Github](https://img.shields.io/github/license/hansatcode/HCSAuto?style=flat-square)](https://github.com/HanSatCode/HCSAuto/blob/main/LICENSE)


## 소개
HCSAuto(은)는 전작 윈도우와 리눅스 환경에서 백그라운드 작업으로 여려명의 사람들을 자동으로 자가진단을 수행하는 프로그램 입니다.<br/>
이 프로그램은 Python Selenium와 ChromeDriver을 기반으로 제작되었습니다.

## 주의
```
각 시·도별 방역수칙을 지키면서 사용해주세요. 
이상증상이 있으면 사용을 중단하고, 자가진단 앱 혹은 웹사이트에 직접 접속해서 변경이 가능합니다.
사용한 이후로 발생하는 피해는 사용자 본인에게 책임이 있습니다.
```
## 설치
사용하기에 앞서, [데스크톱용 Chrome](https://www.google.com/intl/ko/chrome/) 및 [ChromeDriver](https://chromedriver.chromium.org/home)(이)가 필요합니다.
```
1. 데스크톱용 Chrome 설치 프로그램을 실행하여 설치합니다.
2. 주소 표시줄에 'chrome://version/'을 입력하여 현재 데스크톱용 Chrome의 버전을 확인합니다.
3. 데스크톱용 Chrome 버전에 맞는 ChromeDriver(을)를 다운로드 받아줍니다.
4. 다운로드 받은 파일을 패키지의 'Driver' 폴더에 삽입합니다.
```
## 사용
이 프로그램은 메신저 프로그램 'Discord'의 Bot Alert 혹은 Windows Alert를 지원합니다.<br/>
Windows Alert의 경우, 정상적으로 종료된 경우 Alert창을 띄우지 않습니다.
```
1. 'Data.csv'을 편집해 [학교이름, 작업대상 이름, 생년월일 6자리, 비밀번호 4자리] 순으로 입력합니다.
   작업할 인원이 2명 이상일 경우, 줄바꿈을 통해 새로운 데이터를 입력합니다.
2. 본인이 Alert를 받고자 하는 플랫폼을 선택하여 실행합니다.
```
