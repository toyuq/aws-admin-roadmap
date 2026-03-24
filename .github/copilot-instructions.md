## 목적
이 파일은 AI 기반 코딩 에이전트(예: Copilot-like assistant)가 이 리포지토리에서 빠르게 생산적으로 작업할 수 있도록, 코드베이스의 구조와 프로젝트 고유 규약을 간결하게 정리합니다.

## 한눈에 보는 아키텍처
- 루트: `README.md`, `requirements.txt`
- 문서: `docs/`
  - `docs/aws-admin-roadmap.md` — AWS Admin 입문 로드맵
  - `docs/progress/` — 단계별 학습 기록 파일
  - `docs/session-notes.md` — 대화/학습 요약

현재 이 저장소는 AWS Admin 학습 로드맵과 진행 기록을 관리하는 용도로 사용합니다.

## 핵심 코드 패턴 및 규약
- 문서 갱신 시 날짜와 학습 단계가 명확하게 보이도록 작성합니다.
- 변경 기록은 `docs/progress/`와 `docs/session-notes.md`에 남깁니다.

## 작은 '계약' (함수별 기대형태)
- `main()`
  - 입력: 없음
  - 출력: 콘솔 안내 또는 학습 관련 메시지
  - 실패: 문서 경로 누락 시 안내 메시지 출력

## 자주 발생하는 엣지 케이스
- 문서 경로가 바뀌면 링크가 깨질 수 있음
- 기록 파일이 늘어날수록 최신 파일을 먼저 찾기 어려울 수 있음
- 다음 단계와 완료 여부를 명확히 적지 않으면 복습이 어려움

## 개발자 워크플로우(발견 가능한 커맨드)
- 의존성 설치: `pip install -r requirements.txt` (프로젝트 루트)
- 실행: `python src/main.py`
- 문서 확인: `docs/aws-admin-roadmap.md`

## 수정 시 주의사항(프로젝트 특화)
- 문서 구조가 바뀌면 `README.md`와 `docs/` 하위 링크도 함께 수정하세요.
- 의존성 추가 시 `requirements.txt`를 반드시 업데이트 하세요.

## 통합 포인트 및 외부 의존성
- 외부 문서: `README.md`, `docs/aws-admin-roadmap.md`, `docs/session-notes.md`
- 파이썬 라이브러리: 현재 학습 문서 관리 용도만 있으면 추가 의존성은 최소화합니다.

## 변경 제안/PR 작성 가이드(간단)
- 문서 변경 시: 변경 전/후 구조와 새로 추가된 파일을 PR 본문에 적어 주세요.
- 학습 단계 추가 시: 어떤 단계가 추가되었는지를 한 줄로 요약해 주세요.

---
필요한 다른 정보(예: 테스트 실행 방법, CI 설정, 더 많은 예시 로그)가 있으면 알려 주세요 — 해당 내용을 반영해 `.github/copilot-instructions.md`를 빠르게 보완하겠습니다.
