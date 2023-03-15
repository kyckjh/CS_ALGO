# Chapter 3-1 프로세스 관리



## Job vs Process



### 작업 (job) / 프로그램 (Program)

- 실행 할 프로그램 + 데이터

- 컴퓨터 시스탬에 실행 요청 전의 상태

### 프로세스 (Process)

- 실행을 위해 시스템(커널)에 등록된 작업

- 시스템 성능 향상을 위해 커널에 의해 관리 됨

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-22-57-59-image.png)



## 프로세스의 정의

실행중인 프로그램

- 커널에 등록되고 커널의 관리하에 있는 작업

- 각종 자원들을 요청하고 할당 받을 수 있는 개채

- 프로세스 관리 블록(PCB)을 할당 받은 개체

- 능동적인 개채(active entity)
  
  - 실행 중에 각종 자원을 요구, 할당, 반납하며 진행

Process Control Block (PCB)

- 커널 공간 (Kernel space) 내에 존재

- 각 프로세스들에 대한 정보를 관리

### 프로세스의 종류

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-00-17-image.png)

### 자원(Resource)의 개념

- 커널의 관리 하에 프로세스에게 할당/반납 되는 수동적 개채(passive entity)

- 자원의 분류
  
  - H/W resoruces
    
    - Processor, memory, disk, monitor, keyboard, Etc
  
  - S/W resource
    
    - Message, signal, files, installed SWs, Etc.

## Process Control Block (PCB)

- os가 프로세스 관리에 필요한 정보 저장

- 프로세스 생성 시, 생성 됨

## PCB가 관리하는 정보

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-05-25-image.png)

### 프로세스의 상태(Process States)

- 프로세스 - 자원 간의 상호작용에 의해 결정

- 프로세스 상태 및 특성

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-06-19-image.png)

## Created State

- 작업(Job)을 커널에 등록

- PCB 할당 및 프로세스 생성

- 커널
  
  - 가용 메모리 공간 체크 및 프로세스 상태 전이

## Ready State

- 프로세서 외에 다른 모든 자원을 할당 받은 상태
  
  - 프로세서 할당 대기 상태
  
  - 즉시 실행 가능 상태

## Running State

- 프로세서와 필요한 자원을 모두 할당 받은 상태

- Preemption
  
  ## Running state -> ready states
  
  - 프로세서 스케줄링(e.g, time-out, prioity changes)Block/sleep
  
  - Running state -> asleep state
  
  - I/O 등 자원 할당 요청

## Suspended State

- 메모리를 할당 받지 못한(빼앗긴) 상태
  
  - Memory image를 swap device에 보관
    
    - swap device : 프로그램 정보 저장을 위한 특별한 파일 시스템
  
  - 커널 또는 사용자에 의해 발생

- Swap-out, Swap-in

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-18-05-image.png)

## Turminated/Zombie State

- 프로세스 수행이 끝난 상태

- 모든 자원 반납 후, 커널 내에 일부 PCB 정보만 남아 있는 상태
  
  - 이후 프로세스 관리를 위해 정보 수집(비슷한 작업이 들어왔을 때, 정보가 있다면 관리하기 쉬움)

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-23-42-image.png)

![](C:\Users\kjr58\AppData\Roaming\marktext\images\2023-03-14-23-27-53-image.png)
