## 1. 인터럽트(interrupt)

- 예상치 못한, 외부에서 발생한 이벤트
  
  - Unexpected, extenral events

- 인터럽트의 종류
  
  - i/o interrupt
  - Clock interrupt
  - Console interrupt
  - Program check interrupt
  - Machine check interrupt
  - inter - process interrupt
  - System call interrupt

### 1.1 인터럽트의 처리과정

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c024352-185a-468c-a933-ded767e7b05a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ff801f03-7919-47d2-9657-83c6aeff42e1/Untitled.png)

## 2. Context Switching (문맥교환)

- Context
  
  - 프로세스와 관련된 정보들의 집합
    - Cpu register context ⇒ in cpu
    - code & data, stack, PCB ⇒ memory

- Context saving
  
  - 현재 프로세스의 Register context 를 저장하는 작업

- context restoring
  
  - register context 를 프로세스로 복구하는 작업

- Context switching
  
  - 실행 중인 프로세스의 context를 저장하고, 앞으로 실행 할 프로세스의 context를 복구 하는 일
    - 커널의 개입으로 이루어짐

### 2.1 Context Switch overhead

- Context switching 에 소요되는 비용
  
  - os마다 다름
  - os의 성능에 큰 영향을 줌

- 불필요한 Context switching을 줄이는 것이 중요
  
  - 예, 스레드(thread) tkdyd emd

## < 요약 >

- 프로세스의 개념
- 프로세스 상태 변화
- PCB(프로세스 관리 블록)
- 인터럽트
- Context switching
