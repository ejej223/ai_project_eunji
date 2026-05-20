import csv
from pathlib import Path

# 데이터 파일 경로
input_file = r"c:\Users\ejej2\OneDrive\바탕 화면\Hello.txt"
output_file = Path("d:/은지/회사/교육/project/output.html")

def is_missing_value(name, age, bp):
    """결측치 판단 및 사유 반환"""

    # 1. 이름이 비어 있음
    if not name or name.strip() == '':
        return True, '이름 비어 있음'

    # 2. 나이가 비어 있음
    if not age or age.strip() == '':
        return True, '나이 비어 있음'

    # 3. 혈압이 비어 있음
    if not bp or bp.strip() == '':
        return True, '혈압 비어 있음'

    # 5. 공백만 있는 값
    if name.strip() == '' or age.strip() == '' or bp.strip() == '':
        return True, '공백만 있는 값'

    # 6. 숫자 컬럼(age, bp)에 숫자가 아닌 값
    try:
        int(age.strip())
    except ValueError:
        return True, f'나이에 숫자 아닌 값: {age.strip()}'

    try:
        int(bp.strip())
    except ValueError:
        return True, f'혈압에 숫자 아닌 값: {bp.strip()}'

    return False, None

# 데이터 읽기 및 전처리
valid_data = []
excluded_data = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 헤더 읽기

    for row_num, row in enumerate(reader, start=1):
        if len(row) != 3:
            continue

        name, age, bp = row
        is_missing, reason = is_missing_value(name, age, bp)

        if is_missing:
            excluded_data.append({
                'row_num': row_num,
                'data': ','.join(row),
                'reason': reason
            })
        else:
            valid_data.append({
                'row_num': row_num,
                'name': name.strip(),
                'age': age.strip(),
                'bp': bp.strip()
            })

# 통계 출력
total_count = len(valid_data) + len(excluded_data)
excluded_count = len(excluded_data)
valid_count = len(valid_data)

print("[전처리 결과]")
print(f"전체 데이터 개수: {total_count}")
print(f"제외된 데이터 개수: {excluded_count}")
print(f"정상 데이터 개수: {valid_count}")
print()

if excluded_data:
    print("[제외된 행]")
    for item in excluded_data:
        print(f"행 {item['row_num']}: {item['data']} → {item['reason']}")
    print()

print("[HTML로 변환할 정상 데이터]")
for item in valid_data:
    print(f"{item['row_num']}: {item['name']}, {item['age']}, {item['bp']}")

# HTML 파일 생성
html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>전처리된 데이터</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .stats {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>전처리된 데이터 - HTML 테이블</h1>
    <div class="stats">
        <p><strong>전체 데이터:</strong> """ + str(total_count) + """개</p>
        <p><strong>제외된 데이터:</strong> """ + str(excluded_count) + """개</p>
        <p><strong>정상 데이터:</strong> """ + str(valid_count) + """개</p>
    </div>
    <table>
        <thead>
            <tr>
                <th>번호</th>
                <th>이름</th>
                <th>나이</th>
                <th>혈압</th>
            </tr>
        </thead>
        <tbody>
"""

for idx, item in enumerate(valid_data, start=1):
    html_content += f"""            <tr>
                <td>{idx}</td>
                <td>{item['name']}</td>
                <td>{item['age']}</td>
                <td>{item['bp']}</td>
            </tr>
"""

html_content += """        </tbody>
    </table>
</body>
</html>
"""

# HTML 파일 저장
output_file.parent.mkdir(parents=True, exist_ok=True)
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"\n✓ HTML 파일 생성 완료: {output_file}")
