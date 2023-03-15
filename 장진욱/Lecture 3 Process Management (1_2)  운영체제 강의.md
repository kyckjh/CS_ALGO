## 1. 프로세스 관리

### 1.1 Job vs Process

- 작업 (job) / 프로그램 (program)
  
  - 실행 할 프로그램 + 데이터
  - 컴퓨터 시스템에 실행 요청 전의 상태

- 프로세스 (process)
  
  - 실행을 위해 시스템 (커널)에 등록된 작업
  - 시스템 성능 향상을 위해 커널에 의해 관리 됨

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/23f135cd-c972-4792-865b-a25cebad1153/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/172acd2a-1551-4cc8-9c58-f35d273f8575/Untitled.png)

### 1.2 프로세스의 정의

- 실행중인 프로그램
  
  - 커널에 등록되고 커널의 관리하에 있는 작업
  - 각종 자원들을 요청하고 할당 받을 수 있는 개체
  - 프로세서 관리 블록(pcb)을 할당 받은 개체
  - 능동적인 개체(active entity)
    - 실행 중에 각종 자원을 요구, 할당, 반납하며 진행

- Process Control Block (PCB)
  
  - 커널 공간 (kernel space) 내에 존재
  - 각 프로세스들에 대한 정보를 관리

### 1.3 프로세스의 종류

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/77ea249f-5708-4076-b6dd-f2b8a18c64cb/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/295b40b6-314d-4b4c-bc1e-dd801538a04a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21e08256-48f7-46ec-8673-1640fa968052/Untitled.png)

## 2. Process Control Block (PCB)

### 2.1 PCB가 관리하는 정보

- PID : Process Identification Number
  - 프로세스 고유 식별 번호
- 스케줄링 정보
  - 프로세스 우선순위 등과 같은 스케줄링 관련 정보들
- 프로세스 상태
  - 자원 할당, 요청 정보 등
- 메모리 관리 정보
  - page table, segment table
- 입출력 상태 정보
  - 할당 받은 입출력 장치, 파일 등에 대한 정보 등
- 문맥 저장 영역
  - 프로세스의 레지스터 상태를 저장하는 공간 등
- 계정 정보
  - 자원 사용 시간 등을 관리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c74a7cb4-5d42-444b-95cb-0b62498f3c24/Untitled.png)

## 3. 프로세스의 상태

- 프로세스 - 자원 간의 상호작용에 의해 결정

- 프로세스 상태 및 특성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/89cee9b1-3213-4765-9a8c-195d7912fad3/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4184cf3-9d74-4a97-8bb3-5f04a4389e57/Untitled.png)

### 3.1 Created state

- 작업을 커널에 등록
- PCB 할당 및 프로세스 생성
- 커널
  - 가용 메모리 공간 체크 및 프로세스 상태 전이

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7dfcf5c4-c78f-4898-bedb-0b42b05ab1b8/Untitled.png)

### 3.2 Ready State

- 프로세서 외의 다른 모든 자원을 할당 받은 상태
  - 프로세서 할당 대기 상태
  - 즉시 실행 가능 상태
- Dispatch (or Schedule)
  - Ready state → running state

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/10c03cae-15b1-4032-8663-99b9eb0cf0e0/Untitled.png)

### 3.3 Running state

- 프로세서와 필요한 자원을 모두 할당 받은 상태

- Preemption
  
  - Running state → ready states
  - 프로세서 스케줄링 ( time - out, Priority changes)

- Block / sleep
  
  - Running state → asleep state
  - I/O 등 자원 할당 요청

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/831ed4e8-f609-4f6d-9548-2a83508acdf7/Untitled.png)

### 3.4 Blocked / Asleep State

- 프로세서 외에 다른 자원을 기다리는 상태
  - 자원 할당은 System call에 의해 이루어짐
- Wake - up
  - Asleep state → ready state

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d75629e-1e8a-4c1d-9a1b-3fd245eb4a7f/Untitled.png)

### 3.5 Process State Transition Diagram

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7c23a05-e00c-487a-ab07-549003eaaaa9/Untitled.png)

### 3.6 Suspended State

- 메모리를 할당 받지 못한 (빼앗긴) 상태
  - Memory image를 swap device에 보관
    - Swap device : 프로그램 정보 저장을 위한 특별한 파일 시스템
  - 커널 또는 사용자에 의해 발생
- Swap - out ( suspended), Swap -in (resume)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fc503b10-d564-4e2c-9328-fbfbb41b8d21/Untitled.png)

### 3.7 Terminated / Zombie State

- 프로세스 수행이 끝난 상태
- 모든 자원 반납 후,
- 커널 내에 일부 PCB 정보만 남아 있는 상태
  - 이후 프로세스 관리를 위해 정보 수집

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/517a606d-c6e0-40a7-a89a-860fa7a958d8/Untitled.png)

### 3.8 프로세스 관리를 위한 자료구조

- Ready Queue
- I/O Queue
- Device Queue

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/03a10316-5a27-45cf-9b20-4450c62068ac/Untitled.png)
