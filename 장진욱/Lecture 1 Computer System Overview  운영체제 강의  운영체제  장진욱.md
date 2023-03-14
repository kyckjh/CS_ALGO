## 0. 운영체제란

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ea4f32f-129d-4118-b0b0-414a62eb1dfa/Untitled.png)

- 하드웨어(HW)를 효율적으로 관리하여 응용프로그램(Application)이라든가 사용자들에게 서비스를 제공하는것

## 1. 컴퓨터 시스템 개요

### 1.1 컴퓨터의 하드웨어

- 프로세서 (processor) : 계산하는 녀석
  - CPU
  - 그래픽카드 (GPU)
  - 응용 전용 처리 장치 등
- 메모리 (Memory)
  - 주 기억장치
  - 보조 기억장치
- 주변 장치
  - 키보드/마우스
  - 모니터, 프린터
  - 네트워크 모뎀 등

## 2. 프로세서 (Processor)

- 컴퓨터의 두뇌 (중앙처리장치)
  
  - 연산 수행
  - 컴퓨터의 모든 장치의 동작 제어
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fc8f3f1-cf91-406f-9d56-2f487dce57d0/Untitled.png)

### 2.1 레지스터 (Register)

- 프로세서 내부에 있는 메모리
  
  - 프로세서가 사용할 데이터 저장
  - 컴퓨터에서 가장 빠른 메모리

- 레지스터의 종류
  
  - 용도에 따른 분류
    - 전용 레지스터, 범용 레지스터
  - 사용자가 정보 변경 가능 여부에 따른 분류
    - 사용자 가시 레지스터, 사용자 불가시 레지스터
  - 저장하는 정보의 종류에 따른 분류
    - 데이터 레지스터, 주소 레지스터, 상태 레지스터

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2f7a11b-0a40-47fa-b138-774676090fb5/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc91a60e-9b42-442b-bc89-a5b2c30899cb/Untitled.png)

### 2.2 프로세서의 동작

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22890624-ac26-4df6-ac66-2b6ec9a9d013/Untitled.png)

### 2.3 운영체제와 프로세서

- 프로세서에게 처리할 작업 할당 및 관리
  
  - 프로세스(Process) 생성 및 관리

- 프로그램의 프로세서 사용 제어
  
  - 프로그램의 프로세서 사용 시간 관리
  - 복수 프로그램간 사용 시간 조율

## 3. 메모리 (Memory)

- 데이터를 저장하는 장치 (기억장치)
  - 프로그램(os, 사용자sw 등), 사용자 데이터 등
- 메모리의 종류

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d66e69b8-580f-4ef8-87f5-5a696216f4e7/Untitled.png)

### 3.1 메모리의 종류

- 주기억장치 (Main memory)
  - 프로세서가 수행할 프로그램과 데이터 저장
  - DRAM을 주로 사용
    - 용량이 크고, 가격이 저렴
  - 디스크 입출력 병목현상(I/O bottleneck) 해소

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e67ea333-4139-45a3-af74-e0a406cb7d96/Untitled.png)

- 캐시 (cache)
  - 프로세서 내부에 있는 메모리 (L1, L2 캐시 등)
    - 속도가 빠르고, 가격이 비쌈
  - 메인 메모리의 입출력 병목현상 해소

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7689007-2da2-44a2-8d49-b49092f503b7/Untitled.png)

- 보조기억 장치 ( Auxiliary memory / secondary memory / storage)
  - 프로그램과 데이터를 저장
  - 프로세서가 직접 접근할 수 없음 (주변장치)
    - 주기억장치를 거쳐서 접근
    - (프로그램/데이터 → 주기억장치) 인 경우
      - 가상 메모리 ( Virtual memory)
  - 용량이 크고, 가격이 저렴

### 3.2 메모리와 운영 체제

- 메모리 할당 및 관리
  - 프로그램의 요청에 따른 메모리 할당 및 회수
  - 할당된 메모리 관리
- 가상 메모리 관리
  - 가상메모리 생성 및 관리
  - 논리주소 → 물리주소 변환

## 4. 메모리 - 캐시

### 4.1 캐시의 동작

- 일반적으로 HW적으로 관리 됨
- 캐시 히트 (Cache hit)
  - 필요한 데이터 블록이 캐시 존재
- 캐시 미스 (Cache miss)
  - 필요한 데이터 블록이 없는 경우

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c40796b-7ebc-434c-868d-3e0a382cdc9d/Untitled.png)

### 4.2 지역성

- 공간적 지역성 (Spatial locality)
  
  - 참조한 주소와 인접한 주소를 참조하는 특성
    - 예) 순차적 프로그램 수행

- 시간적 지역성 (Temporal locality)
  
  - 한 번 참조한 주소를 곧 다시 참조하는 특성
    - 예) For 문 등의 순환문

- 지역성은 캐시 적중률 (cache hit ratio ) 과 밀접
  
  - 알고리즘 성능 향상 위한 중요한 요소중 하나

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ec6cfb3-6a0f-44d0-a0c7-cc47088d91b9/Untitled.png)

## 5. 시스템 버스 (System Bus)

- 하드웨어들이 데이터 및 신호를 주고 받는 물리적인 통로

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e72e9bf-4145-443d-b192-963addb8a642/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a45fed3c-25ee-4c8a-8f74-90751a084242/Untitled.png)

## 6. 주변 장치

- 프로세서와 메모리를 제외 하드웨어들
  - 입력장치
  - 출력장치
  - 저장장치

### 6.1 주변장치와 운영체제

- 장치 드라이버 관리
  - 주변 장치 사용을 위한 인터페이스 제공
- 인터럽트 (interrupt) 처리
  - 주변 장치의 요청 처리
- 파일 및 디스크 관리
  - 파일 생성 및 삭제
  - 디스크 공간 관리
