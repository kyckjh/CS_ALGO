## 1. 스레드 관리

### 1.1 프로세스(Process)와 스레드(Thread)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26b6725c-19c2-45ff-85a8-c4e1fcd0c9f3/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8d9207af-f402-47ea-af43-68618ef56e9e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4d9390c-539a-4ad5-ac76-230d21d423da/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/087f557e-57e8-4537-8c2a-31cab6b12311/Untitled.png)

### 1.2 스레드

- Light Weight Process (LWP)
- 프로세서(e.g CPU) 활용의 기본 단위
- 구성 요소
  - Thread ID
  - Register set (pc, sp 등)
  - Stack (i.e. local data)
- 제어 요소 외 코드, 데이터 및 자원들은 프로세스 내 다른 스레드들과 공유
- 전통적 프로세스 = 단일 스레드 프로세스

### 1.3 Single - thread VS Multi - threads

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/60e17966-2c30-4c4a-8357-9fbfd7328b12/Untitled.png)

### 1.4 스레드의 장점

- 사용자 응답성 (Responsiveness)
  
  - 일부 스레드의 처리가 지연되어도, 다른 스레드는 작업을 계속 처리 가능

- 자원 공유 (Resource sharing)
  
  - 자원을 공유해서 효율성 증가 (커널의 개입을 피할 수 있음)
    - ex) 동일 address space에서 스레드 여러 개

- 경제성 (Economy)
  
  - 프로세스의 생성, context switch에 비해 효율적

- 멀티 프로세서 (multi - processor) 활용
  
  - 병렬처리를 통해 성능 향상

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/31ce17c8-56a4-4c99-b706-5ef428166610/Untitled.png)

## 2. 스레드의 구현

### 2.1 사용자 수준 스레드 (User Thread)

- 사용자 영역의 스레드 라이브러리로 구현 됨
  
  - 스레드의 생성, 스케줄링 등
  - POSIX threads, Win32 threads, Java thread API 등

- 커널은 스레드의 존재를 모름
  
  - 커널의 관리(개입)를 받지 않음
    - 생성 및 관리의 부하가 적음, 유연한 관리 가능
    - 이식성(protability)이 높음

- 커널은 프로세스 단위로 자원 할당
  
  - 하나의 스레드가 block 상태가 되면, 모든 스레드가 대기
  - (single - threaded kernel의 경우)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15bba60a-5f7d-4526-aa63-7b0deb4c73bc/Untitled.png)

### 2.2 커널 수준 스레드 (Kernel Threads)

- OS(Kernel)가 직접 관리

- 커널 영역에서 스레드의 생성, 관리 수행
  
  - Context switching 등 부하(Overhead)가 큼

- 커널이 각 스레드를 개별적으로 관리
  
  - 프로세스 내 스레드들이 병행 수행 가능
    - 하나의 스레드가 block 상태가 되어도, 다른 스레드는 계속 작업 수행 가능

### 2.3 Multi - Threading Model

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ed06577f-27b3-44f6-b825-5ec3b3434f68/Untitled.png)

### 2.4 혼합형 (n : m) 스레드

- n개 사용자 수준 스레드 - m개의 커널 스레드 (n>m)
  - 사용자는 원하는 수만 큼 스레드 사용
  - 커널 스레드는 자신에게 할당된 하나의 스레드가 block 상태가 되어도, 다른 스레드 수행 가능
    - 병행 처리 가능
- 효율적이면서도 유연함

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9dd4ea71-0c4a-408a-8f40-8736a9c7dd10/Untitled.png)

## <Summary>

- 스레드의 개념
- 스레드의 구현
  - 사용자 수준 스레드
    - n:1 모델
  - 커널 수준 스레드
    - 1:1 모델
  - 혼합형 스레드
    - n:m 모델
