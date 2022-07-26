## [**SECTION1**](https://github.com/sangahnim/section_project/blob/main/section_1/AI_05_%EC%9D%B4%EC%83%81%EC%95%84_Section1.ipynb)
1. **주제**: 다음 분기에 설계해야할 게임에 대한 EDA Project
2. **데이터** : Kaggle의 Video Game Sales 바탕으로 변형된 csv file
> 데이터선정이유 및 문제정의
>  * 서비스산업 중 가장 인기있는 게임시장에 대해 분석해보고자 데이터를 선정.
>  * 지역별 선호하는 게임장르, 연도별 게임의 트렌드, 출고량이 높은 게임 및 플랫폼별 출고량 대해 확인하고 의사결정함.
3. **EDA, Data preprocessing** : 
>  1) 결측치제거 : 불필요한 'N/A'을 공란으로 만든 후, 해당내용 및 이 외의 결측치 포함된 행 제거
>  2) data type 변경 : Year 컬럼의 값들을 정수4자리로 변경
>  3) data 내용 정리 : 지역별 Sales 컬럼에 문자가 들어간 경우 삭제 후, Sales타입을 수치로 변경, Total_Sales 특성 생성, '-'->'_' 컬럼이름정리
>  4) 이상치제거 : Year 컬럼의 값 중 이상치 제거 (2000년대는 게임의 종류가 더 많은 데이터가 있어야하는데, 수치가 더 적어진 2016년 이후의 데이터가 누락됐다 판단함)
4. **시각화**
>  1) 지역별, 게임 장르별 출고율 (북미,EU,일본,기타지역의 장르별 게임 출고량을 원그래프로 나타냄)
<img width="960" alt="스크린샷 2022-07-26 오후 4 36 41" src="https://user-images.githubusercontent.com/86824895/180950539-1c97f0f3-e477-4e6d-8787-7468898a7e22.png">
<img width="968" alt="스크린샷 2022-07-26 오후 4 36 52" src="https://user-images.githubusercontent.com/86824895/180950564-82ba11ed-315b-4d43-9a28-1646147b6782.png">

>  2) 연도별 게임 장르의 출고량 시각화 (데이터의 Genre컬럼을 Year별로 구분하여 피봇테이테이블로 정리 후, 게임 장르별로 연간 출고량 변화를 선그래프로 나타냄)
>>      -> 액션과 스포츠는 2000년대 급성장을 하고, 플랫폼은 계속 꾸준히 인기있음을 확인.    
<img width="814" alt="스크린샷 2022-07-26 오후 4 37 02" src="https://user-images.githubusercontent.com/86824895/180950627-399e8e99-f226-4d9b-b167-2b190eb72508.png">

5. **출고량이 높은 게임에 대한 분석 및 시각화 프로세스**
>  1) 전체 출고량이 높은 게임에 대한 분석
>  2) 미국시장의 연도별 플랫폼 게임 출고량 (가장 큰 게임시장인 미국시장에서 플랫폼게임의 종류별 출고량을 선그래프로 나타냄)
>  <img width="1052" alt="스크린샷 2022-07-26 오후 4 39 47" src="https://user-images.githubusercontent.com/86824895/180950924-923e6bbe-16dd-4050-995a-38512b575d24.png">

6. **ttest 가설검정** (Wii와 플레이스테이션3 중 어떤 플랫폼을 사용해야 출고량이 더 높을지에 대한 ttest 가설검정)
>  1) 해당 가설검정을 하기 위해 데이터가 정규성, 등분산성을 띄지 않음을 확인 후, 데이터를 각각 box-cox로 변환하여 가설성립여부확인
>  <img width="782" alt="스크린샷 2022-07-26 오후 8 10 41" src="https://user-images.githubusercontent.com/86824895/180992959-43d89a4e-c88a-46b1-9957-da4718ad2f54.png">

>  2) 귀무가설 : Wii를 플랫폼으로 사용한 일반회사 출고량의 평균은 플레이스테이션3를 플랫폼으로 사용한 일반회사 출고량의 평균보다 높을 것이다.
>  3) 대립가설 : Wii를 플랫폼으로 사용한 일반회사 출고량의 평균은 플레이스테이션3를 플랫폼으로 사용한 일반회사 출고량의 평균보다 낮거나 같을 것이다.
>  <img width="1101" alt="스크린샷 2022-07-26 오후 8 10 55" src="https://user-images.githubusercontent.com/86824895/180993004-024fd1e3-57da-48df-9edb-f3005b115209.png">

7. **결론** : 귀무가설의 pvalue가 0.05를 초과하지 못해 기각하고, 대립가설을 채택한다.
>>        => ps3의 액션게임으로 북미시장에 진출해야함.
>>        => 2022년 현재 ps5까지 나온 상황으로, ps 버전별 추가분석이 필요해보임.
>>        (해당데이터에는 ps5에 대한 내용이 없음)
<img width="992" alt="스크린샷 2022-07-26 오후 8 11 25" src="https://user-images.githubusercontent.com/86824895/180993046-a36924fa-9ca8-4ed1-af21-ba9318369c7b.png">


![EDA_Project 001](https://user-images.githubusercontent.com/86824895/178964037-a989193f-f07b-4624-a6f9-25c07a2f7897.jpeg)
![EDA_Project 002](https://user-images.githubusercontent.com/86824895/178964058-beb3f6d1-79cb-4052-b294-aa0d377acb23.jpeg)
![EDA_Project 003](https://user-images.githubusercontent.com/86824895/178964062-dc31c85c-8844-463b-9c5b-9aa81a355a94.jpeg)
![EDA_Project 004](https://user-images.githubusercontent.com/86824895/178964068-55d2c88c-99fe-4075-97ce-482ce952e087.jpeg)
![EDA_Project 005](https://user-images.githubusercontent.com/86824895/178964076-994f2ed9-4768-4baf-acb8-8dfa197a3649.jpeg)
![EDA_Project 006](https://user-images.githubusercontent.com/86824895/178964081-cd333436-57a1-420b-8111-7bfb8559a895.jpeg)
![EDA_Project 007](https://user-images.githubusercontent.com/86824895/178964086-065a2b45-8392-4ec0-8acb-13f9a2433e21.jpeg)
![EDA_Project 008](https://user-images.githubusercontent.com/86824895/178964089-4713201b-11c0-46b3-8ee5-41cbd2842cdf.jpeg)
![EDA_Project 009](https://user-images.githubusercontent.com/86824895/178964091-2c3c2db5-7b31-4e90-9396-655c7855087b.jpeg)
![EDA_Project 010](https://user-images.githubusercontent.com/86824895/178964095-5eb575de-b1e5-410f-9623-79f9a5cf95d9.jpeg)
![EDA_Project 011](https://user-images.githubusercontent.com/86824895/178964097-fa8dfa22-a600-4e37-ad85-c94fa281329e.jpeg)
![EDA_Project 012](https://user-images.githubusercontent.com/86824895/178964098-fbcc4dae-fcbb-4ea3-ad19-de22552d91d2.jpeg)
![EDA_Project 013](https://user-images.githubusercontent.com/86824895/178964101-c4cd5478-ff9b-48e6-b22d-cbd24a068826.jpeg)
![EDA_Project 014](https://user-images.githubusercontent.com/86824895/178964104-8ba24c36-e6f7-45e3-b7de-f312b1245d03.jpeg)
![EDA_Project 015](https://user-images.githubusercontent.com/86824895/178964106-c7543fa8-374f-44a5-bb07-a896b9213237.jpeg)
![EDA_Project 016](https://user-images.githubusercontent.com/86824895/178964111-c81f1445-21f1-4a5c-8847-9e83c87673ec.jpeg)
![EDA_Project 017](https://user-images.githubusercontent.com/86824895/178964115-00b56fbc-e95e-4340-9b50-dee26420dd0a.jpeg)
![EDA_Project 018](https://user-images.githubusercontent.com/86824895/178964116-8538992b-5188-4190-bfef-8ae7a32da413.jpeg)
![EDA_Project 019](https://user-images.githubusercontent.com/86824895/178964117-2b2498c6-56ba-4d9b-aff3-221e2122964a.jpeg)
