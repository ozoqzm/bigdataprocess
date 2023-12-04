input_file_name = input("입력 파일 이름 입력: ")
output_file_name = input("출력 파일 이름 입력: ")
delete_string = input("삭제할 문자열을 입력: ")

input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

for line in input_file:
    # 문자열에서 삭제할 문자열을 삭제하고 결과를 출력 파일에 쓰기
    updated_line = line.replace(delete_string, '')
    output_file.write(updated_line)
print("변경된 파일이 저장되었습니다.")
input_file.close()
output_file.close()

