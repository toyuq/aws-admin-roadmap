# Step 02. IAM과 보안

## 목표

- IAM의 기본 구성요소를 이해한다.
- 최소 권한 원칙을 설명할 수 있다.

## 복습용 정리

### 1. IAM이란 무엇인가

- IAM은 **Identity and Access Management**의 약자다.
- AWS에서 **누가 로그인할 수 있는지**, **무엇을 할 수 있는지**를 관리하는 서비스다.
- AWS 보안의 시작점이므로 가장 먼저 이해해야 한다.

### 2. IAM의 기본 구성요소

- **Account**: AWS 자원을 담는 가장 큰 단위의 계정 공간
- **User**: 사람이 직접 로그인할 때 쓰는 계정
- **Role**: 특정 작업이나 서비스에 잠시 부여하는 권한 묶음
- **Policy**: 어떤 리소스에 어떤 작업을 허용하거나 거부할지 적은 규칙

### 3. User / Role / Policy 차이

- **User**는 사람에게 붙는 계정이다.
- **Role**은 서비스나 작업에 붙는 권한이다.
- **Policy**는 권한의 내용 자체다.
- 쉽게 말하면, `User`와 `Role`이 권한을 받는 대상이고 `Policy`가 권한 규칙이다.

### 4. MFA

- **MFA (Multi-Factor Authentication)** 는 비밀번호 외에 한 번 더 확인하는 보안 장치다.
- 보통 인증 앱, 문자, 하드웨어 키 같은 추가 수단을 사용한다.
- 비밀번호가 유출돼도 추가 인증이 필요하므로 보안이 훨씬 강해진다.

### 5. Access Key

- Access Key는 AWS를 코드나 CLI로 사용할 때 쓰는 자격 증명이다.
- 보통 `Access Key ID`와 `Secret Access Key`가 한 세트다.
- 프로그램이나 스크립트에서 AWS API를 호출할 때 사용한다.
- 노출되면 위험하므로 절대 코드에 그대로 넣지 않는다.

### 6. Secrets Manager

- Secrets Manager는 비밀번호, API 키, DB 접속 정보 같은 민감한 값을 안전하게 저장하는 서비스다.
- 코드나 설정 파일에 직접 쓰지 않고 이 서비스에서 꺼내 쓰는 방식이 안전하다.
- 비밀값을 교체하거나 관리할 때도 편하다.

### 7. 최소 권한 원칙

- 필요한 권한만 주는 것이 AWS 보안의 기본이다.
- 권한이 많을수록 실수와 사고의 피해가 커진다.
- 예: 개발자는 배포용 리소스를 조회할 수 있어도, 운영 DB 삭제 권한은 없어야 한다.

### 8. 이 단계에서 꼭 기억할 관계

- Account 안에 User, Role, Policy가 있다.
- User나 Role에는 Policy가 연결된다.
- MFA는 계정 로그인 보안을 강화한다.
- Access Key는 자동화와 CLI 작업에 쓰인다.
- Secrets Manager는 민감한 정보를 안전하게 보관한다.

### 9. 자주 헷갈리는 점

- **User와 Role**: User는 사람, Role은 작업/서비스용이다.
- **Password와 Access Key**: Password는 콘솔 로그인용, Access Key는 CLI/API용이다.
- **Secrets Manager와 Policy**: Secrets Manager는 비밀값 저장, Policy는 권한 규칙이다.

### 10. 스스로 답해볼 질문

- IAM은 무엇을 관리하는 서비스인가?
- Account, User, Role, Policy는 각각 어떤 의미인가?
- User와 Role은 왜 구분해서 쓰는가?
- MFA는 왜 필요한가?
- Access Key는 언제 쓰는가?
- Access Key를 안전하게 다루려면 무엇을 조심해야 하는가?
- Secrets Manager는 왜 사용하는가?
- 최소 권한 원칙이 왜 중요한가?

## 학습 내용

- User
- Role
- Policy
- MFA
- Access Key
- Secrets Manager

## 기록

- 오늘 배운 내용:
- 헷갈린 개념:
- 권한 점검이 필요한 항목:

## 체크

- [ ] User, Role, Policy 차이를 이해했다
- [ ] MFA 적용 여부를 확인했다
- [ ] 불필요한 권한이 없는지 점검했다
