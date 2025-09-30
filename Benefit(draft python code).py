#주석 : Benefit.mac 파일 을 Python으로 변환한 초기버전임. 
#해당 코드 실행 및 검증은 하지 않았으므로, 참고용임. 


from inro.modeller import Tool
import inro.modeller as _modeller

class CalculateNetworkBenefits(Tool):
    """
    Emme Modeller Tool: 주요 교통 편익 지표를 링크 수준에 계산하여 저장하는 도구
    실행하면 다음을 수행:
      1. 필요한 extra attributes를 정리 후 생성
      2. 속도 기반 VOCS 계산 (Peak/Non-Peak/통합)
      3. 통행시간 기반 VOTS 계산
    """

    def __init__(self, modeller):
        self.modeller = modeller
        self.calc = modeller.tool("inro.emme.network_calculation.network_calculator")
        self.create_attr = modeller.tool("inro.emme.data.extra_attribute.create_extra_attribute")
        self.delete_attr = modeller.tool("inro.emme.data.extra_attribute.delete_extra_attribute")

    def __call__(self):
        # Step 1: Attribute 정의
        attributes = [
            ("LINK", "@pvocs", "Peak Vehicle Operating Cost"),
            ("LINK", "@nvocs", "Non-Peak Vehicle Operating Cost"),
            ("LINK", "@vocs", "Daily Vehicle Operating Cost"),
            ("LINK", "@vots", "Value of Travel Time Saving")
        ]

        # Step 2: 기존 Attribute 삭제 후 재생성
        for obj_class, name, desc in attributes:
            try:
                self.delete_attr(extra_attribute=obj_class + ":" + name)
            except:
                pass  # 존재하지 않으면 무시

            self.create_attr(extra_attribute_spec={
                "type": obj_class,
                "name": name,
                "description": desc,
                "default_value": 0.0
            })

        # Step 3: VOCS 계산 계수
        vocs_params = {
            "r1": 0.786701,
            "r2": 0.003427,
            "r3": 0.154045,
            "r4": 0.029522,
            "r5": 0.026303
        }

        # Step 4: Peak VOCS 계산식
        peak_expr = f"""
((0.00000492*(@pspd)^4 - 0.00174193*(@pspd)^3 + 0.25106799*(@pspd)^2 - 17.78182586*(@pspd) + 765.13001217) * length * @ptota * {vocs_params['r1']} +
 (0.00001393*(@pspd)^4 - 0.00441911*(@pspd)^3 + 0.57815961*(@pspd)^2 - 36.56152235*(@pspd) + 1384.340464) * length * @ptota * {vocs_params['r2']} +
 (0.00000966*(@pspd)^4 - 0.00269479*(@pspd)^3 + 0.31552798*(@pspd)^2 - 18.52720300*(@pspd) + 694.610224) * length * @ptota * {vocs_params['r3']} +
 (0.00002769*(@pspd)^4 - 0.00694719*(@pspd)^3 + 0.70669201*(@pspd)^2 - 35.29357075*(@pspd) + 1135.2051535) * length * @ptota * {vocs_params['r4']} +
 (0.0000239*(@pspd)^4 - 0.00657652*(@pspd)^3 + 0.75632506*(@pspd)^2 - 42.85518051*(@pspd) + 1576.454715) * length * @ptota * {vocs_params['r5']}) * 365 / 1e8
"""
        self.calc(expression=peak_expr, result="@pvocs", aggregation=False)
        print("Peak VOCS 계산 완료")

        # Step 5: Non-Peak VOCS 계산식
        nonpeak_expr = f"""
((0.00000492*(@nspd)^4 - 0.00174193*(@nspd)^3 + 0.25106799*(@nspd)^2 - 17.78182586*(@nspd) + 765.13001217) * length * @ntota * {vocs_params['r1']} +
 (0.00001393*(@nspd)^4 - 0.00441911*(@nspd)^3 + 0.57815961*(@nspd)^2 - 36.56152235*(@nspd) + 1384.340464) * length * @ntota * {vocs_params['r2']} +
 (0.00000966*(@nspd)^4 - 0.00269479*(@nspd)^3 + 0.31552798*(@nspd)^2 - 18.52720300*(@nspd) + 694.610224) * length * @ntota * {vocs_params['r3']} +
 (0.00002769*(@nspd)^4 - 0.00694719*(@nspd)^3 + 0.70669201*(@nspd)^2 - 35.29357075*(@nspd) + 1135.2051535) * length * @ntota * {vocs_params['r4']} +
 (0.0000239*(@nspd)^4 - 0.00657652*(@nspd)^3 + 0.75632506*(@nspd)^2 - 42.85518051*(@nspd) + 1576.454715) * length * @ntota * {vocs_params['r5']}) * 365 / 1e8
"""
        self.calc(expression=nonpeak_expr, result="@nvocs", aggregation=False)
        print("Non-Peak VOCS 계산 완료")

        # Step 6: VOCS 통합 (5시간 첨두, 14시간 비첨두)
        self.calc(expression="@pvocs*5 + @nvocs*14", result="@vocs", aggregation=False)
        print("전체 VOCS 계산 완료 (@vocs)")

        # Step 7: VOTS 계산 (KDI 기준)
        vots_expr = f"""
((@ptimea/60) * @ptota * ({vocs_params['r1']}*23319 + {vocs_params['r2']}*191626 + ({vocs_params['r3']}+{vocs_params['r4']}+{vocs_params['r5']})*27809) * 365 / 1e8)*5
+ ((@ntimea/60) * @ntota * ({vocs_params['r1']}*23319 + {vocs_params['r2']}*191626 + ({vocs_params['r3']}+{vocs_params['r4']}+{vocs_params['r5']})*27809) * 365 / 1e8)*14
"""
        self.calc(expression=vots_expr, result="@vots", aggregation=False)
        print("VOTS 계산 완료")

        print("모든 계산이 완료되었습니다.")
