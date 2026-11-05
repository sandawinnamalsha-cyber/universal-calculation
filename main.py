import flet as ft
import math

def main(page: ft.Page):
    page.title = "Universal Unit Converter & Math App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 480
    page.window_height = 850
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Main Category Dropdown
    category_dd = ft.Dropdown(
        label="Select Category",
        options=[
            ft.dropdown.Option("1", "1. Distance / Length"),
            ft.dropdown.Option("2", "2. Weight / Mass"),
            ft.dropdown.Option("3", "3. Temperature"),
            ft.dropdown.Option("4", "4. Time"),
            ft.dropdown.Option("5", "5. Speed"),
            ft.dropdown.Option("6", "6. Area"),
            ft.dropdown.Option("7", "7. Volume"),
            ft.dropdown.Option("8", "8. Trigonometry"),
        ],
        width=420,
    )

    subcategory_dd = ft.Dropdown(
        label="Select Conversion / Shape / Option",
        width=420,
        visible=False
    )

    trig_calc_dd = ft.Dropdown(
        label="Select Trigonometry Calculation",
        width=420,
        visible=False
    )

    # Input Fields
    input_1 = ft.TextField(label="Enter Value 1", keyboard_type=ft.KeyboardType.NUMBER, width=420, visible=False)
    input_2 = ft.TextField(label="Enter Value 2", keyboard_type=ft.KeyboardType.NUMBER, width=420, visible=False)
    input_3 = ft.TextField(label="Enter Value 3", keyboard_type=ft.KeyboardType.NUMBER, width=420, visible=False)

    result_text = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD,
        color="blue"
    )

    # 1. Distance (1 to 30)
    distance_options = [
        ("1", "1. cm to m"), ("2", "2. m to cm"), ("3", "3. mm to cm"), ("4", "4. cm to mm"),
        ("5", "5. mm to m"), ("6", "6. m to mm"), ("7", "7. m to km"), ("8", "8. km to m"),
        ("9", "9. cm to km"), ("10", "10. km to cm"), ("11", "11. m to feet"), ("12", "12. feet to m"),
        ("13", "13. cm to feet"), ("14", "14. feet to cm"), ("15", "15. cm to inch"), ("16", "16. inch to cm"),
        ("17", "17. m to inch"), ("18", "18. inch to m"), ("19", "19. inch to feet"), ("20", "20. feet to inch"),
        ("21", "21. km to mile"), ("22", "22. mile to km"), ("23", "23. m to mile"), ("24", "24. mile to m"),
        ("25", "25. m to yard"), ("26", "26. yard to m"), ("27", "27. yard to mile"), ("28", "28. mile to yard"),
        ("29", "29. yard to km"), ("30", "30. km to yard")
    ]

    # 2. Weight (1 to 20)
    weight_options = [
        ("1", "1. g to kg"), ("2", "2. kg to g"), ("3", "3. g to mg"), ("4", "4. mg to g"),
        ("5", "5. mg to kg"), ("6", "6. kg to mg"), ("7", "7. kg to ton"), ("8", "8. ton to kg"),
        ("9", "9. g to ton"), ("10", "10. ton to g"), ("11", "11. kg to pound"), ("12", "12. pound to kg"),
        ("13", "13. g to pound"), ("14", "14. pound to g"), ("15", "15. kg to ounce"), ("16", "16. ounce to kg"),
        ("17", "17. g to ounce"), ("18", "18. ounce to g"), ("19", "19. pound to ounce"), ("20", "20. ounce to pound")
    ]

    # 3. Temperature (1 to 6)
    temp_options = [
        ("1", "1. C to F"), ("2", "2. F to C"), ("3", "3. C to K"),
        ("4", "4. K to C"), ("5", "5. F to K"), ("6", "6. K to F")
    ]

    # 4. Time (1 to 30)
    time_options = [
        ("1", "1. s to min"), ("2", "2. min to s"), ("3", "3. min to h"), ("4", "4. h to min"),
        ("5", "5. s to ms"), ("6", "6. ms to s"), ("7", "7. s to h"), ("8", "8. h to s"),
        ("9", "9. days to h"), ("10", "10. h to days"), ("11", "11. days to min"), ("12", "12. days to s"),
        ("13", "13. days to weeks"), ("14", "14. week to days"), ("15", "15. weeks to hours"), ("16", "16. years to days"),
        ("17", "17. years to weeks"), ("18", "18. years to h"), ("19", "19. years to min"), ("20", "20. years to s"),
        ("21", "21. months to days"), ("22", "22. days to months"), ("23", "23. months to hours"), ("24", "24. months to years"),
        ("25", "25. years to months"), ("26", "26. years to decades"), ("27", "27. decades to years"), ("28", "28. years to centuries"),
        ("29", "29. centuries to years"), ("30", "30. centuries to decades")
    ]

    # 5. Speed (1 to 30)
    speed_options = [
        ("1", "1. m/s to km/h"), ("2", "2. km/h to m/s"), ("3", "3. m/s to mph"), ("4", "4. mph to m/s"),
        ("5", "5. km/h to mph"), ("6", "6. mph to km/h"), ("7", "7. m/s to knots"), ("8", "8. knots to m/s"),
        ("9", "9. km/h to knots"), ("10", "10. knots to km/h"), ("11", "11. mph to knots"), ("12", "12. knots to mph"),
        ("13", "13. m/s to ft/s"), ("14", "14. ft/s to m/s"), ("15", "15. km/h to ft/s"), ("16", "16. ft/s to km/h"),
        ("17", "17. mph to ft/s"), ("18", "18. ft/s to mph"), ("19", "19. km/h to m/min"), ("20", "20. m/min to km/h"),
        ("21", "21. m/s to km/s"), ("22", "22. km/s to m/s"), ("23", "23. km/h to km/s"), ("24", "24. km/s to km/h"),
        ("25", "25. mph to m/min"), ("26", "26. m/min to mph"), ("27", "27. knots to ft/s"), ("28", "28. ft/s to knots"),
        ("29", "29. m/s to mi/min"), ("30", "30. mi/min to m/s")
    ]

    # 6. Area (1 to 14)
    area_options = [
        ("1", "1. Rectangle"), ("2", "2. Square"), ("3", "3. Triangle"), ("4", "4. Circle"),
        ("5", "5. Parallelogram"), ("6", "6. Trapezium"), ("7", "7. Rhombus"), ("8", "8. Ellipse"),
        ("9", "9. Sector of circle"), ("10", "10. Right Triangle"), ("11", "11. Heron's formula (any triangle)"),
        ("12", "12. Cube Surface Area"), ("13", "13. Cuboid Surface Area"), ("14", "14. Cylinder Surface Area")
    ]

    # 7. Volume (1 to 14)
    volume_options = [
        ("1", "1. Cube"), ("2", "2. Cuboid"), ("3", "3. Cylinder"), ("4", "4. Sphere"),
        ("5", "5. Hemisphere"), ("6", "6. Cone"), ("7", "7. Pyramid"), ("8", "8. Torus"),
        ("9", "9. Triangular Prism"), ("10", "10. Rectangular Prism"), ("11", "11. Capsule"),
        ("12", "12. Ellipsoid"), ("13", "13. Frustum of Cone"), ("14", "14. Hollow Cylinder")
    ]

    # 8. Trigonometry (1 to 7)
    trig_options = [
        ("1", "1. Basic Definitions"), ("2", "2. Identities"), ("3", "3. A+B Formulas"),
        ("4", "4. Double Angle (2θ)"), ("5", "5. Half Angle"), ("6", "6. For Triangle"), ("7", "7. Other Cal")
    ]

    # Trigonometry 7 Sub-Calculations (1 to 14)
    trig_sub_options = [
        ("1", "1. DEG to RAD"), ("2", "2. RAD to DEG"), ("3", "3. SIN from DEG"),
        ("4", "4. COS from DEG"), ("5", "5. TAN from DEG"), ("6", "6. ASIN"),
        ("7", "7. ACOS"), ("8", "8. 3rd side of triangle (COSINE RULE)"),
        ("9", "9. Angle of triangle (COSINE RULE)"), ("10", "10. Height / Distance"),
        ("11", "11. Slope / Gradient"), ("12", "12. Polar to Cartesian"),
        ("13", "13. Cartesian to Polar"), ("14", "14. Area of Triangle (2 sides + angle)")
    ]

    def hide_all_inputs():
        input_1.visible = False
        input_2.visible = False
        input_3.visible = False
        trig_calc_dd.visible = False
        input_1.value = ""
        input_2.value = ""
        input_3.value = ""

    def category_changed(e):
        cat = category_dd.value
        subcategory_dd.options.clear()
        hide_all_inputs()
        
        opts = []
        if cat == "1": opts = distance_options
        elif cat == "2": opts = weight_options
        elif cat == "3": opts = temp_options
        elif cat == "4": opts = time_options
        elif cat == "5": opts = speed_options
        elif cat == "6": opts = area_options
        elif cat == "7": opts = volume_options
        elif cat == "8": opts = trig_options

        for val, text in opts:
            subcategory_dd.options.append(ft.dropdown.Option(val, text))
        
        subcategory_dd.visible = True
        subcategory_dd.value = None
        result_text.value = ""
        page.update()

    category_dd.on_change = category_changed

    def subcategory_changed(e):
        cat = category_dd.value
        sub = subcategory_dd.value
        hide_all_inputs()

        if cat in ["1", "2", "3", "4", "5"]:
            input_1.label = "Enter Value"
            input_1.visible = True

        elif cat == "6":
            if sub in ["2", "12"]:
                input_1.label = "Enter Side (a)"
                input_1.visible = True
            elif sub in ["1", "3", "5", "7", "8", "10"]:
                input_1.label = "Enter Base / Length / Semi-axis 1 / Diagonal 1"
                input_2.label = "Enter Height / Width / Semi-axis 2 / Diagonal 2"
                input_1.visible = True; input_2.visible = True
            elif sub in ["4"]:
                input_1.label = "Enter Radius (r)"
                input_1.visible = True
            elif sub == "6":
                input_1.label = "Enter First Parallel Base (a)"
                input_2.label = "Enter Second Parallel Base (b)"
                input_3.label = "Enter Height (h)"
                input_1.visible = True; input_2.visible = True; input_3.visible = True
            elif sub == "9":
                input_1.label = "Enter Radius (r)"
                input_2.label = "Enter Central Angle (θ in deg)"
                input_1.visible = True; input_2.visible = True
            elif sub in ["11", "13"]:
                input_1.label = "Enter Length / Side a"
                input_2.label = "Enter Width / Side b"
                input_3.label = "Enter Height / Side c"
                input_1.visible = True; input_2.visible = True; input_3.visible = True
            elif sub == "14":
                input_1.label = "Enter Radius (r)"
                input_2.label = "Enter Height (h)"
                input_1.visible = True; input_2.visible = True

        elif cat == "7":
            if sub == "1":
                input_1.label = "Enter Edge Length (a)"
                input_1.visible = True
            elif sub in ["2", "9", "10"]:
                input_1.label = "Enter Length / Base (l/a)"
                input_2.label = "Enter Width / Height (w/h)"
                input_3.label = "Enter Height / Length (h/l)"
                input_1.visible = True; input_2.visible = True; input_3.visible = True
            # FIXED: 14 අයින් කරා, වෙනම 3 inputs දෙනවා
            elif sub in ["3", "6", "7", "8", "11"]:
                input_1.label = "Enter Radius / Base Area / Outer Radius (r/a/R)"
                input_2.label = "Enter Height / Inner Radius (h/r)"
                input_1.visible = True; input_2.visible = True
            elif sub == "14": # FIXED: Hollow Cylinder - 3 inputs
                input_1.label = "Enter Outer Radius (R)"
                input_2.label = "Enter Inner Radius (r)"
                input_3.label = "Enter Height (h)"
                input_1.visible = True; input_2.visible = True; input_3.visible = True
            elif sub in ["4", "5"]:
                input_1.label = "Enter Radius (r)"
                input_1.visible = True
            elif sub in ["12", "13"]:
                input_1.label = "Enter Radius a / Top Radius R"
                input_2.label = "Enter Radius b / Bottom Radius r"
                input_3.label = "Enter Radius c / Height h"
                input_1.visible = True; input_2.visible = True; input_3.visible = True

        elif cat == "8":
            if sub == "7":
                trig_calc_dd.options.clear()
                for val, text in trig_sub_options:
                    trig_calc_dd.options.append(ft.dropdown.Option(val, text))
                trig_calc_dd.visible = True
                trig_calc_dd.value = None

        page.update()

    subcategory_dd.on_change = subcategory_changed

    def trig_calc_changed(e):
        tch = trig_calc_dd.value
        input_1.visible = False
        input_2.visible = False
        input_3.visible = False
        input_1.value = ""
        input_2.value = ""
        input_3.value = ""

        if tch in ["1", "3", "4", "5", "11"]:
            input_1.label = "Enter Angle in Degrees"
            input_1.visible = True
        elif tch == "2":
            input_1.label = "Enter rad as times of pi (ex: 0.3333 for pi/3, 1 for pi)"
            input_1.visible = True
        elif tch in ["6", "7"]:
            input_1.label = "Enter Value (-1 to 1)"
            input_1.visible = True
        # FIXED: 8 & 14 ට Inputs 3ක් ඕන
        elif tch in ["8", "14"]:
            input_1.label = "Enter Side 1"
            input_2.label = "Enter Side 2"
            input_3.label = "Enter Included Angle (deg)"
            input_1.visible = True; input_2.visible = True; input_3.visible = True
        elif tch in ["10", "12", "13"]:
            input_1.label = "Enter Side 1 / Distance / Radius / x"
            input_2.label = "Enter Side 2 / Angle / y"
            input_1.visible = True; input_2.visible = True
        elif tch == "9":
            input_1.label = "Enter Side a"
            input_2.label = "Enter Side b"
            input_3.label = "Enter Side c"
            input_1.visible = True; input_2.visible = True; input_3.visible = True
        
        page.update()

    trig_calc_dd.on_change = trig_calc_changed

    def calculate(e):
        try:
            cat = category_dd.value
            sub = subcategory_dd.value
            v1 = float(input_1.value) if input_1.value and input_1.visible else 0.0
            v2 = float(input_2.value) if input_2.value and input_2.visible else 0.0
            v3 = float(input_3.value) if input_3.value and input_3.visible else 0.0
            ans = ""

            if cat == "1":
                if sub == "1": ans = f"{v1 / 100} m"
                elif sub == "2": ans = f"{v1 * 100} cm"
                elif sub == "3": ans = f"{v1 / 10} cm"
                elif sub == "4": ans = f"{v1 * 10} mm"
                elif sub == "5": ans = f"{v1 / 1000} m"
                elif sub == "6": ans = f"{v1 * 1000} mm"
                elif sub == "7": ans = f"{v1 / 1000} km"
                elif sub == "8": ans = f"{v1 * 1000} m"
                elif sub == "9": ans = f"{v1 / 100000} km"
                elif sub == "10": ans = f"{v1 * 100000} cm"
                elif sub == "11": ans = f"{v1 * 3.28084} feet"
                elif sub == "12": ans = f"{v1 * 0.3048} m"
                elif sub == "13": ans = f"{v1 * 0.0328084} feet"
                elif sub == "14": ans = f"{v1 * 30.48} cm"
                elif sub == "15": ans = f"{v1 / 2.54} inches"
                elif sub == "16": ans = f"{v1 * 2.54} cm"
                elif sub == "17": ans = f"{v1 * 39.3701} inches"
                elif sub == "18": ans = f"{v1 * 0.0254} m"
                elif sub == "19": ans = f"{v1 / 12} feet"
                elif sub == "20": ans = f"{v1 * 12} inches"
                elif sub == "21": ans = f"{v1 * 0.621371} miles"
                elif sub == "22": ans = f"{v1 * 1.60934} km"
                elif sub == "23": ans = f"{v1 / 1609.34} miles"
                elif sub == "24": ans = f"{v1 * 1609.34} m"
                elif sub == "25": ans = f"{v1 * 1.09361} yards"
                elif sub == "26": ans = f"{v1 * 0.9144} m"
                elif sub == "27": ans = f"{v1 / 1760} miles"
                elif sub == "28": ans = f"{v1 * 1760} yards"
                elif sub == "29": ans = f"{v1 * 0.0009144} km"
                elif sub == "30": ans = f"{v1 * 1093.61} yards"

            elif cat == "2":
                if sub == "1": ans = f"{v1 / 1000} kg"
                elif sub == "2": ans = f"{v1 * 1000} g"
                elif sub == "3": ans = f"{v1 * 1000} mg"
                elif sub == "4": ans = f"{v1 / 1000} g"
                elif sub == "5": ans = f"{v1 / 1000000} kg"
                elif sub == "6": ans = f"{v1 * 1000000} mg"
                elif sub == "7": ans = f"{v1 / 1000} tons"
                elif sub == "8": ans = f"{v1 * 1000} kg"
                elif sub == "9": ans = f"{v1 / 1000000} tons"
                elif sub == "10": ans = f"{v1 * 1000000} g"
                elif sub == "11": ans = f"{v1 * 2.20462} lbs"
                elif sub == "12": ans = f"{v1 * 0.453592} kg"
                elif sub == "13": ans = f"{v1 * 0.00220462} lbs"
                elif sub == "14": ans = f"{v1 * 453.592} g"
                elif sub == "15": ans = f"{v1 * 35.274} oz"
                elif sub == "16": ans = f"{v1 * 0.0283495} kg"
                elif sub == "17": ans = f"{v1 * 0.035274} oz"
                elif sub == "18": ans = f"{v1 * 28.3495} g"
                elif sub == "19": ans = f"{v1 * 16} oz"
                elif sub == "20": ans = f"{v1 / 16} lbs"

            elif cat == "3":
                if sub == "1": ans = f"{(v1 * (9/5)) + 32:.4f} °F"
                elif sub == "2": ans = f"{(v1 - 32) * (5/9):.4f} °C"
                elif sub == "3": ans = f"{v1 + 273.15:.4f} K"
                elif sub == "4": ans = f"{v1 - 273.15:.4f} °C"
                elif sub == "5": ans = f"{((v1 - 32) * (5/9)) + 273.15:.4f} K"
                elif sub == "6": ans = f"{((v1 - 273.15) * (9/5)) + 32:.4f} °F"

            elif cat == "4":
                if sub == "1": ans = f"{v1 / 60:.4f} min"
                elif sub == "2": ans = f"{v1 * 60:.4f} s"
                elif sub == "3": ans = f"{v1 / 60:.4f} h"
                elif sub == "4": ans = f"{v1 * 60:.4f} min"
                elif sub == "5": ans = f"{v1 * 1000:.4f} ms"
                elif sub == "6": ans = f"{v1 / 1000:.4f} s"
                elif sub == "7": ans = f"{v1 / 3600:.4f} h"
                elif sub == "8": ans = f"{v1 * 3600:.4f} s"
                elif sub == "9": ans = f"{v1 * 24:.4f} h"
                elif sub == "10": ans = f"{v1 / 24:.4f} days"
                elif sub == "11": ans = f"{v1 * 1440:.4f} min"
                elif sub == "12": ans = f"{v1 * 86400:.4f} s"
                elif sub == "13": ans = f"{v1 / 7:.4f} weeks"
                elif sub == "14": ans = f"{v1 * 7:.4f} days"
                elif sub == "15": ans = f"{v1 * 168:.4f} hours"
                elif sub == "16": ans = f"{v1 * 365.25:.4f} days"
                elif sub == "17": ans = f"{v1 * 52.14:.4f} weeks"
                elif sub == "18": ans = f"{v1 * 8766:.4f} h"
                elif sub == "19": ans = f"{v1 * 525960:.4f} min"
                elif sub == "20": ans = f"{v1 * 31557600:.4f} s"
                elif sub == "21": ans = f"{v1 * 30.44:.4f} days"
                elif sub == "22": ans = f"{v1 / 30.44:.4f} months"
                elif sub == "23": ans = f"{v1 * 730.56:.4f} hours"
                elif sub == "24": ans = f"{v1 / 12:.4f} years"
                elif sub == "25": ans = f"{v1 * 12:.4f} months"
                elif sub == "26": ans = f"{v1 / 10:.4f} decades"
                elif sub == "27": ans = f"{v1 * 10:.4f} years"
                elif sub == "28": ans = f"{v1 / 100:.4f} centuries"
                elif sub == "29": ans = f"{v1 * 100:.4f} years"
                elif sub == "30": ans = f"{v1 * 10:.4f} decades"

            elif cat == "5":
                if sub == "1": ans = f"{v1 * 3.6:.4f} km/h"
                elif sub == "2": ans = f"{v1 / 3.6:.4f} m/s"
                elif sub == "3": ans = f"{v1 * 2.23694:.4f} mph"
                elif sub == "4": ans = f"{v1 / 2.23694:.4f} m/s"
                elif sub == "5": ans = f"{v1 / 1.60934:.4f} mph"
                elif sub == "6": ans = f"{v1 * 1.60934:.4f} km/h"
                elif sub == "7": ans = f"{v1 * 1.94384:.4f} knots"
                elif sub == "8": ans = f"{v1 / 1.94384:.4f} m/s"
                elif sub == "9": ans = f"{v1 / 1.852:.4f} knots"
                elif sub == "10": ans = f"{v1 * 1.852:.4f} km/h"
                elif sub == "11": ans = f"{v1 / 1.15078:.4f} knots"
                elif sub == "12": ans = f"{v1 * 1.15078:.4f} mph"
                elif sub == "13": ans = f"{v1 * 3.28084:.4f} ft/s"
                elif sub == "14": ans = f"{v1 / 3.28084:.4f} m/s"
                elif sub == "15": ans = f"{v1 * 0.91134:.4f} ft/s"
                elif sub == "16": ans = f"{v1 * 1.09728:.4f} km/h"
                elif sub == "17": ans = f"{v1 * 1.46667:.4f} ft/s"
                elif sub == "18": ans = f"{v1 / 1.46667:.4f} mph"
                elif sub == "19": ans = f"{v1 * 16.667:.4f} m/min"
                elif sub == "20": ans = f"{v1 / 16.667:.4f} km/h"
                elif sub == "21": ans = f"{v1 / 1000:.4f} km/s"
                elif sub == "22": ans = f"{v1 * 1000:.4f} m/s"
                elif sub == "23": ans = f"{v1 / 3600:.4f} km/s"
                elif sub == "24": ans = f"{v1 * 3600:.4f} km/h"
                elif sub == "25": ans = f"{v1 * 26.8224:.4f} m/min"
                elif sub == "26": ans = f"{v1 / 26.8224:.4f} mph"
                elif sub == "27": ans = f"{v1 * 1.68781:.4f} ft/s"
                elif sub == "28": ans = f"{v1 / 1.68781:.4f} knots"
                elif sub == "29": ans = f"{v1 * 0.03728:.4f} mi/min"
                elif sub == "30": ans = f"{v1 / 0.03728:.4f} m/s"

            elif cat == "6":
                if sub == "1": ans = f"Area = {v1 * v2:.4f}"
                elif sub == "2": ans = f"Area = {v1 * v1:.4f}"
                elif sub == "3": ans = f"Area = {0.5 * v1 * v2:.4f}"
                elif sub == "4": ans = f"Area = {3.1416 * v1 * v1:.4f}"
                elif sub == "5": ans = f"Area = {v1 * v2:.4f}"
                elif sub == "6": ans = f"Area = {0.5 * (v1 + v2) * v3:.4f}"
                elif sub == "7": ans = f"Area = {0.5 * v1 * v2:.4f}"
                elif sub == "8": ans = f"Area = {3.1416 * v1 * v2:.4f}"
                elif sub == "9": ans = f"Area = {(v2 / 360) * 3.1416 * v1 * v1:.4f}"
                elif sub == "10": ans = f"Area = {0.5 * v1 * v2:.4f}"
                elif sub == "11":
                    s = (v1 + v2 + v3) / 2
                    ans = f"Area = {(s * (s - v1) * (s - v2) * (s - v3)) ** 0.5:.4f}"
                elif sub == "12": ans = f"Area = {6 * v1 * v1:.4f}"
                elif sub == "13": ans = f"Area = {2 * ((v1 * v2) + (v2 * v3) + (v1 * v3)):.4f}"
                elif sub == "14":
                    csa = 2 * 3.1416 * v1 * v2
                    ta = 2 * 3.1416 * v1 * (v1 + v2)
                    ans = f"Curved Surface Area = {csa:.4f}\nTotal Area = {ta:.4f}"

            elif cat == "7":
                if sub == "1": ans = f"Volume = {v1 ** 3:.4f}"
                elif sub == "2": ans = f"Volume = {v1 * v2 * v3:.4f}"
                elif sub == "3": ans = f"Volume = {3.1416 * (v1 ** 2) * v2:.4f}"
                elif sub == "4": ans = f"Volume = {(4/3) * 3.1416 * (v1 ** 3):.4f}"
                elif sub == "5": ans = f"Volume = {(2/3) * 3.1416 * (v1 ** 3):.4f}"
                elif sub == "6": ans = f"Volume = {(1/3) * 3.1416 * (v1 ** 2) * v2:.4f}"
                elif sub == "7": ans = f"Volume = {(1/3) * v1 * v2:.4f}"
                elif sub == "8": ans = f"Volume = {2 * 3.1416 * 3.1416 * v1 * (v2 ** 2):.4f}"
                elif sub == "9": ans = f"Volume = {0.5 * v1 * v2 * v3:.4f}"
                elif sub == "10": ans = f"Volume = {v1 * v2 * v3:.4f}"
                elif sub == "11": ans = f"Volume = {3.1416 * (v1 ** 2) * ((4/3)*v1 + v2):.4f}"
                elif sub == "12": ans = f"Volume = {(4/3) * 3.1416 * v1 * v2 * v3:.4f}"
                elif sub == "13": ans = f"Volume = {(1/3) * 3.1416 * v3 * ((v1**2) + (v1*v2) + (v2**2)):.4f}"
                elif sub == "14": ans = f"Volume = {3.1416 * v3 * ((v1**2) - (v2**2)):.4f}"

            elif cat == "8":
                if sub == "1":
                    ans = "sin = Opposite / Hypotenuse\ncos = Adjacent / Hypotenuse\ntan = Opposite / Adjacent"
                elif sub == "2":
                    ans = "1. sin²A + cos²A = 1\n2. tanA = sinA / cosA\n3. sec²A - tan²A = 1\n4. csc²A - cot²A = 1"
                elif sub == "3":
                    ans = "sin(A+B) = sinA·cosB + cosA·sinB\ncos(A+B) = cosA·cosB - sinAsinB\ntan(A+B) = (tanA + tanB) / (1 - tanA·tanB)"
                elif sub == "4":
                    ans = "sin2A = 2sinAcosA\ncos2A = 2cos²A - 1\ncos2A = 1 - 2sin²A"
                elif sub == "5":
                    ans = "sin²(A/2) = (1 - cosA) / 2\ncos²(A/2) = (1 + cosA) / 2"
                elif sub == "6":
                    ans = "Area = (1/2)ab sinC\nSine Rule: a/sinA = b/sinB\nCosine Rule: a² = b² + c² - 2bc cosA"
                elif sub == "7":
                    tch = trig_calc_dd.value
                    if tch == "1":
                        rad = v1 * math.pi / 180
                        num, den = int(v1), 180
                        g = math.gcd(num, den)
                        n, d = num // g, den // g
                        exact = '0' if v1 == 0 else ('pi' if n == 1 and d == 1 else (f"pi/{d}" if n == 1 else (f"{n}pi" if d == 1 else f"{n}pi/{d}")))
                        ans = f"DEG: {v1}\nRAD (exact): {exact}\nRAD (decimal): {rad:.4f}"
                    elif tch == "2":
                        rad = v1 * math.pi
                        deg = v1 * 180
                        ans = f"RAD (exact): {v1}\nDEG: {deg:.4f}\nRAD (decimal): {rad:.4f}"
                    elif tch == "3": ans = f"sin({v1}) = {math.sin(v1 * math.pi / 180):.4f}"
                    elif tch == "4": ans = f"cos({v1}) = {math.cos(v1 * math.pi / 180):.4f}"
                    elif tch == "5": ans = f"tan({v1}) = {math.tan(v1 * math.pi / 180):.4f}"
                    elif tch == "6": ans = f"asin({v1}) = {math.asin(v1) * 180 / math.pi:.4f}°"
                    elif tch == "7": ans = f"acos({v1}) = {math.acos(v1) * 180 / math.pi:.4f}°"
                    elif tch == "8":
                        c = math.sqrt(v1**2 + v2**2 - 2*v1*v2*math.cos(v3 * math.pi / 180))
                        ans = f"Third side (c) = {c:.4f}"
                    elif tch == "9":
                        cos_C = (v1**2 + v2**2 - v3**2) / (2 * v1 * v2)
                        C = math.acos(cos_C) * 180 / math.pi
                        ans = f"Angle C = {C:.4f}°"
                    elif tch == "10":
                        height = v1 * math.tan(v2 * math.pi / 180)
                        ans = f"Height = {height:.4f}"
                    elif tch == "11":
                        slope = math.tan(v1 * math.pi / 180)
                        ans = f"Slope = {slope:.4f}"
                    elif tch == "12":
                        rad = v2 * math.pi / 180
                        ans = f"x = {v1 * math.cos(rad):.4f}\ny = {v1 * math.sin(rad):.4f}"
                    elif tch == "13":
                        r = math.sqrt(v1**2 + v2**2)
                        deg = math.atan(v2 / v1) * 180 / math.pi
                        ans = f"Radius (r) = {r:.4f}\nAngle (deg) = {deg:.4f}°"
                    elif tch == "14":
                        area_val = 0.5 * v1 * v2 * math.sin(v3 * math.pi / 180)
                        ans = f"Area = {area_val:.4f}"

            result_text.value = f"Result:\n{ans}"
        except Exception as ex:
            result_text.value = "Please enter valid numeric inputs!"
        
        page.update()

    calc_button = ft.ElevatedButton("Calculate / Show Result", on_click=calculate, width=420)

    page.add(
        ft.Column(
            [
                ft.Text("Universal Unit Converter & Math App", size=20, weight=ft.FontWeight.BOLD),
                category_dd,
                subcategory_dd,
                trig_calc_dd,
                input_1,
                input_2,
                input_3,
                calc_button,
                ft.Divider(),
                result_text
            ],
            spacing=15
        )
    )

ft.app(target=main)
