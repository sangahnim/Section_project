## [**SECTION2**](https://github.com/sangahnim/section_project/blob/master/Ai_05_%EC%9D%B4%EC%83%81%EC%95%84_Section2.ipynb)

1.  **주제** : 어플평점 4점을 넘기위해 고려해야 할 사항에 대한 Machine
    Learning Project

2.  **데이터** : kaggle의 2017/07 앱스토어데이터 csv file \>
    데이터선정이유 및 문제정의 \> \* 코로나시국, 비대면 사회에서 가장
    중요한 도구인 휴대폰에서 만족도가 높은 어플의 특징들을 파악해보고자
    함 \> \* 많은 휴대폰 중 많은 사람들의 사랑받는 애플, 앱스토어를
    이용하여 7,197의 데이터 기준으로 분석 \> \* 어플평점 4점을
    넘느냐/안넘느냐의 2진분류문제로 정리하여 4점초과하는 데이터의 특성을
    도출

3.  **EDA, preprocessing** : \> 1) 불필요한 컬럼 제거 :
    ‘currency’,‘Unnamed: 0’, ‘id’,‘user_rating_ver’, ‘rating_count_ver’
    \> 2) ver컬럼 정리 : 주된 버전만 참고하도록 첫번째 수치만 남기고
    제거 (ex) 6.3.5-\> 6) \> 3) 이상치제거 : 데이터의 분포확인 후,
    user_rating_tot의 컬럼이 0이면 이상치로보고 제거 (어떤 회사라도
    1개는 있을 것이다는 가정. 점수가 없다면 만들어진지 얼마 안된 어플일
    것이다.) \> 4) Feature Engineering : recommend 특성을 생성하여
    true/false의 이진분류문제로 정리.

4.  Baseline model, 데이터의 기준모델 및 평가지표 설명

5.  **reccommend 특성의 True를 예측하기 위한 모델링** \> 1.
    기준모델(Baseline model): \>\> 1) 모델링 전 csv file을
    train/validation/test로 나눔 (학습과 테스트할 데이터를 구분하여
    학습한 모델에 과적합되는 것을 방지) \>\> 2) Decision Tree의 f1-score
    1로 과적합됨을 확인 후, high cardinlity(범주의 종류가 많음)로
    불필요한 특성들을 제거 및 recommend 특성을 만들 시 참고했던 특성을
    제거. \> 2. 모델링(XGBClassifier, DecisionTree, RandomForest)
    \>\> 1) 1에서 정리된 file을 train, validation, test로 나누고,
    train으로 학습시, 세 모델 중 RandomForest가 f-1score 성능이 가장
    좋음을 확인. \>\> 2) 하이퍼파라미터로 조정 후 train데이터 학습시,
    XGBClassifier의 f1-score가 0.61-\>0.64로 높아짐을 확인. \>\> 3)
    Randomforest 모델성능향상을 위해 순열중요도(Permutation Importance)
    및 RandomizedSearch를 이용하여 테스트데이터로 확인시, f1-score는
    0.60 \>\> 4) 이용하여 최적의 하이퍼파라미터로 조정,

6.  **머신러닝 모델 해석** \> 1) 변수의 중요도를 알아보기 위해
    permutationimportanc사용

7.  데이터의 기준모델 및 평가지표 설명

8.  탐색적 데이터분석 및 데이터전처리 방식

9.  머신러닝방식적용 및 교차검증

10. 머신러닝모델해석결과
