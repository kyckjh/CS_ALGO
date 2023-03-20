## Interrupt

- 예상치 못한, 외부에서 발생한 이벤트
  
  - unexpected, external events

- 인터럽트의 종류
  
  - I/O interrupt
  
  - Clock interrupt
  
  - Console interrupt
  
  - Program check interrupt
  
  - Machine check interrupt
  
  - Inter-process interrupt
  
  - System call interrupt
  
  ### 인터럽트 처리과정
  
  인터럽트 발생 -> 프로세스 중단(커널 개입) -> 인터럽트 처리 -> 인터럽트 발생 장소, 원인 파악 -> 인터럽트 서비스 여부 결정 -> 인터럽트 서비스 루틴 호출
  
  흐름 저장 - context saving. @ PCB
  
  Interrupt handler를 통해 kernel의 ISR-n을 통해 인터럽트 서비스 프로세스를 진행
  
  이후 context restoring으로 이전 프로세스 수행

### Context Switching(문맥 교환)

- Context
  
  - 프로세스와 관련된 정보들의 집합
    
    - CPU register context => in CPU
    
    - Code & data, Stack, PCB => in memory

- Context saving
  
  - 현재 프로세스의 Register context를 저장하는 작업

- Context restoring
  
  - Register context를 프로세스로 복구하는 작업

- Context switching
  
  - 실행 중인 프로세스의 context를 저장하고, 앞으로 실행할 프로세스의 context를 복구하는 일
    
    - 커널의 개입으로 이루어짐

### Context Switch Overhead

- Context Switching에 소요되는 비용
  
  - varies by OS
  
  - affects on OS performance

- 불필요한 Context switching을 줄이는 것이 중요
  
  - 예, 스레드 사
