# Step 01. AWS 기본 개념

## 목표

- AWS 핵심 서비스가 무엇인지 설명할 수 있다.
- 각 서비스의 역할을 한 줄로 정리할 수 있다.

## 복습용 정리

### 핵심 서비스 한 줄 요약

- **EC2 (Elastic Compute Cloud)**: AWS에서 서버를 직접 띄워서 쓰는 가상 서버
- **S3 (Simple Storage Service)**: 이미지, 로그, 백업 같은 파일을 저장하는 객체 저장소
- **RDS (Relational Database Service)**: MySQL, PostgreSQL 같은 데이터베이스를 쉽게 운영하게 해주는 관리형 DB
- **CloudWatch (Amazon CloudWatch)**: 서버 상태, 로그, 알람을 확인하는 모니터링 도구
- **Route 53 (Amazon Route 53)**: 도메인 이름과 DNS를 관리하는 서비스
- **VPC (Virtual Private Cloud)**: AWS 안에서 네트워크를 분리하고 구성하는 가상 네트워크

### 서비스별 감각

- **EC2**는 직접 서버를 관리하는 느낌이다.
- **S3**는 파일을 저장하고 꺼내는 저장소다.
- **RDS**는 DB 운영 부담을 줄여주는 관리형 데이터베이스다.
- **CloudWatch**는 상태 확인과 장애 분석에 쓰는 눈 역할이다.
- **Route 53**은 사용자를 정확한 서비스 주소로 보내주는 길잡이다.
- **VPC**는 AWS 리소스를 안전하게 묶고 분리하는 네트워크 공간이다.
- **VPC**는 가상 컴퓨터가 아니라, AWS 안에서 독립적으로 구성하는 **가상 네트워크**다.

### IAM에서 꼭 기억할 것

- **Account**: AWS 자원을 담는 가장 큰 단위의 계정 공간이다.
  - 보통 하나의 AWS 로그인 단위 또는 조직 안의 계정 단위를 뜻한다.
  - IAM User, Role, Policy는 이 Account 안에서 관리된다.
- **User**: 사람이 직접 로그인할 때 쓰는 계정
- **Role**: 특정 작업이나 서비스에 잠시 부여하는 권한 묶음
- **Policy**: 어떤 리소스에 어떤 작업을 허용하거나 거부할지 적은 규칙

### 가장 중요한 관계

- Account 안에 User, Role, Policy가 있다.
- User나 Role에 Policy가 연결되면서 실제 권한이 결정된다.
- 사람 계정은 User, 서비스 작업은 Role 중심으로 생각하면 이해하기 쉽다.

### 최소 권한 원칙

- 필요한 권한만 주는 것이 AWS 운영의 기본이다.
- 권한이 너무 많으면 실수나 계정 탈취 때 피해가 커진다.
- 예: 백업 담당자는 S3 업로드만 허용하고, EC2 종료는 막는 식으로 설정한다.

### 이 단계에서 스스로 답해볼 질문

- EC2는 왜 쓰는가?
- S3는 어떤 데이터를 저장할 때 적합한가?
- RDS는 왜 직접 DB를 운영하는 것보다 편한가?
- CloudWatch는 무엇을 확인하는 도구인가?
- Route 53은 어떤 역할을 하는가?
- VPC는 왜 필요한가?
- User와 Role은 어떻게 다른가?
- Policy는 어떤 역할을 하는가?
- Account는 IAM에서 어떤 의미인가?
- 최소 권한 원칙이 왜 중요한가?

### 암기용 짧은 정리

- EC2 = 서버
- S3 = 파일 저장소
- RDS = 관리형 DB
- CloudWatch = 모니터링/로그
- Route 53 = DNS
- VPC = Virtual Private Cloud = 네트워크 공간
- IAM = 권한 관리
- Account = AWS 계정 공간
- User = 사람
- Role = 작업용 권한
- Policy = 권한 규칙

## 학습 내용

- EC2
- S3
- RDS
- CloudWatch
- Route 53
- VPC

## 기록

- 오늘 배운 내용:
- 헷갈린 개념:
- 다시 확인할 내용:

## 체크

- [ok] 서비스 이름을 외웠다
- [ok] 각 서비스의 역할을 설명할 수 있다
- [ok] 내 프로젝트에서 해당 서비스가 쓰이는지 확인했다
