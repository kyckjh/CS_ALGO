## 1. 운영체제의 구조

### 1.1 커널(kernel)

- os의 핵심 부분 (메모리 상주)
  
  - 가장 빈번하게 사용되는 기능들 담당
    - 시스템 관리(processor, memory, Etc) 등
  - 동의어
    - 핵, 관리자 프로그램, 상주 프로그램, 제어 프로그램 등

- 유틸리티
  
  - 비상주 프로그램
  - ui등 서비스 프로그램

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ba43883b-de9e-4b86-8bea-b005370633a9/Untitled.png)

### 1.2 단일 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebd9ef09-e827-473e-b552-224e4a06ff8c/Untitled.png)

- 장점
  - 커널 내 모듈간 직접 통신
    - 효율적 자원 관리 및 사용
- 단점
  - 커널의 거대화
    - 오류 및 버그, 추가 기능 구현 등 유지보수가 어려움
    - 동일 메모리에 모든 기능이 있어, 한 모듈의 문제가 전체 시스템에 영향

### 1.3 계층구조

- 장점
  
  - 모듈화
    - 계층간 검증 및 수정 용의
  - 설계 및 구현의 단순화

- 단점
  
  - 단일구조 대비 성능 저하
    - 원하는 기능 수행을 위해 여러 계층을 거쳐야 함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d92559a7-a240-4588-8c32-f2788f1d75ec/Untitled.png)

### 1.4 마이크로 커널 구조

- 커널의 크기 최소화
  
  - 필수 기능만 포함
  - 기타 기능은 사용자 영역에서 수행
  
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/40bcd121-199c-4ada-b916-96f9adfd820e/Untitled.png)

## 2. 운영체제의 기능

- 프로세스 관리
- 프로세서 관리
- 메모리 관리
- 파일 관리
- 입출력 관리
- 보조 기억 장치 및 기타 주변 장치 관리 등

### 2.1 Process Management

- 프로세스 (process)
  
  - 커널에 등록된 실행 단위 ( 실행 중인 프로그램)
  - 사용자 요청/프로그램의 수행 주체(entity)

- os의 프로세스 관리 기능
  
  - 생성/삭제, 상태관리
  - 자원 할당
  - 프로세스 간 통신 및 동기화(synchronization)
  - 교착상태(deadlock) 해결

- 프로세스 정보 관리
  
  - PCB (Process Control Bloc)

### 2.2 Processor Management

- 중앙 처리 장치(cpu)
  - 프로그램을 실행하는 핵심 자원
- 프로세스 스케줄링(Scheduling)
  - 시스템 내의 프로세스 처리 순서 결정
- 프로세서 할당 관리
  - 프로세스들에 대한 프로세서 할당
    - 한번에 하나의 프로세스만 사용 가능

### 2.3 Memory Management

- 주기억장치
  
  - 작업을 위한 프로그램 및 데이터를 올려 놓는 공간

- Multi-user, Multi-tasking 시스템
  
  - 프로세스에 대한 메모리 할당 및 회수
  - 메모리 여유 공간 관리
  - 각 프로세스의 할당 메모리 영역 접근 보호

- 메모리 할당 방법(scheme)
  
  - 전체 적재
    - 장점 : 구현이 간단 / 단점 : 제한이 공간
  - 일부 적재
    - 프로그램 및 데이터의 일부만 적재
    - 장점: 메모리의 효율적 활용 / 단점 : 보조기억 장치 접근 필요

### 2.4 File Management

- 파일 : 논리적 데이터 저장 단위

- 사용자 및 시스템의 파일 관리

- 디렉토리 구조 지원

- 파일 관리 기능
  
  - 파일 및 디렉토리 생성, 삭제
  - 파일 접근 및 조작
  - 파일을 물리적 저장 공간으로 사상(mapping)
  - 백업 등

### 2.5 I/O Management

- 입출력(i/o) 과정
  - os를 반드시 거쳐야 함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c08c14c0-d917-4724-9ac1-8f8a20ed254a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7ed1557d-5da2-47f2-ac2e-30dc8f006026/Untitled.png)
