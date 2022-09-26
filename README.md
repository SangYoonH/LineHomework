*Test 수행 방법 소개
로그인, 추가, 수정, 삭제 각 flow 별로 검증해야하는 항목들을 하나의 ‘TestCase’로 설계
(상세 설계는 첨부된 ‘TestCase 설계명세서' 파일 참조)
‘pytest’라는 command를 통해 수행한다. 

1) TestCase 개별 test

- 수행 방법 : 환경 구축 후, terminal에서 proejct 폴더 이동 후, 아래 command 사용
$ pytest ./tests/<코드파일명>

2) 모든 TestCase 한번에 test

- 수행 방법 : 환경 구축 후, terminal에서 proejct 폴더 이동 후, 아래 command 사용
$ pytest ./tests/*
