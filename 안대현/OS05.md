# 프로세스 관리

- 작업(Job) / 프로그램(Program)
  
  - 실행할 프로그램 + 데이터
  
  - 컴퓨터 시스템에 실행 요청 전의 상태

- 프로세스(Process)
  
  - 실행을 위해 시스템(커널)에 등록된 작업
  
  - 시스템 성능 향상을 위해 커널에 의해 관리됨

디스크에 있는 잡이 메모리에 올라가서 실행되는 것이 프로세스

### 프로세서의 정의

- 실행 중인 프로그램
  
  - 커널에 등록되고 커널의 관리하에 있는 작업
  
  - 각종 자원들을 요청하고 할당 받을 수 있는 개체
  
  - 프로세스 관리 블록(PCB)을 할당 받은 개체
  
  - 능동적인 개체(active entity)
    
    - 실행 중에 각종 자원을 요구, 할당, 반납하며 진행

프로세스의 종류;

- 시스템 프로세스: 모든 시스템 메모리와 프로세서의 명령에 엑세스할 수 있는 프로세스

- 사용자 프로세스: 사용자 코드를 수행하는 프로세스

- 독립 프로세스: 다른 프로세스에 영향을 주거나 받지 않으면서 수행하는 병렬 프로세스

- 협력 프로세서: 다른 프로세세 영향을 주고나 받는 병행 프로세스

### 자원(resource)의 개념

- 커널의 관리 하에 프로세스에 할당/반납되는 수동적 개체(passive entity)

- 자원의 분류
  
  - Hardware resource
    
    - processor, memory, disk, monitor, keyboard, etc
  
  - Software resource
    
    - message, signal, files, installed software, etc

### Process Control Block

- OS saves the information to manage the processes

- Created upon the creation of a process on kernel

### Informations PCB manages

- PID: process identification number

- Scheduling Information

- Process status: resource allocation, request information etc

- Memory management information: page table, segment table etc

- I/O status Information

- Context Save Area: Space to save the register status of a process

- Account Information: resource usage time 

PCB info varies by OS

참조 및 갱신 속도는 OS의 성능을 결정짓는 요소 중 하나

---

### 프로세스의 상태

- 프로세스 - 자원 간의 상호작용에 의해 결정

- 프로세스 상태 및 특성

![스크린샷 2023-03-14 오후 11.43.38.png](/Users/daehyunan/Library/Application%20Support/marktext/images/6cd25a6a368ad4118b41af1587a9e097a9f3ad67.png)

프로세스 상태 이동;

- Created State
  
  - 작업을 커널에 등록
  
  - PCB 할당 및 프로세스 생성
  
  - 커널
    
    - 가용 메모리 공간 체크 및 프로세스 상태 전이(ready or suspended ready) Memory allocated or Waiting memory allocated

- Ready State
  
  - 프로세서 외에 다른 모든 자원을 할당 받은 상태
    
    - 프로세서 할당 대기 상태
    
    - 즉시 실행 가능 상태
  
  - Dispatch(or Schedule)
    
    - Ready state -> running state

- Running State
  
  - 프로세서와 필요한 자원을 모두 할당 받은 상태
  
  - Preemption
    
    - Running state -> ready state
    
    - Process scheduling(e.g. time-out, priority change)
  
  - Block/sleep
    
    - Running state -> asleep state
    
    - I/O 등 자원 할당 요청

- Blocked/Asleep State
  
  - 프로세서 외에 다른 자원을 기다리는 상태
    
    - 자원 할당은 System call에 의해 이루어 짐
  
  - Wake-up
    
    - Asleep state -> ready state

- Suspended State
  
  - 메모리를 할당 받지 못한 상태
    
    - Memory image를 swap device에 보관
      
      - swap device: 프로그램 정보 저장을 위한 특별한 파일 시스템
    
    - 커널 또는 사용자에 의해 발생
  
  - swap-out(suspended), swap-in(resume)

- Terminated/Zombie State
  
  - 프로세스 수행이 끝난 상태
  
  - 모든 자원 반납 후, 커널 내에 일부 PCB 정보만 남아있는 상태
    
    - 이후 프로세스 관리를 위해 정보 수집

### 프로세스 관리를 위한 자료구조

- Ready Queue

- I/O Queue

- Device Queue


