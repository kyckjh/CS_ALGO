## 1. 운영체제의 역할

- User Interface (편리성)
  - CUI - Character user interface
  - GUI - Graphical user interface
  - EUCI - End-User Comfortable Interface
- Resource management (효율성)
- Process and Thread management
- System management (시스템 보호)

## 2. 컴퓨터 시스템의 구성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8386fd11-5c96-4b96-9781-4fc3de5a9cbe/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88bddaad-b943-40b6-9701-9b7d483fd193/Untitled.png)

## 3. 운영체제의 구분

- 동시 사용자 수 : 운영체제를 혼자쓰는가 or 같이 쓰는가
  - Single - user - system
  - Multi - user - system
- 동시 실행 프로세스 수
  - Single - tasking system
  - Multi - tasking system (Multiprogramming system)
- 작업 수행 방식 (사용자가 느끼는 사용 환경)
  - Batch processing system
  - Time-sharing system
  - Distributed processing system
  - Real - time system

### 3.1 동시 사용자 수

- 단일 사용자 (Single - user - system)
  
  - 한 명의 사용자만 시스템 사용 가능
    - 한 명의 사용자가 모든 시스템 자원 독점
    - 자원관리 및 시스템 보호 방식이 간단 함
  - 개인용 장비 (pc, mobile) 등에 사용
    - windows 7/10, android, MS-DOS 등

- 다중 사용자 (Multi - user - system)
  
  - 동시에 여러 사용자들이 시스템 사용
    - 각종 시스템 자원(파일 등) 들에 대한 소유 권한 관리 필요
    - 기본적으로 Multi - tasking 기능 필요
    - os의 기능 및 구조가 복잡
  - 서버, 클러스터(cluster) 장비 등에 사용
    - Unix, Linux, Windows server 등

### 3.2 동시 실행 프로세스 수

- 단일 작업 (Single - tasking system)
  - 시스템 내에 하나의 작업(프로세스)만 존재
    - 하나의 프로그램 실행을 마친 뒤에 다른 프로그램의 실행
  - 운영체제의 구조가 간단
  - 예)MS-DOS
- 다중작업(Multi - tasking system)
  - 동시에 여러 작업(프로세스)의 수행 가능
    - 작업들 사이의 동시 수행, 동기화 등을 관리해야 함
  - 운영체제의 기능 및 구조가 복잡
  - Unix, Linux, Windows server 등
