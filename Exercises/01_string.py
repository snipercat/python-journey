#Task 1: Name format (Data Cleaning)
print("Task 1".center(80,'-'))
print("Remove leading and trailing whitespace")

v_input = "  mouredev  "
v_output = v_input.strip()
print(f"Input:{v_input}")
print(f"User is: {v_output}")

#Task 2: Extract Domain (Networking/Email)
print("Task 2".center(80,'-'))
print("Extract domain from email address")

v_input = "contacto@braismoure.com"
at_pos = v_input.find('@')
v_output = v_input[at_pos+1:]
print(f"Input:{v_input}")
print(f"Mail domain is: {v_output}")


#Task 3: Extract Domain (Networking/Email)
print("Task 3".center(80,'-'))
print("Extract file extention")

v_input = "reporte_mensual_abril.pdf"
last_point_pos = v_input.rfind('.')
v_output = v_input[last_point_pos+1:]
is_pdf = v_output.lower() == 'pdf'

print(f"Input:{v_input}")
print(f"File extention is: {v_output}")
print(f"is a PDF file?: {is_pdf}")

