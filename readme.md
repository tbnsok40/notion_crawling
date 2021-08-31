> # Notion Crawling for 🦁 Likelion PNU 9th applicant


## 🦁 개요 - 취지
1. 멋쟁이사자처럼 9기 부산대 지원자 정보 취합 프로그램 from Notion
2. 서류 합격자 선별 및 이름, 개별 점수 크롤링
3. 그냥 해보고 싶었다

<hr/>


## 🦁 설명

1. chromedriver 설치 후 실행파일(Crawling_notion.py)과 같은 디렉토리에 배치합니다.

![image](https://user-images.githubusercontent.com/40200760/111263240-e1ec1b80-8668-11eb-9a0a-031dcc4259de.png)

- 우선 Crawling_notion.py와 chromedriver 파일만 고려합니다.
- (crawling_phone.py --> Crawling_notion.py)


2. 크롤링 할 notion page의 url을 url 변수로 지정합니다.

![image](https://user-images.githubusercontent.com/40200760/111264425-d7328600-866a-11eb-879f-396d283dffc8.png)

<br/>

3. 아래 사진처럼 1차 합격자의 명단과 번호가 박스형태로 저장돼 있습니다. 박스 내부의 지원자 이름과 휴대폰 번호의 개별 Xpath를 가져옵니다(개발자 도구). 
<br/>

![image](https://user-images.githubusercontent.com/40200760/111266806-655c3b80-866e-11eb-9f05-649929ec471c.png)

<br/>


- Xpath를 분석하여, iterate 시켜야 할 element를 for문 처리하면 합격자를 추합할 수 있습니다.
- 해당 페이지의 지원자 xpath를 분석하면, 아래의 str(i)부분의 i값이 각 지원자의 순서를 나타내는 것을 알 수 있습니다.
- <br/>
- 예를 들어, 첫번째 지원자의 str(i)가 3이라면, for문의 첫번째 인자는 3이 되고,
- 두번째 인자는 전체 지원자의 수를 크롤링하여 동적으로 처리할 수 있습니다.

```html
'/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[19]/div[2]/div/div/div[2]/div[1]/div[' + str(i) + ']/a/div/div[2]/div'
```
![image](https://user-images.githubusercontent.com/40200760/111264594-28db1080-866b-11eb-82fa-6b01f8fa86ea.png)

<br/>


4. 총 합격자 인원의 값을 xpath로 가져와 for문의 두번째 인자로 넣습니다. 

![image](https://user-images.githubusercontent.com/40200760/111265175-0bf30d00-866c-11eb-8c5d-e79332b4cb07.png)

<br/>


5. 코드를 실행하면 notion 페이지가 자동으로 열리는데, 이때 <strong> 노션 페이지를 하단으로 스크롤</strong>해주어야 합니다.
- 그렇지 않으면 렌더링이 마저 돌지않아, 크롤러가 위치를 제대로 찾을 수 없게 됩니다.

<br/>


6. 나머지 과정은 코드를 그대로 실행하면 됩니다.


- 여담이지만, 이 프로젝트 로직 짜는게 너무 재밌어서 집 가는 버스 맨 뒷 좌석에서 코딩한 기억이 나네요 ㅎ,,