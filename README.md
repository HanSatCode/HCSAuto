# HCSAuto

> 이 프로그램은 2022년 2월 1일 이후로 새로운 기능 추가 및 버그 수정에 관한 업데이트가 중단됩니다.  
> 이 시간 이후로 프로그램이 정상적으로 작동하는 것에 대해서 보장할 수 없습니다.

HCSAuto는 Windows 및 Linux 환경에서 여러 사용자의 자가진단을 자동으로 수행하는 프로그램입니다.  
이 프로그램은 **Python Selenium** 및 **ChromeDriver**를 기반으로 제작되었습니다.

## ⚠️ 주의사항
- 각 지역 및 학교/직장의 방역 수칙을 잘 지키며 안전하게 사용해 주세요.
- 본인이나 진단 대상 분에게 조금이라도 이상 증상이 보인다면 바로 프로그램 사용을 멈추고, 공식 자가진단 앱이나 웹사이트에 직접 접속하셔서 상태를 변경해 주세요.
- 프로그램 사용으로 인해 생길 수 있는 결과와 책임은 사용자 본인에게 있으니 늘 유의해서 사용해 주세요.

## 🛠️ 설치 및 설정

사용하기에 앞서 [데스크톱용 Chrome](https://www.google.com/intl/ko/chrome/) 및 [ChromeDriver](https://chromedriver.chromium.org/home)가 필요합니다.

### 1. ChromeDriver 설정 (필수)
프로그램 실행을 위해 현재 PC에 설치된 Chrome 브라우저 버전과 일치하는 **ChromeDriver** 파일이 반드시 `src` 폴더 내에 존재해야 합니다.

> 1. 데스크톱용 Chrome 브라우저를 설치합니다.
> 2. 주소 표시줄에 `chrome://version/`을 입력하여 설치된 Chrome 버전을 확인합니다.
> 3. 확인한 버전에 딱 맞는 버전을 [ChromeDriver 다운로드 페이지](https://chromedriver.chromium.org/home)에서 다운로드합니다.
> 4. 다운로드한 `chromedriver.exe`(Windows) 또는 `chromedriver`(Linux) 파일을 **패키지의 `src` 폴더에 삽입**합니다.

### 2. Python 환경 설정
[Python 3](https://www.python.org/) 및 Selenium 라이브러리가 필요합니다.
> 1. Python 3을 설치합니다.
> 2. 터미널에서 아래 명령어를 실행하여 Selenium을 설치합니다.
   ```bash
   pip install selenium
   ```

## 🚀 사용 방법

이 프로그램은 Discord 봇 알림 또는 Windows Alert 알림을 지원합니다.

1. `src/member.csv` 파일을 편집하여 아래 순서대로 입력합니다. 여러 명을 등록하려면 줄바꿈을 통해 추가 데이터를 입력합니다.
   ```csv
   학교이름,이름,생년월일6자리,비밀번호4자리
   ```
   
2. Discord 알림을 사용하는 경우, `src/bot.csv` 파일을 편집하여 아래 순서대로 입력합니다.
   ```csv
   채널ID,봇토큰 <-- e.g. 123456789012345678,OTMyNzA1...
   ```
3. 원하는 실행 방식의 파일을 구동합니다.
   - **Windows 알림**: `HCSAuto_Windows.pyw` 실행 (완료 후 백그라운드 구동)
   - **Discord 알림**: `HCSAuto_Discord.pyw` 또는 `HCSAuto_Linux.py` 실행

## 💡 팁 & 기타 설정

### ChromeDriver 콘솔 창 숨기기 (Windows)
프로그램 실행 시 뜨는 ChromeDriver의 검은색 콘솔 창을 보이지 않게 하고 싶다면 아래와 같이 조치할 수 있습니다.

1. Python 설치 경로 내의 `selenium/webdriver/common/service.py` 파일을 엽니다.
2. `subprocess.Popen`을 호출하는 부분을 찾아 인자값으로 `creationflags=0x08000000`를 추가하고 저장합니다.

```python
self.process = subprocess.Popen(cmd, env=self.env,
                                close_fds=platform.system() != 'Windows',
                                stdout=self.log_file,
                                stderr=self.log_file,
                                stdin=PIPE,
                                creationflags=0x08000000)
```

## ⚙️ 작동 원리

1. **사용자 데이터 로드**: `src/member.csv` 파일로부터 자가진단을 수행할 사용자 정보(학교명, 이름, 생년월일, 가상 비밀번호)를 파싱합니다.
2. **브라우저 자동 구동**: `Selenium WebDriver`를 사용해 자가진단 공식 웹사이트에 접속합니다.
3. **가상 키패드 매핑 및 로그인**: 보안 상 랜덤하게 배치되는 가상 키패드 버튼의 `aria-label` 속성을 실시간으로 읽어와 비밀번호 입력을 수행합니다.
4. **설문 작성 및 제출**: 지정된 기본 설문(이상 증상 없음 등) 항목에 일괄 체크 후 자가진단을 제출합니다.
5. **결과 알림**: 정상 완료 여부를 Windows Alert 알림창 또는 Discord Bot 메시지를 통해 발송합니다.

## 🔗 참조 문서
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [ChromeDriver Download](https://chromedriver.chromium.org/home)
- [Chrome Download](https://www.google.com/intl/ko/chrome/)
