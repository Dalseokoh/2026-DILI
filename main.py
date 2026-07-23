
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DILI · iDILI · HILI 비교분석",
    page_icon="🧬",
    layout="wide",
)

# ---------------------------------------------------------
# 헤더
# ---------------------------------------------------------
st.title("🧬 약인성 간손상(DILI) 비교분석")
st.caption("일반 DILI vs 특발성 DILI(iDILI) vs 허브유래 간손상(HILI)")

st.markdown(
    """
이 앱은 **약물유발 간손상(Drug-Induced Liver Injury, DILI)** 의 전체 개념 안에서,
용량 의존적으로 발생하는 **내인성(intrinsic) DILI**, 예측이 어려운 **특발성(idiosyncratic) DILI, iDILI**,
그리고 한약재·건강기능식품·전통의학 제제로 인한 **허브유발 간손상(Herb-Induced Liver Injury, HILI)** 을
비교·정리한 자료입니다. (일반적인 의학 교육 목적의 요약이며, 개별 환자 진단·치료 판단을 대체하지 않습니다.)
"""
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📖 개요", "⚖️ DILI vs iDILI", "🌿 HILI 심층분석", "📊 종합 비교표", "📚 참고 자료"]
)

# ---------------------------------------------------------
# TAB 1. 개요
# ---------------------------------------------------------
with tab1:
    st.header("DILI의 분류 체계")

    st.markdown(
        """
    **DILI(Drug-Induced Liver Injury)** 는 처방약, 일반의약품(OTC), 생물학적제제뿐 아니라
    한약재·건강기능식품(HDS, herbal and dietary supplements)까지 포함하는 xenobiotic에 의한
    간손상을 총칭하는 개념입니다. 최근에는 HDS로 인한 손상을 별도로 **HILI**라는 용어로
    구분해 부르는 경향이 늘고 있습니다.
    """
    )

    st.subheader("분류 흐름")
    st.markdown(
        """
    ```
    DILI (약인성 간손상, 넓은 의미)
    ├── 내인성(Intrinsic) DILI  — 용량 의존적, 예측 가능 (예: 아세트아미노펜 과량)
    ├── 특발성(Idiosyncratic) DILI, iDILI — 용량 비의존적, 예측 불가능, 개인 감수성 기반
    └── 간접(Indirect) DILI — 기저질환 악화/면역 변화 등 간접 기전 (예: 면역항암제, 스테로이드 중단 후 B형간염 재활성화)

    HILI (허브유발 간손상)
    └── 대부분 iDILI의 하위 범주로 분류되며, 원인물질이 단일화합물이 아닌
        복합 성분 혼합물(mixture)이라는 점이 가장 큰 차이
    ```
    """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("전체 급성간부전 중 DILI 비중 (미국)", "약 10~13%")
    with col2:
        st.metric("iDILI가 전체 DILI에서 차지하는 비중", "대다수")
    with col3:
        st.metric("HILI 보고 원인 허브·제품 수", "70종 이상")

    st.info(
        "핵심 포인트: iDILI는 'DILI의 하위유형'이고, HILI는 '원인물질(허브/HDS)에 따른 분류'입니다. "
        "즉 두 용어는 서로 배타적이지 않으며, 대부분의 HILI는 임상적으로 iDILI의 패턴을 보입니다."
    )

# ---------------------------------------------------------
# TAB 2. DILI vs iDILI
# ---------------------------------------------------------
with tab2:
    st.header("일반 DILI(내인성) vs 특발성 DILI(iDILI)")

    df_compare = pd.DataFrame(
        {
            "항목": [
                "정의",
                "대표 기전",
                "용량 의존성",
                "예측 가능성",
                "동물실험 재현",
                "발생 빈도",
                "잠복기(노출~발현)",
                "대표 원인 물질",
                "위험인자",
                "중증도 경향",
                "재노출 시 반응",
                "진단 방법",
            ],
            "내인성(Intrinsic) DILI / 일반 DILI": [
                "약물 자체 또는 대사체의 직접적 간세포 독성",
                "직접적 세포독성, 활성대사체 축적 → 미토콘드리아 손상, 산화스트레스",
                "명확히 존재 (용량이 많을수록 손상 심화)",
                "높음 (용량·혈중농도로 예측 가능)",
                "잘 재현됨",
                "상대적으로 흔함, 용량 초과 시 거의 모든 사람에서 발생 가능",
                "짧음 (수 시간~수일)",
                "아세트아미노탄(과량), 일부 항암제, 사염화탄소 등",
                "총 섭취량, 병용 약물(대사효소 유도/억제), 영양상태, 음주",
                "예측된 만큼 발생, 조기 대응 시 회복률 높음(해독제 존재 시)",
                "재현됨(용량 재초과 시)",
                "혈중 약물/대사체 농도 측정, 용량-반응 관계 확인",
            ],
            "특발성(Idiosyncratic) DILI, iDILI": [
                "일부 개인에서만 발생하는 예측 불가능한 간손상",
                "면역매개 과민반응(HLA 연관) 또는 대사 특이체질(대사효소 다형성)",
                "명확한 용량-반응 관계 없음 (저용량에서도 발생 가능)",
                "낮음 (개인 감수성에 좌우)",
                "잘 재현되지 않음 (동물모델 확립이 어려움)",
                "드묾 (10,000~100,000명 중 1명 수준)",
                "다양함 (수일~수개월, 때로 약물 중단 후에도 발생)",
                "항결핵제, 항생제(아목시실린-클라불란산 등), 항경련제, NSAIDs 등",
                "HLA 유전형, 연령, 성별, 기저 간질환, 다약제 복용",
                "예측 불가능, 일부에서 급성간부전으로 진행 가능",
                "재노출 시 더 빠르고 심하게 재발하는 경우多 (재노출은 원칙적으로 금기)",
                "RUCAM/CIOMS 척도, 배제진단(다른 원인 배제) 필수",
            ],
        }
    )

    st.dataframe(df_compare, use_container_width=True, hide_index=True)

    st.markdown("#### 요약")
    st.success(
        """
- **내인성 DILI**: "누구나, 충분한 양이면" 발생 — 예측 가능하고 용량과 비례
- **iDILI**: "특정 개인에게만, 예측 불가능하게" 발생 — 면역/유전적 감수성이 핵심
- 임상에서 흔히 "DILI"라고 하면 대부분 **iDILI 패턴**을 의미하는 경우가 많음 (내인성 손상은 원인이 명확해 감별이 쉬움)
"""
    )

# ---------------------------------------------------------
# TAB 3. HILI
# ---------------------------------------------------------
with tab3:
    st.header("허브유발 간손상 (Herb-Induced Liver Injury, HILI)")

    st.markdown(
        """
    HILI는 한약재, 전통의학 제제(TCM 등), 건강기능식품(HDS)에 의해 유발되는 간손상을 지칭합니다.
    임상 양상은 iDILI와 유사하지만 **원인물질의 특성과 진단 과정에서 뚜렷한 차이**가 있습니다.
    """
    )

    df_hili = pd.DataFrame(
        {
            "항목": [
                "원인물질 특성",
                "성분 표준화",
                "품질관리",
                "병용/오염 가능성",
                "환자의 자진 보고율",
                "인과성 평가 도구",
                "대표 원인 허브/제품",
                "손상 패턴",
                "진단의 어려움",
                "규제 현황",
            ],
            "HILI 특징": [
                "단일 화합물이 아닌 **복합 성분 혼합물**(수십~수백 종 화학성분)",
                "제품 간, batch 간 성분 함량 편차 큼 (표준화 미흡)",
                "위·변조, 중금속/농약 오염, 다른 약초·약물 혼입 가능성 존재",
                "여러 허브를 동시 복용하거나 처방약과 병용하는 경우가 많아 원인물질 특정이 어려움",
                "'천연=안전'이라는 인식으로 인해 의료진에게 복용 사실을 알리지 않는 경우 많음 → 과소보고",
                "RUCAM(HILI용 개정판) 사용, 다만 허브 특이적 잠복기·재노출 항목의 신뢰도는 약물보다 낮은 편",
                "하수오(Polygonum multiflorum), 강황/커큐민 고용량 제제, 그린티 추출물(EGCG), 카바(kava), "
                "인도전통의학(Ayurvedic) 제제(아쉬와간다 등), 체중감량 보조제, 보디빌딩 보충제",
                "간세포형이 가장 흔하고, 담즙정체형·혼합형도 보고됨 (약물과 유사한 스펙트럼)",
                "성분 혼합물이라 원인 성분 특정이 어렵고, 라벨 표기와 실제 성분이 불일치하는 경우가 많아 인과성 확정이 까다로움",
                "국가별 편차 큼 — 의약품 수준 규제를 받는 경우와 식품 수준 규제만 받는 경우가 혼재",
            ],
        }
    )

    st.dataframe(df_hili, use_container_width=True, hide_index=True)

    st.markdown("#### RUCAM (HILI 인과성 평가) 7대 핵심 항목")
    df_rucam = pd.DataFrame(
        {
            "평가 항목": [
                "1. 잠복기 (노출~발현 시점)",
                "2. 중단 후 경과 (dechallenge)",
                "3. 위험인자 (연령, 음주/임신 등)",
                "4. 병용 약물/제품",
                "5. 다른 원인 배제 여부",
                "6. 기존 간독성 자료 유무",
                "7. 재노출 반응 (rechallenge)",
            ],
            "점수 범위": [
                "0 ~ +2",
                "−2 ~ +3",
                "0 ~ +2",
                "−3 ~ 0",
                "−3 ~ +2",
                "0 ~ +2",
                "−2 ~ +3",
            ],
        }
    )
    st.table(df_rucam)
    st.caption("※ 총점에 따라 가능성 낮음~거의 확실까지 등급을 매기며, DILI·HILI 공통으로 사용되는 표준화 도구입니다.")

    st.warning(
        "HILI는 정의상 **배제진단(diagnosis of exclusion)** 입니다. 바이러스성 간염, 자가면역성 간질환, "
        "대사/유전 질환, 허혈성 간손상 등 다른 원인을 모두 배제한 뒤에 원인 허브를 특정하게 됩니다."
    )

# ---------------------------------------------------------
# TAB 4. 종합 비교표
# ---------------------------------------------------------
with tab4:
    st.header("DILI · iDILI · HILI 종합 비교")

    df_all = pd.DataFrame(
        {
            "구분": [
                "정의 범위",
                "원인물질",
                "용량-반응 관계",
                "예측 가능성",
                "발생 빈도",
                "주요 기전",
                "진단 도구",
                "가장 큰 난제",
            ],
            "DILI (일반, 내인성 포함)": [
                "약물·화학물질에 의한 모든 간손상의 총칭",
                "단일 화합물(처방약, OTC 등)",
                "내인성은 존재, 특발성은 없음",
                "내인성은 높음",
                "내인성은 흔함(용량 초과 시)",
                "직접 세포독성 / 면역매개 (하위유형에 따라 다름)",
                "혈중 농도 측정, RUCAM",
                "원인 약물이 다수일 때 개별 기여도 특정",
            ],
            "iDILI (특발성)": [
                "DILI의 하위유형: 예측 불가능한 개인 감수성 기반 손상",
                "단일 화합물(처방약 중심)",
                "없음 (저용량에서도 발생)",
                "낮음",
                "드묾 (희귀)",
                "면역매개 과민반응(HLA 연관), 대사 특이체질",
                "RUCAM/CIOMS, 배제진단",
                "사전 예측·스크리닝 불가능",
            ],
            "HILI (허브유발)": [
                "iDILI의 하위 범주 + 원인물질이 허브·HDS인 경우",
                "복합 혼합물(허브, 전통의학 제제, 보충제)",
                "불명확 (성분 표준화 미흡으로 판단 자체가 어려움)",
                "매우 낮음",
                "증가 추세 (허브·보충제 사용 증가와 함께)",
                "iDILI와 유사(면역/특이체질) + 오염·위변조 요인 추가",
                "HILI용 개정 RUCAM, 성분분석 병행 권장",
                "원인 성분 특정, 환자의 복용 미고지, 품질관리 부재",
            ],
        }
    )

    st.dataframe(df_all, use_container_width=True, hide_index=True)

    st.markdown("#### 한눈에 보는 핵심 차이")
    st.markdown(
        """
    | 질문 | DILI(내인성) | iDILI | HILI |
    |---|---|---|---|
    | 용량을 늘리면 위험도가 올라가는가? | ✅ 그렇다 | ❌ 아니다 | ⚠️ 판단 어려움 (성분 불균일) |
    | 사전에 예측 가능한가? | ✅ 가능 | ❌ 불가능 | ❌ 불가능 |
    | 원인물질이 단일 성분인가? | ✅ 단일 | ✅ 단일(주로 약물) | ❌ 복합 혼합물 |
    | 환자가 원인물질 복용을 자진 보고하는 경향 | 비교적 높음 | 비교적 높음 | **낮음** (천연=안전 인식) |
    """
    )

# ---------------------------------------------------------
# TAB 5. 참고자료
# ---------------------------------------------------------
with tab5:
    st.header("참고 자료")
    st.markdown(
        """
    - Teschke R, et al. **RUCAM in Drug and Herb Induced Liver Injury: The Update.** *Int J Mol Sci.* 2016.
    - Teschke R, Danan G. **Idiosyncratic DILI and HILI: Diagnostic Algorithm Based on RUCAM.** 2021.
    - Lee WJ, et al. **A narrative review of herb-induced liver injury.** *Digestive Medicine Research.* 2021.
    - Teschke R. **Herb-Induced Liver Injury (HILI) with 12,068 worldwide cases assessed by RUCAM: an overview.** *Transl Gastroenterol Hepatol.* 2021.
    - Herb-Induced Liver Injury by Ayurvedic Ashwagandha as Assessed for Causality by the Updated RUCAM. *NCBI PMC.* 2023.

    ---
    ⚠️ 본 콘텐츠는 일반적인 의학 교육 목적의 요약 자료이며, 개별 환자에 대한 진단·치료 결정을 대체하지 않습니다.
    간손상이 의심되는 경우 반드시 의료진과 상담하시기 바랍니다.
    """
    )

st.divider()
st.caption("© DILI · iDILI · HILI 비교분석 대시보드 — Streamlit 예제 앱")


import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HILI 유발 허브·식품 리스트",
    page_icon="🌿",
    layout="wide",
)

st.title("🌿 허브유발 간손상(HILI) 유발 허브·식품 리스트")
st.caption("전체 원인 허브/보충제 목록 + 세계 보고 빈도 상위 10개")

st.markdown(
    """
아래 목록은 HILI(Herb-Induced Liver Injury) 관련 체계적 문헌고찰(systematic review) 및
사례보고 취합(pooled case-report) 연구에서 보고된 주요 원인 허브·건강기능식품을 정리한 것입니다.
개별 제품의 안전성을 판단하는 근거가 아니며, 일반 교육 목적의 요약입니다.
"""
)

# ---------------------------------------------------------
# 데이터: 전체 HILI 원인 허브/제품 리스트
# ---------------------------------------------------------
data = [
    ("하수오 (何首烏, He-Shou-Wu / Polygonum multiflorum)", "모발/항노화 강장 한약재", "간세포형", "아시아권(중국·한국) HILI 최다 원인, 잠복기 평균 약 58일"),
    ("그린티 추출물 (Green tea extract, EGCG)", "체중감량 보충제", "간세포형", "고농도 카테킨(EGCG) 함유 제품에서 보고, HLA-B*35:01과 연관"),
    ("헤르발라이프 제품 (Herbalife)", "체중감량/건강기능식품 브랜드", "간세포형", "다성분 복합제, 개별 원인성분 특정이 어려움"),
    ("카바카바 (Kava kava, Piper methysticum)", "불안/불면 완화 허브차", "간세포형", "중년 여성에서 호발, 중증 간부전·이식 사례 보고"),
    ("애기똥풀 (Greater celandine, Chelidonium majus)", "소화불량 개선 허브(유럽 전통)", "간세포형/담즙정체형", "독일 등 유럽에서 보고 비중 높음"),
    ("하이드록시컷 (Hydroxycut)", "체중감량 보충제 브랜드", "간세포형", "미국에서 다수 보고, 2009년 리콜 사례"),
    ("옥시엘리트 프로 (OxyElite Pro)", "체중감량/보디빌딩 보충제", "간세포형", "2013년 미국 하와이 집단 발병 사례로 유명"),
    ("저먼더 (Germander, Teucrium chamaedrys)", "체중감량 허브(과거 유럽 사용)", "간세포형", "1990년대 프랑스에서 다수 보고 후 판매 중단"),
    ("스컬캡/황금 (Skullcap, Scutellaria spp.)", "항불안/항염 허브", "간세포형", "미국에서 다수 보고, 저먼더 혼입 사례도 있었음"),
    ("크라톰 (Kratom, Mitragyna speciosa)", "통증완화/기분전환 식물", "간세포형/담즙정체형", "동남아시아 원산, 미국 내 사용 증가와 함께 보고 증가"),
    ("투산치/천칠 (Gynura segetum, Tusanqi)", "혈액순환 개선 한약재", "간정맥폐쇄병(VOD) 유사", "중국에서 다수 보고, 피롤리지딘 알칼로이드 함유"),
    ("가르시니아 캄보지아 (Garcinia cambogia)", "체중감량 보충제", "간세포형", "하이드록시시트르산(HCA) 함유 제품"),
    ("마황 (Ma huang, Ephedra sinica)", "체중감량/각성 한약재", "간세포형", "심혈관계 부작용과 함께 보고, 다수 국가에서 규제"),
    ("차파랄 (Chaparral, Larrea tridentata)", "항산화 허브(북미 전통)", "간세포형/담즙정체형", "미국 원주민 전통 사용, 급성 간부전 보고"),
    ("센나 (Senna spp.)", "변비 완화 허브 하제", "간세포형", "장기·고용량 사용 시 보고, 비교적 젊은 연령층에서 발생"),
    ("알로에 베라 (Aloe vera, 경구섭취)", "변비/디톡스 보조제", "간세포형", "경구 섭취 제품에서 보고, 국소 사용과는 무관"),
    ("강황/커큐민 고용량 제제 (Turmeric/Curcumin)", "항염 보충제", "간세포형/담즙정체형", "흡수촉진제(피페린) 병용 제품에서 보고 증가, HLA-B*35:01 연관"),
    ("아쉬와간다 (Ashwagandha)", "아유르베다 적응증 보충제", "간세포형/담즙정체형", "최근 보고 증가 중인 인도 전통의학 제제"),
    ("프소랄레아 (Psoralea corylifolia, 보골지)", "탈모/골다공증 개선 한약재", "간세포형", "중국 HILI 주요 원인 중 하나"),
    ("현호색 (Corydalis yanhusuo, 연호색)", "진통 목적 한약재", "간세포형", "중국 HILI 주요 원인 중 하나"),
]

df_full = pd.DataFrame(data, columns=["허브/제품명", "주요 사용 목적", "손상 패턴", "비고"])

tab1, tab2, tab3 = st.tabs(["📋 전체 리스트", "📊 세계 보고 빈도 상위 10개", "📚 출처"])

with tab1:
    st.subheader("HILI 원인 허브·건강기능식품 전체 리스트")

    keyword = st.text_input("🔍 허브/제품명 검색", "")
    filtered = df_full.copy()
    if keyword:
        mask = filtered["허브/제품명"].str.contains(keyword, case=False) | filtered["주요 사용 목적"].str.contains(keyword, case=False)
        filtered = filtered[mask]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.caption(f"총 {len(filtered)}개 항목 표시 중 (전체 {len(df_full)}개)")

with tab2:
    st.subheader("전 세계 보고 빈도 상위 10개 원인 허브·제품")

    st.markdown(
        """
    아래 순위는 두 편의 문헌을 종합한 것입니다.

    - **Ballotin 등 (2021), World J Clin Cases** — HILI 체계적 문헌고찰·메타분석 (총 936례, 79종 허브 분석)
    - **사례보고 취합(Pooled case-report) 분석 (2022)** — 총 428례의 개별 사례 취합 (실제 보고 건수 확인 가능)

    두 연구는 표본과 방법론이 달라 **정확한 절대 수치를 하나의 축으로 직접 비교하기는 어렵습니다.**
    따라서 아래 그래프는 두 문헌에서 공통으로 확인되는 **보고 빈도 순위(1위~10위)** 를 상대적
    막대 길이로 나타낸 것이며, 표에는 각 문헌에서 확인 가능한 **실제 수치**를 함께 표기했습니다.
    """
    )

    rank_data = pd.DataFrame(
        {
            "허브/제품명": [
                "하수오 (He-Shou-Wu)",
                "그린티 추출물",
                "헤르발라이프",
                "카바카바",
                "애기똥풀",
                "하이드록시컷",
                "옥시엘리트 프로",
                "저먼더",
                "스컬캡/황금",
                "크라톰",
            ],
            "순위": list(range(1, 11)),
            "실제 보고 수치 (출처)": [
                "8.3% / 936례 중 (Ballotin 2021); 25례 / 428례 중 (Pooled 2022)",
                "8.3% / 936례 중 (Ballotin 2021); 19례 / 428례 중 (Pooled 2022)",
                "5.9% / 936례 중 (Ballotin 2021); 50례 / 428례 중, 최다 (Pooled 2022)",
                "5.7% / 936례 중 (Ballotin 2021); 16례 / 428례 중 (Pooled 2022)",
                "4.4% / 936례 중 (Ballotin 2021)",
                "19례 / 428례 중 (Pooled 2022)",
                "16례 / 428례 중 (Pooled 2022)",
                "Ballotin(2021) 순위 6위권 (정확한 %는 원문 미기재)",
                "Ballotin(2021) 순위 8위권 (정확한 %는 원문 미기재)",
                "Ballotin(2021) 순위 9위권 (정확한 %는 원문 미기재)",
            ],
        }
    )
    rank_data["상대적 보고 빈도(순위 환산)"] = 11 - rank_data["순위"]

    chart_df = rank_data.set_index("허브/제품명")[["상대적 보고 빈도(순위 환산)"]]
    st.bar_chart(chart_df, horizontal=True)

    st.dataframe(
        rank_data[["순위", "허브/제품명", "실제 보고 수치 (출처)"]],
        use_container_width=True,
        hide_index=True,
    )

    st.info(
        "국가별 편차가 큽니다: **하수오·투산치**는 중국·한국 등 아시아에서, "
        "**애기똥풀·저먼더**는 독일 등 유럽에서, **그린티 추출물·스컬캡·크라톰·차파랄**은 미국에서 "
        "상대적으로 더 많이 보고되는 경향을 보입니다."
    )

with tab3:
    st.header("출처")
    st.markdown(
        """
    - Ballotin VR, et al. **Herb-Induced Liver Injury: Systematic Review and Meta-Analysis.** *World J Clin Cases.* 2021;9(20):5490-5513.
    - **Liver Injury Induced by Herbal and Dietary Supplements: A Pooled Analysis of Case Reports.** *(PubMed ID 36515339)*, 2022.
    - Navarro VJ, et al. **Liver injury from herbals and dietary supplements in the U.S. DILIN.** *Hepatology.* 2014;60(4):1399-1408.
    - Teschke R, et al. **RUCAM in Drug and Herb Induced Liver Injury: The Update.** *Int J Mol Sci.* 2016.
    - Zhu Y, et al. **Herb-Induced Liver Injury Related to Reynoutria multiflora.** review, PMC.

    ---
    ⚠️ 본 자료는 일반적인 의학 교육 목적의 요약이며, 특정 제품 사용 여부에 대한 결정 근거로 사용해서는 안 됩니다.
    간손상이 의심되는 경우 복용 중인 모든 허브·보충제·한약재를 반드시 의료진에게 알리시기 바랍니다.
    """
    )

st.divider()
st.caption("© HILI 유발 허브·식품 리스트 — Streamlit 예제 앱")

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="iDILI 유발 의약품·식품 리스트",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 특발성 약인성 간손상(iDILI) 유발 의약품·식품 리스트")
st.caption("전체 원인물질 목록 + 세계 보고 빈도 상위 10개 약물")

st.markdown(
    """
**iDILI(Idiosyncratic DILI)** 는 용량과 무관하게 일부 개인에서만 예측 불가능하게 발생하는 간손상입니다.
아세트아미노펜 과량처럼 **용량 의존적으로 누구에게나 발생하는 내인성(intrinsic) DILI는 제외**하고,
개인의 면역·유전적 감수성(HLA 연관 등)에 따라 발생하는 원인물질만 정리했습니다.
개별 환자의 진단·치료 판단을 대체하지 않는 일반 교육 목적의 요약입니다.
"""
)

# ---------------------------------------------------------
# 데이터: 전체 iDILI 원인물질 리스트
# ---------------------------------------------------------
data = [
    ("아목시실린-클라불란산", "항생제(페니실린계)", "담즙정체형/혼합형", "전 세계 iDILI 보고에서 가장 흔한 단일 원인 약물, 고령 남성에서 호발"),
    ("플루클록사실린", "항생제(페니실린계)", "담즙정체형", "HLA-B*57:01과 강한 연관, 노출 후 지연성 발현"),
    ("트리메토프림-설파메톡사졸", "항생제(설파계)", "간세포형", "미국 DILIN 등록연구 상위 원인 약물"),
    ("니트로푸란토인", "항생제(요로감염 치료제)", "간세포형(자가면역양상)", "장기 잠복기(>1년 가능), 자가면역성 간염 유사 소견"),
    ("이소니아지드", "항결핵제", "간세포형", "아시아권 iDILI의 가장 흔한 원인, NAT2 유전형(아세틸화 속도)과 연관"),
    ("리팜핀 / 피라진아미드", "항결핵제", "간세포형", "이소니아지드와 병용 시 위험 상승"),
    ("미노사이클린", "항생제(테트라사이클린계)", "간세포형(자가면역양상)", "여드름 치료 목적 장기 복용, 젊은 여성에서 자가면역양상 흔함"),
    ("에리트로마이신", "항생제(마크롤라이드계)", "담즙정체형", "세계 상위 10대 원인 약물"),
    ("세프트리아존 등 세팔로스포린계", "항생제(세팔로스포린계)", "담즙정체형", "동아시아권 입원환자 DILI에서 보고 빈도 높음"),
    ("디클로페낙", "NSAIDs", "간세포형", "세계 상위 10대 원인 약물"),
    ("이부프로펜", "NSAIDs", "간세포형", "상대적으로 드묾이나 세계 상위 10대 원인 약물"),
    ("설린닥", "NSAIDs", "간세포형/담즙정체형", "NSAIDs 중 상대적으로 위험도가 높은 편"),
    ("발프로산", "항경련제", "간세포형(미토콘드리아 기전)", "소아, 다약제 병용 시 위험 증가"),
    ("페니토인", "항경련제", "간세포형", "과민반응증후군(DRESS) 동반 가능"),
    ("카바마제핀", "항경련제", "간세포형/혼합형", "세계 상위 10대 원인 약물, DRESS 동반 가능"),
    ("라모트리진", "항경련제", "간세포형", "중증 피부반응 동반 사례 보고"),
    ("아토르바스타틴", "스타틴(고지혈증약)", "간세포형", "세계 상위 10대 원인 약물, 발생 자체는 드묾"),
    ("심바스타틴", "스타틴(고지혈증약)", "간세포형", "세계 상위 10대 원인 약물"),
    ("아미오다론", "항부정맥제", "간세포형(지방간염 유사)", "장기 복용 시 만성 손상 가능"),
    ("디설피람", "금주보조제", "간세포형", "세계 상위 10대 원인 약물"),
    ("알로퓨리놀", "통풍치료제", "혼합형", "과민반응증후군(DRESS/SJS) 동반 가능"),
    ("아나볼릭 스테로이드", "호르몬제/보디빌딩 보충제", "담즙정체형", "세계 상위 10대 원인 물질, 보충제 오남용과 관련"),
    ("면역관문억제제 (펨브롤리주맙, 니볼루맙 등)", "항암제(면역치료제)", "간세포형(면역매개성 간염)", "최근 급증 추세, 스테로이드 치료에 반응"),
    ("메틸도파", "항고혈압제", "간세포형(자가면역양상)", "임신성 고혈압 치료에 사용, 자가면역성 간염 유사"),
    ("케토코나졸", "항진균제", "간세포형", "경구제형은 다수 국가에서 사용 제한됨"),
    ("테르비나핀", "항진균제(무좀 치료제)", "담즙정체형", "장기 잠복기 후 발현 가능"),
    ("독시사이클린", "항생제(테트라사이클린계)", "간세포형", "상대적으로 드묾"),
    ("아자티오프린", "면역억제제", "간세포형/담즙정체형", "장기이식/자가면역질환 환자에서 사용"),
    ("인플릭시맙", "항암/면역질환 생물학적제제", "간세포형(자가면역양상)", "자가면역성 간염 유사 소견 보고"),
    ("둘록세틴", "항우울제", "간세포형", "DILIN에서 별도 연구된 약물"),
]

df_full = pd.DataFrame(data, columns=["약물명", "분류", "손상 패턴", "비고"])

tab1, tab2, tab3 = st.tabs(["📋 전체 리스트", "📊 세계 보고 빈도 상위 10개", "📚 출처"])

with tab1:
    st.subheader("iDILI 원인 의약품 전체 리스트")

    col1, col2 = st.columns([2, 1])
    with col1:
        keyword = st.text_input("🔍 약물명/분류 검색", "")
    with col2:
        pattern_filter = st.multiselect(
            "손상 패턴 필터",
            options=sorted(df_full["손상 패턴"].unique()),
            default=[],
        )

    filtered = df_full.copy()
    if keyword:
        mask = filtered["약물명"].str.contains(keyword, case=False) | filtered["분류"].str.contains(keyword, case=False)
        filtered = filtered[mask]
    if pattern_filter:
        filtered = filtered[filtered["손상 패턴"].isin(pattern_filter)]

    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.caption(f"총 {len(filtered)}개 항목 표시 중 (전체 {len(df_full)}개)")

with tab2:
    st.subheader("전 세계 보고 빈도 상위 10개 iDILI 원인 약물")

    st.markdown(
        """
    아래 순위는 **Teschke & Danan (2018)** 이 RUCAM(Roussel Uclaf Causality Assessment Method)으로
    인과성이 확인된 전 세계 iDILI 사례 **3,312건**을 검토해 정리한 "가장 흔하게 보고된 원인 약물" 순위입니다.
    국가·코호트마다 정확한 비율은 다르므로, 이 그래프는 **절대 발생 빈도(%)가 아니라 보고 빈도
    순위(1위~10위)** 를 상대적 막대 길이로 시각화한 것입니다.
    """
    )

    rank_data = pd.DataFrame(
        {
            "약물명": [
                "아목시실린-클라불란산",
                "플루클록사실린",
                "아토르바스타틴",
                "디설피람",
                "디클로페낙",
                "심바스타틴",
                "카바마제핀",
                "이부프로펜",
                "에리트로마이신",
                "아나볼릭 스테로이드",
            ],
            "순위": list(range(1, 11)),
        }
    )
    rank_data["상대적 보고 빈도(순위 환산)"] = 11 - rank_data["순위"]

    chart_df = rank_data.set_index("약물명")[["상대적 보고 빈도(순위 환산)"]]
    st.bar_chart(chart_df, horizontal=True)

    st.dataframe(
        rank_data[["순위", "약물명"]].rename(columns={"순위": "세계 보고 빈도 순위"}),
        use_container_width=True,
        hide_index=True,
    )

    st.info(
        "참고: 미국 DILIN 등록연구(Chalasani 2008, 초기 300례) 단독 분석에서는 "
        "**아목시실린-클라불란산 23례**로 단일 최다 원인이었고, "
        "**트리메토프림-설파메톡사졸·니트로푸란토인·이소니아지드가 각 13례**로 공동 2위권을 이루었습니다. "
        "동양권(중국·한국·인도)에서는 **이소니아지드 등 항결핵제**가 최다 원인으로 보고되는 등, "
        "지역별 처방 패턴에 따라 순위 차이가 있습니다."
    )

with tab3:
    st.header("출처")
    st.markdown(
        """
    - Teschke R, Danan G. **Top ranking drugs out of 3312 drug induced liver injury cases evaluated by RUCAM.** *Expert Opin Drug Metab Toxicol.* 2018.
    - Chalasani N, et al. **Causes, clinical features, and outcomes from a prospective study of drug-induced liver injury in the United States.** *Gastroenterology.* 2008;135(6):1924-34.
    - Chalasani N, et al. **Features and outcomes of 899 patients with drug-induced liver injury: the DILIN prospective study.** *Gastroenterology.* 2015;148(7):1340-52.
    - Andrade RJ, et al. **Drug-induced liver injury: an analysis of 461 incidences submitted to the Spanish registry.** *Gastroenterology.* 2005.
    - Björnsson ES, et al. **East versus West: a systematic review and meta-analysis of DILI epidemiology.** *PMC.*
    - Weber S, Gerbes AL. **Hepatotoxicity by Drugs: The Most Common Implicated Agents.** *Int J Mol Sci.* 2016.

    ---
    ⚠️ 본 자료는 일반적인 의학 교육 목적의 요약이며, 개별 환자에 대한 진단·처방 변경의 근거로 사용해서는 안 됩니다.
    """
    )

st.divider()
st.caption("© iDILI 유발 의약품·식품 리스트 — Streamlit 예제 앱")
