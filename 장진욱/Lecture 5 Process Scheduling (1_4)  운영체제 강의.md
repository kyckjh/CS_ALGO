## 1. 프로세스 스케줄링

### 1.1 다중 프로그래밍

- 여러개의 프로세스가 시스템 내 존재
- 자원을 할당 할 프로세스를 선택 해야 함
  - 스케줄링(Scheduling)
- 자원관리
  - 시간 분할 관리
    - 하나의 자원을 여러 스레드들이 번갈아 가며 사용
    - 예) 프로세서 (Processor)
    - 프로세스 스케줄링 (Process scheduling)
      - 프로세서 사용시간을 프로세스들에게 분배
  - 공간 분할 관리
    - 하나의 자원을 분할 하여 동시에 사용
    - 예 메모리

## 2. 스케줄링(Schduling)의 목적

- 시스템의 성능 향상
- 대표적 시스템 성능 지표 (index)
  - 응답시간(response time)
    - 작업요청(submission)으로부터 응답을 받을때까지의 시간
  - 작업 처리량 (throughput)
    - 단위 시간 동안 완료된 작업의 수
  - 자원 활용도 (resource utilization)
    - 주어진 시간동안 자원이 활용된 시간
- 목적에 맞는 지표를 고려하여 스케줄링 기법을 선택

### 2.1 시스템 성능 지표들

- 평균 응답 시간 (mean respose time)
  - 사용자 지향적, 예) interactive systems
- 처리량 (throughput)
  - 시스템 지향적, 예) batch systems
- 자원활용도 (resource utilization)
- 공평성(fairness)
  - FIFO
- 실행 대기 방지
  - 무기한 대기 방지
- 예측 가능성(predictability)
  - 적절한 시간안에 응답을 보장하는가

## 3. 스케줄링(Schduling)의 목적 - 시스템 성능 지표들

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/600ef4cd-27f4-4b11-a19a-65f07dbf04d8/Untitled.png)

## 3.1 대기시간, 응답시간, 반환시간

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bb4496ed-1c4d-4f67-a2ae-5952848e8b4c/Untitled.png)

## 4. 스케줄링 기준 (Criteria)

- 스케줄링 기법이 고려하는 항목들
- 프로세스(process)의 특성
  - i/o - bounded or compute-bounded
- 프로세스의 긴급성 (urgency)
  - hard- or soft- real time, non-real time systems
- 프로세스 우선 순위 (priority)
- 프로세스 총 실행 시간

### 4.1 CPU burst vs i/o burst

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2874c814-e380-4da9-9c3a-f4808a1fcdae/Untitled.png)

## 5 스케줄링의 단계

- 발생하는 빈도 및 할당 자원에 따른 구분
- Long-term scheduling
  - 장기 스케줄링
  - job schduling
- Mid-term scheduling
  - 중기 스케줄링
  - Memory alloaction
- Short - term scheduling
  - 단기 스케줄링
  - Process scheduling

### 5.1 Long - term Scheduling

- job scheduling
  - 시스템에 제출할 작업 결정
- 다중프로그래밍 정도(degree) 조절
  - 시스템 내에 프로세스 수 조절
- i/o-bounded 와 compute-bounded 프로세스들을 잘 섞어서 선택해야 함
- 시분할 시스템에서는 모든 작업을 시스템에 등록
  - Long - term scheduling 이 불필요

### 5.2 MId-term Scheduling

- 메모리 할당 결정 (memory allocation)
  - intermediate - level scheduling
  - Swapping (swap-in / swap - out)

### 5.3 Short - term Scheduling

- process scheduling
  
  - low - level scheduling
  - 프로세서를 할당할 프로세스를 결정

- 가장 빈번하게 발생
  
  - interrput, block (i/o), time-out
  - 매우 빨라야함
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac4a1b16-ca78-43e0-87eb-093008218d1c/Untitled.png)
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86f3b72e-2642-46cc-8f7f-cf8ff4b4988b/Untitled.png)

## 6 스케줄링 정책(Policy)

- 선점 VS 비선점
  
  - Preemptive scheduling, Non - preemptive scheduling

- 우선순위
  
  - Priority

### 6.1 Preemptive / Non - preemptive scheduling

- Non-preemptive scheduling
  
  - 할당 받을 자원을 스스로 반납할 떄까지 사용

- 장점
  
  - Context switch overhead가 적음

- 단점
  
  - 잡은 우선순위 역전, 평균 응답 시간 증가

- Preemptive scheduling
  
  - 타의에 의해 자원을 뺴앗길 수 있음
    - 예) 할당 시간 종료, 우선순위가 높은 프로세스 등장
  - Context switch overhead가 큼
  - time-sharing system, real - time system

### 6.2 Priority

- 프로세스의 중요도
- Static priority ( 정적 우선 순위)
  - 프로세스 생성시 결정된 priority가 유지 됨
  - 구현이 쉽고 odvehead가 적음
  - 시스템 환경 변화에 대한 대응이 어려움
- DYnamic priority (동적 우선순위)
  - 프로세스의 상태 변화에 따라 priority 변경
  - 구현이 복잡, priority 재계산 overhead가 큼
  - 시스템 환경 변화에 유연한 대응 가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ed1c8793-b6ab-485f-bc4d-7ab16edc8776/Untitled.png)
