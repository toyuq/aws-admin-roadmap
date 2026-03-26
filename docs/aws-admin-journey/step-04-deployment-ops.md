# Step 04. 배포와 운영

## 목표

- 배포와 롤백 흐름을 이해한다.
- 로그와 알람을 확인하는 습관을 만든다.

## 복습용 정리

### 핵심 AWS 서비스 한 줄 요약

- **CodePipeline**: 소스 -> 빌드 -> 배포 단계를 자동으로 연결하는 CI/CD 파이프라인 서비스
- **CodeBuild**: 소스 코드를 빌드하고 테스트를 실행하는 관리형 빌드 서비스
- **CodeDeploy**: EC2, 온프레미스, Lambda, ECS 등에 애플리케이션을 배포하는 서비스
- **CodeCommit**: AWS에서 제공하는 Git 기반 소스 저장소
- **CloudFormation**: 인프라를 코드(IaC)로 정의하고 동일하게 재현하는 서비스
- **CloudWatch**: 메트릭, 로그, 알람을 통합 모니터링하는 서비스
- **CloudTrail**: 누가 어떤 API를 호출했는지 기록하는 감사 추적 서비스
- **AWS Systems Manager**: 운영 작업(패치, 실행 명령, 파라미터 관리)을 중앙 제어하는 서비스
- **AWS Backup**: 여러 AWS 리소스의 백업 정책을 통합 관리하는 서비스

### 배포/운영에서 자주 같이 쓰는 조합

- **CodePipeline + CodeBuild + CodeDeploy**: 표준 배포 자동화 조합
- **CloudFormation + CodePipeline**: 인프라 변경까지 배포 파이프라인에 포함
- **CloudWatch + SNS + Incident 대응 채널**: 알람 감지 후 담당자 즉시 통보
- **CloudTrail + CloudWatch Logs**: 장애 시 변경 이력과 애플리케이션 로그를 함께 분석

### 서비스별 감각

- **CodePipeline**은 "배포 흐름 컨트롤러"다.
- **CodeBuild**는 "빌드/테스트 실행기"다.
- **CodeDeploy**는 "실제 배포 엔진"이다.
- **CloudWatch**는 "운영 상태판 + 경보 시스템"이다.
- **CloudTrail**은 "사고 분석용 감사 블랙박스"다.
- **AWS Backup**은 "백업 정책 자동화 관리자"다.
- **Systems Manager**는 "다수 서버 운영 자동화 도구"다.

### 배포 전략에서 알아둘 AWS 개념

- **In-Place 배포**: 기존 인스턴스에 순차 반영. 단순하지만 실패 시 영향 가능성 높음.
- **Blue/Green 배포**: 새 환경(Green) 준비 후 트래픽 전환. 롤백이 빠름.
- **Canary 배포**: 일부 트래픽에 먼저 배포해 위험을 낮춤.
- **Rolling 배포**: 여러 인스턴스에 나눠서 점진 반영.

## 학습 내용

- 배포 파이프라인
- 롤백
- CloudWatch Logs
- Alarm
- Backup / Restore

### 배포 파이프라인에서 AWS 서비스가 어떻게 연결되는가

- 개발자가 **CodeCommit/GitHub**에 코드 푸시
- **CodePipeline**이 변경을 감지해 파이프라인 시작
- **CodeBuild**가 빌드 및 테스트 수행
- 산출물을 **S3/ECR**에 저장
- **CodeDeploy** 또는 **ECS 배포 단계**로 운영 반영
- 배포 후 **CloudWatch**로 메트릭/로그 확인
- 이상 시 **CloudWatch Alarm + SNS**로 즉시 알림

### CloudWatch에서 꼭 보는 항목

- **Metrics**: CPUUtilization, Memory(커스텀), ALB 5xx, Latency
- **Logs**: 애플리케이션 에러, 타임아웃, 배포 직후 예외
- **Alarms**: 임계치 초과 시 알림(SNS, ChatOps)
- **Dashboards**: 운영 핵심 지표를 한 화면에서 확인

### CloudTrail이 중요한 이유

- 장애 시 "누가/언제/무엇을 변경했는지" 확인 가능
- 권한 오남용, 실수 삭제, 보안 이벤트 추적 가능
- 운영 이슈 분석에서 CloudWatch 로그와 함께 보면 원인 파악 속도가 올라감

### Backup / Restore에서 AWS 서비스 적용 예시

- **RDS**: 자동 백업 + 수동 스냅샷 + 시점 복구(PITR)
- **EBS**: 스냅샷으로 볼륨 복원
- **S3**: 버전 관리 + Lifecycle + 필요 시 CRR(교차 리전 복제)
- **AWS Backup**: 서비스별 백업 정책을 중앙에서 통합 관리

### 이 단계에서 스스로 답해볼 질문

- CodePipeline, CodeBuild, CodeDeploy의 역할 차이는 무엇인가?
- Blue/Green 배포가 In-Place보다 유리한 상황은 언제인가?
- CloudWatch Alarm 임계치를 너무 낮게 잡으면 어떤 문제가 생기는가?
- CloudTrail 로그는 CloudWatch Logs와 어떤 점이 다른가?
- RDS 복구에서 RPO와 RTO를 각각 어떻게 해석해야 하는가?

### 암기용 짧은 정리

- CodePipeline = 배포 흐름 자동화
- CodeBuild = 빌드/테스트
- CodeDeploy = 배포 실행
- CloudFormation = 인프라 코드화
- CloudWatch = 메트릭/로그/알람
- CloudTrail = API 감사 로그
- Systems Manager = 운영 자동화
- AWS Backup = 통합 백업 정책

## 기록

- 오늘 배운 내용:
- CodePipeline, CodeBuild, CodeDeploy를 연결하면 기본적인 AWS CI/CD 흐름을 구성할 수 있다.
- CloudWatch는 로그와 알람 중심의 운영 모니터링 핵심 서비스다.
- CloudTrail은 운영 장애 원인 추적과 보안 감사에서 필수다.
- AWS Backup과 RDS/EBS/S3 백업 전략은 복구 목표(RPO/RTO)와 함께 설계해야 한다.

- 장애 대응 순서:
- 1) CloudWatch Alarm으로 이상 감지
- 2) CloudWatch Metrics/Logs로 영향 범위 확인
- 3) CloudTrail로 최근 변경(API 호출) 확인
- 4) CodeDeploy 또는 배포 전략 기반으로 롤백
- 5) 복구 후 알람/대시보드/백업 정책 보완

- 다시 확인할 내용:
- CodeDeploy 배포 방식(In-Place, Blue/Green) 세부 옵션
- CloudWatch Dashboard 실무 구성 예시
- CloudTrail 이벤트 조회와 필터링 방법
- AWS Backup 정책 템플릿(보존 기간, 주기) 설계 기준

## 체크

- [ok] 배포 관련 AWS 서비스 역할을 구분할 수 있다
- [ok] CloudWatch와 CloudTrail의 용도 차이를 설명할 수 있다
- [ok] 백업/복구 설계에서 RPO, RTO를 말할 수 있다
