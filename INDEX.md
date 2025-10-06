# BC-macro 문서 인덱스

## 📚 문서 구성

### 1. 🏠 [README.md](README.md) 
**메인 개요 문서** - BC-macro의 전반적 소개와 주요 기능
- 프로젝트 개요
- 매크로 파일 목록 및 역할
- 기본 사용법
- 경제성 분석 구성요소

### 2. 🔍 [MACRO_ANALYSIS.md](MACRO_ANALYSIS.md)
**상세 매크로 분석** - 각 매크로 파일의 세부 기능 설명
- Benefit.mac 상세 분석
- 시나리오 실행 매크로 (+bc-1.mac, +bc-st.mac)
- 교통배정 관련 매크로
- 보조 매크로들의 역할

### 3. 📖 [USAGE_GUIDE.md](USAGE_GUIDE.md)
**실무 활용 가이드** - 실제 프로젝트 적용 방법
- 설치 및 설정
- 단계별 사용법
- 실무 사례 분석
- 문제해결 방법

### 4. 🔬 [TECHNICAL_DOCS.md](TECHNICAL_DOCS.md)
**기술 문서** - 수학적 모델과 이론적 배경
- 경제성 분석 이론
- 수학적 모델링 (공식 및 계산식)
- 교통배정 모델
- 품질관리 방안

### 5. 📊 [COMPREHENSIVE_ANALYSIS.md](COMPREHENSIVE_ANALYSIS.md)
**종합 분석 보고서** - 전체 시스템의 통합적 이해
- 시스템 아키텍처
- 경제학적 이론 배경
- 실무 적용 분야
- 국제 표준과의 비교

## 🚀 빠른 시작 가이드

### 처음 사용하는 경우
1. [README.md](README.md) → 전체 개요 파악
2. [USAGE_GUIDE.md](USAGE_GUIDE.md) → 기본 사용법 학습
3. 실제 데이터로 테스트 실행

### 심화 학습이 필요한 경우  
1. [TECHNICAL_DOCS.md](TECHNICAL_DOCS.md) → 이론적 배경 이해
2. [MACRO_ANALYSIS.md](MACRO_ANALYSIS.md) → 매크로별 세부 기능
3. [COMPREHENSIVE_ANALYSIS.md](COMPREHENSIVE_ANALYSIS.md) → 전체 시스템 이해

### 실무 적용시
1. [USAGE_GUIDE.md](USAGE_GUIDE.md) → 실무 사례 참고
2. [MACRO_ANALYSIS.md](MACRO_ANALYSIS.md) → 필요한 매크로 선택
3. 프로젝트 특성에 맞는 매개변수 조정

## 📋 주요 매크로 빠른 참조

| 매크로 파일 | 주요 기능 | 사용 시점 |
|-------------|-----------|-----------|
| `Benefit.mac` | 편익 계산 엔진 | 교통배정 완료 후 |
| `+bc-st.mac` | 다중연도 분석 | 장기 프로젝트 평가 |
| `ResultBC.mac` | 교통배정+결과추출 | 시나리오별 분석 |
| `volatt-bc.mac` | 속성 생성 | 분석 시작 전 |

## 💡 주요 개념 빠른 참조

### 편익 유형
- **VOTS**: 시간가치 편익 (가장 큰 비중)
- **VOCS**: 차량운행비용 편익 
- **VICS**: 교통사고비용 편익
- **VOPCS**: 대기오염비용 편익
- **VONCS**: 소음비용 편익

### 차종 분류
- r1: 승용차 (78.67%)
- r2: 버스 (0.34%)
- r3: 소형화물차 (15.40%)
- r4: 중형화물차 (2.95%)
- r5: 대형화물차 (2.63%)

### 시간대 구분
- 첨두시간: 5시간
- 비첨두시간: 14시간
- 보정계수: 0.9856

## 🆘 문제 해결

### 일반적인 오류
- 속성 생성 오류 → [USAGE_GUIDE.md - 문제해결](USAGE_GUIDE.md#51-일반적인-오류)
- 교통배정 미수렴 → [TECHNICAL_DOCS.md - 수렴기준](TECHNICAL_DOCS.md#32-수렴-기준)
- 비현실적 결과 → [USAGE_GUIDE.md - 결과검증](USAGE_GUIDE.md#71-편익-규모-평가)

### 추가 지원
1. 각 문서의 상세 설명 참조
2. 매크로 파일 내 주석 확인
3. 실무 사례와 비교 검증

---

**💫 이 문서들을 통해 BC-macro의 모든 기능을 완전히 이해하고 활용하실 수 있습니다!**