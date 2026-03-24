from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    roadmap = root / "docs" / "aws-admin-roadmap.md"
    session_notes = root / "docs" / "session-notes.md"

    print("AWS-ADMIN-ROADMAP")
    print(f"로드맵: {roadmap}")
    print(f"세션 메모: {session_notes}")
    print("docs/progress/ 폴더를 열어서 단계별 학습 기록을 이어가세요.")


if __name__ == "__main__":
    main()