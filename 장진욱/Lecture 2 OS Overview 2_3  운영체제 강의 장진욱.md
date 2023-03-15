## 1. 운영 체제의 구분

### 1.1 작업 수행 방식

- Batch processing system
  - 일괄처리 시스템
- Time - sharing system
  - 시분할 시스템
- Distributed processing system
  - 분산처리 시스템
- Real-time system
  - 실시간 시스템

## 2. 운영체제의 구분 - 작업 수행 방식

### 2.1 순차 처리

- 운영체제 개념 존재하지 않음
  - 사용자가 기계어로 직접 프로그램 작성
  - 컴퓨터에 필요한 모든 작업 프로그램에 포함
    - 프로세서에는 명령어 저장 방법, 계산 대상, 결과 저장 위치와 방법, 출력 시점, 위치 등
- 실행하는 작업 별 순차 처리
  - 각각의 작업에 대한 준비 시간이 소요

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9e50e5dc-a750-43b2-9a8e-48550818165f/Untitled.png)

### 2.2 Batch Systems (1950s ~ 1960s)

- 모든 시스템을 중앙(전자계산소 등) 에서 관리 및 운영
- 사용자의 요청 작업(천공카드 등) 을 일정 시간 모아 두었다가 한번에 처리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5199603-7d11-40b8-9974-5fc294dc7788/Untitled.png)

- 시스템 지향적
- 장점
  - 많은 사용자가 시스템 자원 고유
  - 처리 효율 향상
- 단점
  - 생산성(productivity) 저하
    - 같은 유형의 작업들이 모이기를 기다려야 함
  - 긴 응답시간 (turnaround time)
    - 약 6시간 ( 작업 제출에서 결과 출력까지의 시간)

### 2.3 Time Sharing System

- 여러 사용자가 자원을 동시에 사용
  - os가 파일 시스템 및 가상 메모리 관리
- 사용자 지향적
  - 대화형 시스템
  - 단말기 사용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1387eef0-10db-4b8c-a211-ab6d092866b9/Untitled.png)

- 장점
  
  - 응답시간 단축(약 5초)
  - 생산성 향상
    - 프로세서 유휴 시간 감소

- 단점
  
  - 통신 비용 증가
    - 통신선 비용 보안 문제 등
  - 개인 사용자 체감 속도 저하
    - 동시 사용자 수 up → 시스템 부하 up → 느려짐 (개인관점)

### 2.4 Personal Computing

- 개인이 시스템 전체 독점

- cpu 활용률이 고려의 대상이 아님

- os가 상대적으로 단순함
  
  - 하지만, 다양한 사용자 지원 기능 지원

- 장점
  
  - 빠른 응답시간

- 단점
  
  - 성능이 낮음

### 2.5 Parallel Processing System

- 단일 시스템 내에서 둘 이상의 프로세서 사용
  - 동시에 둘 이상의 프로세스 지원
- 메모리 등의 자원 공유 (Tightly - coupled system)
- 사용 목적
  - 성능 향상
  - 신뢰성 향상
- 프로세서간 관계 및 역할 관리 필요

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/317792c7-59bf-407d-b0fa-b6404f32aa78/Untitled.png)

### 2.6 Distributed Processing System

- 네트워크를 기반으로 구축된 병렬처리 시스템

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3df7b11-6533-4010-937f-6cdc367cfceb/Untitled.png)

- 네트워크를 기반으로 구축된 병렬 처리 시스템
  
  - 물리적인 분산, 통신망 이용한 상호 연결
  - 각각 운영체제 탑재한 다수의 범용 시스템으로 구성
  - 사용자는 분산운영체제를 통해 하나의 프로그램, 자원처럼 사용 가능 (은폐성, transparency)
  - 각 구성 요소들간의 독립성 유지, 공동작업 가능
  - Cluster system, client - server system, p2p등

- 장점
  
  - 자원 공유를 통한 높은 성능
  - 고신뢰성, 높은 확정성

- 단점
  
  - 구축 및 관리가 어려움

## 2.7 Real-time Systems

- 작업 처리에 제한 시간을 갖는 시스템
  
  - 제한 시간 내에 서비스를 제공하는것이 자원 활용 효율보다 중요

- 작업의 종류
  
  - Hard real - time task
    - 시간 제약을 지키지 못하는 경우 시스템에 치명적 영향
    - 예, 발전소 제어, 무기 제어 등
  - soft real-time task
    - 동영상 재생 등
  - Non real - time task
